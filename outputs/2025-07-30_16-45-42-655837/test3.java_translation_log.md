# Translation Log for: `test3.java`
Model: `gemini-2.5-flash`


---

# Processing File: uploads\2025-07-30_16-45-42-655837\test3.java

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
              "text": "test_files",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "test3",
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
              "text": "Scanner",
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
              "text": "test3",
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
                  "type": "EnumDeclaration",
                  "children": [
                    {
                      "type": "terminal",
                      "text": "enum",
                      "token_type": "ENUM"
                    },
                    {
                      "type": "terminal",
                      "text": "Priority",
                      "token_type": "IDENTIFIER"
                    },
                    {
                      "type": "terminal",
                      "text": "{",
                      "token_type": "LBRACE"
                    },
                    {
                      "type": "EnumConstantList",
                      "children": [
                        {
                          "type": "EnumConstant",
                          "children": [
                            {
                              "type": "terminal",
                              "text": "BAIXA",
                              "token_type": "IDENTIFIER"
                            }
                          ]
                        },
                        {
                          "type": "terminal",
                          "text": ",",
                          "token_type": "COMMA"
                        },
                        {
                          "type": "EnumConstant",
                          "children": [
                            {
                              "type": "terminal",
                              "text": "MEDIA",
                              "token_type": "IDENTIFIER"
                            }
                          ]
                        },
                        {
                          "type": "terminal",
                          "text": ",",
                          "token_type": "COMMA"
                        },
                        {
                          "type": "EnumConstant",
                          "children": [
                            {
                              "type": "terminal",
                              "text": "ALTA",
                              "token_type": "IDENTIFIER"
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
                  "type": "ClassDeclaration",
                  "children": [
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
                      "type": "terminal",
                      "text": "class",
                      "token_type": "CLASS"
                    },
                    {
                      "type": "terminal",
                      "text": "Task",
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
                                  "text": "descricao",
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
                              "type": "Type",
                              "children": [
                                {
                                  "type": "ClassOrInterfaceType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "Priority",
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
                                  "text": "prioridade",
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
                              "type": "terminal",
                              "text": "Task",
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
                                          "text": "descricao",
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
                                              "text": "Priority",
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
                                          "text": "prioridade",
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
                                                  "text": "descricao",
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
                                                      "text": "descricao",
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
                                                  "text": "prioridade",
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
                                                      "text": "prioridade",
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
                                          "type": "AdditiveExpr",
                                          "children": [
                                            {
                                              "type": "AdditiveExpr",
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
                                                                  "text": "\"[\"",
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
                                                      "type": "PrimaryExpr",
                                                      "children": [
                                                        {
                                                          "type": "Primary",
                                                          "children": [
                                                            {
                                                              "type": "terminal",
                                                              "text": "prioridade",
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
                                                  "text": "+",
                                                  "token_type": "PLUS"
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
                                                              "text": "\"] \"",
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
                                              "text": "+",
                                              "token_type": "PLUS"
                                            },
                                            {
                                              "type": "PrimaryExpr",
                                              "children": [
                                                {
                                                  "type": "Primary",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "descricao",
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
                                      "text": "Scanner",
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
                                  "text": "scanner",
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
                                                          "text": "Scanner",
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
                                                  "text": "in",
                                                  "token_type": "IDENTIFIER"
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
                                      "text": "ArrayList",
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
                                                      "text": "Task",
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
                                  "text": "tarefas",
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
                          "type": "LocalVariableDeclarationStatement",
                          "children": [
                            {
                              "type": "Type",
                              "children": [
                                {
                                  "type": "PrimitiveType",
                                  "children": [
                                    {
                                      "type": "terminal",
                                      "text": "boolean",
                                      "token_type": "BOOLEAN"
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
                                  "text": "continuar",
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
                                                  "text": "true",
                                                  "token_type": "TRUE"
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
                      "type": "BlockStatement",
                      "children": [
                        {
                          "type": "Statement",
                          "children": [
                            {
                              "type": "WhileStatement",
                              "children": [
                                {
                                  "type": "terminal",
                                  "text": "while",
                                  "token_type": "WHILE"
                                },
                                {
                                  "type": "terminal",
                                  "text": "(",
                                  "token_type": "LPAREN"
                                },
                                {
                                  "type": "PrimaryExpr",
                                  "children": [
                                    {
                                      "type": "Primary",
                                      "children": [
                                        {
                                          "type": "terminal",
                                          "text": "continuar",
                                          "token_type": "IDENTIFIER"
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
                                                                          "text": "\"\\n1. Adicionar tarefa\"",
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
                                                                          "text": "\"2. Listar tarefas\"",
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
                                                                          "text": "\"3. Sair\"",
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
                                                          "text": "print",
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
                                                                          "text": "\"Escolha uma op\u00e7\u00e3o: \"",
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
                                                      "text": "opcao",
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
                                                                      "text": "scanner",
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
                                                              "text": "nextInt",
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
                                                                  "text": "scanner",
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
                                                          "text": "nextLine",
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
                                                  "type": "SwitchStatement",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "switch",
                                                      "token_type": "SWITCH"
                                                    },
                                                    {
                                                      "type": "terminal",
                                                      "text": "(",
                                                      "token_type": "LPAREN"
                                                    },
                                                    {
                                                      "type": "PrimaryExpr",
                                                      "children": [
                                                        {
                                                          "type": "Primary",
                                                          "children": [
                                                            {
                                                              "type": "terminal",
                                                              "text": "opcao",
                                                              "token_type": "IDENTIFIER"
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
                                                      "type": "SwitchBlockStatementGroup",
                                                      "children": [
                                                        {
                                                          "type": "SwitchLabel",
                                                          "children": [
                                                            {
                                                              "type": "terminal",
                                                              "text": "case",
                                                              "token_type": "CASE"
                                                            },
                                                            {
                                                              "type": "ConstantExpression",
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
                                                              "text": ":",
                                                              "token_type": "COLON"
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
                                                                          "text": "print",
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
                                                                                          "text": "\"Descri\u00e7\u00e3o da tarefa: \"",
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
                                                                      "text": "desc",
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
                                                                                      "text": "scanner",
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
                                                                              "text": "nextLine",
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
                                                                          "text": "print",
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
                                                                                          "text": "\"Prioridade (BAIXA, MEDIA, ALTA): \"",
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
                                                                      "text": "prioInput",
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
                                                                                          "text": "scanner",
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
                                                                                  "text": "nextLine",
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
                                                                              "text": ".",
                                                                              "token_type": "DOT"
                                                                            },
                                                                            {
                                                                              "type": "terminal",
                                                                              "text": "toUpperCase",
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
                                                                          "text": "Priority",
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
                                                                      "text": "prio",
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
                                                          "type": "BlockStatement",
                                                          "children": [
                                                            {
                                                              "type": "Statement",
                                                              "children": [
                                                                {
                                                                  "type": "TryStatement",
                                                                  "children": [
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": "try",
                                                                      "token_type": "<INVALID>"
                                                                    },
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
                                                                                      "type": "AssignmentExpr",
                                                                                      "children": [
                                                                                        {
                                                                                          "type": "PrimaryExpr",
                                                                                          "children": [
                                                                                            {
                                                                                              "type": "Primary",
                                                                                              "children": [
                                                                                                {
                                                                                                  "type": "terminal",
                                                                                                  "text": "prio",
                                                                                                  "token_type": "IDENTIFIER"
                                                                                                }
                                                                                              ]
                                                                                            }
                                                                                          ]
                                                                                        },
                                                                                        {
                                                                                          "type": "terminal",
                                                                                          "text": "=",
                                                                                          "token_type": "ASSIGN"
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
                                                                                                      "text": "Priority",
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
                                                                                              "text": "valueOf",
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
                                                                                                          "text": "prioInput",
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
                                                                    },
                                                                    {
                                                                      "type": "CatchClause",
                                                                      "children": [
                                                                        {
                                                                          "type": "terminal",
                                                                          "text": "catch",
                                                                          "token_type": "<INVALID>"
                                                                        },
                                                                        {
                                                                          "type": "terminal",
                                                                          "text": "(",
                                                                          "token_type": "LPAREN"
                                                                        },
                                                                        {
                                                                          "type": "Type",
                                                                          "children": [
                                                                            {
                                                                              "type": "ClassOrInterfaceType",
                                                                              "children": [
                                                                                {
                                                                                  "type": "terminal",
                                                                                  "text": "IllegalArgumentException",
                                                                                  "token_type": "IDENTIFIER"
                                                                                }
                                                                              ]
                                                                            }
                                                                          ]
                                                                        },
                                                                        {
                                                                          "type": "terminal",
                                                                          "text": "e",
                                                                          "token_type": "IDENTIFIER"
                                                                        },
                                                                        {
                                                                          "type": "terminal",
                                                                          "text": ")",
                                                                          "token_type": "RPAREN"
                                                                        },
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
                                                                                                              "text": "\"Prioridade inv\u00e1lida. Tarefa ignorada.\"",
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
                                                                                      "type": "BreakStatement",
                                                                                      "children": [
                                                                                        {
                                                                                          "type": "terminal",
                                                                                          "text": "break",
                                                                                          "token_type": "BREAK"
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
                                                                          "type": "PrimaryExpr",
                                                                          "children": [
                                                                            {
                                                                              "type": "Primary",
                                                                              "children": [
                                                                                {
                                                                                  "type": "terminal",
                                                                                  "text": "tarefas",
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
                                                                                                  "text": "Task",
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
                                                                                      "type": "PrimaryExpr",
                                                                                      "children": [
                                                                                        {
                                                                                          "type": "Primary",
                                                                                          "children": [
                                                                                            {
                                                                                              "type": "terminal",
                                                                                              "text": "desc",
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
                                                                                              "text": "prio",
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
                                                                                          "text": "\"Tarefa adicionada.\"",
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
                                                                  "type": "BreakStatement",
                                                                  "children": [
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": "break",
                                                                      "token_type": "BREAK"
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
                                                        }
                                                      ]
                                                    },
                                                    {
                                                      "type": "SwitchBlockStatementGroup",
                                                      "children": [
                                                        {
                                                          "type": "SwitchLabel",
                                                          "children": [
                                                            {
                                                              "type": "terminal",
                                                              "text": "case",
                                                              "token_type": "CASE"
                                                            },
                                                            {
                                                              "type": "ConstantExpression",
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
                                                                              "text": "2",
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
                                                              "text": ":",
                                                              "token_type": "COLON"
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
                                                                                  "text": "tarefas",
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
                                                                                                              "text": "\"Nenhuma tarefa.\"",
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
                                                                                                              "text": "\"\\nTarefas:\"",
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
                                                                                                          "text": "Task",
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
                                                                                                      "text": "t",
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
                                                                                                          "text": "tarefas",
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
                                                                                                                                      "text": "\"- \"",
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
                                                                                                                          "type": "PrimaryExpr",
                                                                                                                          "children": [
                                                                                                                            {
                                                                                                                              "type": "Primary",
                                                                                                                              "children": [
                                                                                                                                {
                                                                                                                                  "type": "terminal",
                                                                                                                                  "text": "t",
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
                                                                  "type": "BreakStatement",
                                                                  "children": [
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": "break",
                                                                      "token_type": "BREAK"
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
                                                        }
                                                      ]
                                                    },
                                                    {
                                                      "type": "SwitchBlockStatementGroup",
                                                      "children": [
                                                        {
                                                          "type": "SwitchLabel",
                                                          "children": [
                                                            {
                                                              "type": "terminal",
                                                              "text": "case",
                                                              "token_type": "CASE"
                                                            },
                                                            {
                                                              "type": "ConstantExpression",
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
                                                                              "text": "3",
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
                                                              "text": ":",
                                                              "token_type": "COLON"
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
                                                                          "type": "PrimaryExpr",
                                                                          "children": [
                                                                            {
                                                                              "type": "Primary",
                                                                              "children": [
                                                                                {
                                                                                  "type": "terminal",
                                                                                  "text": "continuar",
                                                                                  "token_type": "IDENTIFIER"
                                                                                }
                                                                              ]
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
                                                                                  "type": "Literal",
                                                                                  "children": [
                                                                                    {
                                                                                      "type": "terminal",
                                                                                      "text": "false",
                                                                                      "token_type": "FALSE"
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
                                                                                          "text": "\"A sair...\"",
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
                                                                  "type": "BreakStatement",
                                                                  "children": [
                                                                    {
                                                                      "type": "terminal",
                                                                      "text": "break",
                                                                      "token_type": "BREAK"
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
                                                        }
                                                      ]
                                                    },
                                                    {
                                                      "type": "SwitchBlockStatementGroup",
                                                      "children": [
                                                        {
                                                          "type": "SwitchLabel",
                                                          "children": [
                                                            {
                                                              "type": "terminal",
                                                              "text": "default",
                                                              "token_type": "DEFAULT"
                                                            },
                                                            {
                                                              "type": "terminal",
                                                              "text": ":",
                                                              "token_type": "COLON"
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
                                                                                          "text": "\"Op\u00e7\u00e3o inv\u00e1lida.\"",
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
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "scanner",
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
                                      "text": "close",
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
      "module": "enum",
      "names": [
        {
          "type": "alias",
          "name": "Enum",
          "asname": null
        },
        {
          "type": "alias",
          "name": "auto",
          "asname": null
        }
      ],
      "level": 0
    },
    {
      "type": "ClassDef",
      "name": "test3",
      "bases": [],
      "keywords": [],
      "decorator_list": [],
      "body": [
        {
          "type": "ClassDef",
          "name": "Priority",
          "bases": [
            {
              "type": "Name",
              "id": "Enum",
              "ctx": "Load"
            }
          ],
          "keywords": [],
          "decorator_list": [],
          "body": [
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Name",
                  "id": "BAIXA",
                  "ctx": "Store"
                }
              ],
              "value": {
                "type": "Call",
                "func": {
                  "type": "Name",
                  "id": "auto",
                  "ctx": "Load"
                },
                "args": [],
                "keywords": []
              }
            },
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Name",
                  "id": "MEDIA",
                  "ctx": "Store"
                }
              ],
              "value": {
                "type": "Call",
                "func": {
                  "type": "Name",
                  "id": "auto",
                  "ctx": "Load"
                },
                "args": [],
                "keywords": []
              }
            },
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Name",
                  "id": "ALTA",
                  "ctx": "Store"
                }
              ],
              "value": {
                "type": "Call",
                "func": {
                  "type": "Name",
                  "id": "auto",
                  "ctx": "Load"
                },
                "args": [],
                "keywords": []
              }
            }
          ]
        },
        {
          "type": "ClassDef",
          "name": "Task",
          "bases": [],
          "keywords": [],
          "decorator_list": [],
          "body": [
            {
              "type": "AnnAssign",
              "target": {
                "type": "Name",
                "id": "descricao",
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
                "id": "prioridade",
                "ctx": "Store"
              },
              "annotation": {
                "type": "Constant",
                "value": "test3.Priority",
                "kind": null
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
                    "arg": "descricao",
                    "annotation": {
                      "type": "Name",
                      "id": "str",
                      "ctx": "Load"
                    }
                  },
                  {
                    "type": "arg",
                    "arg": "prioridade",
                    "annotation": {
                      "type": "Constant",
                      "value": "test3.Priority",
                      "kind": null
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
                      "attr": "descricao",
                      "ctx": "Store"
                    }
                  ],
                  "value": {
                    "type": "Name",
                    "id": "descricao",
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
                      "attr": "prioridade",
                      "ctx": "Store"
                    }
                  ],
                  "value": {
                    "type": "Name",
                    "id": "prioridade",
                    "ctx": "Load"
                  }
                }
              ],
              "decorator_list": [],
              "returns": null
            },
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
                        "value": "[",
                        "kind": null
                      },
                      {
                        "type": "FormattedValue",
                        "value": {
                          "type": "Attribute",
                          "value": {
                            "type": "Attribute",
                            "value": {
                              "type": "Name",
                              "id": "self",
                              "ctx": "Load"
                            },
                            "attr": "prioridade",
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
                        "value": "] ",
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
                          "attr": "descricao",
                          "ctx": "Load"
                        },
                        "conversion": -1,
                        "format_spec": null
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
        },
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
              "type": "AnnAssign",
              "target": {
                "type": "Name",
                "id": "tarefas",
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
                  "value": "test3.Task",
                  "kind": null
                },
                "ctx": "Load"
              },
              "value": {
                "type": "List",
                "elts": [],
                "ctx": "Load"
              },
              "simple": 1
            },
            {
              "type": "AnnAssign",
              "target": {
                "type": "Name",
                "id": "continuar",
                "ctx": "Store"
              },
              "annotation": {
                "type": "Name",
                "id": "bool",
                "ctx": "Load"
              },
              "value": {
                "type": "Constant",
                "value": true,
                "kind": null
              },
              "simple": 1
            },
            {
              "type": "While",
              "test": {
                "type": "Name",
                "id": "continuar",
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
                        "type": "Constant",
                        "value": "\n1. Adicionar tarefa",
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
                      "type": "Name",
                      "id": "print",
                      "ctx": "Load"
                    },
                    "args": [
                      {
                        "type": "Constant",
                        "value": "2. Listar tarefas",
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
                      "type": "Name",
                      "id": "print",
                      "ctx": "Load"
                    },
                    "args": [
                      {
                        "type": "Constant",
                        "value": "3. Sair",
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
                      "id": "choice_str",
                      "ctx": "Store"
                    }
                  ],
                  "value": {
                    "type": "Call",
                    "func": {
                      "type": "Name",
                      "id": "input",
                      "ctx": "Load"
                    },
                    "args": [
                      {
                        "type": "Constant",
                        "value": "Escolha uma opção: ",
                        "kind": null
                      }
                    ],
                    "keywords": []
                  }
                },
                {
                  "type": "Try",
                  "body": [
                    {
                      "type": "Assign",
                      "targets": [
                        {
                          "type": "Name",
                          "id": "opcao",
                          "ctx": "Store"
                        }
                      ],
                      "value": {
                        "type": "Call",
                        "func": {
                          "type": "Name",
                          "id": "int",
                          "ctx": "Load"
                        },
                        "args": [
                          {
                            "type": "Name",
                            "id": "choice_str",
                            "ctx": "Load"
                          }
                        ],
                        "keywords": []
                      }
                    }
                  ],
                  "handlers": [
                    {
                      "_nodetype": "ExceptHandler",
                      "type": {
                        "type": "Name",
                        "id": "ValueError",
                        "ctx": "Load"
                      },
                      "name": null,
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
                                "value": "Opção inválida. Por favor, insira um número.",
                                "kind": null
                              }
                            ],
                            "keywords": []
                          }
                        },
                        {
                          "type": "Continue"
                        }
                      ]
                    }
                  ],
                  "orelse": [],
                  "finalbody": []
                },
                {
                  "type": "Match",
                  "subject": {
                    "type": "Name",
                    "id": "opcao",
                    "ctx": "Load"
                  },
                  "cases": [
                    {
                      "_nodetype": "match_case",
                      "pattern": {
                        "type": "MatchValue",
                        "value": {
                          "type": "Constant",
                          "value": 1,
                          "kind": null
                        }
                      },
                      "guard": null,
                      "body": [
                        {
                          "type": "Assign",
                          "targets": [
                            {
                              "type": "Name",
                              "id": "desc",
                              "ctx": "Store"
                            }
                          ],
                          "value": {
                            "type": "Call",
                            "func": {
                              "type": "Name",
                              "id": "input",
                              "ctx": "Load"
                            },
                            "args": [
                              {
                                "type": "Constant",
                                "value": "Descrição da tarefa: ",
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
                              "id": "prio_input",
                              "ctx": "Store"
                            }
                          ],
                          "value": {
                            "type": "Call",
                            "func": {
                              "type": "Attribute",
                              "value": {
                                "type": "Call",
                                "func": {
                                  "type": "Name",
                                  "id": "input",
                                  "ctx": "Load"
                                },
                                "args": [
                                  {
                                    "type": "Constant",
                                    "value": "Prioridade (BAIXA, MEDIA, ALTA): ",
                                    "kind": null
                                  }
                                ],
                                "keywords": []
                              },
                              "attr": "upper",
                              "ctx": "Load"
                            },
                            "args": [],
                            "keywords": []
                          }
                        },
                        {
                          "type": "AnnAssign",
                          "target": {
                            "type": "Name",
                            "id": "prio",
                            "ctx": "Store"
                          },
                          "annotation": {
                            "type": "Constant",
                            "value": "test3.Priority",
                            "kind": null
                          },
                          "value": null,
                          "simple": 1
                        },
                        {
                          "type": "Try",
                          "body": [
                            {
                              "type": "Assign",
                              "targets": [
                                {
                                  "type": "Name",
                                  "id": "prio",
                                  "ctx": "Store"
                                }
                              ],
                              "value": {
                                "type": "Subscript",
                                "value": {
                                  "type": "Attribute",
                                  "value": {
                                    "type": "Name",
                                    "id": "test3",
                                    "ctx": "Load"
                                  },
                                  "attr": "Priority",
                                  "ctx": "Load"
                                },
                                "slice": {
                                  "type": "Name",
                                  "id": "prio_input",
                                  "ctx": "Load"
                                },
                                "ctx": "Load"
                              }
                            }
                          ],
                          "handlers": [
                            {
                              "_nodetype": "ExceptHandler",
                              "type": {
                                "type": "Name",
                                "id": "KeyError",
                                "ctx": "Load"
                              },
                              "name": null,
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
                                        "value": "Prioridade inválida. Tarefa ignorada.",
                                        "kind": null
                                      }
                                    ],
                                    "keywords": []
                                  }
                                },
                                {
                                  "type": "Continue"
                                }
                              ]
                            }
                          ],
                          "orelse": [],
                          "finalbody": []
                        },
                        {
                          "type": "Expr",
                          "value": {
                            "type": "Call",
                            "func": {
                              "type": "Attribute",
                              "value": {
                                "type": "Name",
                                "id": "tarefas",
                                "ctx": "Load"
                              },
                              "attr": "append",
                              "ctx": "Load"
                            },
                            "args": [
                              {
                                "type": "Call",
                                "func": {
                                  "type": "Attribute",
                                  "value": {
                                    "type": "Name",
                                    "id": "test3",
                                    "ctx": "Load"
                                  },
                                  "attr": "Task",
                                  "ctx": "Load"
                                },
                                "args": [
                                  {
                                    "type": "Name",
                                    "id": "desc",
                                    "ctx": "Load"
                                  },
                                  {
                                    "type": "Name",
                                    "id": "prio",
                                    "ctx": "Load"
                                  }
                                ],
                                "keywords": []
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
                                "type": "Constant",
                                "value": "Tarefa adicionada.",
                                "kind": null
                              }
                            ],
                            "keywords": []
                          }
                        }
                      ]
                    },
                    {
                      "_nodetype": "match_case",
                      "pattern": {
                        "type": "MatchValue",
                        "value": {
                          "type": "Constant",
                          "value": 2,
                          "kind": null
                        }
                      },
                      "guard": null,
                      "body": [
                        {
                          "type": "If",
                          "test": {
                            "type": "UnaryOp",
                            "op": {
                              "type": "Not"
                            },
                            "operand": {
                              "type": "Name",
                              "id": "tarefas",
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
                                    "value": "Nenhuma tarefa.",
                                    "kind": null
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
                                    "value": "\nTarefas:",
                                    "kind": null
                                  }
                                ],
                                "keywords": []
                              }
                            },
                            {
                              "type": "For",
                              "target": {
                                "type": "Name",
                                "id": "t",
                                "ctx": "Store"
                              },
                              "iter": {
                                "type": "Name",
                                "id": "tarefas",
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
                                        "type": "JoinedStr",
                                        "values": [
                                          {
                                            "type": "Constant",
                                            "value": "- ",
                                            "kind": null
                                          },
                                          {
                                            "type": "FormattedValue",
                                            "value": {
                                              "type": "Name",
                                              "id": "t",
                                              "ctx": "Load"
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
                              "orelse": null
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "_nodetype": "match_case",
                      "pattern": {
                        "type": "MatchValue",
                        "value": {
                          "type": "Constant",
                          "value": 3,
                          "kind": null
                        }
                      },
                      "guard": null,
                      "body": [
                        {
                          "type": "Assign",
                          "targets": [
                            {
                              "type": "Name",
                              "id": "continuar",
                              "ctx": "Store"
                            }
                          ],
                          "value": {
                            "type": "Constant",
                            "value": false,
                            "kind": null
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
                                "value": "A sair...",
                                "kind": null
                              }
                            ],
                            "keywords": []
                          }
                        }
                      ]
                    },
                    {
                      "_nodetype": "match_case",
                      "pattern": {
                        "type": "MatchAs",
                        "name": null,
                        "pattern": null
                      },
                      "guard": null,
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
                                "value": "Opção inválida.",
                                "kind": null
                              }
                            ],
                            "keywords": []
                          }
                        }
                      ]
                    }
                  ]
                }
              ],
              "orelse": []
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
                "id": "test3",
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

### Testing `Task.__str__`

**AI-Generated Test Script:**

```python
import unittest
from test_files.test3 import test3

class TestTaskStr(unittest.TestCase):

    def test_task_str_representation(self):
        # Test case 1: Basic task with BAIXA priority
        task1 = test3.Task("Comprar pão", test3.Priority.BAIXA)
        self.assertEqual(str(task1), "[BAIXA] Comprar pão")

        # Test case 2: Task with MEDIA priority
        task2 = test3.Task("Revisar código", test3.Priority.MEDIA)
        self.assertEqual(str(task2), "[MEDIA] Revisar código")

        # Test case 3: Task with ALTA priority
        task3 = test3.Task("Entregar projeto", test3.Priority.ALTA)
        self.assertEqual(str(task3), "[ALTA] Entregar projeto")

        # Test case 4: Task with empty description
        task4 = test3.Task("", test3.Priority.BAIXA)
        self.assertEqual(str(task4), "[BAIXA] ")

        # Test case 5: Task with numeric description
        task5 = test3.Task("12345", test3.Priority.MEDIA)
        self.assertEqual(str(task5), "[MEDIA] 12345")

        # Test case 6: Task with special characters in description
        task6 = test3.Task("Tarefa com !@#$%^&*()", test3.Priority.ALTA)
        self.assertEqual(str(task6), "[ALTA] Tarefa com !@#$%^&*()")

if __name__ == '__main__':
    unittest.main()
```

**Test Execution Results:**

```
❌ FAILED

Stderr:
Traceback (most recent call last):
  File "D:\Reposit�rios\JavaToPython-Transpiler-Web-app\outputs\2025-07-30_16-45-42-655837\temp_test_Task.__str__.py", line 2, in <module>
    from test_files.test3 import test3
ModuleNotFoundError: No module named 'test_files'

Stdout:

```

**Overall Test Result: ❌ One or more generated tests failed.**

## Final Generated Python Code

```python
# Unit test result: ❌ FAILED (see log for details)
from enum import Enum, auto

class test3:

    class Priority(Enum):
        BAIXA = auto()
        MEDIA = auto()
        ALTA = auto()

    class Task:
        descricao: str
        prioridade: 'test3.Priority'

        def __init__(self, descricao: str, prioridade: 'test3.Priority'):
            self.descricao = descricao
            self.prioridade = prioridade

        def __str__(self) -> str:
            return f'[{self.prioridade.name}] {self.descricao}'

    @staticmethod
    def main(args: list[str]):
        tarefas: list['test3.Task'] = []
        continuar: bool = True
        while continuar:
            print('\n1. Adicionar tarefa')
            print('2. Listar tarefas')
            print('3. Sair')
            choice_str = input('Escolha uma opção: ')
            try:
                opcao = int(choice_str)
            except ValueError:
                print('Opção inválida. Por favor, insira um número.')
                continue
            match opcao:
                case 1:
                    desc = input('Descrição da tarefa: ')
                    prio_input = input('Prioridade (BAIXA, MEDIA, ALTA): ').upper()
                    prio: 'test3.Priority'
                    try:
                        prio = test3.Priority[prio_input]
                    except KeyError:
                        print('Prioridade inválida. Tarefa ignorada.')
                        continue
                    tarefas.append(test3.Task(desc, prio))
                    print('Tarefa adicionada.')
                case 2:
                    if not tarefas:
                        print('Nenhuma tarefa.')
                    else:
                        print('\nTarefas:')
                        for t in tarefas:
                            print(f'- {t}')
                case 3:
                    continuar = False
                    print('A sair...')
                case _:
                    print('Opção inválida.')
if __name__ == '__main__':
    test3.main([])
```
