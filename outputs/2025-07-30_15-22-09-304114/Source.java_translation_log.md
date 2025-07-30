# Translation Log for: `Source.java`
Model: `gemini-2.5-flash`


---

# Processing File: uploads\2025-07-30_15-22-09-304114\Source.java

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
              "text": "demo",
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
              "text": "org",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "springframework",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "boot",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "SpringApplication",
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
              "text": "org",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "springframework",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "boot",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "autoconfigure",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "SpringBootApplication",
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
              "text": "org",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "springframework",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "web",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "bind",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "annotation",
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
          "text": "*",
          "token_type": "MULT"
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
              "text": "org",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "springframework",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "stereotype",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "Service",
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
              "text": "org",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "springframework",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "stereotype",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "Repository",
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
              "text": "org",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "springframework",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "beans",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "factory",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "annotation",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "Autowired",
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
              "text": "javax",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "annotation",
              "token_type": "IDENTIFIER"
            },
            {
              "type": "terminal",
              "text": ".",
              "token_type": "DOT"
            },
            {
              "type": "terminal",
              "text": "PostConstruct",
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
          "text": "*",
          "token_type": "MULT"
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
                      "text": "SpringBootApplication",
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
              "type": "terminal",
              "text": "class",
              "token_type": "CLASS"
            },
            {
              "type": "terminal",
              "text": "DemoApplication",
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
                                      "type": "PrimaryExpr",
                                      "children": [
                                        {
                                          "type": "Primary",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "SpringApplication",
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
                                      "text": "run",
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
                                                  "type": "ClassOrInterfaceType",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "DemoApplication",
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
                                                  "text": "class",
                                                  "token_type": "CLASS"
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
                      "text": "Usuario",
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
                                      "text": "Long",
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
                                  "text": "nome",
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
                              "text": "Usuario",
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
                              "text": "Usuario",
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
                                              "text": "Long",
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
                                          "text": "nome",
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
                                                  "text": "nome",
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
                                                      "text": "nome",
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
                                      "type": "ClassOrInterfaceType",
                                      "children": [
                                        {
                                          "type": "terminal",
                                          "text": "Long",
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
                                          "type": "ClassOrInterfaceType",
                                          "children": [
                                            {
                                              "type": "terminal",
                                              "text": "Long",
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
                              "text": "getNome",
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
                                                  "text": "nome",
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
                              "text": "setNome",
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
                                          "text": "nome",
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
                                                  "text": "nome",
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
                                                      "text": "nome",
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
                              "text": "RestController",
                              "token_type": "IDENTIFIER"
                            }
                          ]
                        }
                      ]
                    },
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
                              "text": "RequestMapping",
                              "token_type": "IDENTIFIER"
                            }
                          ]
                        },
                        {
                          "type": "terminal",
                          "text": "(",
                          "token_type": "LPAREN"
                        },
                        {
                          "type": "ElementValuePairList",
                          "children": [
                            {
                              "type": "ElementValuePair",
                              "children": [
                                {
                                  "type": "ElementValue",
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
                                                  "text": "\"/api/usuarios\"",
                                                  "token_type": "StringLiteral"
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
                      "type": "terminal",
                      "text": "class",
                      "token_type": "CLASS"
                    },
                    {
                      "type": "terminal",
                      "text": "UsuarioController",
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
                                      "text": "Autowired",
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
                                      "text": "UsuarioService",
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
                                      "text": "GetMapping",
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
                                                          "text": "Usuario",
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
                                }
                              ]
                            },
                            {
                              "type": "terminal",
                              "text": "listar",
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
                                              "text": "obterTodos",
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
                                      "text": "GetMapping",
                                      "token_type": "IDENTIFIER"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": "(",
                                  "token_type": "LPAREN"
                                },
                                {
                                  "type": "ElementValuePairList",
                                  "children": [
                                    {
                                      "type": "ElementValuePair",
                                      "children": [
                                        {
                                          "type": "ElementValue",
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
                                                          "text": "\"/{id}\"",
                                                          "token_type": "StringLiteral"
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
                                          "text": "Usuario",
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
                              "text": "obter",
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
                                              "text": "PathVariable",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
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
                                              "text": "Long",
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
                                              "text": "obterPorId",
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
                                      "text": "PostMapping",
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
                                          "text": "Usuario",
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
                              "text": "criar",
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
                                              "text": "RequestBody",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
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
                                              "text": "Usuario",
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
                                          "text": "usuario",
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
                                              "text": "criar",
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
                                                          "text": "usuario",
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
                                      "text": "PutMapping",
                                      "token_type": "IDENTIFIER"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": "(",
                                  "token_type": "LPAREN"
                                },
                                {
                                  "type": "ElementValuePairList",
                                  "children": [
                                    {
                                      "type": "ElementValuePair",
                                      "children": [
                                        {
                                          "type": "ElementValue",
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
                                                          "text": "\"/{id}\"",
                                                          "token_type": "StringLiteral"
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
                                          "text": "Usuario",
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
                              "text": "atualizar",
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
                                              "text": "PathVariable",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
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
                                              "text": "Long",
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
                                              "text": "RequestBody",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
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
                                              "text": "Usuario",
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
                                          "text": "usuario",
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
                                              "type": "PrimaryExpr",
                                              "children": [
                                                {
                                                  "type": "Primary",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "usuario",
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
                                              "text": "setId",
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
                                              "text": "atualizar",
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
                                                          "text": "usuario",
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
                                      "text": "DeleteMapping",
                                      "token_type": "IDENTIFIER"
                                    }
                                  ]
                                },
                                {
                                  "type": "terminal",
                                  "text": "(",
                                  "token_type": "LPAREN"
                                },
                                {
                                  "type": "ElementValuePairList",
                                  "children": [
                                    {
                                      "type": "ElementValuePair",
                                      "children": [
                                        {
                                          "type": "ElementValue",
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
                                                          "text": "\"/{id}\"",
                                                          "token_type": "StringLiteral"
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
                              "text": "remover",
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
                                              "text": "PathVariable",
                                              "token_type": "IDENTIFIER"
                                            }
                                          ]
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
                                              "text": "Long",
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
                                              "text": "remover",
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
                  "type": "ClassDeclaration",
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
                              "text": "Service",
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
                      "text": "UsuarioService",
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
                                      "text": "Autowired",
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
                                      "text": "UsuarioRepository",
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
                                  "text": "repo",
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
                                                          "text": "Usuario",
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
                                }
                              ]
                            },
                            {
                              "type": "terminal",
                              "text": "obterTodos",
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
                                                      "text": "repo",
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
                                              "text": "findAll",
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
                                          "text": "Usuario",
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
                              "text": "obterPorId",
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
                                              "text": "Long",
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
                                                          "text": "repo",
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
                                                  "text": "findById",
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
                                              "text": "orElse",
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
                                          "text": "Usuario",
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
                              "text": "criar",
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
                                              "text": "Usuario",
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
                                          "text": "usuario",
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
                                                      "text": "repo",
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
                                              "text": "save",
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
                                                          "text": "usuario",
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
                                          "text": "Usuario",
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
                              "text": "atualizar",
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
                                              "text": "Usuario",
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
                                          "text": "usuario",
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
                                                      "text": "repo",
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
                                              "text": "save",
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
                                                          "text": "usuario",
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
                              "text": "remover",
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
                                              "text": "Long",
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
                                                      "text": "repo",
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
                                              "text": "deleteById",
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
                  "type": "ClassDeclaration",
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
                              "text": "Repository",
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
                      "text": "UsuarioRepository",
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
                                      "text": "Map",
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
                                                      "text": "Long",
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
                                          "text": ",",
                                          "token_type": "COMMA"
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
                                                      "text": "Usuario",
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
                                  "text": "armazenamento",
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
                                                          "text": "HashMap",
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
                                      "text": "Long",
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
                                  "text": "sequence",
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
                                                  "text": "0L",
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
                                      "text": "PostConstruct",
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
                                  "type": "terminal",
                                  "text": "void",
                                  "token_type": "VOID"
                                }
                              ]
                            },
                            {
                              "type": "terminal",
                              "text": "init",
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
                                          "type": "MethodCallExpr",
                                          "children": [
                                            {
                                              "type": "PrimaryExpr",
                                              "children": [
                                                {
                                                  "type": "Primary",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "save",
                                                      "token_type": "IDENTIFIER"
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
                                                                      "text": "Usuario",
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
                                          "type": "MethodCallExpr",
                                          "children": [
                                            {
                                              "type": "PrimaryExpr",
                                              "children": [
                                                {
                                                  "type": "Primary",
                                                  "children": [
                                                    {
                                                      "type": "terminal",
                                                      "text": "save",
                                                      "token_type": "IDENTIFIER"
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
                                                                      "text": "Usuario",
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
                                                                      "text": "\"Bruno\"",
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
                                                                      "text": "\"bruno@example.com\"",
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
                                          "text": "Optional",
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
                                                          "text": "Usuario",
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
                                }
                              ]
                            },
                            {
                              "type": "terminal",
                              "text": "findById",
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
                                              "text": "Long",
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
                                                      "text": "Optional",
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
                                              "text": "ofNullable",
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
                                                              "text": "armazenamento",
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
                                                      "text": "get",
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
                                                          "text": "Usuario",
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
                                }
                              ]
                            },
                            {
                              "type": "terminal",
                              "text": "findAll",
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
                                                              "text": "armazenamento",
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
                                                      "text": "values",
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
                                          "text": "Usuario",
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
                              "text": "save",
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
                                              "text": "Usuario",
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
                                          "text": "usuario",
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
                                                          "text": "usuario",
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
                                                                  "type": "PrimaryExpr",
                                                                  "children": [
                                                                    {
                                                                      "type": "Primary",
                                                                      "children": [
                                                                        {
                                                                          "type": "terminal",
                                                                          "text": "usuario",
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
                                                                  "text": "setId",
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
                                                                      "type": "PreIncrementExpr",
                                                                      "children": [
                                                                        {
                                                                          "type": "terminal",
                                                                          "text": "++",
                                                                          "token_type": "INC"
                                                                        },
                                                                        {
                                                                          "type": "PrimaryExpr",
                                                                          "children": [
                                                                            {
                                                                              "type": "Primary",
                                                                              "children": [
                                                                                {
                                                                                  "type": "terminal",
                                                                                  "text": "sequence",
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
                                                      "text": "armazenamento",
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
                                              "text": "put",
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
                                                              "text": "usuario",
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
                                                          "text": "usuario",
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
                                                  "text": "usuario",
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
                              "text": "deleteById",
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
                                              "text": "Long",
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
                                                      "text": "armazenamento",
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
                                              "text": "remove",
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
      "module": "flask",
      "names": [
        { "type": "alias", "name": "Flask", "asname": null },
        { "type": "alias", "name": "jsonify", "asname": null },
        { "type": "alias", "name": "request", "asname": null }
      ],
      "level": 0
    },
    {
      "type": "ImportFrom",
      "module": "typing",
      "names": [
        { "type": "alias", "name": "List", "asname": null },
        { "type": "alias", "name": "Optional", "asname": null }
      ],
      "level": 0
    },
    {
      "type": "ClassDef",
      "name": "Usuario",
      "bases": [],
      "keywords": [],
      "decorator_list": [],
      "body": [
        {
          "type": "AnnAssign",
          "target": { "type": "Name", "id": "id", "ctx": "Store" },
          "annotation": {
            "type": "Subscript",
            "value": { "type": "Name", "id": "Optional", "ctx": "Load" },
            "slice": { "type": "Name", "id": "int", "ctx": "Load" },
            "ctx": "Load"
          },
          "value": null,
          "simple": 1
        },
        {
          "type": "AnnAssign",
          "target": { "type": "Name", "id": "nome", "ctx": "Store" },
          "annotation": { "type": "Name", "id": "str", "ctx": "Load" },
          "value": null,
          "simple": 1
        },
        {
          "type": "AnnAssign",
          "target": { "type": "Name", "id": "email", "ctx": "Store" },
          "annotation": { "type": "Name", "id": "str", "ctx": "Load" },
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
              { "type": "arg", "arg": "self", "annotation": null },
              {
                "type": "arg",
                "arg": "id",
                "annotation": {
                  "type": "Subscript",
                  "value": { "type": "Name", "id": "Optional", "ctx": "Load" },
                  "slice": { "type": "Name", "id": "int", "ctx": "Load" },
                  "ctx": "Load"
                }
              },
              {
                "type": "arg",
                "arg": "nome",
                "annotation": { "type": "Name", "id": "str", "ctx": "Load" }
              },
              {
                "type": "arg",
                "arg": "email",
                "annotation": { "type": "Name", "id": "str", "ctx": "Load" }
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
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "id",
                  "ctx": "Store"
                }
              ],
              "value": { "type": "Name", "id": "id", "ctx": "Load" }
            },
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Attribute",
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "nome",
                  "ctx": "Store"
                }
              ],
              "value": { "type": "Name", "id": "nome", "ctx": "Load" }
            },
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Attribute",
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "email",
                  "ctx": "Store"
                }
              ],
              "value": { "type": "Name", "id": "email", "ctx": "Load" }
            }
          ],
          "decorator_list": [],
          "returns": null
        },
        {
          "type": "FunctionDef",
          "name": "to_dict",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              { "type": "arg", "arg": "self", "annotation": null }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Return",
              "value": {
                "type": "Dict",
                "keys": [
                  { "type": "Constant", "value": "id", "kind": null },
                  { "type": "Constant", "value": "nome", "kind": null },
                  { "type": "Constant", "value": "email", "kind": null }
                ],
                "values": [
                  {
                    "type": "Attribute",
                    "value": { "type": "Name", "id": "self", "ctx": "Load" },
                    "attr": "id",
                    "ctx": "Load"
                  },
                  {
                    "type": "Attribute",
                    "value": { "type": "Name", "id": "self", "ctx": "Load" },
                    "attr": "nome",
                    "ctx": "Load"
                  },
                  {
                    "type": "Attribute",
                    "value": { "type": "Name", "id": "self", "ctx": "Load" },
                    "attr": "email",
                    "ctx": "Load"
                  }
                ]
              }
            }
          ],
          "decorator_list": [],
          "returns": null
        }
      ],
      "type_comment": null
    },
    {
      "type": "ClassDef",
      "name": "UsuarioRepository",
      "bases": [],
      "keywords": [],
      "decorator_list": [],
      "body": [
        {
          "type": "AnnAssign",
          "target": { "type": "Name", "id": "armazenamento", "ctx": "Store" },
          "annotation": {
            "type": "Subscript",
            "value": { "type": "Name", "id": "dict", "ctx": "Load" },
            "slice": {
              "type": "Tuple",
              "elts": [
                { "type": "Name", "id": "int", "ctx": "Load" },
                { "type": "Name", "id": "Usuario", "ctx": "Load" }
              ],
              "ctx": "Load"
            },
            "ctx": "Load"
          },
          "value": null,
          "simple": 1
        },
        {
          "type": "AnnAssign",
          "target": { "type": "Name", "id": "sequence", "ctx": "Store" },
          "annotation": { "type": "Name", "id": "int", "ctx": "Load" },
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
              { "type": "arg", "arg": "self", "annotation": null }
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
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "armazenamento",
                  "ctx": "Store"
                }
              ],
              "value": { "type": "Dict", "keys": [], "values": [] }
            },
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Attribute",
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "sequence",
                  "ctx": "Store"
                }
              ],
              "value": { "type": "Constant", "value": 0, "kind": null }
            },
            {
              "type": "Expr",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Attribute",
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "init_data",
                  "ctx": "Load"
                },
                "args": [],
                "keywords": []
              }
            }
          ],
          "decorator_list": [],
          "returns": null
        },
        {
          "type": "FunctionDef",
          "name": "init_data",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              { "type": "arg", "arg": "self", "annotation": null }
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
                  "type": "Attribute",
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "save",
                  "ctx": "Load"
                },
                "args": [
                  {
                    "type": "Call",
                    "func": { "type": "Name", "id": "Usuario", "ctx": "Load" },
                    "args": [
                      { "type": "Constant", "value": null, "kind": null },
                      { "type": "Constant", "value": "Alice", "kind": null },
                      { "type": "Constant", "value": "alice@example.com", "kind": null }
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
                  "type": "Attribute",
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "save",
                  "ctx": "Load"
                },
                "args": [
                  {
                    "type": "Call",
                    "func": { "type": "Name", "id": "Usuario", "ctx": "Load" },
                    "args": [
                      { "type": "Constant", "value": null, "kind": null },
                      { "type": "Constant", "value": "Bruno", "kind": null },
                      { "type": "Constant", "value": "bruno@example.com", "kind": null }
                    ],
                    "keywords": []
                  }
                ],
                "keywords": []
              }
            }
          ],
          "decorator_list": [],
          "returns": null
        },
        {
          "type": "FunctionDef",
          "name": "find_by_id",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              { "type": "arg", "arg": "self", "annotation": null },
              { "type": "arg", "arg": "id", "annotation": { "type": "Name", "id": "int", "ctx": "Load" } }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Return",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Attribute",
                  "value": {
                    "type": "Attribute",
                    "value": { "type": "Name", "id": "self", "ctx": "Load" },
                    "attr": "armazenamento",
                    "ctx": "Load"
                  },
                  "attr": "get",
                  "ctx": "Load"
                },
                "args": [
                  { "type": "Name", "id": "id", "ctx": "Load" }
                ],
                "keywords": []
              }
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Subscript",
            "value": { "type": "Name", "id": "Optional", "ctx": "Load" },
            "slice": { "type": "Name", "id": "Usuario", "ctx": "Load" },
            "ctx": "Load"
          }
        },
        {
          "type": "FunctionDef",
          "name": "find_all",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              { "type": "arg", "arg": "self", "annotation": null }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Return",
              "value": {
                "type": "Call",
                "func": { "type": "Name", "id": "list", "ctx": "Load" },
                "args": [
                  {
                    "type": "Call",
                    "func": {
                      "type": "Attribute",
                      "value": {
                        "type": "Attribute",
                        "value": { "type": "Name", "id": "self", "ctx": "Load" },
                        "attr": "armazenamento",
                        "ctx": "Load"
                      },
                      "attr": "values",
                      "ctx": "Load"
                    },
                    "args": [],
                    "keywords": []
                  }
                ],
                "keywords": []
              }
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Subscript",
            "value": { "type": "Name", "id": "List", "ctx": "Load" },
            "slice": { "type": "Name", "id": "Usuario", "ctx": "Load" },
            "ctx": "Load"
          }
        },
        {
          "type": "FunctionDef",
          "name": "save",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              { "type": "arg", "arg": "self", "annotation": null },
              { "type": "arg", "arg": "usuario", "annotation": { "type": "Name", "id": "Usuario", "ctx": "Load" } }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "If",
              "test": {
                "type": "Compare",
                "left": {
                  "type": "Attribute",
                  "value": { "type": "Name", "id": "usuario", "ctx": "Load" },
                  "attr": "id",
                  "ctx": "Load"
                },
                "ops": [ { "type": "Is" } ],
                "comparators": [ { "type": "Constant", "value": null, "kind": null } ]
              },
              "body": [
                {
                  "type": "AugAssign",
                  "target": {
                    "type": "Attribute",
                    "value": { "type": "Name", "id": "self", "ctx": "Load" },
                    "attr": "sequence",
                    "ctx": "Store"
                  },
                  "op": { "type": "Add" },
                  "value": { "type": "Constant", "value": 1, "kind": null }
                },
                {
                  "type": "Assign",
                  "targets": [
                    {
                      "type": "Attribute",
                      "value": { "type": "Name", "id": "usuario", "ctx": "Load" },
                      "attr": "id",
                      "ctx": "Store"
                    }
                  ],
                  "value": {
                    "type": "Attribute",
                    "value": { "type": "Name", "id": "self", "ctx": "Load" },
                    "attr": "sequence",
                    "ctx": "Load"
                  }
                }
              ],
              "orelse": []
            },
            {
              "type": "Assign",
              "targets": [
                {
                  "type": "Subscript",
                  "value": {
                    "type": "Attribute",
                    "value": { "type": "Name", "id": "self", "ctx": "Load" },
                    "attr": "armazenamento",
                    "ctx": "Load"
                  },
                  "slice": {
                    "type": "Attribute",
                    "value": { "type": "Name", "id": "usuario", "ctx": "Load" },
                    "attr": "id",
                    "ctx": "Load"
                  },
                  "ctx": "Store"
                }
              ],
              "value": { "type": "Name", "id": "usuario", "ctx": "Load" }
            },
            {
              "type": "Return",
              "value": { "type": "Name", "id": "usuario", "ctx": "Load" }
            }
          ],
          "decorator_list": [],
          "returns": { "type": "Name", "id": "Usuario", "ctx": "Load" }
        },
        {
          "type": "FunctionDef",
          "name": "delete_by_id",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              { "type": "arg", "arg": "self", "annotation": null },
              { "type": "arg", "arg": "id", "annotation": { "type": "Name", "id": "int", "ctx": "Load" } }
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
                  "type": "Attribute",
                  "value": {
                    "type": "Attribute",
                    "value": { "type": "Name", "id": "self", "ctx": "Load" },
                    "attr": "armazenamento",
                    "ctx": "Load"
                  },
                  "attr": "pop",
                  "ctx": "Load"
                },
                "args": [
                  { "type": "Name", "id": "id", "ctx": "Load" },
                  { "type": "Constant", "value": null, "kind": null }
                ],
                "keywords": []
              }
            }
          ],
          "decorator_list": [],
          "returns": null
        }
      ],
      "type_comment": null
    },
    {
      "type": "ClassDef",
      "name": "UsuarioService",
      "bases": [],
      "keywords": [],
      "decorator_list": [],
      "body": [
        {
          "type": "AnnAssign",
          "target": { "type": "Name", "id": "repo", "ctx": "Store" },
          "annotation": { "type": "Name", "id": "UsuarioRepository", "ctx": "Load" },
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
              { "type": "arg", "arg": "self", "annotation": null },
              {
                "type": "arg",
                "arg": "repo",
                "annotation": { "type": "Name", "id": "UsuarioRepository", "ctx": "Load" }
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
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "repo",
                  "ctx": "Store"
                }
              ],
              "value": { "type": "Name", "id": "repo", "ctx": "Load" }
            }
          ],
          "decorator_list": [],
          "returns": null
        },
        {
          "type": "FunctionDef",
          "name": "obterTodos",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              { "type": "arg", "arg": "self", "annotation": null }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Return",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Attribute",
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "repo",
                  "ctx": "Load"
                },
                "attr": "find_all",
                "ctx": "Load"
              },
              "args": [],
              "keywords": []
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Subscript",
            "value": { "type": "Name", "id": "List", "ctx": "Load" },
            "slice": { "type": "Name", "id": "Usuario", "ctx": "Load" },
            "ctx": "Load"
          }
        },
        {
          "type": "FunctionDef",
          "name": "obterPorId",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              { "type": "arg", "arg": "self", "annotation": null },
              { "type": "arg", "arg": "id", "annotation": { "type": "Name", "id": "int", "ctx": "Load" } }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Return",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Attribute",
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "repo",
                  "ctx": "Load"
                },
                "attr": "find_by_id",
                "ctx": "Load"
              },
              "args": [
                { "type": "Name", "id": "id", "ctx": "Load" }
              ],
              "keywords": []
            }
          ],
          "decorator_list": [],
          "returns": {
            "type": "Subscript",
            "value": { "type": "Name", "id": "Optional", "ctx": "Load" },
            "slice": { "type": "Name", "id": "Usuario", "ctx": "Load" },
            "ctx": "Load"
          }
        },
        {
          "type": "FunctionDef",
          "name": "criar",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              { "type": "arg", "arg": "self", "annotation": null },
              { "type": "arg", "arg": "usuario", "annotation": { "type": "Name", "id": "Usuario", "ctx": "Load" } }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Return",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Attribute",
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "repo",
                  "ctx": "Load"
                },
                "attr": "save",
                "ctx": "Load"
              },
              "args": [
                { "type": "Name", "id": "usuario", "ctx": "Load" }
              ],
              "keywords": []
            }
          ],
          "decorator_list": [],
          "returns": { "type": "Name", "id": "Usuario", "ctx": "Load" }
        },
        {
          "type": "FunctionDef",
          "name": "atualizar",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              { "type": "arg", "arg": "self", "annotation": null },
              { "type": "arg", "arg": "usuario", "annotation": { "type": "Name", "id": "Usuario", "ctx": "Load" } }
            ],
            "kwonlyargs": [],
            "kw_defaults": [],
            "defaults": []
          },
          "body": [
            {
              "type": "Return",
              "value": {
                "type": "Call",
                "func": {
                  "type": "Attribute",
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "repo",
                  "ctx": "Load"
                },
                "attr": "save",
                "ctx": "Load"
              },
              "args": [
                { "type": "Name", "id": "usuario", "ctx": "Load" }
              ],
              "keywords": []
            }
          ],
          "decorator_list": [],
          "returns": { "type": "Name", "id": "Usuario", "ctx": "Load" }
        },
        {
          "type": "FunctionDef",
          "name": "remover",
          "args": {
            "type": "arguments",
            "posonlyargs": [],
            "args": [
              { "type": "arg", "arg": "self", "annotation": null },
              { "type": "arg", "arg": "id", "annotation": { "type": "Name", "id": "int", "ctx": "Load" } }
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
                  "type": "Attribute",
                  "value": { "type": "Name", "id": "self", "ctx": "Load" },
                  "attr": "repo",
                  "ctx": "Load"
                },
                "attr": "delete_by_id",
                "ctx": "Load"
              },
              "args": [
                { "type": "Name", "id": "id", "ctx": "Load" }
              ],
              "keywords": []
            }
          ],
          "decorator_list": [],
          "returns": null
        }
      ],
      "type_comment": null
    },
    {
      "type": "Assign",
      "targets": [
        { "type": "Name", "id": "app", "ctx": "Store" }
      ],
      "value": {
        "type": "Call",
        "func": { "type": "Name", "id": "Flask", "ctx": "Load" },
        "args": [
          { "type": "Name", "id": "__name__", "ctx": "Load" }
        ],
        "keywords": []
      }
    },
    {
      "type": "Assign",
      "targets": [
        { "type": "Name", "id": "usuario_repo", "ctx": "Store" }
      ],
      "value": {
        "type": "Call",
        "func": { "type": "Name", "id": "UsuarioRepository", "ctx": "Load" },
        "args": [],
        "keywords": []
      }
    },
    {
      "type": "Assign",
      "targets": [
        { "type": "Name", "id": "usuario_service", "ctx": "Store" }
      ],
      "value": {
        "type": "Call",
        "func": { "type": "Name", "id": "UsuarioService", "ctx": "Load" },
        "args": [
          { "type": "Name", "id": "usuario_repo", "ctx": "Load" }
        ],
        "keywords": []
      }
    },
    {
      "type": "FunctionDef",
      "name": "listar_usuarios",
      "args": {
        "type": "arguments",
        "posonlyargs": [],
        "args": [],
        "kwonlyargs": [],
        "kw_defaults": [],
        "defaults": []
      },
      "body": [
        {
          "type": "Assign",
          "targets": [
            { "type": "Name", "id": "usuarios", "ctx": "Store" }
          ],
          "value": {
            "type": "Call",
            "func": {
              "type": "Attribute",
              "value": { "type": "Name", "id": "usuario_service", "ctx": "Load" },
              "attr": "obterTodos",
              "ctx": "Load"
            },
            "args": [],
            "keywords": []
          }
        },
        {
          "type": "Return",
          "value": {
            "type": "Call",
            "func": { "type": "Name", "id": "jsonify", "ctx": "Load" },
            "args": [
              {
                "type": "ListComp",
                "elt": {
                  "type": "Call",
                  "func": {
                    "type": "Attribute",
                    "value": { "type": "Name", "id": "u", "ctx": "Load" },
                    "attr": "to_dict",
                    "ctx": "Load"
                  },
                  "args": [],
                  "keywords": []
                },
                "generators": [
                  {
                    "type": "comprehension",
                    "target": { "type": "Name", "id": "u", "ctx": "Store" },
                    "iter": { "type": "Name", "id": "usuarios", "ctx": "Load" },
                    "ifs": [],
                    "is_async": 0
                  }
                ]
              }
            ],
            "keywords": []
          }
        }
      ],
      "decorator_list": [
        {
          "type": "Call",
          "func": {
            "type": "Attribute",
            "value": { "type": "Name", "id": "app", "ctx": "Load" },
            "attr": "route",
            "ctx": "Load"
          },
          "args": [
            { "type": "Constant", "value": "/api/usuarios", "kind": null }
          ],
          "keywords": [
            {
              "type": "keyword",
              "arg": "methods",
              "value": {
                "type": "List",
                "elts": [
                  { "type": "Constant", "value": "GET", "kind": null }
                ],
                "ctx": "Load"
              }
            }
          ]
        }
      ],
      "returns": null
    },
    {
      "type": "FunctionDef",
      "name": "obter_usuario",
      "args": {
        "type": "arguments",
        "posonlyargs": [],
        "args": [
          { "type": "arg", "arg": "id", "annotation": { "type": "Name", "id": "int", "ctx": "Load" } }
        ],
        "kwonlyargs": [],
        "kw_defaults": [],
        "defaults": []
      },
      "body": [
        {
          "type": "Assign",
          "targets": [
            { "type": "Name", "id": "usuario", "ctx": "Store" }
          ],
          "value": {
            "type": "Call",
            "func": {
              "type": "Attribute",
              "value": { "type": "Name", "id": "usuario_service", "ctx": "Load" },
              "attr": "obterPorId",
              "ctx": "Load"
            },
            "args": [
              { "type": "Name", "id": "id", "ctx": "Load" }
            ],
            "keywords": []
          }
        },
        {
          "type": "If",
          "test": { "type": "Name", "id": "usuario", "ctx": "Load" },
          "body": [
            {
              "type": "Return",
              "value": {
                "type": "Call",
                "func": { "type": "Name", "id": "jsonify", "ctx": "Load" },
                "args": [
                  {
                    "type": "Call",
                    "func": {
                      "type": "Attribute",
                      "value": { "type": "Name", "id": "usuario", "ctx": "Load" },
                      "attr": "to_dict",
                      "ctx": "Load"
                    },
                    "args": [],
                    "keywords": []
                  }
                ],
                "keywords": []
              }
            }
          ],
          "orelse": [
            {
              "type": "Return",
              "value": {
                "type": "Tuple",
                "elts": [
                  {
                    "type": "Call",
                    "func": { "type": "Name", "id": "jsonify", "ctx": "Load" },
                    "args": [
                      {
                        "type": "Dict",
                        "keys": [
                          { "type": "Constant", "value": "message", "kind": null }
                        ],
                        "values": [
                          { "type": "Constant", "value": "Usuario not found", "kind": null }
                        ]
                      }
                    ],
                    "keywords": []
                  },
                  { "type": "Constant", "value": 404, "kind": null }
                ],
                "ctx": "Load"
              }
            }
          ]
        }
      ],
      "decorator_list": [
        {
          "type": "Call",
          "func": {
            "type": "Attribute",
            "value": { "type": "Name", "id": "app", "ctx": "Load" },
            "attr": "route",
            "ctx": "Load"
          },
          "args": [
            { "type": "Constant", "value": "/api/usuarios/<int:id>", "kind": null }
          ],
          "keywords": [
            {
              "type": "keyword",
              "arg": "methods",
              "value": {
                "type": "List",
                "elts": [
                  { "type": "Constant", "value": "GET", "kind": null }
                ],
                "ctx": "Load"
              }
            }
          ]
        }
      ],
      "returns": null
    },
    {
      "type": "FunctionDef",
      "name": "criar_usuario",
      "args": {
        "type": "arguments",
        "posonlyargs": [],
        "args": [],
        "kwonlyargs": [],
        "kw_defaults": [],
        "defaults": []
      },
      "body": [
        {
          "type": "Assign",
          "targets": [
            { "type": "Name", "id": "data", "ctx": "Store" }
          ],
          "value": {
            "type": "Attribute",
            "value": { "type": "Name", "id": "request", "ctx": "Load" },
            "attr": "json",
            "ctx": "Load"
          }
        },
        {
          "type": "Assign",
          "targets": [
            { "type": "Name", "id": "new_usuario", "ctx": "Store" }
          ],
          "value": {
            "type": "Call",
            "func": { "type": "Name", "id": "Usuario", "ctx": "Load" },
            "args": [
              { "type": "Constant", "value": null, "kind": null },
              {
                "type": "Subscript",
                "value": { "type": "Name", "id": "data", "ctx": "Load" },
                "slice": { "type": "Constant", "value": "nome", "kind": null },
                "ctx": "Load"
              },
              {
                "type": "Subscript",
                "value": { "type": "Name", "id": "data", "ctx": "Load" },
                "slice": { "type": "Constant", "value": "email", "kind": null },
                "ctx": "Load"
              }
            ],
            "keywords": []
          }
        },
        {
          "type": "Assign",
          "targets": [
            { "type": "Name", "id": "created_usuario", "ctx": "Store" }
          ],
          "value": {
            "type": "Call",
            "func": {
              "type": "Attribute",
              "value": { "type": "Name", "id": "usuario_service", "ctx": "Load" },
              "attr": "criar",
              "ctx": "Load"
            },
            "args": [
              { "type": "Name", "id": "new_usuario", "ctx": "Load" }
            ],
            "keywords": []
          }
        },
        {
          "type": "Return",
          "value": {
            "type": "Tuple",
            "elts": [
              {
                "type": "Call",
                "func": { "type": "Name", "id": "jsonify", "ctx": "Load" },
                "args": [
                  {
                    "type": "Call",
                    "func": {
                      "type": "Attribute",
                      "value": { "type": "Name", "id": "created_usuario", "ctx": "Load" },
                      "attr": "to_dict",
                      "ctx": "Load"
                    },
                    "args": [],
                    "keywords": []
                  }
                ],
                "keywords": []
              },
              { "type": "Constant", "value": 201, "kind": null }
            ],
            "ctx": "Load"
          }
        }
      ],
      "decorator_list": [
        {
          "type": "Call",
          "func": {
            "type": "Attribute",
            "value": { "type": "Name", "id": "app", "ctx": "Load" },
            "attr": "route",
            "ctx": "Load"
          },
          "args": [
            { "type": "Constant", "value": "/api/usuarios", "kind": null }
          ],
          "keywords": [
            {
              "type": "keyword",
              "arg": "methods",
              "value": {
                "type": "List",
                "elts": [
                  { "type": "Constant", "value": "POST", "kind": null }
                ],
                "ctx": "Load"
              }
            }
          ]
        }
      ],
      "returns": null
    },
    {
      "type": "FunctionDef",
      "name": "atualizar_usuario",
      "args": {
        "type": "arguments",
        "posonlyargs": [],
        "args": [
          { "type": "arg", "arg": "id", "annotation": { "type": "Name", "id": "int", "ctx": "Load" } }
        ],
        "kwonlyargs": [],
        "kw_defaults": [],
        "defaults": []
      },
      "body": [
        {
          "type": "Assign",
          "targets": [
            { "type": "Name", "id": "data", "ctx": "Store" }
          ],
          "value": {
            "type": "Attribute",
            "value": { "type": "Name", "id": "request", "ctx": "Load" },
            "attr": "json",
            "ctx": "Load"
          }
        },
        {
          "type": "Assign",
          "targets": [
            { "type": "Name", "id": "usuario_to_update", "ctx": "Store" }
          ],
          "value": {
            "type": "Call",
            "func": { "type": "Name", "id": "Usuario", "ctx": "Load" },
            "args": [
              { "type": "Name", "id": "id", "ctx": "Load" },
              {
                "type": "Subscript",
                "value": { "type": "Name", "id": "data", "ctx": "Load" },
                "slice": { "type": "Constant", "value": "nome", "kind": null },
                "ctx": "Load"
              },
              {
                "type": "Subscript",
                "value": { "type": "Name", "id": "data", "ctx": "Load" },
                "slice": { "type": "Constant", "value": "email", "kind": null },
                "ctx": "Load"
              }
            ],
            "keywords": []
          }
        },
        {
          "type": "Assign",
          "targets": [
            { "type": "Name", "id": "updated_usuario", "ctx": "Store" }
          ],
          "value": {
            "type": "Call",
            "func": {
              "type": "Attribute",
              "value": { "type": "Name", "id": "usuario_service", "ctx": "Load" },
              "attr": "atualizar",
              "ctx": "Load"
            },
            "args": [
              { "type": "Name", "id": "usuario_to_update", "ctx": "Load" }
            ],
            "keywords": []
          }
        },
        {
          "type": "If",
          "test": { "type": "Name", "id": "updated_usuario", "ctx": "Load" },
          "body": [
            {
              "type": "Return",
              "value": {
                "type": "Call",
                "func": { "type": "Name", "id": "jsonify", "ctx": "Load" },
                "args": [
                  {
                    "type": "Call",
                    "func": {
                      "type": "Attribute",
                      "value": { "type": "Name", "id": "updated_usuario", "ctx": "Load" },
                      "attr": "to_dict",
                      "ctx": "Load"
                    },
                    "args": [],
                    "keywords": []
                  }
                ],
                "keywords": []
              }
            }
          ],
          "orelse": [
            {
              "type": "Return",
              "value": {
                "type": "Tuple",
                "elts": [
                  {
                    "type": "Call",
                    "func": { "type": "Name", "id": "jsonify", "ctx": "Load" },
                    "args": [
                      {
                        "type": "Dict",
                        "keys": [
                          { "type": "Constant", "value": "message", "kind": null }
                        ],
                        "values": [
                          { "type": "Constant", "value": "Usuario not found for update", "kind": null }
                        ]
                      }
                    ],
                    "keywords": []
                  },
                  { "type": "Constant", "value": 404, "kind": null }
                ],
                "ctx": "Load"
              }
            }
          ]
        }
      ],
      "decorator_list": [
        {
          "type": "Call",
          "func": {
            "type": "Attribute",
            "value": { "type": "Name", "id": "app", "ctx": "Load" },
            "attr": "route",
            "ctx": "Load"
          },
          "args": [
            { "type": "Constant", "value": "/api/usuarios/<int:id>", "kind": null }
          ],
          "keywords": [
            {
              "type": "keyword",
              "arg": "methods",
              "value": {
                "type": "List",
                "elts": [
                  { "type": "Constant", "value": "PUT", "kind": null }
                ],
                "ctx": "Load"
              }
            }
          ]
        }
      ],
      "returns": null
    },
    {
      "type": "FunctionDef",
      "name": "remover_usuario",
      "args": {
        "type": "arguments",
        "posonlyargs": [],
        "args": [
          { "type": "arg", "arg": "id", "annotation": { "type": "Name", "id": "int", "ctx": "Load" } }
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
              "type": "Attribute",
              "value": { "type": "Name", "id": "usuario_service", "ctx": "Load" },
              "attr": "remover",
              "ctx": "Load"
            },
            "args": [
              { "type": "Name", "id": "id", "ctx": "Load" }
            ],
            "keywords": []
          }
        },
        {
          "type": "Return",
          "value": {
            "type": "Tuple",
            "elts": [
              { "type": "Constant", "value": "", "kind": null },
              { "type": "Constant", "value": 204, "kind": null }
            ],
            "ctx": "Load"
          }
        }
      ],
      "decorator_list": [
        {
          "type": "Call",
          "func": {
            "type": "Attribute",
            "value": { "type": "Name", "id": "app", "ctx": "Load" },
            "attr": "route",
            "ctx": "Load"
          },
          "args": [
            { "type": "Constant", "value": "/api/usuarios/<int:id>", "kind": null }
          ],
          "keywords": [
            {
              "type": "keyword",
              "arg": "methods",
              "value": {
                "type": "List",
                "elts": [
                  { "type": "Constant", "value": "DELETE", "kind": null }
                ],
                "ctx": "Load"
              }
            }
          ]
        }
      ],
      "returns": null
    },
    {
      "type": "If",
      "test": {
        "type": "Compare",
        "left": { "type": "Name", "id": "__name__", "ctx": "Load" },
        "ops": [ { "type": "Eq" } ],
        "comparators": [ { "type": "Constant", "value": "__main__", "kind": null } ]
      },
      "body": [
        {
          "type": "Expr",
          "value": {
            "type": "Call",
            "func": {
              "type": "Attribute",
              "value": { "type": "Name", "id": "app", "ctx": "Load" },
              "attr": "run",
              "ctx": "Load"
            },
            "args": [],
            "keywords": [
              {
                "type": "keyword",
                "arg": "debug",
                "value": { "type": "Constant", "value": true, "kind": null }
              }
            ]
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

### Testing `Usuario.to_dict`

**AI-Generated Test Script:**

```python
import unittest
from temp_subject_for_test import Usuario

class TestUsuarioToDict(unittest.TestCase):

    def test_to_dict_with_all_fields(self):
        # Test case with all fields populated
        usuario = Usuario(id=1, nome='Alice', email='alice@example.com')
        expected_dict = {'id': 1, 'nome': 'Alice', 'email': 'alice@example.com'}
        self.assertEqual(usuario.to_dict(), expected_dict)

    def test_to_dict_with_none_id(self):
        # Test case with id as None (e.g., before saving to repository)
        usuario = Usuario(id=None, nome='Bob', email='bob@example.com')
        expected_dict = {'id': None, 'nome': 'Bob', 'email': 'bob@example.com'}
        self.assertEqual(usuario.to_dict(), expected_dict)

    def test_to_dict_with_empty_strings(self):
        # Test case with empty strings for nome and email
        usuario = Usuario(id=3, nome='', email='')
        expected_dict = {'id': 3, 'nome': '', 'email': ''}
        self.assertEqual(usuario.to_dict(), expected_dict)

    def test_to_dict_with_special_characters(self):
        # Test case with special characters in nome and email
        usuario = Usuario(id=4, nome='João Silva', email='joao.silva+test@example.com')
        expected_dict = {'id': 4, 'nome': 'João Silva', 'email': 'joao.silva+test@example.com'}
        self.assertEqual(usuario.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()
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
from flask import Flask, jsonify, request
from typing import List, Optional
app = Flask(__name__)

class Usuario:
    id: Optional[int]
    nome: str
    email: str

    def __init__(self, id: Optional[int], nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'email': self.email}

class UsuarioRepository:
    armazenamento: dict[int, Usuario]
    sequence: int

    def __init__(self):
        self.armazenamento = {}
        self.sequence = 0
        self.init_data()

    def init_data(self):
        self.save(Usuario(None, 'Alice', 'alice@example.com'))
        self.save(Usuario(None, 'Bruno', 'bruno@example.com'))

    def find_by_id(self, id: int) -> Optional[Usuario]:
        return self.armazenamento.get(id)

    def find_all(self) -> List[Usuario]:
        return list(self.armazenamento.values())

    def save(self, usuario: Usuario) -> Usuario:
        if usuario.id is None:
            self.sequence += 1
            usuario.id = self.sequence
        self.armazenamento[usuario.id] = usuario
        return usuario

    def delete_by_id(self, id: int):
        self.armazenamento.pop(id, None)

class UsuarioService:
    repo: UsuarioRepository

    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    def obterTodos(self) -> List[Usuario]:
        return self.repo()

    def obterPorId(self, id: int) -> Optional[Usuario]:
        return self.repo()

    def criar(self, usuario: Usuario) -> Usuario:
        return self.repo()

    def atualizar(self, usuario: Usuario) -> Usuario:
        return self.repo()

    def remover(self, id: int):
        self.repo()
usuario_repo = UsuarioRepository()
usuario_service = UsuarioService(usuario_repo)

@app.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = usuario_service.obterTodos()
    return jsonify([u.to_dict() for u in usuarios])

@app.route('/api/usuarios/<int:id>', methods=['GET'])
def obter_usuario(id: int):
    usuario = usuario_service.obterPorId(id)
    if usuario:
        return jsonify(usuario.to_dict())
    else:
        return (jsonify({'message': 'Usuario not found'}), 404)

@app.route('/api/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    new_usuario = Usuario(None, data['nome'], data['email'])
    created_usuario = usuario_service.criar(new_usuario)
    return (jsonify(created_usuario.to_dict()), 201)

@app.route('/api/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id: int):
    data = request.json
    usuario_to_update = Usuario(id, data['nome'], data['email'])
    updated_usuario = usuario_service.atualizar(usuario_to_update)
    if updated_usuario:
        return jsonify(updated_usuario.to_dict())
    else:
        return (jsonify({'message': 'Usuario not found for update'}), 404)

@app.route('/api/usuarios/<int:id>', methods=['DELETE'])
def remover_usuario(id: int):
    usuario_service.remover(id)
    return ('', 204)
if __name__ == '__main__':
    app.run(debug=True)
```
