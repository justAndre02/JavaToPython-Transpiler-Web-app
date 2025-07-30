# File: web_app.py

import os
import uuid
import zipfile
import shutil
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, jsonify
from werkzeug.utils import secure_filename

from app_automated_ast_translation import main as run_translation

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.secret_key = 'super-secret-key-for-flash'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# --- CORRECTED zip_directory function for cleaner archives ---
def zip_directory(path, zip_handle):
    """Zips the contents of a directory without including the top-level folder."""
    for root, _, files in os.walk(path):
        for file in files:
            # Create a relative path for files to avoid including the full system path
            relative_path = os.path.relpath(os.path.join(root, file), path)
            zip_handle.write(os.path.join(root, file), relative_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transpile', methods=['POST'])
def transpile_file():
    form_type = request.form.get('form_type')
    request_id = str(uuid.uuid4())
    # The root directory for all generated content for this request
    output_dir_for_request = os.path.join(app.config['OUTPUT_FOLDER'], request_id)
    upload_dir_for_request = os.path.join(app.config['UPLOAD_FOLDER'], request_id)
    os.makedirs(output_dir_for_request, exist_ok=True)
    os.makedirs(upload_dir_for_request, exist_ok=True)

    try:
        if form_type == 'file':
            return handle_single_file_upload(request, request_id, upload_dir_for_request, output_dir_for_request)
        elif form_type == 'project':
            return handle_project_upload(request, request_id, upload_dir_for_request, output_dir_for_request)
        else:
            flash('Invalid form submission.')
            return redirect(url_for('index'))
    except Exception as e:
        shutil.rmtree(upload_dir_for_request)
        shutil.rmtree(output_dir_for_request)
        error_message = f"An unexpected error occurred: {str(e)}"
        return render_template('result.html', error=error_message)

def handle_single_file_upload(req, request_id, upload_dir, output_dir):
    file = req.files.get('java_file')
    if not file or file.filename == '':
        flash('No file selected.')
        return redirect(url_for('index'))

    if allowed_file(file.filename, {'java'}):
        # We pass the output_dir to the translation function now
        filename = "Source.java"
        file_path = os.path.join(upload_dir, filename)
        file.save(file_path)

        # The run_translation function will now place its output in our designated 'output_dir'
        translation_result = run_translation(file_path, output_dir)
        if translation_result is None:
            return render_template('result.html', error="Translation failed to produce a result.")
        _, log_path, error = translation_result
        # Note: The 'output_py_path' is now relative to the known output_dir
        output_py_path = os.path.join(output_dir, "Source.py")


        if error:
            return render_template('result.html', error=error)
        
        with open(output_py_path, 'r', encoding='utf-8') as f:
            python_code = f.read()
        
        log_content = ""
        if log_path and os.path.exists(log_path):
            with open(log_path, 'r', encoding='utf-8') as f:
                log_content = f.read()

        return render_template('result.html',
                               is_project=False,
                               python_code=python_code,
                               log_content=log_content,
                               request_id=request_id)
    else:
        flash('Invalid file type. Please upload a .java file.')
        return redirect(url_for('index'))

def handle_project_upload(req, request_id, upload_dir, output_dir):
    file = req.files.get('project_file')
    if not file or file.filename == '':
        flash('No project file selected.')
        return redirect(url_for('index'))

    if allowed_file(file.filename, {'zip'}):
        extracted_dir = os.path.join(upload_dir, 'source')
        os.makedirs(extracted_dir, exist_ok=True)
        zip_path = os.path.join(upload_dir, "project.zip")
        file.save(zip_path)

        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extracted_dir)
        except zipfile.BadZipFile:
            return render_template('result.html', error="The uploaded file is not a valid ZIP archive.")

        # Let the transpiler work directly into our clean output directory
        translation_result = run_translation(extracted_dir, output_dir)
        if translation_result is None:
            return render_template('result.html', error="Translation failed to produce a result.")
        output_project_dir, log_path, error = translation_result

        if error:
            return render_template('result.html', error=error)

        # Define the path for the output zip file
        output_zip_path = os.path.join(output_dir, 'translated_project.zip')
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zip_directory(output_project_dir, zipf)

        log_content = ""
        if log_path and os.path.exists(log_path):
            with open(log_path, 'r', encoding='utf-8') as f:
                log_content = f.read()
        
        file_tree = get_directory_structure(output_project_dir)

        return render_template('result.html',
                               is_project=True,
                               file_tree=file_tree,
                               log_content=log_content,
                               request_id=request_id)
    else:
        flash('Invalid file type. Please upload a .zip file.')
        return redirect(url_for('index'))

def get_directory_structure(root_dir):
    tree = {}
    if not os.path.isdir(root_dir):
        return tree
    for root, _, files in os.walk(root_dir):
        path_parts = os.path.relpath(root, root_dir).split(os.sep)
        if path_parts == ['.']: path_parts = []
        current_level = tree
        for part in path_parts:
            current_level = current_level.setdefault(part, {})
        for f in files:
            # We don't want to show the zip file in the file tree
            if not f.endswith('.zip'):
                current_level[f] = None
    return tree

# --- CORRECTED download_file function ---
@app.route('/download/<string:request_id>/<string:type>')
def download_file(request_id, type):
    # All outputs for a request are now in one predictable directory
    output_dir = os.path.join(app.config['OUTPUT_FOLDER'], request_id)
    filename = None

    if type == 'single_code':
        filename = next((f for f in os.listdir(output_dir) if f.endswith('.py')), None)
    elif type == 'project_zip':
        filename = 'translated_project.zip'
    elif type == 'log':
        filename = next((f for f in os.listdir(output_dir) if f.endswith('.md')), None)
    else:
        flash('Invalid download type.')
        return redirect('/')

    if filename and os.path.exists(os.path.join(output_dir, filename)):
        return send_from_directory(output_dir, filename, as_attachment=True)
    else:
        flash('File not found or has been cleaned up.')
        return redirect('/')

# --- CORRECTED view_file function ---
@app.route('/view_file/<string:request_id>')
def view_file(request_id):
    file_path_rel = request.args.get('path')
    if not file_path_rel:
        return jsonify({"error": "No file path provided"}), 400
    
    # The base directory for all translated files is now simple and correct
    base_output_dir = os.path.join(app.config['OUTPUT_FOLDER'], request_id)
    
    full_path = os.path.abspath(os.path.join(base_output_dir, file_path_rel))
    
    if not full_path.startswith(os.path.abspath(base_output_dir)):
        return jsonify({"error": "Access denied"}), 403

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return jsonify({"content": content})
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)