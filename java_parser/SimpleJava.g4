grammar SimpleJava;

// Parser rules
// MODIFIED: Added optional packageDeclaration at the beginning.
compilationUnit: packageDeclaration? importDeclaration* typeDeclaration+ EOF;

// ADDED: Rule for package statements.
packageDeclaration: PACKAGE qualifiedName SEMI;

// MODIFIED: Changed literal 'import' to IMPORT token for consistency.
importDeclaration: IMPORT qualifiedName ('.' '*')? SEMI;

qualifiedName: IDENTIFIER ('.' IDENTIFIER)*;

// Allow modifiers for classes 
typeDeclaration:
    classDeclaration |
    enumDeclaration |
    interfaceDeclaration; // Added interfaceDeclaration

classDeclaration: annotation* modifier* CLASS IDENTIFIER typeParameters? ('extends' type)? implementsClause? LBRACE memberDeclaration* RBRACE;  // Added implementsClause

// vvv Rules for interfaces (look correct) vvv
interfaceDeclaration:
    modifier* INTERFACE IDENTIFIER typeParameters? ('extends' typeList)? // Interfaces can extend other interfaces
    LBRACE interfaceMemberDeclaration* RBRACE;

implementsClause: IMPLEMENTS typeList;

interfaceMemberDeclaration:
    fieldDeclaration            // Constant declarations (implicitly public static final)
    | interfaceMethodDeclaration
    | classDeclaration          // Nested classes
    | interfaceDeclaration      // Nested interfaces
    | enumDeclaration           // Nested enums
    | SEMI                      // Allows empty statements like a lone semicolon
    ;

interfaceMethodDeclaration:
    modifier* returnType IDENTIFIER LPAREN formalParameters? RPAREN ('throws' qualifiedNameList)? SEMI; // No body, ends with SEMI
// ^^^ End of interface rules ^^^

enumDeclaration: modifier* ENUM IDENTIFIER ('implements' typeList)? LBRACE (enumConstantList (COMMA)?)? enumBodyDeclarations? RBRACE;

enumConstantList: enumConstant (COMMA enumConstant)*;

enumConstant: IDENTIFIER (arguments)? (classBody)?;

enumBodyDeclarations: SEMI memberDeclaration*;

typeParameters: '<' typeParameter (',' typeParameter)* '>';
typeParameter: IDENTIFIER ('extends' typeBound)?;
typeBound: type ('&' type)*;

memberDeclaration:
    fieldDeclaration |
    methodDeclaration |
    constructorDeclaration |
    classDeclaration |  // Allow inner classes~
    enumDeclaration;   // Add this to allow inner enums

fieldDeclaration: annotation* modifier* type variableDeclarator (COMMA variableDeclarator)* SEMI;
variableDeclarator: IDENTIFIER ('=' variableInitializer)?;
variableInitializer: expression | arrayInitializer;


constructorDeclaration:
    modifier* IDENTIFIER LPAREN formalParameters? RPAREN
    LBRACE blockStatement* RBRACE; // Use blockStatement

methodDeclaration:
    annotation* modifier* returnType IDENTIFIER LPAREN formalParameters? RPAREN ('throws' qualifiedNameList)?
    LBRACE blockStatement* RBRACE; // Use blockStatement

modifier: PUBLIC | PRIVATE | PROTECTED | STATIC | FINAL | ABSTRACT | SYNCHRONIZED | NATIVE | STRICTFP; 

returnType: type | VOID;


type:
    primitiveType (LBRACK RBRACK)* |
    classOrInterfaceType (LBRACK RBRACK)*;

classOrInterfaceType:
    IDENTIFIER typeArguments? ('.' IDENTIFIER typeArguments?)*;

primitiveType: BOOLEAN | CHAR | BYTE | SHORT | INT | LONG | FLOAT | DOUBLE; // Added more primitives

typeArguments: '<' typeArgument (',' typeArgument)* '>';
typeArgument: type | '?' (('extends' | 'super') type)?;

typeList: type (COMMA type)*;

annotation: AT qualifiedName (LPAREN elementValuePairList? RPAREN)?;

elementValuePairList: elementValuePair (COMMA elementValuePair)*;
elementValuePair: IDENTIFIER ASSIGN elementValue | elementValue; // For key=value pairs or single value annotations
elementValue: expression | annotation | elementValueArrayInitializer; // An annotation value can be an expression, another annotation, or an array initializer
elementValueArrayInitializer: LBRACE (elementValue (COMMA elementValue)*)? COMMA? RBRACE;


// Renamed parameterList to formalParameters for clarity
formalParameters: formalParameter (COMMA formalParameter)*;
formalParameter: annotation* type variableDeclaratorId; // Use variableDeclaratorId
variableDeclaratorId: IDENTIFIER (LBRACK RBRACK)*; // Allow array parameters

qualifiedNameList: qualifiedName (COMMA qualifiedName)*;

// Use blockStatement within blocks for better structure
block: LBRACE blockStatement* RBRACE;

blockStatement:
    localVariableDeclarationStatement |
    statement |
    typeDeclaration; // Allow local classes

statement:
    block |
    ifStatement |
    whileStatement |
    forStatement |
    tryStatement |
    returnStatement |
    expressionStatement |
    switchStatement | // Added switch
    breakStatement |  // Added break
    continueStatement | // Added continue
    doWhileStatement | // Added do-while
    throwStatement | // Added throw
    synchronizedStatement | // Added synchronized
    ASSERT expression (':' expression)? SEMI | // Added assert
    SEMI // Empty statement
    ;

    // --- Added Switch Statement ---
    switchStatement: SWITCH LPAREN expression RPAREN LBRACE switchBlockStatementGroup* RBRACE;
    switchBlockStatementGroup: switchLabel+ blockStatement*;
    switchLabel: (CASE constantExpression | CASE enumConstantName | DEFAULT) COLON;
    constantExpression: expression; // Needs refinement for actual constant expressions
    enumConstantName: IDENTIFIER;
    // --- End Added Switch Statement ---

    // --- Added Break/Continue/DoWhile/Throw/Synchronized ---
    breakStatement: BREAK IDENTIFIER? SEMI;
    continueStatement: CONTINUE IDENTIFIER? SEMI;
    doWhileStatement: DO statement WHILE LPAREN expression RPAREN SEMI;
    throwStatement: THROW expression SEMI;
    synchronizedStatement: SYNCHRONIZED LPAREN expression RPAREN block;
    // --- End Added ---


localVariableDeclarationStatement: type variableDeclarator (COMMA variableDeclarator)* SEMI;

ifStatement: IF LPAREN expression RPAREN statement (ELSE statement)?;

whileStatement: WHILE LPAREN expression RPAREN statement;

forStatement: FOR LPAREN forControl RPAREN statement;
forControl:
    enhancedForControl |
    basicForControl;

enhancedForControl: type variableDeclaratorId COLON expression; // For-each loop

basicForControl:
    forInit? SEMI expression? SEMI forUpdate?;

forInit: localVariableDeclarationStatement | expressionList SEMI; // Corrected: expressionList needs SEMI here
forUpdate: expressionList;


tryStatement: 'try' block catchClause* ('finally' block)?; 
catchClause: 'catch' LPAREN type IDENTIFIER RPAREN block;

returnStatement: RETURN expression? SEMI;

expressionStatement: expression SEMI;


// --- Modified Expression Rule with Labels ---
expression:
    primary                                         # PrimaryExpr
    | expression LBRACK expression RBRACK           # ArrayAccessExpr
    // Use specific rule for method calls via dot
    | expression DOT IDENTIFIER LPAREN expressionList? RPAREN # DotMethodCallExpr
    | expression LPAREN expressionList? RPAREN      # MethodCallExpr // For cases like this() or super() or (expr)()
    | expression DOT IDENTIFIER                     # FieldAccessExpr
    | expression DOT THIS                           # DotThisExpr
    | expression DOT NEW typeArgumentsOrDiamond? IDENTIFIER arguments classBody? # InnerClassCreationExpr
    | expression DOT SUPER superSuffix              # DotSuperExpr
    | NEW creator                                   # NewCreatorExpr // Use modified creator
    | LPAREN type RPAREN expression                 # CastExpr
    | expression op=(MULT|DIV|MOD) expression       # MultiplicativeExpr
    | expression op=(PLUS|MINUS) expression         # AdditiveExpr
    // Shift operators (add if needed, check precedence)
    // | expression op=(LSHIFT | RSHIFT | URSHIFT) expression # ShiftExpr
    | expression op=(LT|GT|LE|GE) expression        # RelationalExpr
    | expression INSTANCEOF type                    # InstanceofExpr
    | expression op=(EQUAL|NOTEQUAL) expression     # EqualityExpr
    | expression op=BITAND expression               # BitwiseAndExpr
    | expression op=CARET expression                # BitwiseXorExpr
    | expression op=BITOR expression                # BitwiseOrExpr
    | expression op=AND expression                  # LogicalAndExpr
    | expression op=OR expression                   # LogicalOrExpr
    | expression '?' expression ':' expression      # TernaryExpr
    | expression op=(ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN |AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | LSHIFT_ASSIGN | RSHIFT_ASSIGN | URSHIFT_ASSIGN) expression # AssignmentExpr
    | expression (LT {not self.isTypeArgumentsAhead()}? | op=(GT | LE | GE)) expression        # RelationalExpr
    | prefix=('-'|'+'|'~'|'!') expression           # PrefixExpr
    | prefix=('++'|'--') expression                 # PreIncrementExpr
    | expression postfix=('++'|'--')                # PostIncrementExpr
    | lambdaExpression                              # LambdaExpr // Ensure defined
    ;

// --- Modified Creator Rules ---
creator:
    createdName (arrayCreatorRest| classCreatorRest);

createdName: // Helper rule for the type being created
    primitiveType |
    classOrInterfaceType;

typeArgumentsOrDiamond: '<' typeList? '>' ; // Allows <Type, Type> or <>


// --- Ensure these helper rules are defined correctly ---
arrayCreatorRest:
    LBRACK (RBRACK (LBRACK RBRACK)* arrayInitializer | expression RBRACK (LBRACK expression RBRACK)* (LBRACK RBRACK)*);

classCreatorRest:
    typeArgumentsOrDiamond? | // <…> ou <> |
    arguments |
    classBody?;

arguments: LPAREN expressionList? RPAREN;

classBody: LBRACE memberDeclaration* RBRACE;

expressionList: expression (COMMA expression)*;

lambdaExpression: formalParameters '->' (expression | block); // Basic lambda structure

superSuffix: arguments | DOT IDENTIFIER arguments?;

primary:
    LPAREN expression RPAREN |
    THIS |
    SUPER |
    literal |
    IDENTIFIER |
    // Handle qualified this, .class, etc.
    classOrInterfaceType DOT THIS | // Qualified this
    classOrInterfaceType DOT CLASS | // .class
    primitiveType DOT CLASS |
    VOID DOT CLASS |
    // Method call starting with IDENTIFIER needs careful handling with typeArguments
    // Let MethodCallExpr handle most calls. Primary focuses on basic elements.
    typeArguments IDENTIFIER LPAREN expressionList? RPAREN // Explicit Generic Method Invocation like <T>method() ? (Needs testing)
    ;
// --- End Modified Expression Rule ---

literal:
    DecimalIntegerLiteral |
    FloatingPointLiteral | 
    StringLiteral |
    CharacterLiteral |
    TRUE |
    FALSE |
    NULL;

arrayInitializer: LBRACE (variableInitializer (COMMA variableInitializer)*)? COMMA? RBRACE; // Allow trailing comma

// Lexer rules
// ADDED: IMPORT and PACKAGE tokens
IMPORT: 'import';
PACKAGE: 'package';

CLASS: 'class';
INTERFACE: 'interface'; // Added INTERFACE token
IMPLEMENTS: 'implements'; // Added IMPLEMENTS token
PUBLIC: 'public';
ENUM: 'enum';
PRIVATE: 'private';
PROTECTED: 'protected';
STATIC: 'static';
FINAL: 'final';
ABSTRACT: 'abstract'; 
SYNCHRONIZED: 'synchronized'; 
NATIVE: 'native'; 
STRICTFP: 'strictfp'; 
VOID: 'void';
BOOLEAN: 'boolean';
CHAR: 'char';
BYTE: 'byte';
SHORT: 'short'; 
INT: 'int';
LONG: 'long'; 
FLOAT: 'float'; 
DOUBLE: 'double'; 
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
NULL: 'null';
SWITCH: 'switch'; 
CASE: 'case';     
DEFAULT: 'default'; 
BREAK: 'break';   
CONTINUE: 'continue'; 
DO: 'do';         
THROW: 'throw';   
THROWS: 'throws'; 
ASSERT: 'assert'; 
NEW: 'new';       
INSTANCEOF: 'instanceof'; 
THIS: 'this';     
SUPER: 'super';   

// Operations
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%'; 
EQUAL: '==';
NOTEQUAL: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
ASSIGN: '=';
DOT: '.';
AND: '&&';
OR: '||';
INC: '++';
DEC: '--';
BITAND: '&'; 
BITOR: '|';  
CARET: '^';  
TILDE: '~';  
BANG: '!';   
ADD_ASSIGN: '+='; 
SUB_ASSIGN: '-='; 
MUL_ASSIGN: '*='; 
DIV_ASSIGN: '/='; 
MOD_ASSIGN: '%='; 
AND_ASSIGN: '&='; 
OR_ASSIGN: '|=';  
XOR_ASSIGN: '^='; 
LSHIFT_ASSIGN: '<<='; 
RSHIFT_ASSIGN: '>>='; 
URSHIFT_ASSIGN: '>>>='; 


// Separators & punctuation
LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';
SEMI: ';';
QUESTION: '?';
COLON: ':';
ELLIPSIS: '...'; // Added for varargs if needed
AT: '@';       // Added for annotations if needed

// Identifiers & literals
IDENTIFIER: [a-zA-Z$_][a-zA-Z0-9$_]*; // Allow $ and _
DecimalIntegerLiteral: [0-9]+[lL]?; // Allow L/l suffix
FloatingPointLiteral: // More complete float definition
    [0-9]+ '.' [0-9]* Exponent? [fFdD]? |
    '.' [0-9]+ Exponent? [fFdD]? |
    [0-9]+ Exponent [fFdD]? |
    [0-9]+ Exponent? [fFdD];
fragment Exponent: [eE] [+\-]? [0-9]+;

StringLiteral: '"' (~["\r\n\\] | EscapeSequence)* '"';
CharacterLiteral: '\'' (~['\r\n\\] | EscapeSequence) '\'';
fragment EscapeSequence: '\\' ([btnfr"'\\] | UnicodeEscape | OctalEscape); // More escapes
fragment UnicodeEscape: 'u'+ [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F];
fragment OctalEscape: '\\' [0-3]? [0-7]? [0-7];


// Skip whitespace and comments
WS: [ \t\r\n\f]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip; // Consider channel for documentation
LINE_COMMENT: '//' ~[\r\n]* -> skip;