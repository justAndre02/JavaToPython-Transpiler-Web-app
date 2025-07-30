import sys
import json
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from .SimpleJavaLexer import SimpleJavaLexer  # Relative import for when used as a module
from .SimpleJavaParser import SimpleJavaParser # Relative import
from antlr4.tree.Trees import Trees
from antlr4 import TerminalNode

def tree_to_dict(tree, parser):
    """Convert ANTLR parse tree to a JSON-serializable dictionary."""
    if tree is None:
        return None
    
    result = {}
    
    # Check if it's a terminal node
    if isinstance(tree, TerminalNode):
        result["type"] = "terminal"
        result["text"] = tree.getText()
        # Get token type name
        token_type = tree.symbol.type
        # Ensure parser.symbolicNames is accessed safely
        if parser and hasattr(parser, 'symbolicNames') and \
           0 <= token_type < len(parser.symbolicNames) and parser.symbolicNames[token_type]:
            result["token_type"] = parser.symbolicNames[token_type]
        else:
            result["token_type"] = f"UNKNOWN_TOKEN_TYPE_{token_type}" # Fallback
    else:  # It's a rule node
        # Get the rule name from the parser's rule names
        ctx_name = type(tree).__name__
        if ctx_name.endswith("Context"):
            ctx_name = ctx_name[:-7]  # Remove "Context" suffix
        result["type"] = ctx_name
        
        # Process all children
        children = []
        for i in range(tree.getChildCount()):
            child = tree.getChild(i)
            child_dict = tree_to_dict(child, parser)
            if child_dict:
                children.append(child_dict)
        
        if children:
            result["children"] = children
    
    return result

def generate_ast_dict(source_file): # Renamed function
    """
    Generates an AST dictionary from a Java source file.
    Returns the AST dictionary or None if an error occurs.
    """
    try:  
        input_stream = FileStream(source_file, encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found in antlr_parser.")
        return None # Return None on error

    # Create lexer
    lexer = SimpleJavaLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Optional: Print tokens for debugging (can be commented out for cleaner library use)
    # stream.fill()
    # print("--- Tokens from antlr_parser ---")
    # for token in stream.tokens:
    #     if token.type == -1:
    #         print("Token: 'EOF' (type: EOF)")
    #     elif 0 <= token.type < len(SimpleJavaLexer.symbolicNames):
    #         print(f"Token: '{token.text}' (type: {SimpleJavaLexer.symbolicNames[token.type]})")
    #     else:
    #         print(f"Token: '{token.text}' (type: UNKNOWN_TYPE_{token.type})")
    # print("-----------------------------")


    # Create parser
    parser = SimpleJavaParser(stream)
    parser.removeErrorListeners() # Optional: remove default console error listener if you add a custom one

    # Parse the input
    try:
        tree = parser.compilationUnit()
    except Exception as e:
        print(f"Parsing error in '{source_file}' within antlr_parser: {e}")
        return None # Return None on error

    # Convert parse tree to dictionary
    tree_dict = tree_to_dict(tree, parser)
    
    return tree_dict # Return the dictionary

def main():
    if len(sys.argv) != 2:
        print("Usage: python antlr_parser.py <source_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    ast_dictionary = generate_ast_dict(source_file)

    if ast_dictionary:
        # Write dictionary to JSON file if main is called directly
        output_file = source_file.replace('.java', '_ast.json') # Changed suffix to avoid overwriting
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(ast_dictionary, f, indent=4)
            print(f"Parse tree written to '{output_file}' by antlr_parser main.")
        except IOError as e:
            print(f"Error writing AST to JSON file: {e}")
    else:
        print(f"Failed to generate AST for {source_file} in antlr_parser main.")

if __name__ == '__main__':
    main()