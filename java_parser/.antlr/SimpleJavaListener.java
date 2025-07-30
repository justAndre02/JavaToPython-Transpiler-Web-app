// Generated from c:/Users/andre/OneDrive/Ambiente de Trabalho/app_tese/java_parser/SimpleJava.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SimpleJavaParser}.
 */
public interface SimpleJavaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void enterCompilationUnit(SimpleJavaParser.CompilationUnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void exitCompilationUnit(SimpleJavaParser.CompilationUnitContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#importDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterImportDeclaration(SimpleJavaParser.ImportDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#importDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitImportDeclaration(SimpleJavaParser.ImportDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#qualifiedName}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedName(SimpleJavaParser.QualifiedNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#qualifiedName}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedName(SimpleJavaParser.QualifiedNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#typeDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterTypeDeclaration(SimpleJavaParser.TypeDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#typeDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitTypeDeclaration(SimpleJavaParser.TypeDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#classDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterClassDeclaration(SimpleJavaParser.ClassDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#classDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitClassDeclaration(SimpleJavaParser.ClassDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#enumDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterEnumDeclaration(SimpleJavaParser.EnumDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#enumDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitEnumDeclaration(SimpleJavaParser.EnumDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#enumConstantList}.
	 * @param ctx the parse tree
	 */
	void enterEnumConstantList(SimpleJavaParser.EnumConstantListContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#enumConstantList}.
	 * @param ctx the parse tree
	 */
	void exitEnumConstantList(SimpleJavaParser.EnumConstantListContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#enumConstant}.
	 * @param ctx the parse tree
	 */
	void enterEnumConstant(SimpleJavaParser.EnumConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#enumConstant}.
	 * @param ctx the parse tree
	 */
	void exitEnumConstant(SimpleJavaParser.EnumConstantContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#enumBodyDeclarations}.
	 * @param ctx the parse tree
	 */
	void enterEnumBodyDeclarations(SimpleJavaParser.EnumBodyDeclarationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#enumBodyDeclarations}.
	 * @param ctx the parse tree
	 */
	void exitEnumBodyDeclarations(SimpleJavaParser.EnumBodyDeclarationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#typeParameters}.
	 * @param ctx the parse tree
	 */
	void enterTypeParameters(SimpleJavaParser.TypeParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#typeParameters}.
	 * @param ctx the parse tree
	 */
	void exitTypeParameters(SimpleJavaParser.TypeParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#typeParameter}.
	 * @param ctx the parse tree
	 */
	void enterTypeParameter(SimpleJavaParser.TypeParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#typeParameter}.
	 * @param ctx the parse tree
	 */
	void exitTypeParameter(SimpleJavaParser.TypeParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#typeBound}.
	 * @param ctx the parse tree
	 */
	void enterTypeBound(SimpleJavaParser.TypeBoundContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#typeBound}.
	 * @param ctx the parse tree
	 */
	void exitTypeBound(SimpleJavaParser.TypeBoundContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#memberDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterMemberDeclaration(SimpleJavaParser.MemberDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#memberDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitMemberDeclaration(SimpleJavaParser.MemberDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#fieldDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterFieldDeclaration(SimpleJavaParser.FieldDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#fieldDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitFieldDeclaration(SimpleJavaParser.FieldDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#variableDeclarator}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclarator(SimpleJavaParser.VariableDeclaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#variableDeclarator}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclarator(SimpleJavaParser.VariableDeclaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#variableInitializer}.
	 * @param ctx the parse tree
	 */
	void enterVariableInitializer(SimpleJavaParser.VariableInitializerContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#variableInitializer}.
	 * @param ctx the parse tree
	 */
	void exitVariableInitializer(SimpleJavaParser.VariableInitializerContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#constructorDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterConstructorDeclaration(SimpleJavaParser.ConstructorDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#constructorDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitConstructorDeclaration(SimpleJavaParser.ConstructorDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#methodDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterMethodDeclaration(SimpleJavaParser.MethodDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#methodDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitMethodDeclaration(SimpleJavaParser.MethodDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#modifier}.
	 * @param ctx the parse tree
	 */
	void enterModifier(SimpleJavaParser.ModifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#modifier}.
	 * @param ctx the parse tree
	 */
	void exitModifier(SimpleJavaParser.ModifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#returnType}.
	 * @param ctx the parse tree
	 */
	void enterReturnType(SimpleJavaParser.ReturnTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#returnType}.
	 * @param ctx the parse tree
	 */
	void exitReturnType(SimpleJavaParser.ReturnTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(SimpleJavaParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(SimpleJavaParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#classOrInterfaceType}.
	 * @param ctx the parse tree
	 */
	void enterClassOrInterfaceType(SimpleJavaParser.ClassOrInterfaceTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#classOrInterfaceType}.
	 * @param ctx the parse tree
	 */
	void exitClassOrInterfaceType(SimpleJavaParser.ClassOrInterfaceTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#primitiveType}.
	 * @param ctx the parse tree
	 */
	void enterPrimitiveType(SimpleJavaParser.PrimitiveTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#primitiveType}.
	 * @param ctx the parse tree
	 */
	void exitPrimitiveType(SimpleJavaParser.PrimitiveTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#typeArguments}.
	 * @param ctx the parse tree
	 */
	void enterTypeArguments(SimpleJavaParser.TypeArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#typeArguments}.
	 * @param ctx the parse tree
	 */
	void exitTypeArguments(SimpleJavaParser.TypeArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#typeArgument}.
	 * @param ctx the parse tree
	 */
	void enterTypeArgument(SimpleJavaParser.TypeArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#typeArgument}.
	 * @param ctx the parse tree
	 */
	void exitTypeArgument(SimpleJavaParser.TypeArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#typeList}.
	 * @param ctx the parse tree
	 */
	void enterTypeList(SimpleJavaParser.TypeListContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#typeList}.
	 * @param ctx the parse tree
	 */
	void exitTypeList(SimpleJavaParser.TypeListContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#formalParameters}.
	 * @param ctx the parse tree
	 */
	void enterFormalParameters(SimpleJavaParser.FormalParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#formalParameters}.
	 * @param ctx the parse tree
	 */
	void exitFormalParameters(SimpleJavaParser.FormalParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#formalParameter}.
	 * @param ctx the parse tree
	 */
	void enterFormalParameter(SimpleJavaParser.FormalParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#formalParameter}.
	 * @param ctx the parse tree
	 */
	void exitFormalParameter(SimpleJavaParser.FormalParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#variableDeclaratorId}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclaratorId(SimpleJavaParser.VariableDeclaratorIdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#variableDeclaratorId}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclaratorId(SimpleJavaParser.VariableDeclaratorIdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#qualifiedNameList}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedNameList(SimpleJavaParser.QualifiedNameListContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#qualifiedNameList}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedNameList(SimpleJavaParser.QualifiedNameListContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(SimpleJavaParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(SimpleJavaParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#blockStatement}.
	 * @param ctx the parse tree
	 */
	void enterBlockStatement(SimpleJavaParser.BlockStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#blockStatement}.
	 * @param ctx the parse tree
	 */
	void exitBlockStatement(SimpleJavaParser.BlockStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(SimpleJavaParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(SimpleJavaParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#switchStatement}.
	 * @param ctx the parse tree
	 */
	void enterSwitchStatement(SimpleJavaParser.SwitchStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#switchStatement}.
	 * @param ctx the parse tree
	 */
	void exitSwitchStatement(SimpleJavaParser.SwitchStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#switchBlockStatementGroup}.
	 * @param ctx the parse tree
	 */
	void enterSwitchBlockStatementGroup(SimpleJavaParser.SwitchBlockStatementGroupContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#switchBlockStatementGroup}.
	 * @param ctx the parse tree
	 */
	void exitSwitchBlockStatementGroup(SimpleJavaParser.SwitchBlockStatementGroupContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#switchLabel}.
	 * @param ctx the parse tree
	 */
	void enterSwitchLabel(SimpleJavaParser.SwitchLabelContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#switchLabel}.
	 * @param ctx the parse tree
	 */
	void exitSwitchLabel(SimpleJavaParser.SwitchLabelContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#constantExpression}.
	 * @param ctx the parse tree
	 */
	void enterConstantExpression(SimpleJavaParser.ConstantExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#constantExpression}.
	 * @param ctx the parse tree
	 */
	void exitConstantExpression(SimpleJavaParser.ConstantExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#enumConstantName}.
	 * @param ctx the parse tree
	 */
	void enterEnumConstantName(SimpleJavaParser.EnumConstantNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#enumConstantName}.
	 * @param ctx the parse tree
	 */
	void exitEnumConstantName(SimpleJavaParser.EnumConstantNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void enterBreakStatement(SimpleJavaParser.BreakStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void exitBreakStatement(SimpleJavaParser.BreakStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void enterContinueStatement(SimpleJavaParser.ContinueStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void exitContinueStatement(SimpleJavaParser.ContinueStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#doWhileStatement}.
	 * @param ctx the parse tree
	 */
	void enterDoWhileStatement(SimpleJavaParser.DoWhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#doWhileStatement}.
	 * @param ctx the parse tree
	 */
	void exitDoWhileStatement(SimpleJavaParser.DoWhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#throwStatement}.
	 * @param ctx the parse tree
	 */
	void enterThrowStatement(SimpleJavaParser.ThrowStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#throwStatement}.
	 * @param ctx the parse tree
	 */
	void exitThrowStatement(SimpleJavaParser.ThrowStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#synchronizedStatement}.
	 * @param ctx the parse tree
	 */
	void enterSynchronizedStatement(SimpleJavaParser.SynchronizedStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#synchronizedStatement}.
	 * @param ctx the parse tree
	 */
	void exitSynchronizedStatement(SimpleJavaParser.SynchronizedStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#localVariableDeclarationStatement}.
	 * @param ctx the parse tree
	 */
	void enterLocalVariableDeclarationStatement(SimpleJavaParser.LocalVariableDeclarationStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#localVariableDeclarationStatement}.
	 * @param ctx the parse tree
	 */
	void exitLocalVariableDeclarationStatement(SimpleJavaParser.LocalVariableDeclarationStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(SimpleJavaParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(SimpleJavaParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(SimpleJavaParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(SimpleJavaParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void enterForStatement(SimpleJavaParser.ForStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void exitForStatement(SimpleJavaParser.ForStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#forControl}.
	 * @param ctx the parse tree
	 */
	void enterForControl(SimpleJavaParser.ForControlContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#forControl}.
	 * @param ctx the parse tree
	 */
	void exitForControl(SimpleJavaParser.ForControlContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#enhancedForControl}.
	 * @param ctx the parse tree
	 */
	void enterEnhancedForControl(SimpleJavaParser.EnhancedForControlContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#enhancedForControl}.
	 * @param ctx the parse tree
	 */
	void exitEnhancedForControl(SimpleJavaParser.EnhancedForControlContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#basicForControl}.
	 * @param ctx the parse tree
	 */
	void enterBasicForControl(SimpleJavaParser.BasicForControlContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#basicForControl}.
	 * @param ctx the parse tree
	 */
	void exitBasicForControl(SimpleJavaParser.BasicForControlContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#forInit}.
	 * @param ctx the parse tree
	 */
	void enterForInit(SimpleJavaParser.ForInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#forInit}.
	 * @param ctx the parse tree
	 */
	void exitForInit(SimpleJavaParser.ForInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#forUpdate}.
	 * @param ctx the parse tree
	 */
	void enterForUpdate(SimpleJavaParser.ForUpdateContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#forUpdate}.
	 * @param ctx the parse tree
	 */
	void exitForUpdate(SimpleJavaParser.ForUpdateContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#tryStatement}.
	 * @param ctx the parse tree
	 */
	void enterTryStatement(SimpleJavaParser.TryStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#tryStatement}.
	 * @param ctx the parse tree
	 */
	void exitTryStatement(SimpleJavaParser.TryStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#catchClause}.
	 * @param ctx the parse tree
	 */
	void enterCatchClause(SimpleJavaParser.CatchClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#catchClause}.
	 * @param ctx the parse tree
	 */
	void exitCatchClause(SimpleJavaParser.CatchClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(SimpleJavaParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(SimpleJavaParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void enterExpressionStatement(SimpleJavaParser.ExpressionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void exitExpressionStatement(SimpleJavaParser.ExpressionStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitwiseOrExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseOrExpr(SimpleJavaParser.BitwiseOrExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitwiseOrExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseOrExpr(SimpleJavaParser.BitwiseOrExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RelationalExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterRelationalExpr(SimpleJavaParser.RelationalExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RelationalExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitRelationalExpr(SimpleJavaParser.RelationalExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DotMethodCallExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterDotMethodCallExpr(SimpleJavaParser.DotMethodCallExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DotMethodCallExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitDotMethodCallExpr(SimpleJavaParser.DotMethodCallExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LogicalAndExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalAndExpr(SimpleJavaParser.LogicalAndExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LogicalAndExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalAndExpr(SimpleJavaParser.LogicalAndExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PostIncrementExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterPostIncrementExpr(SimpleJavaParser.PostIncrementExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PostIncrementExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitPostIncrementExpr(SimpleJavaParser.PostIncrementExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PreIncrementExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterPreIncrementExpr(SimpleJavaParser.PreIncrementExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PreIncrementExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitPreIncrementExpr(SimpleJavaParser.PreIncrementExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MultiplicativeExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeExpr(SimpleJavaParser.MultiplicativeExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MultiplicativeExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeExpr(SimpleJavaParser.MultiplicativeExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DotSuperExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterDotSuperExpr(SimpleJavaParser.DotSuperExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DotSuperExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitDotSuperExpr(SimpleJavaParser.DotSuperExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EqualityExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterEqualityExpr(SimpleJavaParser.EqualityExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EqualityExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitEqualityExpr(SimpleJavaParser.EqualityExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CastExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterCastExpr(SimpleJavaParser.CastExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CastExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitCastExpr(SimpleJavaParser.CastExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PrimaryExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpr(SimpleJavaParser.PrimaryExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PrimaryExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpr(SimpleJavaParser.PrimaryExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FieldAccessExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterFieldAccessExpr(SimpleJavaParser.FieldAccessExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FieldAccessExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitFieldAccessExpr(SimpleJavaParser.FieldAccessExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DotThisExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterDotThisExpr(SimpleJavaParser.DotThisExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DotThisExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitDotThisExpr(SimpleJavaParser.DotThisExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TernaryExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterTernaryExpr(SimpleJavaParser.TernaryExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TernaryExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitTernaryExpr(SimpleJavaParser.TernaryExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitwiseAndExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseAndExpr(SimpleJavaParser.BitwiseAndExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitwiseAndExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseAndExpr(SimpleJavaParser.BitwiseAndExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ArrayAccessExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterArrayAccessExpr(SimpleJavaParser.ArrayAccessExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ArrayAccessExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitArrayAccessExpr(SimpleJavaParser.ArrayAccessExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code InstanceofExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterInstanceofExpr(SimpleJavaParser.InstanceofExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code InstanceofExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitInstanceofExpr(SimpleJavaParser.InstanceofExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LambdaExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLambdaExpr(SimpleJavaParser.LambdaExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LambdaExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLambdaExpr(SimpleJavaParser.LambdaExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AssignmentExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpr(SimpleJavaParser.AssignmentExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AssignmentExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpr(SimpleJavaParser.AssignmentExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PrefixExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterPrefixExpr(SimpleJavaParser.PrefixExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PrefixExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitPrefixExpr(SimpleJavaParser.PrefixExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LogicalOrExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOrExpr(SimpleJavaParser.LogicalOrExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LogicalOrExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOrExpr(SimpleJavaParser.LogicalOrExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AdditiveExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveExpr(SimpleJavaParser.AdditiveExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AdditiveExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveExpr(SimpleJavaParser.AdditiveExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code InnerClassCreationExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterInnerClassCreationExpr(SimpleJavaParser.InnerClassCreationExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code InnerClassCreationExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitInnerClassCreationExpr(SimpleJavaParser.InnerClassCreationExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitwiseXorExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseXorExpr(SimpleJavaParser.BitwiseXorExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitwiseXorExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseXorExpr(SimpleJavaParser.BitwiseXorExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NewCreatorExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNewCreatorExpr(SimpleJavaParser.NewCreatorExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NewCreatorExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNewCreatorExpr(SimpleJavaParser.NewCreatorExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MethodCallExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMethodCallExpr(SimpleJavaParser.MethodCallExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MethodCallExpr}
	 * labeled alternative in {@link SimpleJavaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMethodCallExpr(SimpleJavaParser.MethodCallExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#creator}.
	 * @param ctx the parse tree
	 */
	void enterCreator(SimpleJavaParser.CreatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#creator}.
	 * @param ctx the parse tree
	 */
	void exitCreator(SimpleJavaParser.CreatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#createdName}.
	 * @param ctx the parse tree
	 */
	void enterCreatedName(SimpleJavaParser.CreatedNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#createdName}.
	 * @param ctx the parse tree
	 */
	void exitCreatedName(SimpleJavaParser.CreatedNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#nonWildcardTypeArgumentsOrDiamond}.
	 * @param ctx the parse tree
	 */
	void enterNonWildcardTypeArgumentsOrDiamond(SimpleJavaParser.NonWildcardTypeArgumentsOrDiamondContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#nonWildcardTypeArgumentsOrDiamond}.
	 * @param ctx the parse tree
	 */
	void exitNonWildcardTypeArgumentsOrDiamond(SimpleJavaParser.NonWildcardTypeArgumentsOrDiamondContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#arrayCreatorRest}.
	 * @param ctx the parse tree
	 */
	void enterArrayCreatorRest(SimpleJavaParser.ArrayCreatorRestContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#arrayCreatorRest}.
	 * @param ctx the parse tree
	 */
	void exitArrayCreatorRest(SimpleJavaParser.ArrayCreatorRestContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#classCreatorRest}.
	 * @param ctx the parse tree
	 */
	void enterClassCreatorRest(SimpleJavaParser.ClassCreatorRestContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#classCreatorRest}.
	 * @param ctx the parse tree
	 */
	void exitClassCreatorRest(SimpleJavaParser.ClassCreatorRestContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(SimpleJavaParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(SimpleJavaParser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#classBody}.
	 * @param ctx the parse tree
	 */
	void enterClassBody(SimpleJavaParser.ClassBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#classBody}.
	 * @param ctx the parse tree
	 */
	void exitClassBody(SimpleJavaParser.ClassBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#expressionList}.
	 * @param ctx the parse tree
	 */
	void enterExpressionList(SimpleJavaParser.ExpressionListContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#expressionList}.
	 * @param ctx the parse tree
	 */
	void exitExpressionList(SimpleJavaParser.ExpressionListContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#lambdaExpression}.
	 * @param ctx the parse tree
	 */
	void enterLambdaExpression(SimpleJavaParser.LambdaExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#lambdaExpression}.
	 * @param ctx the parse tree
	 */
	void exitLambdaExpression(SimpleJavaParser.LambdaExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#superSuffix}.
	 * @param ctx the parse tree
	 */
	void enterSuperSuffix(SimpleJavaParser.SuperSuffixContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#superSuffix}.
	 * @param ctx the parse tree
	 */
	void exitSuperSuffix(SimpleJavaParser.SuperSuffixContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(SimpleJavaParser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(SimpleJavaParser.PrimaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(SimpleJavaParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(SimpleJavaParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleJavaParser#arrayInitializer}.
	 * @param ctx the parse tree
	 */
	void enterArrayInitializer(SimpleJavaParser.ArrayInitializerContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleJavaParser#arrayInitializer}.
	 * @param ctx the parse tree
	 */
	void exitArrayInitializer(SimpleJavaParser.ArrayInitializerContext ctx);
}