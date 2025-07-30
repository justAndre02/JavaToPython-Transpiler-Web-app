# Translation Log for: `uploads\218933ec-d64e-42e2-9a28-1a0a7bd9d6d6\source`
Model: `gemini-2.5-flash`


---

# Processing File: D:\Repositórios\JavaToPython-Transpiler-Web-app\uploads\218933ec-d64e-42e2-9a28-1a0a7bd9d6d6\source\test_project\src\com\example\Main.java

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
              "type": "AnnAssign",
              "target": {
                "type": "Name",
                "id": "service",
                "ctx": "Store"
              },
              "annotation": {
                "type": "Name",
                "id": "UserService",
                "ctx": "Load"
              },
              "value": {
                "type": "Call",
                "func": {
                  "type": "Name",
                  "id": "UserService",
                  "ctx": "Load"
                },
                "args": [],
                "keywords": []
              },
              "simple": 1
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
                  "attr": "createUser",
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
                  "attr": "createUser",
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
                  "attr": "printAllUsers",
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
              "type": "AnnAssign",
              "target": {
                "type": "Name",
                "id": "found_user",
                "ctx": "Store"
              },
              "annotation": {
                "type": "Subscript",
                "value": {
                  "type": "Name",
                  "id": "Optional",
                  "ctx": "Load"
                },
                "slice": {
                  "type": "Name",
                  "id": "User",
                  "ctx": "Load"
                },
                "ctx": "Load"
              },
              "value": {
                "type": "Call",
                "func": {
                  "type": "Attribute",
                  "value": {
                    "type": "Name",
                    "id": "service",
                    "ctx": "Load"
                  },
                  "attr": "findUserById",
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
              },
              "simple": 1
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
                                "attr": "getName",
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
          "returns": {
            "type": "Constant",
            "value": null,
            "kind": null
          }
        }
      ]
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
from typing import Optional
from com.example.model.User import User
from com.example.service.UserService import UserService

class Main:

    @staticmethod
    def main(args: list[str]) -> None:
        print('Starting User Management System...')
        service: UserService = UserService()
        service.createUser('Alice', 'alice@example.com')
        service.createUser('Bob', 'bob@example.com')
        service.printAllUsers()
        print('\nSearching for user with ID 1...')
        found_user: Optional[User] = service.findUserById(1)
        if found_user is not None:
            print(f'Found: {found_user.getName()}')
        else:
            print('User with ID 1 not found.')
        print('\nSystem finished.')
if __name__ == '__main__':
    Main.main([])
```


---

# Processing File: D:\Repositórios\JavaToPython-Transpiler-Web-app\uploads\218933ec-d64e-42e2-9a28-1a0a7bd9d6d6\source\test_project\src\com\example\model\User.java

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
          "returns": {
            "type": "Constant",
            "value": null,
            "kind": null
          }
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
      "decorator_list": []
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
          "returns": null
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

    def test_get_id_basic(self):
        # Test with a positive integer ID
        user = User(id=1, name="Alice", email="alice@example.com")
        self.assertEqual(user.get_id(), 1)

    def test_get_id_zero(self):
        # Test with ID 0
        user = User(id=0, name="Bob", email="bob@example.com")
        self.assertEqual(user.get_id(), 0)

    def test_get_id_negative(self):
        # Test with a negative integer ID
        user = User(id=-5, name="Charlie", email="charlie@example.com")
        self.assertEqual(user.get_id(), -5)

    def test_get_id_large_number(self):
        # Test with a large integer ID
        user = User(id=999999999, name="David", email="david@example.com")
        self.assertEqual(user.get_id(), 999999999)

    def test_get_id_after_set_id(self):
        # Test get_id after set_id changes the ID
        user = User(id=10, name="Eve", email="eve@example.com")
        self.assertEqual(user.get_id(), 10)
        user.set_id(20)
        self.assertEqual(user.get_id(), 20)
        user.set_id(-100)
        self.assertEqual(user.get_id(), -100)

if __name__ == '__main__':
    unittest.main()
```

**Test Execution Results:**

```
❌ FAILED

Stderr:
EEEEE
======================================================================
ERROR: test_get_id_after_set_id (__main__.TestUserGetId)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Reposit�rios\JavaToPython-Transpiler-Web-app\outputs\218933ec-d64e-42e2-9a28-1a0a7bd9d6d6\source\temp_test_User.get_id.py", line 28, in test_get_id_after_set_id
    user = User(id=10, name="Eve", email="eve@example.com")
TypeError: User() takes no arguments

======================================================================
ERROR: test_get_id_basic (__main__.TestUserGetId)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Reposit�rios\JavaToPython-Transpiler-Web-app\outputs\218933ec-d64e-42e2-9a28-1a0a7bd9d6d6\source\temp_test_User.get_id.py", line 8, in test_get_id_basic
    user = User(id=1, name="Alice", email="alice@example.com")
TypeError: User() takes no arguments

======================================================================
ERROR: test_get_id_large_number (__main__.TestUserGetId)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Reposit�rios\JavaToPython-Transpiler-Web-app\outputs\218933ec-d64e-42e2-9a28-1a0a7bd9d6d6\source\temp_test_User.get_id.py", line 23, in test_get_id_large_number
    user = User(id=999999999, name="David", email="david@example.com")
TypeError: User() takes no arguments

======================================================================
ERROR: test_get_id_negative (__main__.TestUserGetId)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Reposit�rios\JavaToPython-Transpiler-Web-app\outputs\218933ec-d64e-42e2-9a28-1a0a7bd9d6d6\source\temp_test_User.get_id.py", line 18, in test_get_id_negative
    user = User(id=-5, name="Charlie", email="charlie@example.com")
TypeError: User() takes no arguments

======================================================================
ERROR: test_get_id_zero (__main__.TestUserGetId)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Reposit�rios\JavaToPython-Transpiler-Web-app\outputs\218933ec-d64e-42e2-9a28-1a0a7bd9d6d6\source\temp_test_User.get_id.py", line 13, in test_get_id_zero
    user = User(id=0, name="Bob", email="bob@example.com")
TypeError: User() takes no arguments

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (errors=5)

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

    def __init__(self, id: int, name: str, email: str) -> None:
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

    def __str__(self):
        return f"User[ID={self.id}, Name='{self.name}', Email='{self.email}']"
```


---

# Processing File: D:\Repositórios\JavaToPython-Transpiler-Web-app\uploads\218933ec-d64e-42e2-9a28-1a0a7bd9d6d6\source\test_project\src\com\example\service\UserService.java

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
      "name": "UserService",
      "bases": [],
      "keywords": [],
      "decorator_list": [],
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
          "name": "createUser",
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
                            "attr": "getName",
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
          "name": "findUserById",
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
                        "attr": "getId",
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
          "name": "printAllUsers",
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
          "returns": null
        }
      ]
    }
  ],
  "type_ignores": []
}
```


## Unit Test Generation and Execution

### Testing `UserService.createUser`

**AI-Generated Test Script:**

```python
import unittest
import io
import sys
from typing import Optional

# Mock User class for testing purposes
# This class mimics the essential behavior of the com.example.model.User class
# required by UserService for testing.
class User:
    def __init__(self, id: int, name: str, email: str):
        self._id = id
        self._name = name
        self._email = email

    def getId(self) -> int:
        return self._id

    def getName(self) -> str:
        return self._name

    def getEmail(self) -> str:
        return self._email

    def __str__(self) -> str:
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"

# The UserService class (System Under Test)
# This code is provided as part of the problem description and is included
# here to make the test script self-contained and runnable.
class UserService:
    userDatabase: list['User']
    nextId: int = 1

    def __init__(self):
        self.userDatabase = []
        self.nextId = 1 # Ensure nextId starts from 1 for each new instance

    def createUser(self, name: str, email: str) -> 'User':
        new_user = User(self.nextId, name, email)
        self.nextId += 1
        self.userDatabase.append(new_user)
        print(f'Created new user: {new_user.getName()}')
        return new_user

    def findUserById(self, id: int) -> Optional['User']:
        for user in self.userDatabase:
            if user.getId() == id:
                return user
        return None

    def printAllUsers(self):
        print('--- All Users ---')
        if not self.userDatabase:
            print('No users in the database.')
        else:
            for user in self.userDatabase:
                print(str(user))
        print('-----------------')


class TestUserService(unittest.TestCase):

    def setUp(self):
        """Set up a fresh UserService instance and capture stdout before each test."""
        self.user_service = UserService()
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        """Restore stdout after each test."""
        sys.stdout = sys.__stdout__

    def test_createUser_basic(self):
        """Test the basic functionality of creating a single user."""
        name = "Alice"
        email = "alice@example.com"
        
        user = self.user_service.createUser(name, email)
        
        # Assertions about the returned user object
        self.assertIsInstance(user, User)
        self.assertEqual(user.getId(), 1)
        self.assertEqual(user.getName(), name)
        self.assertEqual(user.getEmail(), email)
        
        # Assertions about the UserService state
        self.assertEqual(len(self.user_service.userDatabase), 1)
        self.assertEqual(self.user_service.userDatabase[0], user) # Check if the same object is in the list
        self.assertEqual(self.user_service.nextId, 2) # nextId should have incremented

        # Assert print output
        expected_output = f"Created new user: {name}\n"
        self.assertEqual(self.captured_output.getvalue(), expected_output)

    def test_createUser_multiple_users(self):
        """Test creating multiple users to verify ID increment and database additions."""
        user1 = self.user_service.createUser("Bob", "bob@example.com")
        user2 = self.user_service.createUser("Charlie", "charlie@example.com")
        user3 = self.user_service.createUser("David", "david@example.com")

        # Check IDs of created users
        self.assertEqual(user1.getId(), 1)
        self.assertEqual(user2.getId(), 2)
        self.assertEqual(user3.getId(), 3)

        # Check final nextId value
        self.assertEqual(self.user_service.nextId, 4)

        # Check userDatabase size
        self.assertEqual(len(self.user_service.userDatabase), 3)

        # Check if users are in the database in the correct order and are the correct objects
        self.assertEqual(self.user_service.userDatabase[0], user1)
        self.assertEqual(self.user_service.userDatabase[1], user2)
        self.assertEqual(self.user_service.userDatabase[2], user3)

        # Check cumulative print output
        expected_output = (
            "Created new user: Bob\n"
            "Created new user: Charlie\n"
            "Created new user: David\n"
        )
        self.assertEqual(self.captured_output.getvalue(), expected_output)

    def test_createUser_empty_name_email(self):
        """Test creating a user with empty strings for name and email."""
        name = ""
        email = ""
        user = self.user_service.createUser(name, email)

        self.assertEqual(user.getId(), 1)
        self.assertEqual(user.getName(), name)
        self.assertEqual(user.getEmail(), email)
        self.assertEqual(len(self.user_service.userDatabase), 1)
        self.assertEqual(self.user_service.nextId, 2)
        expected_output = f"Created new user: {name}\n"
        self.assertEqual(self.captured_output.getvalue(), expected_output)

    def test_createUser_special_characters_name_email(self):
        """Test creating a user with special characters in name and email."""
        name = "Jöhn Döe"
        email = "john.doe+alias@example.co.uk"
        user = self.user_service.createUser(name, email)

        self.assertEqual(user.getId(), 1)
        self.assertEqual(user.getName(), name)
        self.assertEqual(user.getEmail(), email)
        self.assertEqual(len(self.user_service.userDatabase), 1)
        self.assertEqual(self.user_service.nextId, 2)
        expected_output = f"Created new user: {name}\n"
        self.assertEqual(self.captured_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```

**Test Execution Results:**

```
✅ PASSED

Output:
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

```

**Overall Test Result: ✅ All generated tests passed.**

## Final Generated Python Code

```python
# Unit test result: ✅ PASSED
from com.example.model.User import User
from typing import Optional

class UserService:
    userDatabase: list['User']
    nextId: int = 1

    def __init__(self):
        self.userDatabase = []

    def createUser(self, name: str, email: str) -> 'User':
        new_user = User(self.nextId, name, email)
        self.nextId += 1
        self.userDatabase.append(new_user)
        print(f'Created new user: {new_user.getName()}')
        return new_user

    def findUserById(self, id: int) -> Optional['User']:
        for user in self.userDatabase:
            if user.getId() == id:
                return user
        return None

    def printAllUsers(self):
        print('--- All Users ---')
        if not self.userDatabase:
            print('No users in the database.')
        else:
            for user in self.userDatabase:
                print(str(user))
        print('-----------------')
```
