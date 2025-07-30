# Generated from SimpleJava.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleJavaParser import SimpleJavaParser
else:
    from SimpleJavaParser import SimpleJavaParser

# This class defines a complete listener for a parse tree produced by SimpleJavaParser.
class SimpleJavaListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleJavaParser#compilationUnit.
    def enterCompilationUnit(self, ctx:SimpleJavaParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#compilationUnit.
    def exitCompilationUnit(self, ctx:SimpleJavaParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:SimpleJavaParser.PackageDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#packageDeclaration.
    def exitPackageDeclaration(self, ctx:SimpleJavaParser.PackageDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#importDeclaration.
    def enterImportDeclaration(self, ctx:SimpleJavaParser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#importDeclaration.
    def exitImportDeclaration(self, ctx:SimpleJavaParser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#qualifiedName.
    def enterQualifiedName(self, ctx:SimpleJavaParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#qualifiedName.
    def exitQualifiedName(self, ctx:SimpleJavaParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:SimpleJavaParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:SimpleJavaParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:SimpleJavaParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#classDeclaration.
    def exitClassDeclaration(self, ctx:SimpleJavaParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:SimpleJavaParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:SimpleJavaParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#implementsClause.
    def enterImplementsClause(self, ctx:SimpleJavaParser.ImplementsClauseContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#implementsClause.
    def exitImplementsClause(self, ctx:SimpleJavaParser.ImplementsClauseContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#interfaceMemberDeclaration.
    def enterInterfaceMemberDeclaration(self, ctx:SimpleJavaParser.InterfaceMemberDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#interfaceMemberDeclaration.
    def exitInterfaceMemberDeclaration(self, ctx:SimpleJavaParser.InterfaceMemberDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#interfaceMethodDeclaration.
    def enterInterfaceMethodDeclaration(self, ctx:SimpleJavaParser.InterfaceMethodDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#interfaceMethodDeclaration.
    def exitInterfaceMethodDeclaration(self, ctx:SimpleJavaParser.InterfaceMethodDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:SimpleJavaParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:SimpleJavaParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#enumConstantList.
    def enterEnumConstantList(self, ctx:SimpleJavaParser.EnumConstantListContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#enumConstantList.
    def exitEnumConstantList(self, ctx:SimpleJavaParser.EnumConstantListContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#enumConstant.
    def enterEnumConstant(self, ctx:SimpleJavaParser.EnumConstantContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#enumConstant.
    def exitEnumConstant(self, ctx:SimpleJavaParser.EnumConstantContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#enumBodyDeclarations.
    def enterEnumBodyDeclarations(self, ctx:SimpleJavaParser.EnumBodyDeclarationsContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#enumBodyDeclarations.
    def exitEnumBodyDeclarations(self, ctx:SimpleJavaParser.EnumBodyDeclarationsContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#typeParameters.
    def enterTypeParameters(self, ctx:SimpleJavaParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#typeParameters.
    def exitTypeParameters(self, ctx:SimpleJavaParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#typeParameter.
    def enterTypeParameter(self, ctx:SimpleJavaParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#typeParameter.
    def exitTypeParameter(self, ctx:SimpleJavaParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#typeBound.
    def enterTypeBound(self, ctx:SimpleJavaParser.TypeBoundContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#typeBound.
    def exitTypeBound(self, ctx:SimpleJavaParser.TypeBoundContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:SimpleJavaParser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:SimpleJavaParser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:SimpleJavaParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:SimpleJavaParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:SimpleJavaParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:SimpleJavaParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#variableInitializer.
    def enterVariableInitializer(self, ctx:SimpleJavaParser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#variableInitializer.
    def exitVariableInitializer(self, ctx:SimpleJavaParser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:SimpleJavaParser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:SimpleJavaParser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:SimpleJavaParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:SimpleJavaParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#modifier.
    def enterModifier(self, ctx:SimpleJavaParser.ModifierContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#modifier.
    def exitModifier(self, ctx:SimpleJavaParser.ModifierContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#returnType.
    def enterReturnType(self, ctx:SimpleJavaParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#returnType.
    def exitReturnType(self, ctx:SimpleJavaParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#type.
    def enterType(self, ctx:SimpleJavaParser.TypeContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#type.
    def exitType(self, ctx:SimpleJavaParser.TypeContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#classOrInterfaceType.
    def enterClassOrInterfaceType(self, ctx:SimpleJavaParser.ClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#classOrInterfaceType.
    def exitClassOrInterfaceType(self, ctx:SimpleJavaParser.ClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#primitiveType.
    def enterPrimitiveType(self, ctx:SimpleJavaParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#primitiveType.
    def exitPrimitiveType(self, ctx:SimpleJavaParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#typeArguments.
    def enterTypeArguments(self, ctx:SimpleJavaParser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#typeArguments.
    def exitTypeArguments(self, ctx:SimpleJavaParser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#typeArgument.
    def enterTypeArgument(self, ctx:SimpleJavaParser.TypeArgumentContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#typeArgument.
    def exitTypeArgument(self, ctx:SimpleJavaParser.TypeArgumentContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#typeList.
    def enterTypeList(self, ctx:SimpleJavaParser.TypeListContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#typeList.
    def exitTypeList(self, ctx:SimpleJavaParser.TypeListContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#annotation.
    def enterAnnotation(self, ctx:SimpleJavaParser.AnnotationContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#annotation.
    def exitAnnotation(self, ctx:SimpleJavaParser.AnnotationContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#elementValuePairList.
    def enterElementValuePairList(self, ctx:SimpleJavaParser.ElementValuePairListContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#elementValuePairList.
    def exitElementValuePairList(self, ctx:SimpleJavaParser.ElementValuePairListContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#elementValuePair.
    def enterElementValuePair(self, ctx:SimpleJavaParser.ElementValuePairContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#elementValuePair.
    def exitElementValuePair(self, ctx:SimpleJavaParser.ElementValuePairContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#elementValue.
    def enterElementValue(self, ctx:SimpleJavaParser.ElementValueContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#elementValue.
    def exitElementValue(self, ctx:SimpleJavaParser.ElementValueContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#elementValueArrayInitializer.
    def enterElementValueArrayInitializer(self, ctx:SimpleJavaParser.ElementValueArrayInitializerContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#elementValueArrayInitializer.
    def exitElementValueArrayInitializer(self, ctx:SimpleJavaParser.ElementValueArrayInitializerContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#formalParameters.
    def enterFormalParameters(self, ctx:SimpleJavaParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#formalParameters.
    def exitFormalParameters(self, ctx:SimpleJavaParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#formalParameter.
    def enterFormalParameter(self, ctx:SimpleJavaParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#formalParameter.
    def exitFormalParameter(self, ctx:SimpleJavaParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:SimpleJavaParser.VariableDeclaratorIdContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:SimpleJavaParser.VariableDeclaratorIdContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#qualifiedNameList.
    def enterQualifiedNameList(self, ctx:SimpleJavaParser.QualifiedNameListContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#qualifiedNameList.
    def exitQualifiedNameList(self, ctx:SimpleJavaParser.QualifiedNameListContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#block.
    def enterBlock(self, ctx:SimpleJavaParser.BlockContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#block.
    def exitBlock(self, ctx:SimpleJavaParser.BlockContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#blockStatement.
    def enterBlockStatement(self, ctx:SimpleJavaParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#blockStatement.
    def exitBlockStatement(self, ctx:SimpleJavaParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#statement.
    def enterStatement(self, ctx:SimpleJavaParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#statement.
    def exitStatement(self, ctx:SimpleJavaParser.StatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#switchStatement.
    def enterSwitchStatement(self, ctx:SimpleJavaParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#switchStatement.
    def exitSwitchStatement(self, ctx:SimpleJavaParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#switchBlockStatementGroup.
    def enterSwitchBlockStatementGroup(self, ctx:SimpleJavaParser.SwitchBlockStatementGroupContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#switchBlockStatementGroup.
    def exitSwitchBlockStatementGroup(self, ctx:SimpleJavaParser.SwitchBlockStatementGroupContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#switchLabel.
    def enterSwitchLabel(self, ctx:SimpleJavaParser.SwitchLabelContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#switchLabel.
    def exitSwitchLabel(self, ctx:SimpleJavaParser.SwitchLabelContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#constantExpression.
    def enterConstantExpression(self, ctx:SimpleJavaParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#constantExpression.
    def exitConstantExpression(self, ctx:SimpleJavaParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#enumConstantName.
    def enterEnumConstantName(self, ctx:SimpleJavaParser.EnumConstantNameContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#enumConstantName.
    def exitEnumConstantName(self, ctx:SimpleJavaParser.EnumConstantNameContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#breakStatement.
    def enterBreakStatement(self, ctx:SimpleJavaParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#breakStatement.
    def exitBreakStatement(self, ctx:SimpleJavaParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#continueStatement.
    def enterContinueStatement(self, ctx:SimpleJavaParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#continueStatement.
    def exitContinueStatement(self, ctx:SimpleJavaParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:SimpleJavaParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:SimpleJavaParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#throwStatement.
    def enterThrowStatement(self, ctx:SimpleJavaParser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#throwStatement.
    def exitThrowStatement(self, ctx:SimpleJavaParser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#synchronizedStatement.
    def enterSynchronizedStatement(self, ctx:SimpleJavaParser.SynchronizedStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#synchronizedStatement.
    def exitSynchronizedStatement(self, ctx:SimpleJavaParser.SynchronizedStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#localVariableDeclarationStatement.
    def enterLocalVariableDeclarationStatement(self, ctx:SimpleJavaParser.LocalVariableDeclarationStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#localVariableDeclarationStatement.
    def exitLocalVariableDeclarationStatement(self, ctx:SimpleJavaParser.LocalVariableDeclarationStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#ifStatement.
    def enterIfStatement(self, ctx:SimpleJavaParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#ifStatement.
    def exitIfStatement(self, ctx:SimpleJavaParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#whileStatement.
    def enterWhileStatement(self, ctx:SimpleJavaParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#whileStatement.
    def exitWhileStatement(self, ctx:SimpleJavaParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#forStatement.
    def enterForStatement(self, ctx:SimpleJavaParser.ForStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#forStatement.
    def exitForStatement(self, ctx:SimpleJavaParser.ForStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#forControl.
    def enterForControl(self, ctx:SimpleJavaParser.ForControlContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#forControl.
    def exitForControl(self, ctx:SimpleJavaParser.ForControlContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#enhancedForControl.
    def enterEnhancedForControl(self, ctx:SimpleJavaParser.EnhancedForControlContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#enhancedForControl.
    def exitEnhancedForControl(self, ctx:SimpleJavaParser.EnhancedForControlContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#basicForControl.
    def enterBasicForControl(self, ctx:SimpleJavaParser.BasicForControlContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#basicForControl.
    def exitBasicForControl(self, ctx:SimpleJavaParser.BasicForControlContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#forInit.
    def enterForInit(self, ctx:SimpleJavaParser.ForInitContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#forInit.
    def exitForInit(self, ctx:SimpleJavaParser.ForInitContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#forUpdate.
    def enterForUpdate(self, ctx:SimpleJavaParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#forUpdate.
    def exitForUpdate(self, ctx:SimpleJavaParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#tryStatement.
    def enterTryStatement(self, ctx:SimpleJavaParser.TryStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#tryStatement.
    def exitTryStatement(self, ctx:SimpleJavaParser.TryStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#catchClause.
    def enterCatchClause(self, ctx:SimpleJavaParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#catchClause.
    def exitCatchClause(self, ctx:SimpleJavaParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#returnStatement.
    def enterReturnStatement(self, ctx:SimpleJavaParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#returnStatement.
    def exitReturnStatement(self, ctx:SimpleJavaParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#expressionStatement.
    def enterExpressionStatement(self, ctx:SimpleJavaParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#expressionStatement.
    def exitExpressionStatement(self, ctx:SimpleJavaParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#BitwiseOrExpr.
    def enterBitwiseOrExpr(self, ctx:SimpleJavaParser.BitwiseOrExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#BitwiseOrExpr.
    def exitBitwiseOrExpr(self, ctx:SimpleJavaParser.BitwiseOrExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#RelationalExpr.
    def enterRelationalExpr(self, ctx:SimpleJavaParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#RelationalExpr.
    def exitRelationalExpr(self, ctx:SimpleJavaParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#DotMethodCallExpr.
    def enterDotMethodCallExpr(self, ctx:SimpleJavaParser.DotMethodCallExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#DotMethodCallExpr.
    def exitDotMethodCallExpr(self, ctx:SimpleJavaParser.DotMethodCallExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#LogicalAndExpr.
    def enterLogicalAndExpr(self, ctx:SimpleJavaParser.LogicalAndExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#LogicalAndExpr.
    def exitLogicalAndExpr(self, ctx:SimpleJavaParser.LogicalAndExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#PostIncrementExpr.
    def enterPostIncrementExpr(self, ctx:SimpleJavaParser.PostIncrementExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#PostIncrementExpr.
    def exitPostIncrementExpr(self, ctx:SimpleJavaParser.PostIncrementExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#PreIncrementExpr.
    def enterPreIncrementExpr(self, ctx:SimpleJavaParser.PreIncrementExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#PreIncrementExpr.
    def exitPreIncrementExpr(self, ctx:SimpleJavaParser.PreIncrementExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#MultiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:SimpleJavaParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#MultiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:SimpleJavaParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#DotSuperExpr.
    def enterDotSuperExpr(self, ctx:SimpleJavaParser.DotSuperExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#DotSuperExpr.
    def exitDotSuperExpr(self, ctx:SimpleJavaParser.DotSuperExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#EqualityExpr.
    def enterEqualityExpr(self, ctx:SimpleJavaParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#EqualityExpr.
    def exitEqualityExpr(self, ctx:SimpleJavaParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#CastExpr.
    def enterCastExpr(self, ctx:SimpleJavaParser.CastExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#CastExpr.
    def exitCastExpr(self, ctx:SimpleJavaParser.CastExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#PrimaryExpr.
    def enterPrimaryExpr(self, ctx:SimpleJavaParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#PrimaryExpr.
    def exitPrimaryExpr(self, ctx:SimpleJavaParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#FieldAccessExpr.
    def enterFieldAccessExpr(self, ctx:SimpleJavaParser.FieldAccessExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#FieldAccessExpr.
    def exitFieldAccessExpr(self, ctx:SimpleJavaParser.FieldAccessExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#DotThisExpr.
    def enterDotThisExpr(self, ctx:SimpleJavaParser.DotThisExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#DotThisExpr.
    def exitDotThisExpr(self, ctx:SimpleJavaParser.DotThisExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#TernaryExpr.
    def enterTernaryExpr(self, ctx:SimpleJavaParser.TernaryExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#TernaryExpr.
    def exitTernaryExpr(self, ctx:SimpleJavaParser.TernaryExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#BitwiseAndExpr.
    def enterBitwiseAndExpr(self, ctx:SimpleJavaParser.BitwiseAndExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#BitwiseAndExpr.
    def exitBitwiseAndExpr(self, ctx:SimpleJavaParser.BitwiseAndExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#ArrayAccessExpr.
    def enterArrayAccessExpr(self, ctx:SimpleJavaParser.ArrayAccessExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#ArrayAccessExpr.
    def exitArrayAccessExpr(self, ctx:SimpleJavaParser.ArrayAccessExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#InstanceofExpr.
    def enterInstanceofExpr(self, ctx:SimpleJavaParser.InstanceofExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#InstanceofExpr.
    def exitInstanceofExpr(self, ctx:SimpleJavaParser.InstanceofExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#LambdaExpr.
    def enterLambdaExpr(self, ctx:SimpleJavaParser.LambdaExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#LambdaExpr.
    def exitLambdaExpr(self, ctx:SimpleJavaParser.LambdaExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#AssignmentExpr.
    def enterAssignmentExpr(self, ctx:SimpleJavaParser.AssignmentExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#AssignmentExpr.
    def exitAssignmentExpr(self, ctx:SimpleJavaParser.AssignmentExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#PrefixExpr.
    def enterPrefixExpr(self, ctx:SimpleJavaParser.PrefixExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#PrefixExpr.
    def exitPrefixExpr(self, ctx:SimpleJavaParser.PrefixExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#LogicalOrExpr.
    def enterLogicalOrExpr(self, ctx:SimpleJavaParser.LogicalOrExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#LogicalOrExpr.
    def exitLogicalOrExpr(self, ctx:SimpleJavaParser.LogicalOrExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#AdditiveExpr.
    def enterAdditiveExpr(self, ctx:SimpleJavaParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#AdditiveExpr.
    def exitAdditiveExpr(self, ctx:SimpleJavaParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#InnerClassCreationExpr.
    def enterInnerClassCreationExpr(self, ctx:SimpleJavaParser.InnerClassCreationExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#InnerClassCreationExpr.
    def exitInnerClassCreationExpr(self, ctx:SimpleJavaParser.InnerClassCreationExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#BitwiseXorExpr.
    def enterBitwiseXorExpr(self, ctx:SimpleJavaParser.BitwiseXorExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#BitwiseXorExpr.
    def exitBitwiseXorExpr(self, ctx:SimpleJavaParser.BitwiseXorExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#NewCreatorExpr.
    def enterNewCreatorExpr(self, ctx:SimpleJavaParser.NewCreatorExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#NewCreatorExpr.
    def exitNewCreatorExpr(self, ctx:SimpleJavaParser.NewCreatorExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#MethodCallExpr.
    def enterMethodCallExpr(self, ctx:SimpleJavaParser.MethodCallExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#MethodCallExpr.
    def exitMethodCallExpr(self, ctx:SimpleJavaParser.MethodCallExprContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#creator.
    def enterCreator(self, ctx:SimpleJavaParser.CreatorContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#creator.
    def exitCreator(self, ctx:SimpleJavaParser.CreatorContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#createdName.
    def enterCreatedName(self, ctx:SimpleJavaParser.CreatedNameContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#createdName.
    def exitCreatedName(self, ctx:SimpleJavaParser.CreatedNameContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#typeArgumentsOrDiamond.
    def enterTypeArgumentsOrDiamond(self, ctx:SimpleJavaParser.TypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#typeArgumentsOrDiamond.
    def exitTypeArgumentsOrDiamond(self, ctx:SimpleJavaParser.TypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#arrayCreatorRest.
    def enterArrayCreatorRest(self, ctx:SimpleJavaParser.ArrayCreatorRestContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#arrayCreatorRest.
    def exitArrayCreatorRest(self, ctx:SimpleJavaParser.ArrayCreatorRestContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#classCreatorRest.
    def enterClassCreatorRest(self, ctx:SimpleJavaParser.ClassCreatorRestContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#classCreatorRest.
    def exitClassCreatorRest(self, ctx:SimpleJavaParser.ClassCreatorRestContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#arguments.
    def enterArguments(self, ctx:SimpleJavaParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#arguments.
    def exitArguments(self, ctx:SimpleJavaParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#classBody.
    def enterClassBody(self, ctx:SimpleJavaParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#classBody.
    def exitClassBody(self, ctx:SimpleJavaParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#expressionList.
    def enterExpressionList(self, ctx:SimpleJavaParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#expressionList.
    def exitExpressionList(self, ctx:SimpleJavaParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#lambdaExpression.
    def enterLambdaExpression(self, ctx:SimpleJavaParser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#lambdaExpression.
    def exitLambdaExpression(self, ctx:SimpleJavaParser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#superSuffix.
    def enterSuperSuffix(self, ctx:SimpleJavaParser.SuperSuffixContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#superSuffix.
    def exitSuperSuffix(self, ctx:SimpleJavaParser.SuperSuffixContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#primary.
    def enterPrimary(self, ctx:SimpleJavaParser.PrimaryContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#primary.
    def exitPrimary(self, ctx:SimpleJavaParser.PrimaryContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#literal.
    def enterLiteral(self, ctx:SimpleJavaParser.LiteralContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#literal.
    def exitLiteral(self, ctx:SimpleJavaParser.LiteralContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#arrayInitializer.
    def enterArrayInitializer(self, ctx:SimpleJavaParser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#arrayInitializer.
    def exitArrayInitializer(self, ctx:SimpleJavaParser.ArrayInitializerContext):
        pass



del SimpleJavaParser