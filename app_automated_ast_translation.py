import json
import os
import google.generativeai as genai
import ast
import traceback # For more detailed error logging
import copy # Added for deep copying AST nodes
import argparse # For command-line argument parsing
import xml.etree.ElementTree as ET # For parsing struts.xml

# New imports for unit testing
import sys
import subprocess
from ast import NodeVisitor


# You'll need to ensure this import works in your environment.
try:
    from java_parser.antlr_parser import generate_ast_dict
except ImportError:
    print("Erro Crítico: java_parser.antlr_parser não encontrado.")
    print("Este script requer o parser ANTLR para gerar a AST do Java.")
    print("Por favor, certifique-se de que 'java_parser.antlr_parser' está acessível.")
    exit()

# --- Configuração ---
GEMINI_MODEL_NAME = "gemini-2.5-flash" # Using a modern, capable model
MAX_MEMBERS_PER_CHUNK = 10 # Adjusted for potentially larger files

# --- Framework Identification Helpers ---
def find_nodes_by_type(node, node_type):
    """Recursively finds all nodes of a specific type in the AST dictionary."""
    nodes = []
    if isinstance(node, dict):
        if node.get("type") == node_type:
            nodes.append(node)
        for key, value in node.items():
            nodes.extend(find_nodes_by_type(value, node_type))
    elif isinstance(node, list):
        for item in node:
            nodes.extend(find_nodes_by_type(item, node_type))
    return nodes

def find_xml_files(start_path, filename):
    """Finds all XML files with a specific name in a directory tree."""
    for root, _, files in os.walk(start_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def identify_and_map_framework(ast_dict, file_path, project_root):
    """
    Analyzes the Java AST and project structure for framework usage.
    Returns a metadata dictionary describing the detected frameworks.
    """
    framework_metadata = {
        "frameworks": [],
        "spring_endpoints": [],
        "hibernate_entities": [],
        "struts_actions": [],
        "gwt_services": []
    }
    
    # --- Spring Detection ---
    class_declarations = find_nodes_by_type(ast_dict, "ClassDeclaration")
    for class_node in class_declarations:
        class_annotations = find_nodes_by_type(class_node.get("modifiers", []), "Annotation")
        is_rest_controller = any(ann.get("qualifiedName") in ["RestController", "Controller"] for ann in class_annotations)
        if is_rest_controller:
            if "Spring" not in framework_metadata["frameworks"]:
                framework_metadata["frameworks"].append("Spring")

    # --- Hibernate/JPA Detection ---
    for class_node in class_declarations:
        class_annotations = find_nodes_by_type(class_node.get("modifiers", []), "Annotation")
        is_entity = any(ann.get("qualifiedName") == "Entity" for ann in class_annotations)
        if is_entity:
            if "Hibernate" not in framework_metadata["frameworks"]:
                framework_metadata["frameworks"].append("Hibernate")
            
            class_name_node = find_nodes_by_type(class_node, "Identifier")
            entity_name = class_name_node[0].get("text") if class_name_node else "UnknownEntity"
            
            entity_info = {"name": entity_name, "columns": []}
            
            member_declarations = find_nodes_by_type(class_node, "MemberDeclaration")
            for member in member_declarations:
                field_annotations = find_nodes_by_type(member, "Annotation")
                is_id = any(ann.get("qualifiedName") == "Id" for ann in field_annotations)
                is_column = any(ann.get("qualifiedName") == "Column" for ann in field_annotations)
                if is_id or is_column:
                    field_decl = find_nodes_by_type(member, "FieldDeclaration")
                    if field_decl:
                        var_declarator = find_nodes_by_type(field_decl[0], "VariableDeclarator")
                        if var_declarator:
                            col_name = var_declarator[0].get("identifier")
                            col_type_node = find_nodes_by_type(field_decl[0], "TypeType")
                            col_type = col_type_node[0].get("name", "UnknownType") if col_type_node else "UnknownType"
                            entity_info["columns"].append({"name": col_name, "type": col_type, "is_primary_key": is_id})
            
            framework_metadata["hibernate_entities"].append(entity_info)

    # --- Struts Detection (via struts.xml) ---
    struts_xml_path = find_xml_files(project_root, "struts.xml")
    if struts_xml_path:
        if "Struts" not in framework_metadata["frameworks"]:
            framework_metadata["frameworks"].append("Struts")
        try:
            tree = ET.parse(struts_xml_path)
            root = tree.getroot()
            # Namespace-aware findall
            ns = {'s': 'http://struts.apache.org/dtds/struts-2.0.dtd'} # Adjust ns if needed
            for action_node in root.findall('.//s:action', ns):
                action_name = action_node.get('name')
                action_class = action_node.get('class')
                action_method = action_node.get('method', 'execute')
                results = []
                for result_node in action_node.findall('s:result', ns):
                    text_value = result_node.text.strip() if result_node.text is not None else None
                    results.append({'name': result_node.get('name'), 'target': text_value})
                framework_metadata["struts_actions"].append({
                    "name": action_name,
                    "class": action_class,
                    "method": action_method,
                    "results": results
                })
        except ET.ParseError as e:
            print(f"  WARNING: Could not parse struts.xml: {e}")

    # --- GWT (Google Web Toolkit) Detection ---
    # Simplified check for a .gwt.xml file in the same directory or a parent
    current_dir = os.path.dirname(file_path)
    found_gwt = False
    while len(current_dir) >= len(project_root):
        if any(f.endswith(".gwt.xml") for f in os.listdir(current_dir)):
            if "GWT" not in framework_metadata["frameworks"]:
                framework_metadata["frameworks"].append("GWT")
            found_gwt = True
            break
        # Move up one directory
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir: # Reached the root
            break
        current_dir = parent_dir
    
    if found_gwt:
        for class_node in class_declarations:
            # Look for RemoteService interfaces
            interface_spec = class_node.get("interface")
            if interface_spec:
                # Simplified check, a real one would resolve imports
                if "RemoteService" in str(interface_spec):
                    class_annotations = find_nodes_by_type(class_node.get("modifiers", []), "Annotation")
                    service_path = "unknown_path"
                    for ann in class_annotations:
                        if ann.get("qualifiedName") == "RemoteServiceRelativePath":
                            value_node = find_nodes_by_type(ann.get("elementValue", {}), "Literal")
                            if value_node and isinstance(value_node[0].get("text"), str):
                                service_path = value_node[0]["text"].strip('"')
                    
                    class_name_node = find_nodes_by_type(class_node, "Identifier")
                    service_name = class_name_node[0].get("text") if class_name_node else "UnknownService"

                    framework_metadata["gwt_services"].append({
                        "name": service_name,
                        "path": service_path
                    })

    if framework_metadata["frameworks"]:
         print(f"  Frameworks Detected: {', '.join(framework_metadata['frameworks'])}")
    return framework_metadata


# --- Helper function to convert JSON dictionary to ast.AST object (UNCHANGED) ---
def dict_to_ast_node(node_dict):
    # ... (This function remains unchanged)
    if not isinstance(node_dict, dict):
        raise TypeError(f"Expected a dictionary for AST node, got {type(node_dict)} with value {node_dict}")
    node_type_name = node_dict.get("_nodetype") or node_dict.get("type")
    if node_type_name == "staticmethod" and node_dict.get("id") == "staticmethod":
        node_type_name = "Name" 
    if not isinstance(node_type_name, str):
        raise ValueError(f"AST node dictionary is missing a 'type' key or the value is not a string. Malformed node: {node_dict}")
    node_class = getattr(ast, node_type_name, None)
    if node_class is None:
        raise ValueError(f"Unknown AST node type or non-node type specified: {node_type_name}")
    if not issubclass(node_class, ast.AST) and \
       issubclass(node_class, (ast.operator, ast.expr_context, ast.boolop, ast.cmpop, ast.unaryop)):
        try:
            return node_class()
        except TypeError:
            raise ValueError(f"Cannot auto-instantiate type {node_type_name}. JSON: {node_dict!r}")
    elif not issubclass(node_class, ast.AST):
        raise ValueError(f"Type {node_type_name} is not a recognized AST node class.")
    constructor_args = {}
    known_list_fields = {
        "bases", "keywords", "body", "decorator_list", "args", "posonlyargs", 
        "kwonlyargs", "kw_defaults", "defaults", "names", "elts", "keys", 
        "values", "handlers", "items", "type_ignores", "ops", "comparators", "orelse"
    }
    for field_name in node_class._fields:
        if field_name in node_dict:
            json_value = node_dict[field_name]
            if json_value is None:
                constructor_args[field_name] = [] if field_name in known_list_fields else None
            elif isinstance(json_value, list):
                constructor_args[field_name] = [dict_to_ast_node(item) if isinstance(item, dict) else item for item in json_value]
            elif isinstance(json_value, dict):
                constructor_args[field_name] = dict_to_ast_node(json_value)
            else:
                constructor_args[field_name] = json_value
        else:
            if field_name in known_list_fields:
                constructor_args[field_name] = []
            elif field_name in ['ctx', 'kind', 'type_comment']:
                 constructor_args[field_name] = None
    if 'op' in node_dict and 'op' in node_class._fields:
        op_val = node_dict['op']
        if isinstance(op_val, str):
            op_class = getattr(ast, op_val, None)
            if op_class and issubclass(op_class, (ast.operator, ast.unaryop, ast.boolop)):
                constructor_args['op'] = op_class()
        elif isinstance(op_val, dict):
             constructor_args['op'] = dict_to_ast_node(op_val)
    if 'ops' in node_dict and node_class == ast.Compare:
        processed_ops = []
        for item in node_dict['ops']:
            if isinstance(item, str):
                op_class = getattr(ast, item, None)
                if op_class and issubclass(op_class, ast.cmpop):
                    processed_ops.append(op_class())
            elif isinstance(item, dict):
                processed_ops.append(dict_to_ast_node(item))
        constructor_args['ops'] = processed_ops
    try:
        if 'lineno' not in constructor_args and 'lineno' in node_class._attributes:
            constructor_args['lineno'] = 1
        if 'col_offset' not in constructor_args and 'col_offset' in node_class._attributes:
            constructor_args['col_offset'] = 0
        ast_node = node_class(**constructor_args)
    except TypeError as e:
        print(f"Error creating AST node {node_type_name} with processed args {constructor_args}.")
        print(f"Original JSON chunk for this node: {node_dict!r}")
        print(f"Expected fields for {node_type_name}: {node_class._fields}")
        raise TypeError(f"Failed to instantiate {node_type_name}: {e}")
    return ast_node


# --- Function to split Java AST by class members ---
def split_java_ast_by_class_members(original_cu_dict, max_members):
    output_cu_dicts = []
    if not isinstance(original_cu_dict, dict) or original_cu_dict.get("type") != "CompilationUnit":
        return [original_cu_dict]
    original_children = original_cu_dict.get("children", [])
    if not original_children:
        return [copy.deepcopy(original_cu_dict)]
    eof_node = next((copy.deepcopy(child) for child in reversed(original_children) if child.get("type") == "terminal" and child.get("text") == "<EOF>"), None)
    global_prefix_elements, import_declarations, type_declaration_nodes_original = [], [], []
    for child in original_children:
        child_type = child.get("type")
        if child_type == "ImportDeclaration": import_declarations.append(copy.deepcopy(child))
        elif child_type == "PackageDeclaration": global_prefix_elements.append(copy.deepcopy(child))
        elif child_type == "TypeDeclaration": type_declaration_nodes_original.append(child)
        elif child.get("text") != "<EOF>": global_prefix_elements.append(copy.deepcopy(child))
    if not type_declaration_nodes_original:
        current_chunk_children = global_prefix_elements + import_declarations
        if eof_node: current_chunk_children.append(eof_node)
        if current_chunk_children: output_cu_dicts.append({"type": "CompilationUnit", "children": current_chunk_children})
        elif eof_node: output_cu_dicts.append({"type": "CompilationUnit", "children": [eof_node]})
        else: output_cu_dicts.append(copy.deepcopy(original_cu_dict))
        return output_cu_dicts if output_cu_dicts else [copy.deepcopy(original_cu_dict)]
    for td_node_orig in type_declaration_nodes_original:
        td_node = copy.deepcopy(td_node_orig)
        base_cu_children_for_td = global_prefix_elements + import_declarations
        if len(td_node.get("children", [])) == 1:
            declaration_node = td_node["children"][0]
            if declaration_node.get("type") == "ClassDeclaration":
                original_class_children = declaration_node.get("children", [])
                class_structure_prefix, member_elements, class_structure_suffix = [], [], []
                lbrace_found = False
                for child_el in original_class_children:
                    if not lbrace_found:
                        class_structure_prefix.append(child_el)
                        if child_el.get("token_type") == "LBRACE": lbrace_found = True
                    elif child_el.get("type") == "MemberDeclaration": member_elements.append(child_el)
                    else: class_structure_suffix.append(child_el)
                if not lbrace_found or not any(el.get("token_type") == "RBRACE" for el in class_structure_suffix):
                    new_cu_children = base_cu_children_for_td + [td_node]; output_cu_dicts.append({"type": "CompilationUnit", "children": new_cu_children + ([eof_node] if eof_node else [])}); continue
                if len(member_elements) > max_members:
                    for i in range(0, len(member_elements), max_members):
                        chunk_of_members = member_elements[i : i + max_members]
                        new_class_children_for_chunk = class_structure_prefix + chunk_of_members + class_structure_suffix
                        chunk_class_decl = copy.deepcopy(declaration_node); chunk_class_decl["children"] = new_class_children_for_chunk
                        chunk_type_decl = {"type": "TypeDeclaration", "children": [chunk_class_decl]}
                        new_cu_children_for_split = base_cu_children_for_td + [chunk_type_decl]
                        if eof_node: new_cu_children_for_split.append(eof_node)
                        output_cu_dicts.append({"type": "CompilationUnit", "children": new_cu_children_for_split})
                else:
                    new_cu_children = base_cu_children_for_td + [td_node]; output_cu_dicts.append({"type": "CompilationUnit", "children": new_cu_children + ([eof_node] if eof_node else [])})
            else: new_cu_children = base_cu_children_for_td + [td_node]; output_cu_dicts.append({"type": "CompilationUnit", "children": new_cu_children + ([eof_node] if eof_node else [])})
        else: new_cu_children = base_cu_children_for_td + [td_node]; output_cu_dicts.append({"type": "CompilationUnit", "children": new_cu_children + ([eof_node] if eof_node else [])})
    if not output_cu_dicts:
        current_chunk_children = global_prefix_elements + import_declarations
        for td_node_orig_fallback in type_declaration_nodes_original: current_chunk_children.append(copy.deepcopy(td_node_orig_fallback))
        if eof_node: current_chunk_children.append(eof_node)
        if current_chunk_children: output_cu_dicts.append({"type": "CompilationUnit", "children": current_chunk_children})
        else: output_cu_dicts.append(copy.deepcopy(original_cu_dict))
    return output_cu_dicts 

# --- Preparação do Prompt  ---
# System message is defined once
system_message = """You are an expert code transpiler specializing in converting Java Abstract Syntax Trees (ASTs) directly into Python Abstract Syntax Tree (AST) structures represented in JSON format. Your output MUST be a single, valid JSON object.

### Core Task: JSON AST Transformation
Your primary goal is to transform the input Java AST (provided as JSON) into an equivalent Python AST, also formatted as a JSON object. This JSON object should accurately represent the structure that Python's `ast` module would use.

### JSON Output Requirements:
1.  **Strictly JSON**: The entire output must be a single, valid JSON object. Do NOT output any other text, explanations, or code formatting (like ```json ... ```) outside of this single JSON object.
2.  **Python AST Node Naming**: Use node type names that correspond to Python's `ast` module (e.g., "Module", "FunctionDef", "Assign", "Call", "Constant", "arguments", "arg"). **Every JSON object that represents an AST node, including nested nodes like `ast.arguments` (which is the value of the `args` field in a `FunctionDef`), must have a key like "type" (preferred) or "_nodetype" to specify its node type.**
3.  **Field Names**: Field names within each JSON node object must match the field names used by Python's `ast` nodes (e.g., "body", "targets", "value", "func", "args", "keywords").
4.  **Recursive Structure**: Nested AST nodes must be represented as nested JSON objects or arrays of JSON objects under their respective parent fields.
5.  **No Python Code**: Do NOT generate Python code directly. The output must be the JSON representation of the Python AST.
6.  **Handling Key Collisions for Fields Named 'type'**:
    Certain Python `ast` nodes (e.g., `ast.ExceptHandler`, `ast.TypeVar`, `ast.TypeAlias`) have a field that is literally named `\"type\"`.
    When generating JSON for such a node:
    a.  To identify the node itself (e.g., that the object *is* an `ExceptHandler`), **you MUST use the `\"_nodetype\"` key**. For example: `\"_nodetype\": \"ExceptHandler\"`.
    b.  The field *within* this node that is named `type` (as per Python's `ast` definition) should be represented in the JSON with the key `\"type\"` and its value should be the appropriate AST node (e.g., `\"type\": { \"type\": \"Name\", \"id\": \"ValueError\", ... }`).
    This ensures the node identifier is not confused with its own `type` field.
    Example for an `ast.ExceptHandler` catching `ValueError`:
    ```json
    {
      \"_nodetype\": \"ExceptHandler\",  // Node identifier using _nodetype
      \"type\": {                      // Field named 'type' for the exception class
        \"type\": \"Name\",            // This Name node is the value of the ExceptHandler's 'type' field
        \"id\": \"ValueError\",
        \"ctx\": \"Load\"
      },
      \"name\": \"e\",
      \"body\": [ /* ... */ ]
    }
    ```
    For all other nodes that do *not* have a field named `\"type\"`, you can continue to use `\"type\"` as the primary node type identifier.
7.  **Correct JSON Syntax**: Ensure all JSON objects have correctly placed commas (`,`) separating their key-value pairs. Ensure all JSON arrays have correctly placed commas (`,`) separating their elements. The entire output MUST be parsable by a standard JSON parser without errors.
8.  **Literal Value Representation for `ast.Constant`**:
    *   **Strings**: For string constants, the `value` field should be a JSON string (e.g., `"hello"`).
    *   **Numbers**: For numerical constants, the `value` field should be a JSON number (e.g., `123`, `3.14`).
    *   **Booleans**: For boolean constants (Python `True` or `False`), the `value` field in the JSON **must** be the JSON boolean literals `true` or `false` (lowercase).
        *   Python `True`  -> JSON `value: true`
        *   Python `False` -> JSON `value: false`
    *   **None**: For Python `None`, the `value` field in the JSON **must** be the JSON literal `null`.
    *   The `kind` field for `ast.Constant` should typically be `null` unless representing a specific kind like `None` for certain f-string formatting parts (though for simple `None` constants, `value: null` is primary).
9.  **Vigilance with Repetitive Structures**: When translating long, repetitive sequences of similar statements (such as a series of independent `if` blocks or multiple similar assignments), pay extremely close attention to the JSON syntax. It is critical that every single object in a list is correctly formed and that commas are correctly placed between every element. The entire JSON output. Double-check that every node object has its required `"type"` or `"_nodetype"` key.

### Valid Top-Level (Module Body) Nodes
**CRITICAL**: The `body` array of the root `Module` node in your JSON output can **ONLY** contain nodes that are valid at the Python module level. This is strictly limited to:
- `FunctionDef` (global functions)
- `ClassDef` (classes)
- `Import`
- `ImportFrom`
- `Assign` (for global constants, e.g., `MY_CONSTANT = 10`)
- `AnnAssign` (for type-annotated global variables)
- `If` (ONLY for the `if __name__ == '__main__':` block, as specified in the Main Method rules. No other `If` statements are allowed at the top level.)

**DO NOT** place other statement types like `Expr` (with a `Call` value), `For`, `While`, or general `If` statements directly in the module's top-level `body`. All executable logic must be inside a function or the `if __name__ == '__main__':` block.

### NEW: Python Module Structure and Ordering (CRITICAL)
The order of nodes in the top-level `body` of the `Module` is critical. You MUST follow this sequence to prevent `NameError` exceptions in the generated code:
1.  **Imports**: All `Import` and `ImportFrom` nodes must come first.
2.  **Class Definitions**: All `ClassDef` nodes (e.g., data models, repositories, helper classes) must be defined next.
3.  **Global Assignments & App Instantiation**: `Assign` nodes for global variables or constants, including Flask app instantiation (e.g., `app = Flask(__name__)`), should follow the class definitions.
4.  **Repository/Service Instantiation**: `Assign` nodes that create instances of the previously defined classes (e.g., `usuario_repo = UsuarioRepository()`) must come after the class definitions and app instantiation.
5.  **Route/Function Definitions**: `FunctionDef` nodes, especially those decorated as Flask routes (`@app.route(...)`), must come after the app and repository instances they depend on.
6.  **Main Execution Block**: The `If` node for `if __name__ == '__main__':` must be the last element in the module's `body`.

**Example Correct Order:**
```python
# 1. Imports
from flask import Flask
# 2. Class Definitions
class User: ...
class UserRepository: ...
# 3. App Instantiation
app = Flask(__name__)
# 4. Repository Instantiation
user_repo = UserRepository()
# 5. Route Definitions
@app.route('/users')
def get_users(): ...
# 6. Main Block
if __name__ == '__main__': ...
```

### NEW: Framework-Aware Translation
If the user provides `framework_metadata`, you MUST use it to guide the translation.

**1. Spring to Flask Translation Rules:**
- **Imports**: The Python AST must include `from flask import Flask, jsonify, request`.
- **App Initialization**: Generate `app = Flask(__name__)` at the module level.
- **`@RestController`**: A Java class with this annotation contains endpoint logic. Its methods should be translated into top-level Python functions decorated as Flask routes. The Java class structure itself can be discarded after its methods are translated.
- **`@GetMapping`, `@PostMapping`**: A Java method `public User getUser(@PathVariable Long id)` with `@GetMapping("/{id}")` MUST become a Python function `@app.route("/users/<int:id>", methods=['GET']) def get_user(id):`.
- **Return Value**: `ResponseEntity.ok(user)` becomes `return jsonify(user_dict), 200`.

**2. Hibernate to SQLAlchemy Translation Rules:**
- **Imports**: The Python AST must include necessary SQLAlchemy imports, like `from sqlalchemy import create_engine, Column, Integer, String`, `from sqlalchemy.orm import sessionmaker`, and `from sqlalchemy.ext.declarative import declarative_base`.
- **`@Entity`**: A Java class annotated with `@Entity` MUST be translated into a Python class that inherits from `Base` (where `Base = declarative_base()`).
- **`@Table(name="users")`**: This annotation's `name` attribute becomes the `__tablename__` attribute in the Python class (e.g., `__tablename__ = 'users'`).
- **`@Id` and `@Column`**: A Java field like `@Id @Column(name="user_id") private int userId;` MUST be translated to a SQLAlchemy `Column` definition: `user_id = Column(Integer, primary_key=True)`.
- **Session Management**: Code using Hibernate `Session` or `EntityManager` should be translated to use a SQLAlchemy session. `session.save(object)` becomes `db_session.add(object)`. `session.createQuery(...)` becomes `db_session.query(...)`.

**3. Struts to Flask/Django Translation Rules:**
- **Action Class**: A Java Struts Action class (e.g., `public class LoginAction extends ActionSupport`) should be translated into a Python view function in Flask or Django.
- **`struts.xml` Mappings**: Use the `struts_actions` metadata. An action mapping like `<action name="login" class="com.example.LoginAction" method="authenticate">` should be translated to a Flask route: `@app.route('/login', methods=['GET', 'POST']) def login():`. The `authenticate` method's logic goes inside this `login` function.
- **Form Beans**: Struts `ActionForm` beans can be translated into Python dictionaries, Pydantic models, or Django `Form` classes for data validation.
- **Result Forwards**: A Struts result like `<result name="success">/main.jsp</result>` should be translated to a `render_template('main.html')` call in Flask or its equivalent in Django.

**4. GWT (Google Web Toolkit) to REST API + JavaScript Frontend:**
- **This is a major architectural shift.** The goal is to separate the backend and frontend.
- **GWT RPC to REST API**: A GWT `RemoteService` MUST be translated into a RESTful API backend using Flask or Django.
    - An interface `MyService extends RemoteService` with a method `List<String> getItems()` becomes a Flask/Django backend.
    - The implementation `MyServiceImpl` provides the logic for an API endpoint, e.g., `@app.route('/api/items', methods=['GET']) def get_items():`.
- **Client-side Java**: GWT client-side Java code (UI widgets, logic) is NOT translated to Python. Instead, you should generate a placeholder comment indicating that a JavaScript frontend is needed.
    - **Example Comment in Python file**: `# GWT UI code in 'com.example.client.MyWidget' should be replaced with a JavaScript frontend that calls the /api/items endpoint.`
- **Data Transfer Objects (DTOs)**: Java DTOs used in GWT RPC should be translated into Python dictionaries or objects that can be serialized to JSON by the Flask/Django backend.

### Key Translation Rules

#### Module and Import Management
- If the Java code uses static methods from standard Java classes like `Math` (e.g., `Math.sqrt`, `Math.pow`), the generated Python AST should include an `Import` node for the corresponding Python module (e.g., `import math`) at the beginning of the module's body. The calls should then be translated to use the Python module (e.g., `math.sqrt`, `math.pow`).
- **Java `java.util.Scanner`**:
    - Do NOT generate an `Import` node for `Scanner`.
    - `new Scanner(System.in)` should be translated to Python AST that effectively prepares for using Python's built-in `input()` function. Often, no direct AST equivalent for the `Scanner` object itself is needed if subsequent calls are handled.
    - `scanner.nextLine()` should be translated to Python AST for `input()`.
    - `scanner.nextInt()` should be translated to Python AST for `int(input())`. Ensure to handle potential `ValueError` if the input is not a valid integer, similar to how Java might throw an `InputMismatchException`.
    - **`scanner.close()`**: When the `Scanner` was initialized with `System.in`, `scanner.close()` should generally be omitted in the Python translation, as `sys.stdin` (used by `input()`) does not require explicit closing in typical script usage. If a placeholder AST node is generated, it could be an `ast.Pass` node, but preferably it's omitted. Do NOT translate it to an `input()` call.
- **Java Enums (e.g., `enum MyEnum { VAL1, VAL2 }`)**:
    - Translate to a Python class inheriting from `enum.Enum`.
    - Generate an `Import` node: `from enum import Enum, auto`.
    - Each enum constant (e.g., `VAL1`) becomes an attribute assignment in the class body: `VAL1 = auto()`.
    - `MyEnum.valueOf("VAL1")` should be translated to Python AST for `MyEnum["VAL1"]` (dictionary-style access) or `MyEnum.VAL1` (attribute access if the string is known/static). Accessing by string `MyEnum["VAL1"]` is safer for dynamic inputs and will raise a `KeyError` if the member doesn't exist, which is similar to `IllegalArgumentException`.
- **Java `java.util.List<E>` (Interface)**:
        - Do NOT generate an `Import` node for a module named "List" or "java.util.List".
        - When used as a type (e.g., `List<Integer> numbers`), the Python type hint AST should be for `list[Integer_py]` (e.g., `list[int]`) or `typing.List[Integer_py]` if you need to support older Python versions or be explicit with `typing.List`.
            - For `list[int]`, the AST is a `Subscript` node:
              `{ "type": "Subscript", "value": { "type": "Name", "id": "list", "ctx": "Load" }, "slice": { "type": "Name", "id": "int", "ctx": "Load" } }`
            - If generating an import for `typing.List`, it should be `from typing import List`.
        - Instantiation like `new ArrayList<>()` (if `List` is the declared type) should still map to Python `[]` (empty list literal).
- **Java `java.util.ArrayList<E>`**:
    - Do NOT generate an `Import` node for `ArrayList`.
    - `new ArrayList<>()` or `new ArrayList()` should be translated to Python AST for an empty list literal: `[]`.
    - `arrayList.add(element)` should be translated to Python AST for `list.append(element)`.
    - `arrayList.get(index)` should be translated to Python AST for `list[index]`.
    - `arrayList.size()` should be translated to Python AST for `len(list)`.
    - `arrayList.isEmpty()` should be translated to Python AST for `not list` or `len(list) == 0`.
    - Iterating over an `ArrayList` (e.g., `for (Task t : tarefas)`) should be translated to a standard Python for-in loop (`for t in tarefas:`).
- **Java `java.time.LocalDateTime`**:
    - Generate an `ast.ImportFrom` node: `from datetime import datetime`. This should be added to the module's body.
        AST: `{ "type": "ImportFrom", "module": "datetime", "names": [{ "type": "alias", "name": "datetime", "asname": null }], "level": 0 }`
    - `LocalDateTime.now()`: Translate to an `ast.Call` node for `datetime.now()`.
        AST for `datetime.now()`:
        `{ "type": "Call", "func": { "type": "Attribute", "value": { "type": "Name", "id": "datetime", "ctx": "Load" }, "attr": "now", "ctx": "Load" }, "args": [], "keywords": [] }`
- **Java `java.time.format.DateTimeFormatter`**:
    - `DateTimeFormatter.ofPattern(patternString)`: If this formatter is then used with `localDateTime.format(formatter)`, the Python equivalent is `datetime_instance.strftime(patternString)`. The formatter object itself often doesn't need a direct Python variable if used immediately.
    - `someLocalDateTime.format(someFormatter)` where `someFormatter` was created with `ofPattern(patternStr)`: Translate to `python_datetime_obj.strftime(patternStr)`.
        Example: Java `creationDate = now.format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"));`
        Python AST for `self.creationDate = now.strftime("%Y-%m-%d %H:%M")` (assuming `now` is a Python datetime object):
        ```json
        {
            "type": "Assign",
            "targets": [
            {
                "type": "Attribute",
                "value": { "type": "Name", "id": "self", "ctx": "Load" },
                "attr": "creationDate",
                "ctx": "Store"
            }
            ],
            "value": {
            "type": "Call",
            "func": {
                "type": "Attribute",
                "value": { "type": "Name", "id": "now", "ctx": "Load" }, // 'now' is the datetime object
                "attr": "strftime",
                "ctx": "Load"
            },
            "args": [
                { "type": "Constant", "value": "%Y-%m-%d %H:%M", "kind": null }
            ],
            "keywords": []
            }
        }
        ```
- **Project-Local and Unrecognized Imports**:
    This is the most important rule for multi-file projects.
    - A Java import like `import com.example.model.User;` refers to the `User` class, which is defined in a file named `User.java` under the `com/example/model/` directory structure.
    - The **correct and required** Python translation for this is `from com.example.model.User import User`.
    - The AST for this MUST be an `ast.ImportFrom` node structured as follows:
    - `module`: `com.example.model.User` (the full path to the file, without `.py`)
    - `names`: a list containing an `alias` node for the class `User`.
    - **Example**:
    - **Java**: `import com.example.service.UserService;`
    - **Python AST**:
        ```json
        {
        "type": "ImportFrom",
        "module": "com.example.service.UserService",
        "names": [
            { "type": "alias", "name": "UserService", "asname": null }
        ],
        "level": 0
        }
        ```
    - **DO NOT** translate `import com.example.model.User;` into `from com.example.model import User`. This is incorrect as it treats `User` as a module instead of a class within the `User` module. This single mistake will cause cascading "Module is not callable" and "Module cannot be used as a type" errors.

#### The `self` Parameter in Instance Methods (CRITICAL)
- **Condition**: If a Java method in the AST is **NOT** explicitly marked with a `static` modifier, it is an **instance method**.
- **Action**: Its Python translation **MUST** have `self` as its first parameter. This is a non-negotiable rule of Python syntax. Failure to add `self` is a critical error.
- **AST Template for `self`**: The AST for the `self` parameter is always this exact JSON object:
    ```json
    {
        "type": "arg",
        "arg": "self",
        "annotation": null
    }
    ```
- **Placement**: This arg node for self MUST be the first element in the args array within the FunctionDef's arguments node.
- **Example Context**:
    ```json
    "args": {
    "type": "arguments",
    "posonlyargs": [],
    "args": [
        { "type": "arg", "arg": "self", "annotation": null }, // <-- MUST BE FIRST
        { "type": "arg", "arg": "param1", "annotation": { ... } }
    ],
    "kwonlyargs": [], "kw_defaults": [], "defaults": []
    },
    ```
- Forgetting self will cause the generated code to fail with a TypeError. Do not make this mistake.
- Even for main methods you translate as instance methods, `self` must be included as the first parameter. This is a fundamental aspect of Python's method definitions.

#### Idiomatic Python Expressions
- Convert common Java patterns to their Pythonic equivalents.
- **Checking for non-empty collections/strings**:
    - **Java**: `if (!myList.isEmpty()) { ... }` or `if (!myString.isEmpty()) { ... }`
    - **Pythonic Translation**: Translate this to the AST for `if myList: ...` or `if myString: ...`. The expression `!var.isEmpty()` becomes just `var` in a boolean context.
- **Checking for empty collections/strings**:
    - **Java**: `if (myList.isEmpty()) { ... }`
    - **Pythonic Translation**: Translate this to the AST for `if not myList: ...`. The expression `var.isEmpty()` becomes `not var` in a boolean context.

- **Condition**: If a Java method is declared to return an object type (e.g., `public User findUser(...)`) and its implementation contains a `return null;` statement.
- **Action**: This requires a **mandatory two-step procedure** in the Python AST. Both steps are required.
    1.  **STEP 1: Import `Optional`**: You **MUST** add an `ast.ImportFrom` node at the top of the module's body to import `Optional` from the `typing` module.
        ```json
        {
          "type": "ImportFrom",
          "module": "typing",
          "names": [ { "type": "alias", "name": "Optional", "asname": null } ],
          "level": 0
        }
        ```
    2.  **STEP 2: Update the Type Hint**: You **MUST** wrap the method's return type annotation in `Optional`.
        - **Example AST for `-> Optional['User']`**:
          ```json
          "returns": {
            "type": "Subscript",
            "value": { "type": "Name", "id": "Optional", "ctx": "Load" },
            "slice": { "type": "Constant", "value": "User", "kind": null },
            "ctx": "Load"
          }
          ```
- **Omitting the import while using the type hint will cause the generated code to fail. You must perform both steps.**
    
#### Main Method and Script Execution
- If the Java AST contains a `public static void main(String[] args)` method (typically within a class, e.g., `MyClass`), the Python AST should include:
    1.  A corresponding `FunctionDef` node for `main`.
        *   The `name` of this `FunctionDef` node should be `"main"`.
        *   The `args` field of this `FunctionDef` (which itself is an `ast.arguments` node) should represent a single parameter, typically named `args`. The AST for this parameter's annotation should be for `list[str]`.
            Example for the `args` parameter within the `arguments` node:
            ```json
            {
              "type": "arg",
              "arg": "args",
              "annotation": {
                "type": "Subscript",
                "value": { "type": "Name", "id": "list", "ctx": "Load" },
                "slice": { "type": "Name", "id": "str", "ctx": "Load" },
                "ctx": "Load"
              }
            }
            ```
            This `arg` node would be an element in the `args` list of the `arguments` node.
        *   **Crucially, if the Java `main` method is part of a class and you translate it as a method within the corresponding Python class (preserving the class structure), this `FunctionDef` for `main` MUST include `@staticmethod` in its `decorator_list`.** The AST for this decorator is an `ast.Name` node:
            ```json
            { "type": "Name", "id": "staticmethod", "ctx": "Load" }
            ```
            This `Name` node representing the decorator should be an element in the `decorator_list` array of the `FunctionDef` for `main`.
    2.  At the end of the module's body, an `ast.If` node representing the `if __name__ == '__main__':` block.
        The `test` for this `If` node should be an `ast.Compare` node:
        ```json
        "test": {
          "type": "Compare",
          "left": { "type": "Name", "id": "__name__", "ctx": "Load" },
          "ops": [ { "type": "Eq" } ],
          "comparators": [ { "type": "Constant", "value": "__main__", "kind": null } ]
        }
        ```
    3.  The `body` of this `If` node should contain an AST structure to call the translated `main` function. If `main` is a static method of `ClassName`, the call would be `ClassName.main([])`. If `main` is a top-level function, it would be `main([])`.
        Example AST for calling `ClassName.main([])`:
        ```json
        {
          "type": "Expr",
          "value": {
            "type": "Call",
            "func": {
              "type": "Attribute",
              "value": { "type": "Name", "id": "ClassName", "ctx": "Load" },
              "attr": "main",
              "ctx": "Load"
            },
            "args": [ { "type": "List", "elts": [], "ctx": "Load" } ], // Represents passing an empty list
            "keywords": []
          }
        }
        ```

#### Java AWT/Swing to Python Tkinter Translation Guide (CRITICAL)
You **MUST** translate Java AWT and Swing GUI components to their Python `tkinter` equivalents. This is a primary requirement.

**1. Imports:**
- **Java**: `import java.awt.*;`, `import java.awt.event.*;`
- **Python AST**: Generate `import tkinter as tk` and `from tkinter import *` (or specific components like `Label`, `Button`). A single `import tkinter as tk` is sufficient and preferred.

**2. Frame/Window:**
- **Java**: `Frame f = new Frame("My App");`
- **Python AST**: Translate to `self.f = tk.Tk()` followed by `self.f.title("My App")`. The main window object is typically an instance of `tk.Tk`.
- **Java**: `f.setSize(w, h);` -> **Python AST**: `self.f.geometry(f"{w}x{h}")`
- **Java**: `f.setLayout(null);` -> **Action**: This indicates absolute positioning. Use the `.place()` layout manager in Tkinter for all widgets. No direct AST for `setLayout` is needed.
- **Java**: `f.setVisible(true);` -> **Action**: This is handled by calling `self.f.mainloop()` at the very end of the script execution (typically in the `if __name__ == '__main__':` block after the class is instantiated).
- **Java**: `f.addWindowListener(this);` with `windowClosing` method -> **Python AST**: `self.f.protocol("WM_DELETE_WINDOW", self.windowClosing_handler_method)`
- **Java**: `f.dispose();` -> **Python AST**: `self.f.destroy()`

**3. Components (Widgets):**
- **Java**: `Button b1 = new Button("1");`
- **Python AST**: `self.b1 = tk.Button(self.f, text="1")`. The first argument **MUST** be the parent widget (e.g., `self.f`).
- **Java**: `Label l1 = new Label();` -> **Python AST**: `self.l1 = tk.Label(self.f, text="")`
- **Java**: `l1.setBackground(Color.LIGHT_GRAY);` -> **Python AST**: `self.l1.config(bg="light gray")`
- **Java**: `b1.setBounds(x, y, w, h);` -> **Python AST**: `self.b1.place(x=x, y=y, width=w, height=h)`
- **Java**: `f.add(b1);` -> **Action**: This is handled implicitly in Python by creating the widget with a parent and using a layout manager (`.place()`). Do not generate a separate `.add()` call.

**4. Event Handling:**
- **Java**: `b1.addActionListener(this);` where the class implements `ActionListener`.
- **Python AST**: Translate this by setting the `command` option during widget creation. The command should call a handler method.
  - **Example**: `self.b1 = tk.Button(self.f, text="1", command=self.actionPerformed)`
- **Java**: `public void actionPerformed(ActionEvent e) { if (e.getSource() == b1) { ... } }`
- **Python AST**: The `actionPerformed` method no longer receives an event object. You must refactor the logic. A good pattern is to use `lambda` in the command to pass an identifier for the widget.
  - **Python `__init__` AST**:
    `self.b1 = tk.Button(self.f, text="1", command=lambda: self.handle_button_press("b1"))`
    `self.b2 = tk.Button(self.f, text="2", command=lambda: self.handle_button_press("b2"))`
  - **Python handler method AST**:
    `def handle_button_press(self, button_id):`
    `  if button_id == "b1":`
    `    # logic for button 1`
    `  elif button_id == "b2":`
    `    # logic for button 2`

**5. Widget Interaction:**
- **Java**: `l1.getText();` -> **Python AST**: `self.l1.cget("text")`
- **Java**: `l1.setText("new text");` -> **Python AST**: `self.l1.config(text="new text")`

#### Loop Transformations
- **Java indexed for-loops** → **Python enumerate()** when accessing both index and element
- **Java enhanced for-loops** → **Python for-in loops**
- **Java while loops with iterators** → **Python for-in loops** when appropriate

### String and Output Operations
- **Java `String.format(\"template %s\", arg)` or `printf()` equivalents**:
    - **Preferred**: Translate to Python AST for **f-strings**. Example for `f"Value: {my_var}"`:
      ```json
      {
        "type": "JoinedStr",
        "values": [
          { "type": "Constant", "value": "Value: ", "kind": null },
          {
            "type": "FormattedValue",
            "value": { "type": "Name", "id": "my_var", "ctx": "Load" },
            "conversion": -1,
            "format_spec": null
          }
        ]
      }
      ```
      Example for an f-string with a complex expression like `f"Total: {price + tax}"`:
      ```json
      {
        "type": "JoinedStr",
        "values": [
          { "type": "Constant", "value": "Total: ", "kind": null },
          {
            "type": "FormattedValue",
            "value": {
              "type": "BinOp",
              "left": { "type": "Name", "id": "price", "ctx": "Load" },
              "op": { "type": "Add" },
              "right": { "type": "Name", "id": "tax", "ctx": "Load" }
            },
            "conversion": -1,
            "format_spec": null
          }
        ]
      }
      ```
    - **Alternative (`.format()` method)**: If generating AST for the `.format()` method, ensure the structure is a `Call` to an `Attribute` node.
      For Python code like `"My name is {}".format(name_variable)`, the AST for the format call itself should be:
      ```json
      {
        "type": "Call",
        "func": {
          "type": "Attribute",
          "value": {
            "type": "Constant",
            "value": "My name is {}", // The template string
            "kind": null
          },
          "attr": "format", // The method name
          "ctx": "Load"
        },
        "args": [
          {
            "type": "Name", // AST node for name_variable
            "id": "name_variable",
            "ctx": "Load"
          }
        ],
        "keywords": []
      }
      ```
      **Crucially, do NOT embed the `.format(...)` call or its arguments *inside* the string value of an `ast.Constant` node representing the template string.** The template string itself is a `Constant`, and the `.format` is an `Attribute` on that `Constant`, which is then `Call`ed.

#### Print Statements
- **Java System.out.println(expression)**:
    - Java `System.out.println(expression)` **MUST** be translated to a simple Python `print(expression)`.
    - The AST should be a `Call` node where `func` is a `Name` node with `id: 'print'`.
    - **DO NOT** generate verbose or incorrect ASTs like `print.__call__`. This is wrong.
    - If `expression` involves string concatenation (e.g., `"literal" + nonStringVariable` or `"literal" + methodCall()`), generate Python AST for **f-strings** (e.g., `f"literal{nonStringVariable}"` or `f"literal{methodCall()}"`) or explicit string conversion (e.g., `"literal" + str(nonStringVariable)`). F-strings are preferred for readability.
- Maintain the same output format and variable interpolation. Ensure that the generated Python AST correctly handles type differences between Java's implicit string conversion in concatenation and Python's explicit requirements.

#### Language Constructs
- **Java ternary operator** `condition ? value1 : value2` → **Python conditional expression** `value1 if condition else value2`
- **Java .size()** → **Python len()**
- **Java .get(index)** → **Python [index]** or appropriate method
- **Java `Math.sqrt(expression)`** → Python AST for `math.sqrt(expression)`. Ensure an `Import` node for `math` is present.
- **Java `(int) Math.sqrt(expression)` or casting a double to int** → Python AST for `int(math.sqrt(expression))` or `int(expression)`.
- **Java `switch` statements**:
    - Translate to Python `if/elif/else` chains or, for Python 3.10+, to `match/case` statements if the structure is suitable.
    - For `match/case`, ensure the AST structure is correct (e.g., `ast.Match`, `ast.match_case`, `ast.MatchValue`, `ast.MatchSingleton`).
- **Java `try-catch` blocks**:
    - `try { ... } catch (SpecificException e) { ... } catch (AnotherException e) { ... }` should be translated to Python `try...except SpecificException as e: ... except AnotherException as e: ...`.
    - **Java `IllegalArgumentException`**: Typically translate to Python `ValueError` or `TypeError` depending on context. For enum `valueOf` or similar string-to-object conversions, `KeyError` (when using dictionary-style access like `MyEnum["string_value"]`) or `AttributeError` (for `MyEnum.string_value`) can also be appropriate, or a custom check leading to `ValueError`. For `Priority.valueOf(prioInput)`, the Python equivalent `Priority[prioInput]` will raise `KeyError`, so the `catch (IllegalArgumentException e)` should become `except KeyError as e:`.

#### Object-Oriented Patterns
- **Java Instance Field Declaration**:
    - A Java instance field declaration like `private String myField;` or `List<Task> tasks;` at the class level should be translated into a Python class-level attribute with a type hint.
    - **Correct Python AST**: Generate the AST for `myField: str` or `tasks: list['Task']`. The AST node for this is `AnnAssign`.
    - **Example**:
        Java: `class MyClass { private int count; }`
        Python AST for `class MyClass: count: int` should include this `AnnAssign` node in its body:
        ```json
        {
            "type": "AnnAssign",
            "target": { "type": "Name", "id": "count", "ctx": "Store" },
            "annotation": { "type": "Name", "id": "int", "ctx": "Load" },
            "value": null,
            "simple": 1
        }
        ```
- **Preserving Class Structure (CRITICAL RULE)**: If the input Java AST chunk contains a `ClassDeclaration` node, the output Python AST **MUST** also contain a corresponding `ClassDef` node preserving the class name. Do not flatten a class into top-level functions. **All methods from the Java class, including static methods like `main`, must be translated as methods inside the corresponding Python class.** The class structure is essential for maintaining the relationship between instance methods, static methods, and class instantiations.
- **Method Calls vs. Attribute Access**:
    - A Java method call like `user.getName()` **MUST** be translated to a Python method call, `user.getName()`.
    - Do **NOT** mistake it for attribute access. `user.getName` is wrong; `user.getName()` is correct. The AST must be a `Call` node.
- **List/ArrayList Operations**:
    - `new ArrayList<>()` -> `[]` (an empty list literal).
    - `myList.add(element)` -> `myList.append(element)`.
    - `myList.get(index)` -> `myList[index]`.
    - `myList.size()` -> `len(myList)`.
    - `myList.isEmpty()` -> `not myList`.
    - **Iteration**: A Java enhanced for-loop `for (User user : userDatabase)` becomes a Python for-in loop `for user in self.userDatabase:`. **Ensure you are iterating over the correct instance variable (e.g., `self.userDatabase`), not `self`!**
- **Java `++` Operator (e.g., `nextId++`)**:
    - Python does not have a `++` operator.
    - If `nextId++` is used as an argument in a function call, like `new User(nextId++, name, email)`, it means "use the current value of `nextId`, then increment it".
    - This **MUST** be translated into two separate steps in the AST:
      1.  A `Call` to `User` using the current value of the variable (e.g., `self.nextId`).
      2.  An `AugAssign` statement (`+= 1`) on the *next line* to increment the variable.
    - **Example**:
      - Java: `User newUser = new User(nextId++, name, email);`
      - Python AST (body):
        ```json
        [
          {
            "type": "Assign",
            "targets": [{ "type": "Name", "id": "new_user", "ctx": "Store" }],
            "value": {
              "type": "Call",
              "func": { "type": "Name", "id": "User", "ctx": "Load" },
              "args": [
                { "type": "Attribute", "value": {"type": "Name", "id": "self"}, "attr": "nextId", "ctx": "Load" },
                { "type": "Name", "id": "name", "ctx": "Load" },
                { "type": "Name", "id": "email", "ctx": "Load" }
              ],
              "keywords": []
            }
          },
          {
            "type": "AugAssign",
            "target": { "type": "Attribute", "value": {"type": "Name", "id": "self"}, "attr": "nextId", "ctx": "Store" },
            "op": { "type": "Add" },
            "value": { "type": "Constant", "value": 1, "kind": null }
          }
        ]
        ```
- **Accessing Instance Members (THE `self` PREFIX - CRITICAL)**:
    - This is a fundamental rule that must be applied **consistently throughout the entire class**.
    - Any time a variable is accessed from within an instance method (a method with `self`), you **MUST** first determine if it is an instance variable (a field of the class).
    - If it is an instance variable, you **MUST** prefix it with `self.`. There are no exceptions.
    - **Example**:
        - Java: `if (userDatabase.isEmpty()) { ... }`
        - Python (WRONG): `if not userDatabase:`
        - Python (CORRECT AST `value`): `{ "type": "UnaryOp", "op": { "type": "Not" }, "operand": { "type": "Attribute", "value": { "type": "Name", "id": "self", "ctx": "Load" }, "attr": "userDatabase", "ctx": "Load" } }`
    - This applies to `__init__`, `printAllUsers`, and **all other instance methods**. Check every variable access inside a- **Java Nested Static Classes (e.g., `public class Outer { static class Inner {} }`)**:
    - In Python, these are typically translated as regular classes defined at the module level or, if closely tied to the outer class and not meant to be used independently, as inner classes defined within the outer class's scope.
    - If translated as an inner class in Python (e.g., `class Outer: class Inner: pass`), accessing it from outside would be `Outer.Inner`.
    - If the Java `main` method (or other static methods in the outer class) refers to `Inner` or `Priority` (if `Priority` is a static nested enum), the Python AST should reflect this. For example, if `Priority` is an inner class of `test3`, then references like `Priority.valueOf(...)` inside `test3.main` should become `test3.Priority[...]` or `cls.Priority[...]` if `main` is a `@classmethod`. Given `Task` and `Priority` are used within `test3.main`, they should be accessed via `test3.Task(...)` and `test3.Priority[...]`.
- **Interface**: Translate Java interfaces to Python ABCs (Abstract Base Classes) using `abc.ABC` and `abc.abstractmethod`.
- **Static Methods in Classes**: Java static methods in classes should be translated to Python static methods using the `@staticmethod` decorator.

#### Advanced Transformations
- **Java Stream API** → **Python list comprehensions, generator expressions, or itertools**
- **Java StringBuilder** → **Python string operations or join()**
- **Java Arrays.toString()** → **Python str() or custom formatting**

### Translation Strategy
1. **Analyze Intent**: Understand what the Java code accomplishes functionally
2. **Identify Patterns**: Recognize common Java idioms that have Pythonic equivalents
3. **Choose Optimal Solution**: Select Python constructs that maintain similar performance and readability
"""

### --- NEW: Unit Testing Subsystem --- ###

class FunctionFinder(NodeVisitor):
    """An AST visitor to find all function and method definitions."""
    def __init__(self):
        self.functions = []
        self._current_class_name = None

    def visit_ClassDef(self, node):
        self._current_class_name = node.name
        self.generic_visit(node)
        self._current_class_name = None

    def visit_FunctionDef(self, node):
        # We don't want to test the main execution block or constructors
        if node.name != 'main' and node.name != '__init__':
            self.functions.append({
                "name": node.name,
                "class_name": self._current_class_name,
                "node": node
            })
        self.generic_visit(node)

def get_python_source_root(java_file_path, input_root_path, output_root_dir, ast_dictionary):
    """
    Calculates the Python source root directory needed for PYTHONPATH.
    This allows tests to correctly import other modules from the translated project.
    """
    package_decl = find_nodes_by_type(ast_dictionary, "PackageDeclaration")
    package_path = ""
    if package_decl:
        # Reconstruct package path from identifiers, e.g., ['com', 'example', 'model']
        package_name_node = find_nodes_by_type(package_decl[0], "QualifiedName")
        if package_name_node:
            identifiers = find_nodes_by_type(package_name_node[0], "Identifier")
            package_parts = [i.get("text") for i in identifiers]
            # --- MODIFIED: Check if package_parts is not empty before joining ---
            if package_parts:
                package_path = os.path.join(*package_parts)

    java_file_dir = os.path.dirname(java_file_path)
    
    # Heuristic: find the source root by removing the package path from the file's path
    if package_path and java_file_dir.endswith(package_path):
        java_source_root = java_file_dir[:-len(package_path)].rstrip(os.path.sep)
    else:
        # If no package, the source root is just the file's directory
        java_source_root = java_file_dir

    # Make the source root relative to the project input path
    relative_source_root = os.path.relpath(java_source_root, input_root_path)
    if relative_source_root == '.':
        return output_root_dir
    else:
        return os.path.join(output_root_dir, relative_source_root)

def generate_and_run_unit_tests(model, all_python_module_body_parts, original_java_code, log_file_handle, output_root_dir, java_file_path, input_root_path, ast_dictionary):
    """
    Generates and runs unit tests for the translated Python code.
    Now handles project-level imports by setting PYTHONPATH.
    """
    print("  - Generating and running unit tests...")
    log_file_handle.write("\n## Unit Test Generation and Execution\n\n")

    # 1. Assemble the full Python module to be tested
    test_subject_module = ast.Module(body=all_python_module_body_parts, type_ignores=[])
    test_subject_module = ast.fix_missing_locations(test_subject_module)
    
    # The module being tested will be temporarily saved with a generic name
    # so that the AI-generated test can import from it consistently.
    # Its real dependencies will be found via the calculated PYTHONPATH.
    relative_path_py = os.path.relpath(java_file_path, start=input_root_path)
    module_import_path = os.path.splitext(relative_path_py)[0].replace(os.path.sep, '.')
    
    try:
        test_subject_code = ast.unparse(test_subject_module)
    except Exception as e:
        print(f"    ERROR: Could not unparse the Python AST for testing. Skipping tests. {e}")
        log_file_handle.write("### ERROR: Could not unparse Python AST for testing. Tests skipped.\n")
        return False

    # 2. Find all functions to test
    finder = FunctionFinder()
    finder.visit(test_subject_module)
    testable_functions = finder.functions

    if not testable_functions:
        print("    - No testable functions found. Skipping test generation.")
        log_file_handle.write("No testable functions were found. Skipping test generation.\n")
        return True # No tests to fail, so it's a "pass"

    overall_success = True
    
    # --- NEW: Define the temporary file path for the code being tested ---
    temp_subject_filename = os.path.join(output_root_dir, "temp_subject_for_test.py")

    for func_info in testable_functions:
        func_name = func_info['name']
        class_name = func_info['class_name']
        qualified_name = f"{class_name}.{func_name}" if class_name else func_name

        # The module to import from is now the actual module path, not a temp name
        import_name = class_name if class_name else func_name

        print(f"    - Creating tests for `{qualified_name}`...")
        log_file_handle.write(f"### Testing `{qualified_name}`\n\n")
        
        temp_test_filename = None
        # 3. Generate test code with AI
        test_generation_prompt = f"""You are a senior Python Quality Assurance (QA) engineer. Your task is to write a complete, executable unit test script for a specific Python function.
**Context:**
The function was translated from a Java project. The original Java code for the file is provided below to help you understand the function's intended behavior, edge cases, and expected outputs.

**Original Java Code (in file `{os.path.basename(java_file_path)}`):**
```java
{original_java_code}
```
Translated Python Code (System Under Test):
The function to be tested, {qualified_name}, is located in the Python module {module_import_path}. The full code for this module is:
```python
# File: {module_import_path.replace('.', '/')}.py
{test_subject_code}
```
Your Task:
Write a Python script using the built-in unittest framework to test the {qualified_name} function.

Requirements:

1. Import Necessary Modules: Your script must import unittest and the class/functions from the module temp_subject_for_test.
    - Example for a class: from temp_subject_for_test import {class_name}
    - Example for a standalone function: from temp_subject_for_test import {func_name}
    - If the code to be tested depends on other classes (like User from com.example.model.User), you MUST import them as well. The AI should infer these from the provided Python code. For example: from com.example.model.User import User.
2. Create a Test Class: Define a class that inherits from unittest.TestCase.
3. Write Test Methods: Inside the test class, write one or more test methods (names starting with test_).
4. Instantiate if Needed: If testing an instance method, you must first create an instance of the class (e.g., self.checker = {class_name}()).
5. Assert Correctness: Use unittest.TestCase assertion methods (e.g., self.assertTrue(), self.assertFalse(), self.assertEqual()) to verify the function's behavior. Test a variety of inputs, including edge cases mentioned or implied in the Java code (e.g., for a prime checker, test prime numbers, non-prime numbers, 0, 1, 2).
6. Make it Executable: Include the standard if __name__ == '__main__': unittest.main() block so the script can be run directly.
7. Output ONLY Python Code: Your entire response must be a single, valid, runnable Python script. Do not include any explanations, markdown formatting, or other text.
"""
        temp_test_filename = None
        try:
            # --- NEW: Write the code being tested to the temporary file ---
            with open(temp_subject_filename, "w", encoding="utf-8") as f:
                f.write(test_subject_code)

            response = model.generate_content(test_generation_prompt)
            raw_test_code = response.text.strip()
            
            cleaned_test_code = raw_test_code
            if cleaned_test_code.startswith("```python"):
                cleaned_test_code = cleaned_test_code[len("```python"):].strip()
            if cleaned_test_code.endswith("```"):
                cleaned_test_code = cleaned_test_code[:-len("```")].strip()
            
            log_file_handle.write("**AI-Generated Test Script:**\n\n```python\n" + cleaned_test_code + "\n```\n\n")

            # Save the test script in the root of the output directory to simplify execution
            temp_test_filename = os.path.join(output_root_dir, f"temp_test_{qualified_name}.py")
            with open(temp_test_filename, "w", encoding="utf-8") as f:
                f.write(cleaned_test_code)

            # --- MODIFIED: Use the new environment with the correct PYTHONPATH ---
            # Calculate the Python source root for imports
            python_source_root = get_python_source_root(java_file_path, input_root_path, output_root_dir, ast_dictionary)
            
            # Create a copy of the current environment and set PYTHONPATH
            env = os.environ.copy()
            env["PYTHONPATH"] = os.pathsep.join(sys.path + [python_source_root])

            process = subprocess.run(
                [sys.executable, temp_test_filename],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='replace',
                env=env # Pass the modified environment to the subprocess
            )

            log_file_handle.write("**Test Execution Results:**\n\n")
            if process.returncode == 0:
                print(f"      ✅ PASS: Tests for `{qualified_name}` succeeded.")
                log_file_handle.write("```\n✅ PASSED\n\n")
                log_file_handle.write("Output:\n" + (process.stdout or process.stderr) + "\n```\n")
            else:
                print(f"      ❌ FAIL: Tests for `{qualified_name}` failed.")
                log_file_handle.write("```\n❌ FAILED\n\n")
                log_file_handle.write("Stderr:\n" + process.stderr + "\n")
                log_file_handle.write("Stdout:\n" + process.stdout + "\n```\n")
                overall_success = False

        except Exception as e:
            print(f"    ERROR: Failed during test generation or execution for `{qualified_name}`: {e}")
            traceback.print_exc()
            log_file_handle.write(f"### ERROR during test generation/execution: {e}\n\n")
            overall_success = False
        finally:
            if temp_test_filename and os.path.exists(temp_test_filename):
                os.remove(temp_test_filename)
            # --- NEW: Clean up the temporary subject file ---
            if os.path.exists(temp_subject_filename):
                os.remove(temp_subject_filename)
        
        return overall_success
        
### --- END NEW --- ###

def process_java_file(java_file_path, model, output_root_dir, log_file_handle, input_root_path):
    " Processes a single Java file: generates AST, identifies frameworks, calls AI for translation, and writes the output Python code and logs.  "

    print(f"--- Processing: {java_file_path} ---")
    log_file_handle.write(f"\n\n---\n\n# Processing File: {java_file_path}\n\n")
    try:
        with open(java_file_path, "r", encoding="utf-8") as f:
            original_java_code_content = f.read()
    except Exception as e:
        print(f"  WARNING: Could not read original Java file for context. Testing may be affected. {e}")
        original_java_code_content = "# Could not read original Java file."

    # --- 1. AST Java Generation ---
    ast_dictionary = generate_ast_dict(java_file_path)
    if ast_dictionary is None:
        print(f"  ERROR: Failed to generate Java AST for {java_file_path}. Skipping.")
        log_file_handle.write("## ERROR: Failed to generate Java AST.\n")
        return False

    original_ast_json_string_from_java = json.dumps(ast_dictionary, indent=2)
    log_file_handle.write(f"## Original Java AST\n\n```json\n{original_ast_json_string_from_java}\n```\n\n")

    # --- 2. Identify Framework Usage ---
    framework_metadata = identify_and_map_framework(ast_dictionary, java_file_path, input_root_path)
    log_file_handle.write(f"## Framework Analysis\n\n```json\n{json.dumps(framework_metadata, indent=2)}\n```\n\n")

    # --- 3. Split Java AST if necessary ---
    java_ast_dictionaries_to_process = split_java_ast_by_class_members(ast_dictionary, MAX_MEMBERS_PER_CHUNK)
    num_chunks = len(java_ast_dictionaries_to_process)
    print(f"  Java AST resulted in {num_chunks} chunk(s).")
    log_file_handle.write(f"Translation required **{num_chunks}** chunk(s).\n\n")

    all_python_module_body_parts = []
    all_transformed_ast_texts_from_ai = []

    # --- 4. Loop through Java AST chunks and call AI ---
    for i, java_ast_chunk_dict in enumerate(java_ast_dictionaries_to_process):
        print(f"  - Processing chunk {i+1}/{num_chunks}...")
        current_java_ast_json_for_ai = json.dumps(java_ast_chunk_dict, indent=2)
        # --- UPDATED: Construct user message with framework context ---
        framework_context_prompt = ""
        if framework_metadata.get("frameworks"):
            framework_context_prompt = f"""
Framework Context: This Java code uses the following frameworks: {', '.join(framework_metadata['frameworks'])}. Please translate it to a modern Python equivalent following the rules in the system prompt.
Framework Metadata: {json.dumps(framework_metadata, indent=2)}
""" 
            user_message_content = f"""{framework_context_prompt} 
Please convert the following Java AST (in JSON format) into a Python AST (also in JSON format).
Java AST: {current_java_ast_json_for_ai}
Expected Output: A single, valid JSON object representing the Python AST.
"""
        else:
            user_message_content = f"""
Please convert the following Java AST (in JSON format) into a Python AST (also in JSON format).
Java AST: {current_java_ast_json_for_ai}
Expected Output: A single, valid JSON object representing the Python AST.
"""
        processed_text_for_chunk = ""    
        try:
            response = model.generate_content(user_message_content)
            raw_text_from_ai = response.text.strip()

            if not raw_text_from_ai:
                raise ValueError("Model returned empty text.")
            
            cleaned_text = raw_text_from_ai
            if cleaned_text.startswith("```json"):
                cleaned_text = cleaned_text[len("```json"):].strip()
            if cleaned_text.startswith("```"):
                cleaned_text = cleaned_text[len("```"):].strip()
            if cleaned_text.endswith("```"):
                cleaned_text = cleaned_text[:-len("```")].strip()
                
            processed_text_for_chunk = cleaned_text
            all_transformed_ast_texts_from_ai.append(processed_text_for_chunk)

        except Exception as e:
            print(f"    ERROR: AI call failed for chunk {i+1}: {e}")
            processed_text_for_chunk = f'# AI_ERROR: {e}'
            all_transformed_ast_texts_from_ai.append(processed_text_for_chunk)
            continue

        # --- 5. Convert this chunk's Python AST JSON to Python AST objects ---
        try:
            python_ast_dict_from_json_chunk = json.loads(processed_text_for_chunk)
            
            is_module = isinstance(python_ast_dict_from_json_chunk, dict) and \
                        (python_ast_dict_from_json_chunk.get("type") or python_ast_dict_from_json_chunk.get("_nodetype")) == "Module"
            if not is_module:
                body_list = python_ast_dict_from_json_chunk if isinstance(python_ast_dict_from_json_chunk, list) else [python_ast_dict_from_json_chunk]
                python_ast_dict_from_json_chunk = {"type": "Module", "body": body_list, "type_ignores": []}

            py_ast_object_chunk = dict_to_ast_node(python_ast_dict_from_json_chunk)
                
            if isinstance(py_ast_object_chunk, ast.Module):
                all_python_module_body_parts.extend(py_ast_object_chunk.body)
            else:
                all_python_module_body_parts.append(py_ast_object_chunk)

        except Exception as e:
            print(f"    ERROR: Failed to parse or convert AI JSON for chunk {i+1}: {e}")
            traceback.print_exc(limit=1)
            log_file_handle.write(f"### ERROR Parsing AI JSON for Chunk {i+1}\n\n```json\n{processed_text_for_chunk}\n```\n\n")

    log_file_handle.write("## AI-Generated Python ASTs (JSON)\n\n")
    for i, ai_json_text in enumerate(all_transformed_ast_texts_from_ai):
        log_file_handle.write(f"### Chunk {i+1}:\n\n```json\n{ai_json_text}\n```\n\n")

    if not all_python_module_body_parts:
        print("  ERROR: No valid Python AST parts were generated. Skipping code generation.")
        log_file_handle.write("## Final Python Code\n\n```python\n# ERROR: No valid Python AST parts were generated.\n```\n")
        return False

    # --- MODIFIED: Pass necessary context to the test generator ---
    tests_passed = generate_and_run_unit_tests(
        model, 
        all_python_module_body_parts, 
        original_java_code_content, 
        log_file_handle,
        output_root_dir,
        java_file_path,
        input_root_path,
        ast_dictionary
    )
    if tests_passed:
        log_file_handle.write("\n**Overall Test Result: ✅ All generated tests passed.**\n")
    else:
        log_file_handle.write("\n**Overall Test Result: ❌ One or more generated tests failed.**\n")
    # --- END MODIFICATION ---

    # --- 6. Combine ASTs and Generate Final Code --- 
    generated_python_code = "# ERROR: Could not generate final Python code."
    try:
        # Separate nodes into categories based on the required Python module structure
        imports = []
        class_defs = {}
        app_instantiations = []
        repo_service_instantiations = []
        route_defs = []
        other_nodes = []
        main_if_block = None

        # First pass: Categorize all nodes from the AI's output
        all_nodes_to_sort = []
        if "Spring" in framework_metadata.get("frameworks", []):
            # For Spring, flatten the controller class but keep others
            for node in all_python_module_body_parts:
                if isinstance(node, ast.ClassDef) and node.name.endswith("Controller"):
                     all_nodes_to_sort.extend(node.body) # Add methods and other contents to the list
                else:
                     all_nodes_to_sort.append(node)
        else:
            all_nodes_to_sort = all_python_module_body_parts

        for node in all_nodes_to_sort:
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                imports.append(node)
            elif isinstance(node, ast.ClassDef):
                if node.name not in class_defs:
                    class_defs[node.name] = node
                else:
                    # Merge if class was split into chunks
                    class_defs[node.name].body.extend(node.body)
            elif isinstance(node, ast.FunctionDef):
                route_defs.append(node)
            elif isinstance(node, ast.Assign):
                # Check what is being assigned to categorize correctly
                if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
                    if node.value.func.id == 'Flask':
                        app_instantiations.append(node)
                    elif 'Repository' in node.value.func.id or 'Service' in node.value.func.id:
                        repo_service_instantiations.append(node)
                    else:
                        other_nodes.append(node)
                else:
                    other_nodes.append(node)
            elif (isinstance(node, ast.If) and isinstance(node.test, ast.Compare) and
                  isinstance(node.test.left, ast.Name) and node.test.left.id == '__name__'):
                if main_if_block is None:
                    main_if_block = node
            elif isinstance(node, ast.AST):
                other_nodes.append(node)

        # De-duplicate imports
        unique_import_strs = set()
        deduplicated_imports = []
        for imp_node in imports:
            try:
                s = ast.unparse(imp_node)
                if s not in unique_import_strs:
                    unique_import_strs.add(s)
                    deduplicated_imports.append(imp_node)
            except Exception:
                deduplicated_imports.append(imp_node)

        # Assemble the final body in the correct order
        final_py_body_elements = []
        final_py_body_elements.extend(deduplicated_imports)
        final_py_body_elements.extend(app_instantiations) # Flask app can be defined early
        final_py_body_elements.extend(class_defs.values())
        final_py_body_elements.extend(repo_service_instantiations)
        final_py_body_elements.extend(route_defs)
        final_py_body_elements.extend(other_nodes) # Add any other remaining nodes
        if main_if_block:
            final_py_body_elements.append(main_if_block)

        final_python_module = ast.Module(body=final_py_body_elements, type_ignores=[])
        final_python_module = ast.fix_missing_locations(final_python_module)
        generated_python_code = ast.unparse(final_python_module)
            
        test_comment = "# Unit test result: ✅ PASSED\n" if tests_passed else "# Unit test result: ❌ FAILED (see log for details)\n"
        generated_python_code = test_comment + generated_python_code

    except Exception as e:
        print(f"  ERROR: Failed to combine ASTs or generate final code: {e}")
        traceback.print_exc(limit=1)
        generated_python_code = f"# ERROR: Failed during final code generation.\n# {e}"

    # --- 7. Save the Generated Python Code ---
    try:
        relative_path = os.path.relpath(java_file_path, start=input_root_path)
        py_filename = os.path.splitext(relative_path)[0] + '.py'
        output_py_path = os.path.join(output_root_dir, py_filename)

        os.makedirs(os.path.dirname(output_py_path), exist_ok=True)

        # Create __init__.py files to make packages recognizable
        current_dir = os.path.dirname(output_py_path)
        while output_root_dir in current_dir:
            init_py = os.path.join(current_dir, '__init__.py')
            if not os.path.exists(init_py):
                with open(init_py, 'w') as f:
                    pass
            current_dir = os.path.dirname(current_dir)
            if current_dir == output_root_dir:
                break


        with open(output_py_path, "w", encoding="utf-8") as py_file:
            py_file.write(generated_python_code)
        print(f"  SUCCESS: Generated Python code saved to: {output_py_path}")
            
        log_file_handle.write("\n## Final Generated Python Code\n\n```python\n")
        log_file_handle.write(generated_python_code + "\n")
        log_file_handle.write("```\n")
        return True

    except Exception as e:
        print(f"  ERROR: Could not save the generated Python file: {e}")
        log_file_handle.write(f"## ERROR: Could not save the generated Python file: {e}\n")
        return False
        
def main(input_path, is_web_request=False):
    """
    Main function to orchestrate the translation process.
    Can be run from CLI or called by the web app.
    Handles both single file and directory inputs.
    """
    if not is_web_request:
        parser = argparse.ArgumentParser(
            description="Translate a Java file or project directory to Python using Generative AI."
        )
        parser.add_argument(
            "input_path",
            help="Path to the Java file or the root directory of the Java project."
        )
        args = parser.parse_args()
        input_path = args.input_path

    if not os.path.exists(input_path):
        error_message = f"Error: The path '{input_path}' does not exist."
        print(error_message)
        return (None, None, error_message) if is_web_request else exit(1)

    # --- API and Model Setup ---
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        error_message = "Erro Crítico: A variável de ambiente GOOGLE_API_KEY não está definida."
        print(error_message)
        return (None, None, error_message) if is_web_request else exit(1)

    try:
        genai.configure(api_key=api_key)
        # ... (rest of the model setup is identical)
        generation_config = genai.GenerationConfig(temperature=0.4)
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        model = genai.GenerativeModel(
            model_name=GEMINI_MODEL_NAME,
            generation_config=generation_config,
            safety_settings=safety_settings,
            system_instruction=system_message,
        )
        print(f"Successfully initialized Gemini model: {GEMINI_MODEL_NAME}")
    except Exception as e:
        error_message = f"Erro Crítico ao inicializar o modelo Gemini: {e}"
        print(error_message)
        return (None, None, error_message) if is_web_request else exit(1)

    # --- Identify files to process ---
    java_files_to_process = []
    # --- MODIFIED: The input_path is now the true root for both files and dirs ---
    input_root_path = os.path.abspath(input_path if os.path.isdir(input_path) else os.path.dirname(input_path))

    if os.path.isfile(input_path):
        if input_path.endswith(".java"):
            java_files_to_process.append(input_path)
        else:
            error_message = f"Error: Input file '{input_path}' is not a valid .java or .zip file."
            print(error_message)
            return (None, None, error_message) if is_web_request else exit(1)
    elif os.path.isdir(input_path):
        for root, _, files in os.walk(input_root_path):
            for file in files:
                if file.endswith(".java"):
                    java_files_to_process.append(os.path.join(root, file))

    if not java_files_to_process:
        error_message = f"No .java files found in '{input_path}'."
        print(error_message)
        return (None, None, error_message) if is_web_request else exit(0)

    # --- Setup Output Directory and Log File ---
    base_name = os.path.basename(os.path.normpath(input_path))
    if is_web_request:
        # The web app now controls the full output path structure
        output_root_dir = input_path.replace("uploads", "outputs", 1)
        base_name = "project" # Use a generic name for the log file
    else:
        output_root_dir = f"{base_name}_translated"

    os.makedirs(output_root_dir, exist_ok=True)
    output_root_dir = os.path.abspath(output_root_dir)

    log_filename = os.path.join(output_root_dir, f"{base_name}_translation_log.md")

    print(f"\nFound {len(java_files_to_process)} Java file(s). Starting translation...")
    print(f"Output will be saved in: {output_root_dir}")
    print(f"Log file will be at: {log_filename}")

    # --- Process all files ---
    successful_translations = 0
    with open(log_filename, "w", encoding="utf-8") as log_file:
        log_file.write(f"# Translation Log for: `{input_path}`\n")
        log_file.write(f"Model: `{GEMINI_MODEL_NAME}`\n")
        for i, java_file in enumerate(java_files_to_process):
            print(f"\n[{i+1}/{len(java_files_to_process)}] ", end="")
            if process_java_file(java_file, model, output_root_dir, log_file, input_root_path):
                successful_translations += 1

    print("\n--- Translation Summary ---")
    print(f"Successfully translated: {successful_translations}/{len(java_files_to_process)} files.")
    print(f"Full results and logs are in the '{output_root_dir}' directory.")

    # --- MODIFIED: Return the output directory for the web app ---
    if is_web_request:
        return output_root_dir, log_filename, None

    print("Script finished.")


if __name__ == "__main__":
    main(None)