# Translation Log for: `uploads\7df5c56e-e1c2-450b-ba3d-2e3a39c12326\source`
Model: `gemini-2.5-flash`


---

# Processing File: D:\Repositórios\JavaToPython-Transpiler-Web-app\uploads\7df5c56e-e1c2-450b-ba3d-2e3a39c12326\source\test_project\src\com\example\Main.java

## Original Java AST

```json
{
  "type": "CompilationUnit",
  "children": [
    {
      "type": "PackageDeclaration",
      "children": [
        {
          "type": "terminal",
          "text": "package",
          "token_type": "PACKAGE"
        },
        {
          "type": "QualifiedName",
          "children": [
            {
              "type": "terminal",
              "text": "com",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "example",
              "token_type": "IDENTIFIER"
            }
          ]
        },
        {
          "type": "terminal",
          "text": ";",
          "token_type": "SEMI"
        }
      ]
    },
    {
      "type": "ImportDeclaration",
      "children": [
        {
          "type": "terminal",
          "text": "import",
          "token_type": "IMPORT"
        },
        {
          "type": "QualifiedName",
          "children": [
            {
              "type": "terminal",
              "text": "com",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "example",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "model",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "User",
              "token_type": "IDENTIFIER"
            }
          ]
        },
        {
          "type": "terminal",
          "text": ";",
          "token_type": "SEMI"
        }
      ]
    },
    {
      "type": "ImportDeclaration",
      "children": [
        {
          "type": "terminal",
          "text": "import",
          "token_type": "IMPORT"
        },
        {
          "type": "QualifiedName",
          "children": [
            {
              "type": "terminal",
              "text": "com",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "example",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "service",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "UserService",
              "token_type": "IDENTIFIER"
            }
          ]
        },
        {
          "type": "terminal",
          "text": ";",
          "token_type": "SEMI"
        }
      ]
    },
    {
      "type": "TypeDeclaration",
      "children": [
        {
          "type": "ClassDeclaration",
          "children": [
            {
              "type": "Modifier",
              "children": [
                {
                  "type": "terminal",
                  "text": "public",
                  "token_type": "PUBLIC"
                }
              ]
            },
            {
              "type": "terminal",
              "text": "class",
              "token_type": "CLASS"
            },
            {
              "type": "terminal",
              "text": "Main",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": "{",
              "token_type": "LBRACE"
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "MethodDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "public",
                          "token_type": "PUBLIC"
                        }
                      ]
                    },
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "static",
                          "token_type": "STATIC"
                        }
                      ]
                    },
                    {
                      "type": "ReturnType",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "void",
                          "token_type": "VOID"
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "main",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "(",
                      "token_type": "LPAREN"
                    },
                    {
                      "type": "FormalParameters",
                      "children": [
                        {
                          "type": "FormalParameter",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "ClassOrInterfaceType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "String",
                                      "token_type": "IDENTIFIER"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": "[",
                                  "token_type": "LBRACK"
                                },
                                {
                                  "type": "terminal",
                                  "text": "]",
                                  "token_type": "RBRACK"
                                }
                              ]
                            },
                            {
                              "type": "VariableDeclaratorId",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "args",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": ")",
                      "token_type": "RPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "DotMethodCallExpr",
                                  "children": [
                                    {
                                      "type": "FieldAccessExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "System",
                                                  "token_type": "IDENTIFIER"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "out",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ".",
                                      "token_type": "DOT"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "println",
                                      "token_type": "IDENTIFIER"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "(",
                                      "token_type": "LPAREN"
                                    },
                                    {
                                      "type": "ExpressionList",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "Literal",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "\"Starting User Management System...\"",
                                                      "token_type": "StringLiteral"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ")",
                                      "token_type": "RPAREN"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "LocalVariableDeclarationStatement",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "ClassOrInterfaceType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "UserService",
                                      "token_type": "IDENTIFIER"
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "VariableDeclarator",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "service",
                                  "token_type": "IDENTIFIER"
                                },
                                {
                                  "type": "terminal",
                                  "text": "=",
                                  "token_type": "ASSIGN"
                                },
                                {
                                  "type": "VariableInitializer",
                                  "children": [
                                    {
                                      "type": "MethodCallExpr",
                                      "children": [
                                        {
                                          "type": "NewCreatorExpr",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "new",
                                              "token_type": "NEW"
                                            },
                                            {
                                              "type": "Creator",
                                              "children": [
                                                {
                                                  "type": "CreatedName",
                                                  "children": [
                                                    {
                                                      "type": "ClassOrInterfaceType",
                                                      "children": [
                                                        {
                                                          "type": "terminal",
                                                          "text": "UserService",
                                                          "token_type": "IDENTIFIER"
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                },
                                                {
                                                  "type": "ClassCreatorRest"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "(",
                                          "token_type": "LPAREN"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ")",
                                          "token_type": "RPAREN"
                                        }
                                      ]
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "terminal",
                              "text": ";",
                              "token_type": "SEMI"
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "DotMethodCallExpr",
                                  "children": [
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "service",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ".",
                                      "token_type": "DOT"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "createUser",
                                      "token_type": "IDENTIFIER"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "(",
                                      "token_type": "LPAREN"
                                    },
                                    {
                                      "type": "ExpressionList",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "Literal",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "\"Alice\"",
                                                      "token_type": "StringLiteral"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ",",
                                          "token_type": "COMMA"
                                        },
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "Literal",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "\"alice@example.com\"",
                                                      "token_type": "StringLiteral"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ")",
                                      "token_type": "RPAREN"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "DotMethodCallExpr",
                                  "children": [
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "service",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ".",
                                      "token_type": "DOT"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "createUser",
                                      "token_type": "IDENTIFIER"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "(",
                                      "token_type": "LPAREN"
                                    },
                                    {
                                      "type": "ExpressionList",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "Literal",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "\"Bob\"",
                                                      "token_type": "StringLiteral"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ",",
                                          "token_type": "COMMA"
                                        },
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "Literal",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "\"bob@example.com\"",
                                                      "token_type": "StringLiteral"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ")",
                                      "token_type": "RPAREN"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "DotMethodCallExpr",
                                  "children": [
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "service",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ".",
                                      "token_type": "DOT"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "printAllUsers",
                                      "token_type": "IDENTIFIER"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "(",
                                      "token_type": "LPAREN"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ")",
                                      "token_type": "RPAREN"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "DotMethodCallExpr",
                                  "children": [
                                    {
                                      "type": "FieldAccessExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "System",
                                                  "token_type": "IDENTIFIER"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "out",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ".",
                                      "token_type": "DOT"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "println",
                                      "token_type": "IDENTIFIER"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "(",
                                      "token_type": "LPAREN"
                                    },
                                    {
                                      "type": "ExpressionList",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "Literal",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "\"\\nSearching for user with ID 1...\"",
                                                      "token_type": "StringLiteral"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ")",
                                      "token_type": "RPAREN"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "LocalVariableDeclarationStatement",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "ClassOrInterfaceType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "User",
                                      "token_type": "IDENTIFIER"
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "VariableDeclarator",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "foundUser",
                                  "token_type": "IDENTIFIER"
                                },
                                {
                                  "type": "terminal",
                                  "text": "=",
                                  "token_type": "ASSIGN"
                                },
                                {
                                  "type": "VariableInitializer",
                                  "children": [
                                    {
                                      "type": "DotMethodCallExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "service",
                                                  "token_type": "IDENTIFIER"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "findUserById",
                                          "token_type": "IDENTIFIER"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "(",
                                          "token_type": "LPAREN"
                                        },
                                        {
                                          "type": "ExpressionList",
                                          "children": [
                                            {
                                              "type": "PrimaryExpr",
                                              "children": [
                                                {
                                                  "type": "Primary",
                                                  "children": [
                                                    {
                                                      "type": "Literal",
                                                      "children": [
                                                        {
                                                          "type": "terminal",
                                                          "text": "1",
                                                          "token_type": "DecimalIntegerLiteral"
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ")",
                                          "token_type": "RPAREN"
                                        }
                                      ]
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "terminal",
                              "text": ";",
                              "token_type": "SEMI"
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "IfStatement",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "if",
                                  "token_type": "IF"
                                },
                                {
                                  "type": "terminal",
                                  "text": "(",
                                  "token_type": "LPAREN"
                                },
                                {
                                  "type": "EqualityExpr",
                                  "children": [
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "foundUser",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "!=",
                                      "token_type": "NOTEQUAL"
                                    },
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "Literal",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "null",
                                                  "token_type": "NULL"
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ")",
                                  "token_type": "RPAREN"
                                },
                                {
                                  "type": "Statement",
                                  "children": [
                                    {
                                      "type": "Block",
                                      "children": [
                                        {
                                          "type": "terminal",
                                          "text": "{",
                                          "token_type": "LBRACE"
                                        },
                                        {
                                          "type": "BlockStatement",
                                          "children": [
                                            {
                                              "type": "Statement",
                                              "children": [
                                                {
                                                  "type": "ExpressionStatement",
                                                  "children": [
                                                    {
                                                      "type": "DotMethodCallExpr",
                                                      "children": [
                                                        {
                                                          "type": "FieldAccessExpr",
                                                          "children": [
                                                            {
                                                              "type": "PrimaryExpr",
                                                              "children": [
                                                                {
                                                                  "type": "Primary",
                                                                  "children": [
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": "System",
                                                                      "token_type": "IDENTIFIER"
                                                                    }
                                                                  ]
                                                                }
                                                              ]
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": ".",
                                                              "token_type": "DOT"
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": "out",
                                                              "token_type": "IDENTIFIER"
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": ".",
                                                          "token_type": "DOT"
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": "println",
                                                          "token_type": "IDENTIFIER"
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": "(",
                                                          "token_type": "LPAREN"
                                                        },
                                                        {
                                                          "type": "ExpressionList",
                                                          "children": [
                                                            {
                                                              "type": "AdditiveExpr",
                                                              "children": [
                                                                {
                                                                  "type": "PrimaryExpr",
                                                                  "children": [
                                                                    {
                                                                      "type": "Primary",
                                                                      "children": [
                                                                        {
                                                                          "type": "Literal",
                                                                          "children": [
                                                                            {
                                                                              "type": "terminal",
                                                                              "text": "\"Found: \"",
                                                                              "token_type": "StringLiteral"
                                                                            }
                                                                          ]
                                                                        }
                                                                      ]
                                                                    }
                                                                  ]
                                                                },
                                                                {
                                                                  "type": "terminal",
                                                                  "text": "+",
                                                                  "token_type": "PLUS"
                                                                },
                                                                {
                                                                  "type": "DotMethodCallExpr",
                                                                  "children": [
                                                                    {
                                                                      "type": "PrimaryExpr",
                                                                      "children": [
                                                                        {
                                                                          "type": "Primary",
                                                                          "children": [
                                                                            {
                                                                              "type": "terminal",
                                                                              "text": "foundUser",
                                                                              "token_type": "IDENTIFIER"
                                                                            }
                                                                          ]
                                                                        }
                                                                      ]
                                                                    },
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": ".",
                                                                      "token_type": "DOT"
                                                                    },
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": "getName",
                                                                      "token_type": "IDENTIFIER"
                                                                    },
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": "(",
                                                                      "token_type": "LPAREN"
                                                                    },
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": ")",
                                                                      "token_type": "RPAREN"
                                                                    }
                                                                  ]
                                                                }
                                                              ]
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": ")",
                                                          "token_type": "RPAREN"
                                                        }
                                                      ]
                                                    },
                                                    {
                                                      "type": "terminal",
                                                      "text": ";",
                                                      "token_type": "SEMI"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "}",
                                          "token_type": "RBRACE"
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": "else",
                                  "token_type": "ELSE"
                                },
                                {
                                  "type": "Statement",
                                  "children": [
                                    {
                                      "type": "Block",
                                      "children": [
                                        {
                                          "type": "terminal",
                                          "text": "{",
                                          "token_type": "LBRACE"
                                        },
                                        {
                                          "type": "BlockStatement",
                                          "children": [
                                            {
                                              "type": "Statement",
                                              "children": [
                                                {
                                                  "type": "ExpressionStatement",
                                                  "children": [
                                                    {
                                                      "type": "DotMethodCallExpr",
                                                      "children": [
                                                        {
                                                          "type": "FieldAccessExpr",
                                                          "children": [
                                                            {
                                                              "type": "PrimaryExpr",
                                                              "children": [
                                                                {
                                                                  "type": "Primary",
                                                                  "children": [
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": "System",
                                                                      "token_type": "IDENTIFIER"
                                                                    }
                                                                  ]
                                                                }
                                                              ]
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": ".",
                                                              "token_type": "DOT"
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": "out",
                                                              "token_type": "IDENTIFIER"
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": ".",
                                                          "token_type": "DOT"
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": "println",
                                                          "token_type": "IDENTIFIER"
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": "(",
                                                          "token_type": "LPAREN"
                                                        },
                                                        {
                                                          "type": "ExpressionList",
                                                          "children": [
                                                            {
                                                              "type": "PrimaryExpr",
                                                              "children": [
                                                                {
                                                                  "type": "Primary",
                                                                  "children": [
                                                                    {
                                                                      "type": "Literal",
                                                                      "children": [
                                                                        {
                                                                          "type": "terminal",
                                                                          "text": "\"User with ID 1 not found.\"",
                                                                          "token_type": "StringLiteral"
                                                                        }
                                                                      ]
                                                                    }
                                                                  ]
                                                                }
                                                              ]
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": ")",
                                                          "token_type": "RPAREN"
                                                        }
                                                      ]
                                                    },
                                                    {
                                                      "type": "terminal",
                                                      "text": ";",
                                                      "token_type": "SEMI"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "}",
                                          "token_type": "RBRACE"
                                        }
                                      ]
                                    }
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "DotMethodCallExpr",
                                  "children": [
                                    {
                                      "type": "FieldAccessExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "System",
                                                  "token_type": "IDENTIFIER"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "out",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ".",
                                      "token_type": "DOT"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "println",
                                      "token_type": "IDENTIFIER"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "(",
                                      "token_type": "LPAREN"
                                    },
                                    {
                                      "type": "ExpressionList",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "Literal",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "\"\\nSystem finished.\"",
                                                      "token_type": "StringLiteral"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ")",
                                      "token_type": "RPAREN"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "}",
                      "token_type": "RBRACE"
                    }
                  ]
                }
              ]
            },
            {
              "type": "terminal",
              "text": "}",
              "token_type": "RBRACE"
            }
          ]
        }
      ]
    },
    {
      "type": "terminal",
      "text": "<EOF>",
      "token_type": "UNKNOWN_TOKEN_TYPE_-1"
    }
  ]
}
```

## Framework Analysis

```json
{
  "frameworks": [],
  "spring_endpoints": [],
  "hibernate_entities": [],
  "struts_actions": [],
  "gwt_services": []
}
```

Translation required **1** chunk(s).

## AI-Generated Python ASTs (JSON)

### Chunk 1:

```json
{
  "type": "Module",
  "body": [
    {
      "type": "ImportFrom",
      "module": "com.example.model.User",
      "names": [
        {
          "type": "alias",
          "name": "User",
          "asname": null
        }
      ],
      "level": 0
    },
    {
      "type": "ImportFrom",
      "module": "com.example.service.UserService",
      "names": [
        {
          "type": "alias",
          "name": "UserService",
          "asname": null
        }
      ],
      "level": 0
    },
    {
      "type": "ImportFrom",
      "module": "typing",
      "names": [
        {
          "type": "alias",
          "name": "Optional",
          "asname": null
        }
      ],
      "level": 0
    },
    {
      "type": "ClassDef",
      "name": "Main",
      "bases": [],
      "keywords": [],
      "decorator_list": [],
      "body": [
        {
          "type": "FunctionDef",
          "name": "main",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              {
                "type": "arg",
                "arg": "args",
                "annotation": {
                  "type": "Subscript",
                  "value": {
                    "type": "Name",
                    "id": "list",
                    "ctx": "Load"
                  },
                  "slice": {
                    "type": "Name",
                    "id": "str",
                    "ctx": "Load"
                  },
                  "ctx": "Load"
                }
              }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Expr",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Name",
                  "id": "print",
                  "ctx": "Load"
                },
                "args": [
                  {
                    "type": "Constant",
                    "value": "Starting User Management System...",
                    "kind": null
                  }
                ],
                "keywords": []
              }
            },
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Name",
                  "id": "service",
                  "ctx": "Store"
                }
              ],
              "value": {
                "type": "Call",
                "func": {
                  "type": "Name",
                  "id": "UserService",
                  "ctx": "Load"
                },
                "args": [],
                "keywords": []
              }
            },
            {
              "type": "Expr",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Attribute",
                  "value": {
                    "type": "Name",
                    "id": "service",
                    "ctx": "Load"
                  },
                  "attr": "create_user",
                  "ctx": "Load"
                },
                "args": [
                  {
                    "type": "Constant",
                    "value": "Alice",
                    "kind": null
                  },
                  {
                    "type": "Constant",
                    "value": "alice@example.com",
                    "kind": null
                  }
                ],
                "keywords": []
              }
            },
            {
              "type": "Expr",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Attribute",
                  "value": {
                    "type": "Name",
                    "id": "service",
                    "ctx": "Load"
                  },
                  "attr": "create_user",
                  "ctx": "Load"
                },
                "args": [
                  {
                    "type": "Constant",
                    "value": "Bob",
                    "kind": null
                  },
                  {
                    "type": "Constant",
                    "value": "bob@example.com",
                    "kind": null
                  }
                ],
                "keywords": []
              }
            },
            {
              "type": "Expr",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Attribute",
                  "value": {
                    "type": "Name",
                    "id": "service",
                    "ctx": "Load"
                  },
                  "attr": "print_all_users",
                  "ctx": "Load"
                },
                "args": [],
                "keywords": []
              }
            },
            {
              "type": "Expr",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Name",
                  "id": "print",
                  "ctx": "Load"
                },
                "args": [
                  {
                    "type": "Constant",
                    "value": "\nSearching for user with ID 1...",
                    "kind": null
                  }
                ],
                "keywords": []
              }
            },
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Name",
                  "id": "found_user",
                  "ctx": "Store"
                }
              ],
              "value": {
                "type": "Call",
                "func": {
                  "type": "Attribute",
                  "value": {
                    "type": "Name",
                    "id": "service",
                    "ctx": "Load"
                  },
                  "attr": "find_user_by_id",
                  "ctx": "Load"
                },
                "args": [
                  {
                    "type": "Constant",
                    "value": 1,
                    "kind": null
                  }
                ],
                "keywords": []
              }
            },
            {
              "type": "If",
              "test": {
                "type": "Compare",
                "left": {
                  "type": "Name",
                  "id": "found_user",
                  "ctx": "Load"
                },
                "ops": [
                  {
                    "type": "IsNot"
                  }
                ],
                "comparators": [
                  {
                    "type": "Constant",
                    "value": null,
                    "kind": null
                  }
                ]
              },
              "body": [
                {
                  "type": "Expr",
                  "value": {
                    "type": "Call",
                    "func": {
                      "type": "Name",
                      "id": "print",
                      "ctx": "Load"
                    },
                    "args": [
                      {
                        "type": "JoinedStr",
                        "values": [
                          {
                            "type": "Constant",
                            "value": "Found: ",
                            "kind": null
                          },
                          {
                            "type": "FormattedValue",
                            "value": {
                              "type": "Call",
                              "func": {
                                "type": "Attribute",
                                "value": {
                                  "type": "Name",
                                  "id": "found_user",
                                  "ctx": "Load"
                                },
                                "attr": "get_name",
                                "ctx": "Load"
                              },
                              "args": [],
                              "keywords": []
                            },
                            "conversion": -1,
                            "format_spec": null
                          }
                        ]
                      }
                    ],
                    "keywords": []
                  }
                }
              ],
              "orelse": [
                {
                  "type": "Expr",
                  "value": {
                    "type": "Call",
                    "func": {
                      "type": "Name",
                      "id": "print",
                      "ctx": "Load"
                    },
                    "args": [
                      {
                        "type": "Constant",
                        "value": "User with ID 1 not found.",
                        "kind": null
                      }
                    ],
                    "keywords": []
                  }
                }
              ]
            },
            {
              "type": "Expr",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Name",
                  "id": "print",
                  "ctx": "Load"
                },
                "args": [
                  {
                    "type": "Constant",
                    "value": "\nSystem finished.",
                    "kind": null
                  }
                ],
                "keywords": []
              }
            }
          ],
          "decorator_list": [
            {
              "type": "Name",
              "id": "staticmethod",
              "ctx": "Load"
            }
          ],
          "returns": null
        }
      ],
      "type_comment": null
    },
    {
      "type": "If",
      "test": {
        "type": "Compare",
        "left": {
          "type": "Name",
          "id": "__name__",
          "ctx": "Load"
        },
        "ops": [
          {
            "type": "Eq"
          }
        ],
        "comparators": [
          {
            "type": "Constant",
            "value": "__main__",
            "kind": null
          }
        ]
      },
      "body": [
        {
          "type": "Expr",
          "value": {
            "type": "Call",
            "func": {
              "type": "Attribute",
              "value": {
                "type": "Name",
                "id": "Main",
                "ctx": "Load"
              },
              "attr": "main",
              "ctx": "Load"
            },
            "args": [
              {
                "type": "List",
                "elts": [],
                "ctx": "Load"
              }
            ],
            "keywords": []
          }
        }
      ],
      "orelse": []
    }
  ],
  "type_ignores": []
}
```


## Unit Test Generation and Execution

No testable functions were found. Skipping test generation.

**Overall Test Result: ✅ All generated tests passed.**

## Final Generated Python Code

```python
# Unit test result: ✅ PASSED
from com.example.model.User import User
from com.example.service.UserService import UserService
from typing import Optional

class Main:

    @staticmethod
    def main(args: list[str]):
        print('Starting User Management System...')
        service = UserService()
        service.create_user('Alice', 'alice@example.com')
        service.create_user('Bob', 'bob@example.com')
        service.print_all_users()
        print('\nSearching for user with ID 1...')
        found_user = service.find_user_by_id(1)
        if found_user is not None:
            print(f'Found: {found_user.get_name()}')
        else:
            print('User with ID 1 not found.')
        print('\nSystem finished.')
if __name__ == '__main__':
    Main.main([])
```


---

# Processing File: D:\Repositórios\JavaToPython-Transpiler-Web-app\uploads\7df5c56e-e1c2-450b-ba3d-2e3a39c12326\source\test_project\src\com\example\model\User.java

## Original Java AST

```json
{
  "type": "CompilationUnit",
  "children": [
    {
      "type": "TypeDeclaration",
      "children": [
        {
          "type": "ClassDeclaration",
          "children": [
            {
              "type": "Modifier",
              "children": [
                {
                  "type": "terminal",
                  "text": "public",
                  "token_type": "PUBLIC"
                }
              ]
            },
            {
              "type": "terminal",
              "text": "class",
              "token_type": "CLASS"
            },
            {
              "type": "terminal",
              "text": "User",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": "{",
              "token_type": "LBRACE"
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "FieldDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "private",
                          "token_type": "PRIVATE"
                        }
                      ]
                    },
                    {
                      "type": "Type",
                      "children": [
                        {
                          "type": "PrimitiveType",
                          "children": [
                            {
                              "type": "terminal",
                              "text": "int",
                              "token_type": "INT"
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "VariableDeclarator",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "id",
                          "token_type": "IDENTIFIER"
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": ";",
                      "token_type": "SEMI"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "FieldDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "private",
                          "token_type": "PRIVATE"
                        }
                      ]
                    },
                    {
                      "type": "Type",
                      "children": [
                        {
                          "type": "ClassOrInterfaceType",
                          "children": [
                            {
                              "type": "terminal",
                              "text": "String",
                              "token_type": "IDENTIFIER"
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "VariableDeclarator",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "name",
                          "token_type": "IDENTIFIER"
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": ";",
                      "token_type": "SEMI"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "FieldDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "private",
                          "token_type": "PRIVATE"
                        }
                      ]
                    },
                    {
                      "type": "Type",
                      "children": [
                        {
                          "type": "ClassOrInterfaceType",
                          "children": [
                            {
                              "type": "terminal",
                              "text": "String",
                              "token_type": "IDENTIFIER"
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "VariableDeclarator",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "email",
                          "token_type": "IDENTIFIER"
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": ";",
                      "token_type": "SEMI"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "ConstructorDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "public",
                          "token_type": "PUBLIC"
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "User",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "(",
                      "token_type": "LPAREN"
                    },
                    {
                      "type": "FormalParameters",
                      "children": [
                        {
                          "type": "FormalParameter",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "PrimitiveType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "int",
                                      "token_type": "INT"
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "VariableDeclaratorId",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "id",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        },
                        {
                          "type": "terminal",
                          "text": ",",
                          "token_type": "COMMA"
                        },
                        {
                          "type": "FormalParameter",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "ClassOrInterfaceType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "String",
                                      "token_type": "IDENTIFIER"
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "VariableDeclaratorId",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "name",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        },
                        {
                          "type": "terminal",
                          "text": ",",
                          "token_type": "COMMA"
                        },
                        {
                          "type": "FormalParameter",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "ClassOrInterfaceType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "String",
                                      "token_type": "IDENTIFIER"
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "VariableDeclaratorId",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "email",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": ")",
                      "token_type": "RPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "AssignmentExpr",
                                  "children": [
                                    {
                                      "type": "FieldAccessExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "this",
                                                  "token_type": "THIS"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "id",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "=",
                                      "token_type": "ASSIGN"
                                    },
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "id",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "AssignmentExpr",
                                  "children": [
                                    {
                                      "type": "FieldAccessExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "this",
                                                  "token_type": "THIS"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "name",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "=",
                                      "token_type": "ASSIGN"
                                    },
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "name",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "AssignmentExpr",
                                  "children": [
                                    {
                                      "type": "FieldAccessExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "this",
                                                  "token_type": "THIS"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "email",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "=",
                                      "token_type": "ASSIGN"
                                    },
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "email",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "}",
                      "token_type": "RBRACE"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "MethodDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "public",
                          "token_type": "PUBLIC"
                        }
                      ]
                    },
                    {
                      "type": "ReturnType",
                      "children": [
                        {
                          "type": "Type",
                          "children": [
                            {
                              "type": "PrimitiveType",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "int",
                                  "token_type": "INT"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "getId",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "(",
                      "token_type": "LPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": ")",
                      "token_type": "RPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ReturnStatement",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "return",
                                  "token_type": "RETURN"
                                },
                                {
                                  "type": "PrimaryExpr",
                                  "children": [
                                    {
                                      "type": "Primary",
                                      "children": [
                                        {
                                          "type": "terminal",
                                          "text": "id",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "}",
                      "token_type": "RBRACE"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "MethodDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "public",
                          "token_type": "PUBLIC"
                        }
                      ]
                    },
                    {
                      "type": "ReturnType",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "void",
                          "token_type": "VOID"
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "setId",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "(",
                      "token_type": "LPAREN"
                    },
                    {
                      "type": "FormalParameters",
                      "children": [
                        {
                          "type": "FormalParameter",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "PrimitiveType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "int",
                                      "token_type": "INT"
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "VariableDeclaratorId",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "id",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": ")",
                      "token_type": "RPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "AssignmentExpr",
                                  "children": [
                                    {
                                      "type": "FieldAccessExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "this",
                                                  "token_type": "THIS"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "id",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "=",
                                      "token_type": "ASSIGN"
                                    },
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "id",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "}",
                      "token_type": "RBRACE"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "MethodDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "public",
                          "token_type": "PUBLIC"
                        }
                      ]
                    },
                    {
                      "type": "ReturnType",
                      "children": [
                        {
                          "type": "Type",
                          "children": [
                            {
                              "type": "ClassOrInterfaceType",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "String",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "getName",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "(",
                      "token_type": "LPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": ")",
                      "token_type": "RPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ReturnStatement",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "return",
                                  "token_type": "RETURN"
                                },
                                {
                                  "type": "PrimaryExpr",
                                  "children": [
                                    {
                                      "type": "Primary",
                                      "children": [
                                        {
                                          "type": "terminal",
                                          "text": "name",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "}",
                      "token_type": "RBRACE"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "MethodDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "public",
                          "token_type": "PUBLIC"
                        }
                      ]
                    },
                    {
                      "type": "ReturnType",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "void",
                          "token_type": "VOID"
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "setName",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "(",
                      "token_type": "LPAREN"
                    },
                    {
                      "type": "FormalParameters",
                      "children": [
                        {
                          "type": "FormalParameter",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "ClassOrInterfaceType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "String",
                                      "token_type": "IDENTIFIER"
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "VariableDeclaratorId",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "name",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": ")",
                      "token_type": "RPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "AssignmentExpr",
                                  "children": [
                                    {
                                      "type": "FieldAccessExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "this",
                                                  "token_type": "THIS"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "name",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "=",
                                      "token_type": "ASSIGN"
                                    },
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "name",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "}",
                      "token_type": "RBRACE"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "MethodDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "public",
                          "token_type": "PUBLIC"
                        }
                      ]
                    },
                    {
                      "type": "ReturnType",
                      "children": [
                        {
                          "type": "Type",
                          "children": [
                            {
                              "type": "ClassOrInterfaceType",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "String",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "getEmail",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "(",
                      "token_type": "LPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": ")",
                      "token_type": "RPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ReturnStatement",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "return",
                                  "token_type": "RETURN"
                                },
                                {
                                  "type": "PrimaryExpr",
                                  "children": [
                                    {
                                      "type": "Primary",
                                      "children": [
                                        {
                                          "type": "terminal",
                                          "text": "email",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "}",
                      "token_type": "RBRACE"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "MethodDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "public",
                          "token_type": "PUBLIC"
                        }
                      ]
                    },
                    {
                      "type": "ReturnType",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "void",
                          "token_type": "VOID"
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "setEmail",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "(",
                      "token_type": "LPAREN"
                    },
                    {
                      "type": "FormalParameters",
                      "children": [
                        {
                          "type": "FormalParameter",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "ClassOrInterfaceType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "String",
                                      "token_type": "IDENTIFIER"
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "VariableDeclaratorId",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "email",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": ")",
                      "token_type": "RPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "AssignmentExpr",
                                  "children": [
                                    {
                                      "type": "FieldAccessExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "this",
                                                  "token_type": "THIS"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "email",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "=",
                                      "token_type": "ASSIGN"
                                    },
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "email",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "}",
                      "token_type": "RBRACE"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "MethodDeclaration",
                  "children": [
                    {
                      "type": "Annotation",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "@",
                          "token_type": "AT"
                        },
                        {
                          "type": "QualifiedName",
                          "children": [
                            {
                              "type": "terminal",
                              "text": "Override",
                              "token_type": "IDENTIFIER"
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "public",
                          "token_type": "PUBLIC"
                        }
                      ]
                    },
                    {
                      "type": "ReturnType",
                      "children": [
                        {
                          "type": "Type",
                          "children": [
                            {
                              "type": "ClassOrInterfaceType",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "String",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "toString",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "(",
                      "token_type": "LPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": ")",
                      "token_type": "RPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ReturnStatement",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "return",
                                  "token_type": "RETURN"
                                },
                                {
                                  "type": "DotMethodCallExpr",
                                  "children": [
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "String",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ".",
                                      "token_type": "DOT"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "format",
                                      "token_type": "IDENTIFIER"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "(",
                                      "token_type": "LPAREN"
                                    },
                                    {
                                      "type": "ExpressionList",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "Literal",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "\"User[ID=%d, Name='%s', Email='%s']\"",
                                                      "token_type": "StringLiteral"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ",",
                                          "token_type": "COMMA"
                                        },
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "id",
                                                  "token_type": "IDENTIFIER"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ",",
                                          "token_type": "COMMA"
                                        },
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "name",
                                                  "token_type": "IDENTIFIER"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ",",
                                          "token_type": "COMMA"
                                        },
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "email",
                                                  "token_type": "IDENTIFIER"
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ")",
                                      "token_type": "RPAREN"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "}",
                      "token_type": "RBRACE"
                    }
                  ]
                }
              ]
            },
            {
              "type": "terminal",
              "text": "}",
              "token_type": "RBRACE"
            }
          ]
        }
      ]
    },
    {
      "type": "terminal",
      "text": "<EOF>",
      "token_type": "UNKNOWN_TOKEN_TYPE_-1"
    }
  ]
}
```

## Framework Analysis

```json
{
  "frameworks": [],
  "spring_endpoints": [],
  "hibernate_entities": [],
  "struts_actions": [],
  "gwt_services": []
}
```

Translation required **2** chunk(s).

## AI-Generated Python ASTs (JSON)

### Chunk 1:

```json
{
  "type": "Module",
  "body": [
    {
      "type": "ClassDef",
      "name": "User",
      "bases": [],
      "keywords": [],
      "decorator_list": [],
      "body": [
        {
          "type": "AnnAssign",
          "target": {
            "type": "Name",
            "id": "id",
            "ctx": "Store"
          },
          "annotation": {
            "type": "Name",
            "id": "int",
            "ctx": "Load"
          },
          "value": null,
          "simple": 1
        },
        {
          "type": "AnnAssign",
          "target": {
            "type": "Name",
            "id": "name",
            "ctx": "Store"
          },
          "annotation": {
            "type": "Name",
            "id": "str",
            "ctx": "Load"
          },
          "value": null,
          "simple": 1
        },
        {
          "type": "AnnAssign",
          "target": {
            "type": "Name",
            "id": "email",
            "ctx": "Store"
          },
          "annotation": {
            "type": "Name",
            "id": "str",
            "ctx": "Load"
          },
          "value": null,
          "simple": 1
        },
        {
          "type": "FunctionDef",
          "name": "__init__",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              {
                "type": "arg",
                "arg": "self",
                "annotation": null
              },
              {
                "type": "arg",
                "arg": "id",
                "annotation": {
                  "type": "Name",
                  "id": "int",
                  "ctx": "Load"
                }
              },
              {
                "type": "arg",
                "arg": "name",
                "annotation": {
                  "type": "Name",
                  "id": "str",
                  "ctx": "Load"
                }
              },
              {
                "type": "arg",
                "arg": "email",
                "annotation": {
                  "type": "Name",
                  "id": "str",
                  "ctx": "Load"
                }
              }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Attribute",
                  "value": {
                    "type": "Name",
                    "id": "self",
                    "ctx": "Load"
                  },
                  "attr": "id",
                  "ctx": "Store"
                }
              ],
              "value": {
                "type": "Name",
                "id": "id",
                "ctx": "Load"
              }
            },
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Attribute",
                  "value": {
                    "type": "Name",
                    "id": "self",
                    "ctx": "Load"
                  },
                  "attr": "name",
                  "ctx": "Store"
                }
              ],
              "value": {
                "type": "Name",
                "id": "name",
                "ctx": "Load"
              }
            },
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Attribute",
                  "value": {
                    "type": "Name",
                    "id": "self",
                    "ctx": "Load"
                  },
                  "attr": "email",
                  "ctx": "Store"
                }
              ],
              "value": {
                "type": "Name",
                "id": "email",
                "ctx": "Load"
              }
            }
          ],
          "decorator_list": [],
          "returns": null
        },
        {
          "type": "FunctionDef",
          "name": "get_id",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              {
                "type": "arg",
                "arg": "self",
                "annotation": null
              }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Return",
              "value": {
                "type": "Attribute",
                "value": {
                  "type": "Name",
                  "id": "self",
                  "ctx": "Load"
                },
                "attr": "id",
                "ctx": "Load"
              }
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Name",
            "id": "int",
            "ctx": "Load"
          }
        },
        {
          "type": "FunctionDef",
          "name": "set_id",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              {
                "type": "arg",
                "arg": "self",
                "annotation": null
              },
              {
                "type": "arg",
                "arg": "id",
                "annotation": {
                  "type": "Name",
                  "id": "int",
                  "ctx": "Load"
                }
              }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Attribute",
                  "value": {
                    "type": "Name",
                    "id": "self",
                    "ctx": "Load"
                  },
                  "attr": "id",
                  "ctx": "Store"
                }
              ],
              "value": {
                "type": "Name",
                "id": "id",
                "ctx": "Load"
              }
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Constant",
            "value": null,
            "kind": null
          }
        },
        {
          "type": "FunctionDef",
          "name": "get_name",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              {
                "type": "arg",
                "arg": "self",
                "annotation": null
              }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Return",
              "value": {
                "type": "Attribute",
                "value": {
                  "type": "Name",
                  "id": "self",
                  "ctx": "Load"
                },
                "attr": "name",
                "ctx": "Load"
              }
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Name",
            "id": "str",
            "ctx": "Load"
          }
        },
        {
          "type": "FunctionDef",
          "name": "set_name",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              {
                "type": "arg",
                "arg": "self",
                "annotation": null
              },
              {
                "type": "arg",
                "arg": "name",
                "annotation": {
                  "type": "Name",
                  "id": "str",
                  "ctx": "Load"
                }
              }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Attribute",
                  "value": {
                    "type": "Name",
                    "id": "self",
                    "ctx": "Load"
                  },
                  "attr": "name",
                  "ctx": "Store"
                }
              ],
              "value": {
                "type": "Name",
                "id": "name",
                "ctx": "Load"
              }
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Constant",
            "value": null,
            "kind": null
          }
        },
        {
          "type": "FunctionDef",
          "name": "get_email",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              {
                "type": "arg",
                "arg": "self",
                "annotation": null
              }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Return",
              "value": {
                "type": "Attribute",
                "value": {
                  "type": "Name",
                  "id": "self",
                  "ctx": "Load"
                },
                "attr": "email",
                "ctx": "Load"
              }
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Name",
            "id": "str",
            "ctx": "Load"
          }
        },
        {
          "type": "FunctionDef",
          "name": "set_email",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              {
                "type": "arg",
                "arg": "self",
                "annotation": null
              },
              {
                "type": "arg",
                "arg": "email",
                "annotation": {
                  "type": "Name",
                  "id": "str",
                  "ctx": "Load"
                }
              }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Attribute",
                  "value": {
                    "type": "Name",
                    "id": "self",
                    "ctx": "Load"
                  },
                  "attr": "email",
                  "ctx": "Store"
                }
              ],
              "value": {
                "type": "Name",
                "id": "email",
                "ctx": "Load"
              }
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Constant",
            "value": null,
            "kind": null
          }
        }
      ],
      "lineno": null,
      "col_offset": null
    }
  ],
  "type_ignores": []
}
```

### Chunk 2:

```json
{
  "type": "Module",
  "body": [
    {
      "type": "ClassDef",
      "name": "User",
      "bases": [],
      "keywords": [],
      "decorator_list": [],
      "body": [
        {
          "type": "FunctionDef",
          "name": "__str__",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              {
                "type": "arg",
                "arg": "self",
                "annotation": null
              }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Return",
              "value": {
                "type": "JoinedStr",
                "values": [
                  {
                    "type": "Constant",
                    "value": "User[ID=",
                    "kind": null
                  },
                  {
                    "type": "FormattedValue",
                    "value": {
                      "type": "Attribute",
                      "value": {
                        "type": "Name",
                        "id": "self",
                        "ctx": "Load"
                      },
                      "attr": "id",
                      "ctx": "Load"
                    },
                    "conversion": -1,
                    "format_spec": null
                  },
                  {
                    "type": "Constant",
                    "value": ", Name='",
                    "kind": null
                  },
                  {
                    "type": "FormattedValue",
                    "value": {
                      "type": "Attribute",
                      "value": {
                        "type": "Name",
                        "id": "self",
                        "ctx": "Load"
                      },
                      "attr": "name",
                      "ctx": "Load"
                    },
                    "conversion": -1,
                    "format_spec": null
                  },
                  {
                    "type": "Constant",
                    "value": "', Email='",
                    "kind": null
                  },
                  {
                    "type": "FormattedValue",
                    "value": {
                      "type": "Attribute",
                      "value": {
                        "type": "Name",
                        "id": "self",
                        "ctx": "Load"
                      },
                      "attr": "email",
                      "ctx": "Load"
                    },
                    "conversion": -1,
                    "format_spec": null
                  },
                  {
                    "type": "Constant",
                    "value": "']",
                    "kind": null
                  }
                ]
              }
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Name",
            "id": "str",
            "ctx": "Load"
          }
        }
      ]
    }
  ],
  "type_ignores": []
}
```


## Unit Test Generation and Execution

### Testing `User.get_id`

**AI-Generated Test Script:**

```python
import unittest
from temp_subject_for_test import User

class TestUserGetId(unittest.TestCase):

    def test_get_id_positive(self):
        """
        Test get_id with a positive integer ID.
        """
        user = User(101, "Alice", "alice@example.com")
        self.assertEqual(user.get_id(), 101)

    def test_get_id_zero(self):
        """
        Test get_id with an ID of zero.
        """
        user = User(0, "Bob", "bob@example.com")
        self.assertEqual(user.get_id(), 0)

    def test_get_id_negative(self):
        """
        Test get_id with a negative integer ID.
        """
        user = User(-50, "Charlie", "charlie@example.com")
        self.assertEqual(user.get_id(), -50)

    def test_get_id_after_set_id(self):
        """
        Test get_id after the ID has been changed using set_id.
        """
        user = User(1, "David", "david@example.com")
        self.assertEqual(user.get_id(), 1)
        user.set_id(999)
        self.assertEqual(user.get_id(), 999)
        user.set_id(-123)
        self.assertEqual(user.get_id(), -123)

if __name__ == '__main__':
    unittest.main()
```

**Test Execution Results:**

```
❌ FAILED

Stderr:
EEEE
======================================================================
ERROR: test_get_id_after_set_id (__main__.TestUserGetId)
Test get_id after the ID has been changed using set_id.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Reposit�rios\JavaToPython-Transpiler-Web-app\outputs\7df5c56e-e1c2-450b-ba3d-2e3a39c12326\source\temp_test_User.get_id.py", line 31, in test_get_id_after_set_id
    user = User(1, "David", "david@example.com")
TypeError: User() takes no arguments

======================================================================
ERROR: test_get_id_negative (__main__.TestUserGetId)
Test get_id with a negative integer ID.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Reposit�rios\JavaToPython-Transpiler-Web-app\outputs\7df5c56e-e1c2-450b-ba3d-2e3a39c12326\source\temp_test_User.get_id.py", line 24, in test_get_id_negative
    user = User(-50, "Charlie", "charlie@example.com")
TypeError: User() takes no arguments

======================================================================
ERROR: test_get_id_positive (__main__.TestUserGetId)
Test get_id with a positive integer ID.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Reposit�rios\JavaToPython-Transpiler-Web-app\outputs\7df5c56e-e1c2-450b-ba3d-2e3a39c12326\source\temp_test_User.get_id.py", line 10, in test_get_id_positive
    user = User(101, "Alice", "alice@example.com")
TypeError: User() takes no arguments

======================================================================
ERROR: test_get_id_zero (__main__.TestUserGetId)
Test get_id with an ID of zero.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Reposit�rios\JavaToPython-Transpiler-Web-app\outputs\7df5c56e-e1c2-450b-ba3d-2e3a39c12326\source\temp_test_User.get_id.py", line 17, in test_get_id_zero
    user = User(0, "Bob", "bob@example.com")
TypeError: User() takes no arguments

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (errors=4)

Stdout:

```

**Overall Test Result: ❌ One or more generated tests failed.**

## Final Generated Python Code

```python
# Unit test result: ❌ FAILED (see log for details)
class User:
    id: int
    name: str
    email: str

    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int) -> None:
        self.id = id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str) -> None:
        self.email = email

    def __str__(self) -> str:
        return f"User[ID={self.id}, Name='{self.name}', Email='{self.email}']"
```


---

# Processing File: D:\Repositórios\JavaToPython-Transpiler-Web-app\uploads\7df5c56e-e1c2-450b-ba3d-2e3a39c12326\source\test_project\src\com\example\service\UserService.java

## Original Java AST

```json
{
  "type": "CompilationUnit",
  "children": [
    {
      "type": "PackageDeclaration",
      "children": [
        {
          "type": "terminal",
          "text": "package",
          "token_type": "PACKAGE"
        },
        {
          "type": "QualifiedName",
          "children": [
            {
              "type": "terminal",
              "text": "com",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "example",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "service",
              "token_type": "IDENTIFIER"
            }
          ]
        },
        {
          "type": "terminal",
          "text": ";",
          "token_type": "SEMI"
        }
      ]
    },
    {
      "type": "ImportDeclaration",
      "children": [
        {
          "type": "terminal",
          "text": "import",
          "token_type": "IMPORT"
        },
        {
          "type": "QualifiedName",
          "children": [
            {
              "type": "terminal",
              "text": "com",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "example",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "model",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "User",
              "token_type": "IDENTIFIER"
            }
          ]
        },
        {
          "type": "terminal",
          "text": ";",
          "token_type": "SEMI"
        }
      ]
    },
    {
      "type": "ImportDeclaration",
      "children": [
        {
          "type": "terminal",
          "text": "import",
          "token_type": "IMPORT"
        },
        {
          "type": "QualifiedName",
          "children": [
            {
              "type": "terminal",
              "text": "java",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "util",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "ArrayList",
              "token_type": "IDENTIFIER"
            }
          ]
        },
        {
          "type": "terminal",
          "text": ";",
          "token_type": "SEMI"
        }
      ]
    },
    {
      "type": "ImportDeclaration",
      "children": [
        {
          "type": "terminal",
          "text": "import",
          "token_type": "IMPORT"
        },
        {
          "type": "QualifiedName",
          "children": [
            {
              "type": "terminal",
              "text": "java",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "util",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "List",
              "token_type": "IDENTIFIER"
            }
          ]
        },
        {
          "type": "terminal",
          "text": ";",
          "token_type": "SEMI"
        }
      ]
    },
    {
      "type": "TypeDeclaration",
      "children": [
        {
          "type": "ClassDeclaration",
          "children": [
            {
              "type": "Modifier",
              "children": [
                {
                  "type": "terminal",
                  "text": "public",
                  "token_type": "PUBLIC"
                }
              ]
            },
            {
              "type": "terminal",
              "text": "class",
              "token_type": "CLASS"
            },
            {
              "type": "terminal",
              "text": "UserService",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": "{",
              "token_type": "LBRACE"
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "FieldDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "private",
                          "token_type": "PRIVATE"
                        }
                      ]
                    },
                    {
                      "type": "Type",
                      "children": [
                        {
                          "type": "ClassOrInterfaceType",
                          "children": [
                            {
                              "type": "terminal",
                              "text": "List",
                              "token_type": "IDENTIFIER"
                            },
                            {
                              "type": "TypeArguments",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "<",
                                  "token_type": "LT"
                                },
                                {
                                  "type": "TypeArgument",
                                  "children": [
                                    {
                                      "type": "Type",
                                      "children": [
                                        {
                                          "type": "ClassOrInterfaceType",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "User",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ">",
                                  "token_type": "GT"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "VariableDeclarator",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "userDatabase",
                          "token_type": "IDENTIFIER"
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": ";",
                      "token_type": "SEMI"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "FieldDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "private",
                          "token_type": "PRIVATE"
                        }
                      ]
                    },
                    {
                      "type": "Type",
                      "children": [
                        {
                          "type": "PrimitiveType",
                          "children": [
                            {
                              "type": "terminal",
                              "text": "int",
                              "token_type": "INT"
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "VariableDeclarator",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "nextId",
                          "token_type": "IDENTIFIER"
                        },
                        {
                          "type": "terminal",
                          "text": "=",
                          "token_type": "ASSIGN"
                        },
                        {
                          "type": "VariableInitializer",
                          "children": [
                            {
                              "type": "PrimaryExpr",
                              "children": [
                                {
                                  "type": "Primary",
                                  "children": [
                                    {
                                      "type": "Literal",
                                      "children": [
                                        {
                                          "type": "terminal",
                                          "text": "1",
                                          "token_type": "DecimalIntegerLiteral"
                                        }
                                      ]
                                    }
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": ";",
                      "token_type": "SEMI"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "ConstructorDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "public",
                          "token_type": "PUBLIC"
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "UserService",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "(",
                      "token_type": "LPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": ")",
                      "token_type": "RPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "AssignmentExpr",
                                  "children": [
                                    {
                                      "type": "FieldAccessExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "this",
                                                  "token_type": "THIS"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "userDatabase",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "=",
                                      "token_type": "ASSIGN"
                                    },
                                    {
                                      "type": "MethodCallExpr",
                                      "children": [
                                        {
                                          "type": "NewCreatorExpr",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "new",
                                              "token_type": "NEW"
                                            },
                                            {
                                              "type": "Creator",
                                              "children": [
                                                {
                                                  "type": "CreatedName",
                                                  "children": [
                                                    {
                                                      "type": "ClassOrInterfaceType",
                                                      "children": [
                                                        {
                                                          "type": "terminal",
                                                          "text": "ArrayList",
                                                          "token_type": "IDENTIFIER"
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                },
                                                {
                                                  "type": "ClassCreatorRest",
                                                  "children": [
                                                    {
                                                      "type": "TypeArgumentsOrDiamond",
                                                      "children": [
                                                        {
                                                          "type": "terminal",
                                                          "text": "<",
                                                          "token_type": "LT"
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": ">",
                                                          "token_type": "GT"
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "(",
                                          "token_type": "LPAREN"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ")",
                                          "token_type": "RPAREN"
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "}",
                      "token_type": "RBRACE"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "MethodDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "public",
                          "token_type": "PUBLIC"
                        }
                      ]
                    },
                    {
                      "type": "ReturnType",
                      "children": [
                        {
                          "type": "Type",
                          "children": [
                            {
                              "type": "ClassOrInterfaceType",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "User",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "createUser",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "(",
                      "token_type": "LPAREN"
                    },
                    {
                      "type": "FormalParameters",
                      "children": [
                        {
                          "type": "FormalParameter",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "ClassOrInterfaceType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "String",
                                      "token_type": "IDENTIFIER"
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "VariableDeclaratorId",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "name",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        },
                        {
                          "type": "terminal",
                          "text": ",",
                          "token_type": "COMMA"
                        },
                        {
                          "type": "FormalParameter",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "ClassOrInterfaceType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "String",
                                      "token_type": "IDENTIFIER"
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "VariableDeclaratorId",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "email",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": ")",
                      "token_type": "RPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "LocalVariableDeclarationStatement",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "ClassOrInterfaceType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "User",
                                      "token_type": "IDENTIFIER"
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "VariableDeclarator",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "newUser",
                                  "token_type": "IDENTIFIER"
                                },
                                {
                                  "type": "terminal",
                                  "text": "=",
                                  "token_type": "ASSIGN"
                                },
                                {
                                  "type": "VariableInitializer",
                                  "children": [
                                    {
                                      "type": "MethodCallExpr",
                                      "children": [
                                        {
                                          "type": "NewCreatorExpr",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "new",
                                              "token_type": "NEW"
                                            },
                                            {
                                              "type": "Creator",
                                              "children": [
                                                {
                                                  "type": "CreatedName",
                                                  "children": [
                                                    {
                                                      "type": "ClassOrInterfaceType",
                                                      "children": [
                                                        {
                                                          "type": "terminal",
                                                          "text": "User",
                                                          "token_type": "IDENTIFIER"
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                },
                                                {
                                                  "type": "ClassCreatorRest"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "(",
                                          "token_type": "LPAREN"
                                        },
                                        {
                                          "type": "ExpressionList",
                                          "children": [
                                            {
                                              "type": "PostIncrementExpr",
                                              "children": [
                                                {
                                                  "type": "PrimaryExpr",
                                                  "children": [
                                                    {
                                                      "type": "Primary",
                                                      "children": [
                                                        {
                                                          "type": "terminal",
                                                          "text": "nextId",
                                                          "token_type": "IDENTIFIER"
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                },
                                                {
                                                  "type": "terminal",
                                                  "text": "++",
                                                  "token_type": "INC"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "terminal",
                                              "text": ",",
                                              "token_type": "COMMA"
                                            },
                                            {
                                              "type": "PrimaryExpr",
                                              "children": [
                                                {
                                                  "type": "Primary",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "name",
                                                      "token_type": "IDENTIFIER"
                                                    }
                                                  ]
                                                }
                                              ]
                                            },
                                            {
                                              "type": "terminal",
                                              "text": ",",
                                              "token_type": "COMMA"
                                            },
                                            {
                                              "type": "PrimaryExpr",
                                              "children": [
                                                {
                                                  "type": "Primary",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "email",
                                                      "token_type": "IDENTIFIER"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ")",
                                          "token_type": "RPAREN"
                                        }
                                      ]
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "terminal",
                              "text": ";",
                              "token_type": "SEMI"
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "DotMethodCallExpr",
                                  "children": [
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "userDatabase",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ".",
                                      "token_type": "DOT"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "add",
                                      "token_type": "IDENTIFIER"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "(",
                                      "token_type": "LPAREN"
                                    },
                                    {
                                      "type": "ExpressionList",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "newUser",
                                                  "token_type": "IDENTIFIER"
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ")",
                                      "token_type": "RPAREN"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "DotMethodCallExpr",
                                  "children": [
                                    {
                                      "type": "FieldAccessExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "System",
                                                  "token_type": "IDENTIFIER"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "out",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ".",
                                      "token_type": "DOT"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "println",
                                      "token_type": "IDENTIFIER"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "(",
                                      "token_type": "LPAREN"
                                    },
                                    {
                                      "type": "ExpressionList",
                                      "children": [
                                        {
                                          "type": "AdditiveExpr",
                                          "children": [
                                            {
                                              "type": "PrimaryExpr",
                                              "children": [
                                                {
                                                  "type": "Primary",
                                                  "children": [
                                                    {
                                                      "type": "Literal",
                                                      "children": [
                                                        {
                                                          "type": "terminal",
                                                          "text": "\"Created new user: \"",
                                                          "token_type": "StringLiteral"
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                }
                                              ]
                                            },
                                            {
                                              "type": "terminal",
                                              "text": "+",
                                              "token_type": "PLUS"
                                            },
                                            {
                                              "type": "DotMethodCallExpr",
                                              "children": [
                                                {
                                                  "type": "PrimaryExpr",
                                                  "children": [
                                                    {
                                                      "type": "Primary",
                                                      "children": [
                                                        {
                                                          "type": "terminal",
                                                          "text": "newUser",
                                                          "token_type": "IDENTIFIER"
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                },
                                                {
                                                  "type": "terminal",
                                                  "text": ".",
                                                  "token_type": "DOT"
                                                },
                                                {
                                                  "type": "terminal",
                                                  "text": "getName",
                                                  "token_type": "IDENTIFIER"
                                                },
                                                {
                                                  "type": "terminal",
                                                  "text": "(",
                                                  "token_type": "LPAREN"
                                                },
                                                {
                                                  "type": "terminal",
                                                  "text": ")",
                                                  "token_type": "RPAREN"
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ")",
                                      "token_type": "RPAREN"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ReturnStatement",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "return",
                                  "token_type": "RETURN"
                                },
                                {
                                  "type": "PrimaryExpr",
                                  "children": [
                                    {
                                      "type": "Primary",
                                      "children": [
                                        {
                                          "type": "terminal",
                                          "text": "newUser",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "}",
                      "token_type": "RBRACE"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "MethodDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "public",
                          "token_type": "PUBLIC"
                        }
                      ]
                    },
                    {
                      "type": "ReturnType",
                      "children": [
                        {
                          "type": "Type",
                          "children": [
                            {
                              "type": "ClassOrInterfaceType",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "User",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "findUserById",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "(",
                      "token_type": "LPAREN"
                    },
                    {
                      "type": "FormalParameters",
                      "children": [
                        {
                          "type": "FormalParameter",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "PrimitiveType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "int",
                                      "token_type": "INT"
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "type": "VariableDeclaratorId",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "id",
                                  "token_type": "IDENTIFIER"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": ")",
                      "token_type": "RPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ForStatement",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "for",
                                  "token_type": "FOR"
                                },
                                {
                                  "type": "terminal",
                                  "text": "(",
                                  "token_type": "LPAREN"
                                },
                                {
                                  "type": "ForControl",
                                  "children": [
                                    {
                                      "type": "EnhancedForControl",
                                      "children": [
                                        {
                                          "type": "Type",
                                          "children": [
                                            {
                                              "type": "ClassOrInterfaceType",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "User",
                                                  "token_type": "IDENTIFIER"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "VariableDeclaratorId",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "user",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ":",
                                          "token_type": "COLON"
                                        },
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "userDatabase",
                                                  "token_type": "IDENTIFIER"
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ")",
                                  "token_type": "RPAREN"
                                },
                                {
                                  "type": "Statement",
                                  "children": [
                                    {
                                      "type": "Block",
                                      "children": [
                                        {
                                          "type": "terminal",
                                          "text": "{",
                                          "token_type": "LBRACE"
                                        },
                                        {
                                          "type": "BlockStatement",
                                          "children": [
                                            {
                                              "type": "Statement",
                                              "children": [
                                                {
                                                  "type": "IfStatement",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "if",
                                                      "token_type": "IF"
                                                    },
                                                    {
                                                      "type": "terminal",
                                                      "text": "(",
                                                      "token_type": "LPAREN"
                                                    },
                                                    {
                                                      "type": "EqualityExpr",
                                                      "children": [
                                                        {
                                                          "type": "DotMethodCallExpr",
                                                          "children": [
                                                            {
                                                              "type": "PrimaryExpr",
                                                              "children": [
                                                                {
                                                                  "type": "Primary",
                                                                  "children": [
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": "user",
                                                                      "token_type": "IDENTIFIER"
                                                                    }
                                                                  ]
                                                                }
                                                              ]
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": ".",
                                                              "token_type": "DOT"
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": "getId",
                                                              "token_type": "IDENTIFIER"
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": "(",
                                                              "token_type": "LPAREN"
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": ")",
                                                              "token_type": "RPAREN"
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": "==",
                                                          "token_type": "EQUAL"
                                                        },
                                                        {
                                                          "type": "PrimaryExpr",
                                                          "children": [
                                                            {
                                                              "type": "Primary",
                                                              "children": [
                                                                {
                                                                  "type": "terminal",
                                                                  "text": "id",
                                                                  "token_type": "IDENTIFIER"
                                                                }
                                                              ]
                                                            }
                                                          ]
                                                        }
                                                      ]
                                                    },
                                                    {
                                                      "type": "terminal",
                                                      "text": ")",
                                                      "token_type": "RPAREN"
                                                    },
                                                    {
                                                      "type": "Statement",
                                                      "children": [
                                                        {
                                                          "type": "Block",
                                                          "children": [
                                                            {
                                                              "type": "terminal",
                                                              "text": "{",
                                                              "token_type": "LBRACE"
                                                            },
                                                            {
                                                              "type": "BlockStatement",
                                                              "children": [
                                                                {
                                                                  "type": "Statement",
                                                                  "children": [
                                                                    {
                                                                      "type": "ReturnStatement",
                                                                      "children": [
                                                                        {
                                                                          "type": "terminal",
                                                                          "text": "return",
                                                                          "token_type": "RETURN"
                                                                        },
                                                                        {
                                                                          "type": "PrimaryExpr",
                                                                          "children": [
                                                                            {
                                                                              "type": "Primary",
                                                                              "children": [
                                                                                {
                                                                                  "type": "terminal",
                                                                                  "text": "user",
                                                                                  "token_type": "IDENTIFIER"
                                                                                }
                                                                              ]
                                                                            }
                                                                          ]
                                                                        },
                                                                        {
                                                                          "type": "terminal",
                                                                          "text": ";",
                                                                          "token_type": "SEMI"
                                                                        }
                                                                      ]
                                                                    }
                                                                  ]
                                                                }
                                                              ]
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": "}",
                                                              "token_type": "RBRACE"
                                                            }
                                                          ]
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "}",
                                          "token_type": "RBRACE"
                                        }
                                      ]
                                    }
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ReturnStatement",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "return",
                                  "token_type": "RETURN"
                                },
                                {
                                  "type": "PrimaryExpr",
                                  "children": [
                                    {
                                      "type": "Primary",
                                      "children": [
                                        {
                                          "type": "Literal",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "null",
                                              "token_type": "NULL"
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "}",
                      "token_type": "RBRACE"
                    }
                  ]
                }
              ]
            },
            {
              "type": "MemberDeclaration",
              "children": [
                {
                  "type": "MethodDeclaration",
                  "children": [
                    {
                      "type": "Modifier",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "public",
                          "token_type": "PUBLIC"
                        }
                      ]
                    },
                    {
                      "type": "ReturnType",
                      "children": [
                        {
                          "type": "terminal",
                          "text": "void",
                          "token_type": "VOID"
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "printAllUsers",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "(",
                      "token_type": "LPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": ")",
                      "token_type": "RPAREN"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "DotMethodCallExpr",
                                  "children": [
                                    {
                                      "type": "FieldAccessExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "System",
                                                  "token_type": "IDENTIFIER"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "out",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ".",
                                      "token_type": "DOT"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "println",
                                      "token_type": "IDENTIFIER"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "(",
                                      "token_type": "LPAREN"
                                    },
                                    {
                                      "type": "ExpressionList",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "Literal",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "\"--- All Users ---\"",
                                                      "token_type": "StringLiteral"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ")",
                                      "token_type": "RPAREN"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "IfStatement",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "if",
                                  "token_type": "IF"
                                },
                                {
                                  "type": "terminal",
                                  "text": "(",
                                  "token_type": "LPAREN"
                                },
                                {
                                  "type": "DotMethodCallExpr",
                                  "children": [
                                    {
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "userDatabase",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ".",
                                      "token_type": "DOT"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "isEmpty",
                                      "token_type": "IDENTIFIER"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "(",
                                      "token_type": "LPAREN"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ")",
                                      "token_type": "RPAREN"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ")",
                                  "token_type": "RPAREN"
                                },
                                {
                                  "type": "Statement",
                                  "children": [
                                    {
                                      "type": "Block",
                                      "children": [
                                        {
                                          "type": "terminal",
                                          "text": "{",
                                          "token_type": "LBRACE"
                                        },
                                        {
                                          "type": "BlockStatement",
                                          "children": [
                                            {
                                              "type": "Statement",
                                              "children": [
                                                {
                                                  "type": "ExpressionStatement",
                                                  "children": [
                                                    {
                                                      "type": "DotMethodCallExpr",
                                                      "children": [
                                                        {
                                                          "type": "FieldAccessExpr",
                                                          "children": [
                                                            {
                                                              "type": "PrimaryExpr",
                                                              "children": [
                                                                {
                                                                  "type": "Primary",
                                                                  "children": [
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": "System",
                                                                      "token_type": "IDENTIFIER"
                                                                    }
                                                                  ]
                                                                }
                                                              ]
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": ".",
                                                              "token_type": "DOT"
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": "out",
                                                              "token_type": "IDENTIFIER"
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": ".",
                                                          "token_type": "DOT"
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": "println",
                                                          "token_type": "IDENTIFIER"
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": "(",
                                                          "token_type": "LPAREN"
                                                        },
                                                        {
                                                          "type": "ExpressionList",
                                                          "children": [
                                                            {
                                                              "type": "PrimaryExpr",
                                                              "children": [
                                                                {
                                                                  "type": "Primary",
                                                                  "children": [
                                                                    {
                                                                      "type": "Literal",
                                                                      "children": [
                                                                        {
                                                                          "type": "terminal",
                                                                          "text": "\"No users in the database.\"",
                                                                          "token_type": "StringLiteral"
                                                                        }
                                                                      ]
                                                                    }
                                                                  ]
                                                                }
                                                              ]
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "type": "terminal",
                                                          "text": ")",
                                                          "token_type": "RPAREN"
                                                        }
                                                      ]
                                                    },
                                                    {
                                                      "type": "terminal",
                                                      "text": ";",
                                                      "token_type": "SEMI"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "}",
                                          "token_type": "RBRACE"
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": "else",
                                  "token_type": "ELSE"
                                },
                                {
                                  "type": "Statement",
                                  "children": [
                                    {
                                      "type": "Block",
                                      "children": [
                                        {
                                          "type": "terminal",
                                          "text": "{",
                                          "token_type": "LBRACE"
                                        },
                                        {
                                          "type": "BlockStatement",
                                          "children": [
                                            {
                                              "type": "Statement",
                                              "children": [
                                                {
                                                  "type": "ForStatement",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "for",
                                                      "token_type": "FOR"
                                                    },
                                                    {
                                                      "type": "terminal",
                                                      "text": "(",
                                                      "token_type": "LPAREN"
                                                    },
                                                    {
                                                      "type": "ForControl",
                                                      "children": [
                                                        {
                                                          "type": "EnhancedForControl",
                                                          "children": [
                                                            {
                                                              "type": "Type",
                                                              "children": [
                                                                {
                                                                  "type": "ClassOrInterfaceType",
                                                                  "children": [
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": "User",
                                                                      "token_type": "IDENTIFIER"
                                                                    }
                                                                  ]
                                                                }
                                                              ]
                                                            },
                                                            {
                                                              "type": "VariableDeclaratorId",
                                                              "children": [
                                                                {
                                                                  "type": "terminal",
                                                                  "text": "user",
                                                                  "token_type": "IDENTIFIER"
                                                                }
                                                              ]
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": ":",
                                                              "token_type": "COLON"
                                                            },
                                                            {
                                                              "type": "PrimaryExpr",
                                                              "children": [
                                                                {
                                                                  "type": "Primary",
                                                                  "children": [
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": "userDatabase",
                                                                      "token_type": "IDENTIFIER"
                                                                    }
                                                                  ]
                                                                }
                                                              ]
                                                            }
                                                          ]
                                                        }
                                                      ]
                                                    },
                                                    {
                                                      "type": "terminal",
                                                      "text": ")",
                                                      "token_type": "RPAREN"
                                                    },
                                                    {
                                                      "type": "Statement",
                                                      "children": [
                                                        {
                                                          "type": "Block",
                                                          "children": [
                                                            {
                                                              "type": "terminal",
                                                              "text": "{",
                                                              "token_type": "LBRACE"
                                                            },
                                                            {
                                                              "type": "BlockStatement",
                                                              "children": [
                                                                {
                                                                  "type": "Statement",
                                                                  "children": [
                                                                    {
                                                                      "type": "ExpressionStatement",
                                                                      "children": [
                                                                        {
                                                                          "type": "DotMethodCallExpr",
                                                                          "children": [
                                                                            {
                                                                              "type": "FieldAccessExpr",
                                                                              "children": [
                                                                                {
                                                                                  "type": "PrimaryExpr",
                                                                                  "children": [
                                                                                    {
                                                                                      "type": "Primary",
                                                                                      "children": [
                                                                                        {
                                                                                          "type": "terminal",
                                                                                          "text": "System",
                                                                                          "token_type": "IDENTIFIER"
                                                                                        }
                                                                                      ]
                                                                                    }
                                                                                  ]
                                                                                },
                                                                                {
                                                                                  "type": "terminal",
                                                                                  "text": ".",
                                                                                  "token_type": "DOT"
                                                                                },
                                                                                {
                                                                                  "type": "terminal",
                                                                                  "text": "out",
                                                                                  "token_type": "IDENTIFIER"
                                                                                }
                                                                              ]
                                                                            },
                                                                            {
                                                                              "type": "terminal",
                                                                              "text": ".",
                                                                              "token_type": "DOT"
                                                                            },
                                                                            {
                                                                              "type": "terminal",
                                                                              "text": "println",
                                                                              "token_type": "IDENTIFIER"
                                                                            },
                                                                            {
                                                                              "type": "terminal",
                                                                              "text": "(",
                                                                              "token_type": "LPAREN"
                                                                            },
                                                                            {
                                                                              "type": "ExpressionList",
                                                                              "children": [
                                                                                {
                                                                                  "type": "DotMethodCallExpr",
                                                                                  "children": [
                                                                                    {
                                                                                      "type": "PrimaryExpr",
                                                                                      "children": [
                                                                                        {
                                                                                          "type": "Primary",
                                                                                          "children": [
                                                                                            {
                                                                                              "type": "terminal",
                                                                                              "text": "user",
                                                                                              "token_type": "IDENTIFIER"
                                                                                            }
                                                                                          ]
                                                                                        }
                                                                                      ]
                                                                                    },
                                                                                    {
                                                                                      "type": "terminal",
                                                                                      "text": ".",
                                                                                      "token_type": "DOT"
                                                                                    },
                                                                                    {
                                                                                      "type": "terminal",
                                                                                      "text": "toString",
                                                                                      "token_type": "IDENTIFIER"
                                                                                    },
                                                                                    {
                                                                                      "type": "terminal",
                                                                                      "text": "(",
                                                                                      "token_type": "LPAREN"
                                                                                    },
                                                                                    {
                                                                                      "type": "terminal",
                                                                                      "text": ")",
                                                                                      "token_type": "RPAREN"
                                                                                    }
                                                                                  ]
                                                                                }
                                                                              ]
                                                                            },
                                                                            {
                                                                              "type": "terminal",
                                                                              "text": ")",
                                                                              "token_type": "RPAREN"
                                                                            }
                                                                          ]
                                                                        },
                                                                        {
                                                                          "type": "terminal",
                                                                          "text": ";",
                                                                          "token_type": "SEMI"
                                                                        }
                                                                      ]
                                                                    }
                                                                  ]
                                                                }
                                                              ]
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": "}",
                                                              "token_type": "RBRACE"
                                                            }
                                                          ]
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "}",
                                          "token_type": "RBRACE"
                                        }
                                      ]
                                    }
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "ExpressionStatement",
                              "children": [
                                {
                                  "type": "DotMethodCallExpr",
                                  "children": [
                                    {
                                      "type": "FieldAccessExpr",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "terminal",
                                                  "text": "System",
                                                  "token_type": "IDENTIFIER"
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "type": "terminal",
                                          "text": ".",
                                          "token_type": "DOT"
                                        },
                                        {
                                          "type": "terminal",
                                          "text": "out",
                                          "token_type": "IDENTIFIER"
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ".",
                                      "token_type": "DOT"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "println",
                                      "token_type": "IDENTIFIER"
                                    },
                                    {
                                      "type": "terminal",
                                      "text": "(",
                                      "token_type": "LPAREN"
                                    },
                                    {
                                      "type": "ExpressionList",
                                      "children": [
                                        {
                                          "type": "PrimaryExpr",
                                          "children": [
                                            {
                                              "type": "Primary",
                                              "children": [
                                                {
                                                  "type": "Literal",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "\"-----------------\"",
                                                      "token_type": "StringLiteral"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "type": "terminal",
                                      "text": ")",
                                      "token_type": "RPAREN"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": ";",
                                  "token_type": "SEMI"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "terminal",
                      "text": "}",
                      "token_type": "RBRACE"
                    }
                  ]
                }
              ]
            },
            {
              "type": "terminal",
              "text": "}",
              "token_type": "RBRACE"
            }
          ]
        }
      ]
    },
    {
      "type": "terminal",
      "text": "<EOF>",
      "token_type": "UNKNOWN_TOKEN_TYPE_-1"
    }
  ]
}
```

## Framework Analysis

```json
{
  "frameworks": [],
  "spring_endpoints": [],
  "hibernate_entities": [],
  "struts_actions": [],
  "gwt_services": []
}
```

Translation required **1** chunk(s).

## AI-Generated Python ASTs (JSON)

### Chunk 1:

```json
{
  "type": "Module",
  "body": [
    {
      "type": "ImportFrom",
      "module": "typing",
      "names": [
        {
          "type": "alias",
          "name": "Optional",
          "asname": null
        }
      ],
      "level": 0
    },
    {
      "type": "ImportFrom",
      "module": "com.example.model.User",
      "names": [
        {
          "type": "alias",
          "name": "User",
          "asname": null
        }
      ],
      "level": 0
    },
    {
      "type": "ClassDef",
      "name": "UserService",
      "bases": [],
      "keywords": [],
      "body": [
        {
          "type": "AnnAssign",
          "target": {
            "type": "Name",
            "id": "userDatabase",
            "ctx": "Store"
          },
          "annotation": {
            "type": "Subscript",
            "value": {
              "type": "Name",
              "id": "list",
              "ctx": "Load"
            },
            "slice": {
              "type": "Constant",
              "value": "User",
              "kind": null
            },
            "ctx": "Load"
          },
          "value": null,
          "simple": 1
        },
        {
          "type": "AnnAssign",
          "target": {
            "type": "Name",
            "id": "nextId",
            "ctx": "Store"
          },
          "annotation": {
            "type": "Name",
            "id": "int",
            "ctx": "Load"
          },
          "value": {
            "type": "Constant",
            "value": 1,
            "kind": null
          },
          "simple": 1
        },
        {
          "type": "FunctionDef",
          "name": "__init__",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              {
                "type": "arg",
                "arg": "self",
                "annotation": null
              }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Attribute",
                  "value": {
                    "type": "Name",
                    "id": "self",
                    "ctx": "Load"
                  },
                  "attr": "userDatabase",
                  "ctx": "Store"
                }
              ],
              "value": {
                "type": "List",
                "elts": [],
                "ctx": "Load"
              }
            }
          ],
          "decorator_list": [],
          "returns": null
        },
        {
          "type": "FunctionDef",
          "name": "create_user",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              {
                "type": "arg",
                "arg": "self",
                "annotation": null
              },
              {
                "type": "arg",
                "arg": "name",
                "annotation": {
                  "type": "Name",
                  "id": "str",
                  "ctx": "Load"
                }
              },
              {
                "type": "arg",
                "arg": "email",
                "annotation": {
                  "type": "Name",
                  "id": "str",
                  "ctx": "Load"
                }
              }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Name",
                  "id": "new_user",
                  "ctx": "Store"
                }
              ],
              "value": {
                "type": "Call",
                "func": {
                  "type": "Name",
                  "id": "User",
                  "ctx": "Load"
                },
                "args": [
                  {
                    "type": "Attribute",
                    "value": {
                      "type": "Name",
                      "id": "self",
                      "ctx": "Load"
                    },
                    "attr": "nextId",
                    "ctx": "Load"
                  },
                  {
                    "type": "Name",
                    "id": "name",
                    "ctx": "Load"
                  },
                  {
                    "type": "Name",
                    "id": "email",
                    "ctx": "Load"
                  }
                ],
                "keywords": []
              }
            },
            {
              "type": "AugAssign",
              "target": {
                "type": "Attribute",
                "value": {
                  "type": "Name",
                  "id": "self",
                  "ctx": "Load"
                },
                "attr": "nextId",
                "ctx": "Store"
              },
              "op": {
                "type": "Add"
              },
              "value": {
                "type": "Constant",
                "value": 1,
                "kind": null
              }
            },
            {
              "type": "Expr",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Attribute",
                  "value": {
                    "type": "Attribute",
                    "value": {
                      "type": "Name",
                      "id": "self",
                      "ctx": "Load"
                    },
                    "attr": "userDatabase",
                    "ctx": "Load"
                  },
                  "attr": "append",
                  "ctx": "Load"
                },
                "args": [
                  {
                    "type": "Name",
                    "id": "new_user",
                    "ctx": "Load"
                  }
                ],
                "keywords": []
              }
            },
            {
              "type": "Expr",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Name",
                  "id": "print",
                  "ctx": "Load"
                },
                "args": [
                  {
                    "type": "JoinedStr",
                    "values": [
                      {
                        "type": "Constant",
                        "value": "Created new user: ",
                        "kind": null
                      },
                      {
                        "type": "FormattedValue",
                        "value": {
                          "type": "Call",
                          "func": {
                            "type": "Attribute",
                            "value": {
                              "type": "Name",
                              "id": "new_user",
                              "ctx": "Load"
                            },
                            "attr": "get_name",
                            "ctx": "Load"
                          },
                          "args": [],
                          "keywords": []
                        },
                        "conversion": -1,
                        "format_spec": null
                      }
                    ]
                  }
                ],
                "keywords": []
              }
            },
            {
              "type": "Return",
              "value": {
                "type": "Name",
                "id": "new_user",
                "ctx": "Load"
              }
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Constant",
            "value": "User",
            "kind": null
          }
        },
        {
          "type": "FunctionDef",
          "name": "find_user_by_id",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              {
                "type": "arg",
                "arg": "self",
                "annotation": null
              },
              {
                "type": "arg",
                "arg": "id",
                "annotation": {
                  "type": "Name",
                  "id": "int",
                  "ctx": "Load"
                }
              }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "For",
              "target": {
                "type": "Name",
                "id": "user",
                "ctx": "Store"
              },
              "iter": {
                "type": "Attribute",
                "value": {
                  "type": "Name",
                  "id": "self",
                  "ctx": "Load"
                },
                "attr": "userDatabase",
                "ctx": "Load"
              },
              "body": [
                {
                  "type": "If",
                  "test": {
                    "type": "Compare",
                    "left": {
                      "type": "Call",
                      "func": {
                        "type": "Attribute",
                        "value": {
                          "type": "Name",
                          "id": "user",
                          "ctx": "Load"
                        },
                        "attr": "get_id",
                        "ctx": "Load"
                      },
                      "args": [],
                      "keywords": []
                    },
                    "ops": [
                      {
                        "type": "Eq"
                      }
                    ],
                    "comparators": [
                      {
                        "type": "Name",
                        "id": "id",
                        "ctx": "Load"
                      }
                    ]
                  },
                  "body": [
                    {
                      "type": "Return",
                      "value": {
                        "type": "Name",
                        "id": "user",
                        "ctx": "Load"
                      }
                    }
                  ],
                  "orelse": []
                }
              ],
              "orelse": []
            },
            {
              "type": "Return",
              "value": {
                "type": "Constant",
                "value": null,
                "kind": null
              }
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Subscript",
            "value": {
              "type": "Name",
              "id": "Optional",
              "ctx": "Load"
            },
            "slice": {
              "type": "Constant",
              "value": "User",
              "kind": null
            },
            "ctx": "Load"
          }
        },
        {
          "type": "FunctionDef",
          "name": "print_all_users",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              {
                "type": "arg",
                "arg": "self",
                "annotation": null
              }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Expr",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Name",
                  "id": "print",
                  "ctx": "Load"
                },
                "args": [
                  {
                    "type": "Constant",
                    "value": "--- All Users ---",
                    "kind": null
                  }
                ],
                "keywords": []
              }
            },
            {
              "type": "If",
              "test": {
                "type": "UnaryOp",
                "op": {
                  "type": "Not"
                },
                "operand": {
                  "type": "Attribute",
                  "value": {
                    "type": "Name",
                    "id": "self",
                    "ctx": "Load"
                  },
                  "attr": "userDatabase",
                  "ctx": "Load"
                }
              },
              "body": [
                {
                  "type": "Expr",
                  "value": {
                    "type": "Call",
                    "func": {
                      "type": "Name",
                      "id": "print",
                      "ctx": "Load"
                    },
                    "args": [
                      {
                        "type": "Constant",
                        "value": "No users in the database.",
                        "kind": null
                      }
                    ],
                    "keywords": []
                  }
                }
              ],
              "orelse": [
                {
                  "type": "For",
                  "target": {
                    "type": "Name",
                    "id": "user",
                    "ctx": "Store"
                  },
                  "iter": {
                    "type": "Attribute",
                    "value": {
                      "type": "Name",
                      "id": "self",
                      "ctx": "Load"
                    },
                    "attr": "userDatabase",
                    "ctx": "Load"
                  },
                  "body": [
                    {
                      "type": "Expr",
                      "value": {
                        "type": "Call",
                        "func": {
                          "type": "Name",
                          "id": "print",
                          "ctx": "Load"
                        },
                        "args": [
                          {
                            "type": "Call",
                            "func": {
                              "type": "Name",
                              "id": "str",
                              "ctx": "Load"
                            },
                            "args": [
                              {
                                "type": "Name",
                                "id": "user",
                                "ctx": "Load"
                              }
                            ],
                            "keywords": []
                          }
                        ],
                        "keywords": []
                      }
                    }
                  ],
                  "orelse": []
                }
              ]
            },
            {
              "type": "Expr",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Name",
                  "id": "print",
                  "ctx": "Load"
                },
                "args": [
                  {
                    "type": "Constant",
                    "value": "-----------------",
                    "kind": null
                  }
                ],
                "keywords": []
              }
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Constant",
            "value": null,
            "kind": null
          }
        }
      ],
      "decorator_list": []
    }
  ],
  "type_ignores": []
}
```


## Unit Test Generation and Execution

### Testing `UserService.create_user`

**AI-Generated Test Script:**

```python
import unittest
import sys
from io import StringIO
from typing import Optional

# Mock the User class as it's a dependency for UserService
# In a real project, this would be imported from its actual file (e.g., com.example.model.User).
class User:
    def __init__(self, id: int, name: str, email: str):
        self._id = id
        self._name = name
        self._email = email

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_email(self) -> str:
        return self._email

    def __str__(self) -> str:
        return f"User(ID: {self._id}, Name: {self._name}, Email: {self._email})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return self._id == other._id and self._name == other._name and self._email == other._email

    def __hash__(self) -> int:
        return hash((self._id, self._name, self._email))


# The UserService class to be tested, as provided in the problem description.
# In a real project, this would be imported from its actual file (e.g., test_project.src.com.example.service.UserService).
class UserService:
    userDatabase: list[User]
    nextId: int = 1

    def __init__(self):
        self.userDatabase = []

    def create_user(self, name: str, email: str) -> 'User':
        new_user = User(self.nextId, name, email)
        self.nextId += 1
        self.userDatabase.append(new_user)
        print(f'Created new user: {new_user.get_name()}')
        return new_user

    def find_user_by_id(self, id: int) -> Optional['User']:
        for user in self.userDatabase:
            if user.get_id() == id:
                return user
        return None

    def print_all_users(self) -> None:
        print('--- All Users ---')
        if not self.userDatabase:
            print('No users in the database.')
        else:
            for user in self.userDatabase:
                print(str(user))
        print('-----------------')


class TestUserService(unittest.TestCase):

    def setUp(self):
        """
        Set up a new UserService instance before each test method.
        This ensures tests are isolated and start with a clean state.
        """
        self.user_service = UserService()

    def test_create_user_basic_creation(self):
        """
        Test that create_user correctly creates a user with the given name and email,
        assigns the correct ID, and increments nextId.
        """
        name = "Alice"
        email = "alice@example.com"
        
        # Capture stdout to verify print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        created_user = self.user_service.create_user(name, email)
        
        # Restore stdout
        sys.stdout = sys.__stdout__

        # Assert the returned user object's properties
        self.assertIsNotNone(created_user)
        self.assertIsInstance(created_user, User)
        self.assertEqual(created_user.get_id(), 1)
        self.assertEqual(created_user.get_name(), name)
        self.assertEqual(created_user.get_email(), email)

        # Assert that nextId was incremented correctly
        self.assertEqual(self.user_service.nextId, 2)

        # Assert that the user was added to the internal database
        self.assertEqual(len(self.user_service.userDatabase), 1)
        self.assertEqual(self.user_service.userDatabase[0], created_user)

        # Assert the print output
        self.assertIn(f"Created new user: {name}", captured_output.getvalue())

    def test_create_user_multiple_users(self):
        """
        Test creating multiple users to ensure IDs are assigned sequentially
        and all users are added to the database.
        """
        user1_name, user1_email = "Bob", "bob@example.com"
        user2_name, user2_email = "Charlie", "charlie@example.com"
        user3_name, user3_email = "David", "david@example.com"

        user1 = self.user_service.create_user(user1_name, user1_email)
        user2 = self.user_service.create_user(user2_name, user2_email)
        user3 = self.user_service.create_user(user3_name, user3_email)

        # Verify IDs
        self.assertEqual(user1.get_id(), 1)
        self.assertEqual(user2.get_id(), 2)
        self.assertEqual(user3.get_id(), 3)

        # Verify nextId after multiple creations
        self.assertEqual(self.user_service.nextId, 4)

        # Verify all users are in the database in order
        self.assertEqual(len(self.user_service.userDatabase), 3)
        self.assertEqual(self.user_service.userDatabase[0], user1)
        self.assertEqual(self.user_service.userDatabase[1], user2)
        self.assertEqual(self.user_service.userDatabase[2], user3)

    def test_create_user_with_empty_strings(self):
        """
        Test creating a user with empty strings for name and email.
        """
        name = ""
        email = ""
        created_user = self.user_service.create_user(name, email)

        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.get_id(), 1)
        self.assertEqual(created_user.get_name(), "")
        self.assertEqual(created_user.get_email(), "")
        self.assertEqual(self.user_service.nextId, 2)
        self.assertEqual(len(self.user_service.userDatabase), 1)

    def test_create_user_with_special_characters(self):
        """
        Test creating a user with special characters in name and email.
        """
        name = "Jöhn Döe!"
        email = "john.doe+test@example.co.uk"
        created_user = self.user_service.create_user(name, email)

        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.get_id(), 1)
        self.assertEqual(created_user.get_name(), name)
        self.assertEqual(created_user.get_email(), email)
        self.assertEqual(self.user_service.nextId, 2)
        self.assertEqual(len(self.user_service.userDatabase), 1)


if __name__ == '__main__':
    unittest.main()
```

**Test Execution Results:**

```
✅ PASSED

Output:
Created new user: Bob
Created new user: Charlie
Created new user: David
Created new user: 
Created new user: J�hn D�e!

```

**Overall Test Result: ✅ All generated tests passed.**

## Final Generated Python Code

```python
# Unit test result: ✅ PASSED
from typing import Optional
from com.example.model.User import User

class UserService:
    userDatabase: list['User']
    nextId: int = 1

    def __init__(self):
        self.userDatabase = []

    def create_user(self, name: str, email: str) -> 'User':
        new_user = User(self.nextId, name, email)
        self.nextId += 1
        self.userDatabase.append(new_user)
        print(f'Created new user: {new_user.get_name()}')
        return new_user

    def find_user_by_id(self, id: int) -> Optional['User']:
        for user in self.userDatabase:
            if user.get_id() == id:
                return user
        return None

    def print_all_users(self) -> None:
        print('--- All Users ---')
        if not self.userDatabase:
            print('No users in the database.')
        else:
            for user in self.userDatabase:
                print(str(user))
        print('-----------------')
```
