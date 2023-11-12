# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete generic visitor for a parse tree produced by CSlangParser.

class CSlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_dcl.
    def visitClass_dcl(self, ctx:CSlangParser.Class_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_body.
    def visitClass_body(self, ctx:CSlangParser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#decls.
    def visitDecls(self, ctx:CSlangParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#decl.
    def visitDecl(self, ctx:CSlangParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#att_decl.
    def visitAtt_decl(self, ctx:CSlangParser.Att_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#recursion_att.
    def visitRecursion_att(self, ctx:CSlangParser.Recursion_attContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#vari_decl.
    def visitVari_decl(self, ctx:CSlangParser.Vari_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_decl.
    def visitMethod_decl(self, ctx:CSlangParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#constructor_decl.
    def visitConstructor_decl(self, ctx:CSlangParser.Constructor_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#paramlist.
    def visitParamlist(self, ctx:CSlangParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#paramprime.
    def visitParamprime(self, ctx:CSlangParser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param.
    def visitParam(self, ctx:CSlangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#block_stmt.
    def visitBlock_stmt(self, ctx:CSlangParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmtlist.
    def visitStmtlist(self, ctx:CSlangParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmt.
    def visitStmt(self, ctx:CSlangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#asm_stmt.
    def visitAsm_stmt(self, ctx:CSlangParser.Asm_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#var_stmt.
    def visitVar_stmt(self, ctx:CSlangParser.Var_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#recursion_vari.
    def visitRecursion_vari(self, ctx:CSlangParser.Recursion_variContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#continue_stmt.
    def visitContinue_stmt(self, ctx:CSlangParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#break_stmt.
    def visitBreak_stmt(self, ctx:CSlangParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#return_stmt.
    def visitReturn_stmt(self, ctx:CSlangParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#call_stmt.
    def visitCall_stmt(self, ctx:CSlangParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#if_stmt.
    def visitIf_stmt(self, ctx:CSlangParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#preblock_stmt.
    def visitPreblock_stmt(self, ctx:CSlangParser.Preblock_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#for_stmt.
    def visitFor_stmt(self, ctx:CSlangParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#init_stmt.
    def visitInit_stmt(self, ctx:CSlangParser.Init_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#condition_expr.
    def visitCondition_expr(self, ctx:CSlangParser.Condition_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#post_stmt.
    def visitPost_stmt(self, ctx:CSlangParser.Post_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx:CSlangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr1.
    def visitExpr1(self, ctx:CSlangParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr2.
    def visitExpr2(self, ctx:CSlangParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr3.
    def visitExpr3(self, ctx:CSlangParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr4.
    def visitExpr4(self, ctx:CSlangParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr5.
    def visitExpr5(self, ctx:CSlangParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr6.
    def visitExpr6(self, ctx:CSlangParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr7.
    def visitExpr7(self, ctx:CSlangParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr8.
    def visitExpr8(self, ctx:CSlangParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr9.
    def visitExpr9(self, ctx:CSlangParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr10.
    def visitExpr10(self, ctx:CSlangParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr11.
    def visitExpr11(self, ctx:CSlangParser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#subexpr.
    def visitSubexpr(self, ctx:CSlangParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#data_type_decl.
    def visitData_type_decl(self, ctx:CSlangParser.Data_type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#data_type.
    def visitData_type(self, ctx:CSlangParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_type.
    def visitArray_type(self, ctx:CSlangParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_data_type_decl.
    def visitArray_data_type_decl(self, ctx:CSlangParser.Array_data_type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#super_idlist.
    def visitSuper_idlist(self, ctx:CSlangParser.Super_idlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#idlist.
    def visitIdlist(self, ctx:CSlangParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#empty_exprlist.
    def visitEmpty_exprlist(self, ctx:CSlangParser.Empty_exprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprprime.
    def visitExprprime(self, ctx:CSlangParser.ExprprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#lit.
    def visitLit(self, ctx:CSlangParser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arraylit.
    def visitArraylit(self, ctx:CSlangParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_decl.
    def visitArray_decl(self, ctx:CSlangParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_int.
    def visitArray_int(self, ctx:CSlangParser.Array_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_float.
    def visitArray_float(self, ctx:CSlangParser.Array_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_bool.
    def visitArray_bool(self, ctx:CSlangParser.Array_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_string.
    def visitArray_string(self, ctx:CSlangParser.Array_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#intlit.
    def visitIntlit(self, ctx:CSlangParser.IntlitContext):
        return self.visitChildren(ctx)



del CSlangParser