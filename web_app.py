# File: web_app.py

import os
import uuid
import zipfile
import shutil
from datetime import datetime
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

def zip_directory(path, zip_handle):
    """Zips the contents of a directory without including the top-level folder."""
    for root, _, files in os.walk(path):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), path)
            zip_handle.write(os.path.join(root, file), relative_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transpile', methods=['POST'])
def transpile_file():
    form_type = request.form.get('form_type')
    request_id = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
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
        # Clean up on any failure
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
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_dir, filename)
        file.save(file_path)

        # MODIFIED: Correctly call run_translation with the override argument
        translation_result = run_translation(file_path, output_root_dir_override=output_dir)
        if translation_result is None:
            return render_template('result.html', error="Translation failed to produce a result.")
        
        _, log_path, error = translation_result
        
        # Determine the output path based on the original filename
        base_filename, _ = os.path.splitext(filename)
        output_py_path = os.path.join(output_dir, f"{base_filename}.py")

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

        # MODIFIED: Correctly call run_translation with the override argument
        translation_result = run_translation(extracted_dir, output_root_dir_override=output_dir)
        if translation_result is None:
            return render_template('result.html', error="Translation failed to produce a result.")
        
        output_project_dir, log_path, error = translation_result

        if error:
            return render_template('result.html', error=error)

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
    
    # Walk through the directory tree
    for root, dirs, files in os.walk(root_dir):
        # *** MODIFICATION: Exclude '__pycache__' directories from being processed ***
        dirs[:] = [d for d in dirs if d != '__pycache__']
        
        path_parts = os.path.relpath(root, root_dir).split(os.sep)
        if path_parts == ['.']: path_parts = []
        
        current_level = tree
        for part in path_parts:
            current_level = current_level.setdefault(part, {})
        
        for f in files:
            # Also exclude compiled python files and the zip archive itself
            if not f.endswith('.zip') and not f.endswith('.pyc'):
                file_path = os.path.join(root, f)
                # Check if the file is not empty
                has_content = os.path.getsize(file_path) > 0
                current_level[f] = has_content
    return tree

@app.route('/download/<string:request_id>/<string:type>')
def download_file(request_id, type):
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

@app.route('/view_file/<string:request_id>')
def view_file(request_id):
    file_path_rel = request.args.get('path')
    if not file_path_rel:
        return jsonify({"error": "No file path provided"}), 400
    
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
    # Add extra_files=None and exclude_patterns to prevent the reloader
    # from triggering on temp file creation in the outputs/uploads directories.
    app.run(debug=True, use_reloader=True, extra_files=None, exclude_patterns=['*.pyc', '*/outputs/*', '*/uploads/*'])