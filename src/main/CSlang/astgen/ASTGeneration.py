# MSSV 2013093

from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

class ASTGeneration(CSlangVisitor):

    # program: class_dcl+ EOF ;    
    def visitProgram(self,ctx:CSlangParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.class_dcl()])

    # class_dcl: CLASS ID ('<-' ID | )  class_body;
    def visitClass_dcl(self, ctx: CSlangParser.Class_dclContext):
        if ctx.getChildCount() > 3:
            parentname = Id(ctx.ID(0).getText())
            memlist = self.visit(ctx.class_body())
            classname = Id(ctx.ID(1).getText())
            return ClassDecl(classname, memlist, parentname)
        else:
            classname = Id(ctx.ID(0).getText())
            memlist = self.visit(ctx.class_body())
            parentname = None 
            return ClassDecl(classname, memlist, parentname)
        
    # class_body: LCURB decls RCURB;
    def visitClass_body(self, ctx: CSlangParser.Class_bodyContext):
        return self.visit(ctx.decls())
    
    # decls: decl decls | ;
    def visitDecls(self, ctx: CSlangParser.DeclsContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.decl()) + self.visit(ctx.decls())
    
    # decl: att_decl | constructor_decl | method_decl;
    def visitDecl(self, ctx: CSlangParser.DeclContext):
        if ctx.att_decl():
            return self.visit(ctx.att_decl())
        elif ctx.constructor_decl():
            return [self.visit(ctx.constructor_decl())]
        elif ctx.method_decl():
            return [self.visit(ctx.method_decl())]

    # att_decl: (CONST_VAR super_idlist COLON data_type_decl SEMI) |
    #           (CONST_VAR (ID | A_ID) recursion_att expr SEMI);
    def visitAtt_decl(self, ctx: CSlangParser.Att_declContext):
        if ctx.expr():
            listIDVal = [Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.A_ID().getText())] + self.visit(ctx.recursion_att()) + [self.visit(ctx.expr())]
            variable =  listIDVal[0 : int(len(listIDVal)/2)]
            varType = listIDVal[int(len(listIDVal)/2)]
            varInit = listIDVal[int(len(listIDVal)/2) + 1:]
            if ctx.CONST_VAR().getText() == 'var':
                return list(map(lambda x,y: AttributeDecl(VarDecl(x, varType, y)), variable, varInit))  
            else:
                return list(map(lambda x,y: AttributeDecl(ConstDecl(x, varType, y)), variable, varInit))
        else:
            variable = self.visit(ctx.super_idlist())
            varType = self.visit(ctx.data_type_decl())
            if ctx.CONST_VAR().getText() == 'var':
                return list(map(lambda x: AttributeDecl(VarDecl(x, varType, None)), variable))
            else:
                return list(map(lambda x: AttributeDecl(ConstDecl(x, varType, None)), variable))

    # recursion_att: COMMA (ID | A_ID) recursion_att expr COMMA | vari_decl;
    def visitRecursion_att(self, ctx: CSlangParser.Recursion_attContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.vari_decl())]
        
        ids = Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.A_ID().getText())
        return [ids] + self.visit(ctx.recursion_att()) + [self.visit(ctx.expr())]
        
    # vari_decl: COLON data_type_decl EQUAL;
    def visitVari_decl(self, ctx: CSlangParser.Vari_declContext):
        return self.visit(ctx.data_type_decl())

    # method_decl: FUNC (ID | A_ID) LP paramlist RP COLON data_type block_stmt;
    def visitMethod_decl(self, ctx: CSlangParser.Method_declContext):
        name = Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.A_ID().getText())
        param = self.visit(ctx.paramlist())
        returnType = self.visit(ctx.data_type())  # VoidType for constructor
        body = self.visit(ctx.block_stmt())
        return MethodDecl(name, param, returnType, body);

    # constructor_decl: FUNC CONSTRUCTOR LP paramlist RP block_stmt;
    def visitConstructor_decl(self, ctx: CSlangParser.Constructor_declContext):
        name = Id(ctx.CONSTRUCTOR().getText())
        param = self.visit(ctx.paramlist())
        returnType = VoidType()  # VoidType for constructor
        body = self.visit(ctx.block_stmt())
        return MethodDecl(name, param, returnType, body);

    # paramlist: paramprime | ;
    def visitParamlist(self, ctx: CSlangParser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paramprime())
    
    # paramprime: param COMMA paramprime | param ;
    def visitParamprime(self, ctx: CSlangParser.ParamprimeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.param())
        return self.visit(ctx.param()) + self.visit(ctx.paramprime())
    
    # param: idlist COLON data_type_decl;
    def visitParam(self, ctx: CSlangParser.ParamContext):
        ids = self.visit(ctx.idlist())
        mptype = self.visit(ctx.data_type_decl())
        return [VarDecl(x, mptype, None) for x in ids]

    # block_stmt: LCURB stmtlist RCURB;
    def visitBlock_stmt(self, ctx: CSlangParser.Block_stmtContext):
        return Block(self.visit(ctx.stmtlist()))
    
    # stmtlist: stmt stmtlist | ;
    def visitStmtlist(self, ctx: CSlangParser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.stmt()) + self.visit(ctx.stmtlist())
    
    # stmt: ( var_stmt | asm_stmt | break_stmt | continue_stmt | return_stmt | call_stmt) SEMI
    #             | if_stmt 
    #             | for_stmt
    #             | block_stmt;
    def visitStmt(self, ctx: CSlangParser.StmtContext):
        if ctx.var_stmt():
            return self.visit(ctx.var_stmt())
        elif ctx.asm_stmt():
            return [self.visit(ctx.asm_stmt())]
        elif ctx.break_stmt():
            return [self.visit(ctx.break_stmt())]
        elif ctx.continue_stmt():
            return [self.visit(ctx.continue_stmt())]
        elif ctx.return_stmt():
            return [self.visit(ctx.return_stmt())]
        elif ctx.call_stmt():
            return [self.visit(ctx.call_stmt())]
        elif ctx.if_stmt():
            return [self.visit(ctx.if_stmt())]
        elif ctx.for_stmt():
            return [self.visit(ctx.for_stmt())]
        elif ctx.block_stmt():
            return [self.visit(ctx.block_stmt())]

    # asm_stmt: expr7 ASSIGN expr;
    def visitAsm_stmt(self, ctx: CSlangParser.Asm_stmtContext):
        lhs = self.visit(ctx.expr7())
        exp = self.visit(ctx.expr())
        return Assign(lhs, exp)
    
    # var_stmt: (CONST_VAR idlist COLON data_type_decl) 
    #           | (CONST_VAR ID recursion_vari expr);
    def visitVar_stmt(self, ctx: CSlangParser.Var_stmtContext): 
        if ctx.expr():
            listIDVal = [Id(ctx.ID().getText())] + self.visit(ctx.recursion_vari()) + [self.visit(ctx.expr())]
            
            variable =  listIDVal[0 : int(len(listIDVal)/2)]
            varType = listIDVal[int(len(listIDVal)/2)]
            varInit = listIDVal[int(len(listIDVal)/2) + 1:]
            
            if ctx.CONST_VAR().getText() == 'var':
                return list(map(lambda x,y: VarDecl(x, varType, y), variable, varInit))
            else:
                return list(map(lambda x,y: ConstDecl(x, varType, y), variable, varInit))
        else:
            variable = self.visit(ctx.idlist())
            varType = self.visit(ctx.data_type_decl())
            if ctx.CONST_VAR().getText() == 'var':
                return list(map(lambda x: VarDecl(x, varType, None), variable))
            else:
                return list(map(lambda x: ConstDecl(x, varType, None), variable))
        
    # recursion_vari: COMMA ID recursion_vari expr COMMA | vari_decl;
    def visitRecursion_vari(self, ctx: CSlangParser.Recursion_variContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.vari_decl())]
        
        return [Id(ctx.ID().getText())] + self.visit(ctx.recursion_vari()) + [self.visit(ctx.expr())]
    
    # continue_stmt: CONTINUE;
    def visitContinue_stmt(self, ctx: CSlangParser.Continue_stmtContext):
        return Continue();

    # break_stmt: BREAK	;
    def visitBreak_stmt(self, ctx: CSlangParser.Break_stmtContext):
        return Break();

    # return_stmt: RETURN ( expr | );
    def visitReturn_stmt(self, ctx: CSlangParser.Return_stmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return(None)

    # call_stmt: expr7 DOT ID LP empty_exprlist RP | 
    #           (ID DOT | ) A_ID LP empty_exprlist RP;
    def visitCall_stmt(self, ctx: CSlangParser.Call_stmtContext):
        if ctx.A_ID():
            obj = Id(ctx.ID().getText()) if ctx.ID() else None
            method = Id(ctx.A_ID().getText())
            param = self.visit(ctx.empty_exprlist())
            return CallStmt(obj, method, param)
        else:
            obj = self.visit(ctx.expr7()) 
            method = Id(ctx.ID().getText())
            param = self.visit(ctx.empty_exprlist())
            return CallStmt(obj, method, param)

    # if_stmt: IF (preblock_stmt | ) expr block_stmt (ELSE block_stmt | );
    def visitIf_stmt(self, ctx: CSlangParser.If_stmtContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.block_stmt(0))
        preStmt = self.visit(ctx.preblock_stmt()) if ctx.preblock_stmt() else None
        elseStmt = self.visit(ctx.block_stmt(1)) if ctx.ELSE() else None 
        return If(expr, thenStmt, preStmt, elseStmt)
    
    # preblock_stmt: block_stmt;
    def visitPreblock_stmt(self, ctx: CSlangParser.Preblock_stmtContext):
        return self.visit(ctx.block_stmt())

    # for_stmt: FOR init_stmt SEMI condition_expr SEMI post_stmt block_stmt;
    def visitFor_stmt(self, ctx: CSlangParser.For_stmtContext):
        initStmt = self.visit(ctx.init_stmt())
        expr = self.visit(ctx.condition_expr())
        postStmt = self.visit(ctx.post_stmt())
        loop = self.visit(ctx.block_stmt())  
        return For(initStmt, expr, postStmt, loop)
    
    # init_stmt: expr7 ASSIGN expr;
    def visitInit_stmt(self, ctx: CSlangParser.Init_stmtContext):
        lhs = self.visit(ctx.expr7())
        exp = self.visit(ctx.expr())
        return Assign(lhs, exp)
    
    # condition_expr: expr;
    def visitCondition_expr(self, ctx: CSlangParser.Condition_exprContext):
        return self.visit(ctx.expr())
    
    # post_stmt: expr7 ASSIGN expr;
    def visitPost_stmt(self, ctx: CSlangParser.Post_stmtContext):
        lhs = self.visit(ctx.expr7())
        exp = self.visit(ctx.expr())
        return Assign(lhs, exp)


    # expr: expr1 STRINGCON expr1 | expr1;
    def visitExpr(self, ctx: CSlangParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
    
    # expr1: expr2 (ISEQUAL | NOTEQUAL | LESSTHAN | LESSTHANOREQ | GREATERTHAN | GREATERTHANOREQ) expr2 | expr2;
    def visitExpr1(self, ctx: CSlangParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
    
    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx: CSlangParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
    
    # expr3: expr3 (ADD | SUBTRAC) expr4 | expr4;
    def visitExpr3(self, ctx: CSlangParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))

    # expr4: expr4 (MULTI | DIVID | BSLASH | MODUL) expr5 | expr5;
    def visitExpr4(self, ctx: CSlangParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))

    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx: CSlangParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))

    # expr6: SUBTRAC expr6 | expr7;
    def visitExpr6(self, ctx: CSlangParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))

    # expr7: expr8 LSQAB expr RSQAB | expr8; //index operator
    def visitExpr7(self, ctx: CSlangParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            arr = self.visit(ctx.expr8())
            idx = self.visit(ctx.expr())
            return ArrayCell(arr, idx)
        
    # expr8: expr8 DOT ID | 
    #        expr8 DOT ID LP empty_exprlist RP | 
    #        expr9; //mem access
    def visitExpr8(self, ctx: CSlangParser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif ctx.LP():
            obj =  self.visit(ctx.expr8())
            method = Id(ctx.ID().getText())
            param = self.visit(ctx.empty_exprlist())
            return CallExpr(obj, method, param)
        else:
            obj =  self.visit(ctx.expr8())
            fieldname =  Id(ctx.ID().getText())
            return FieldAccess(obj, fieldname);

    # expr9: (ID DOT | ) A_ID | 
    #        (ID DOT | ) A_ID LP empty_exprlist RP | 
    #        expr10;
    def visitExpr9(self, ctx: CSlangParser.Expr9Context):
        if ctx.A_ID():
            if ctx.LP():
                if ctx.DOT():
                    obj =  Id(ctx.ID().getText())
                    method = Id(ctx.A_ID().getText())
                    param = self.visit(ctx.empty_exprlist())
                    return CallExpr(obj, method, param)
                else:
                    method = Id(ctx.A_ID().getText())
                    param = self.visit(ctx.empty_exprlist())
                    return CallExpr(None, method, param)
            else:
                if ctx.DOT():
                    obj =  Id(ctx.ID().getText())
                    fieldname = Id(ctx.A_ID().getText())
                    return FieldAccess(obj, fieldname);
                else:
                    fieldname =  Id(ctx.A_ID().getText())
                    return FieldAccess(None, fieldname)
        else:
            return self.visit(ctx.getChild(0))
    
    # expr10: NEW ID LP empty_exprlist RP | expr11;
    def visitExpr10(self, ctx: CSlangParser.Expr10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr11())
        
        classname = Id(ctx.ID().getText())
        param = self.visit(ctx.empty_exprlist())
        return NewExpr(classname, param)
    
    # expr11: subexpr | ID | A_ID | lit | SELF | NULL;
    def visitExpr11(self, ctx: CSlangParser.Expr11Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.A_ID():
            return Id(ctx.A_ID().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.lit():
            return self.visit(ctx.lit());
        else:
            return self.visit(ctx.subexpr());
    
    # subexpr: LP expr RP;
    def visitSubexpr(self, ctx:CSlangParser.SubexprContext):
        return self.visit(ctx.expr())
    
    # data_type_decl: INT | FLOAT | BOOL | STRING | array_type | ID ;
    def visitData_type_decl(self, ctx: CSlangParser.Data_type_declContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOL():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.ID():
            return ClassType(Id(ctx.ID().getText()));
        else:
            return self.visit(ctx.array_type());
        
    # data_type: INT | FLOAT | BOOL | STRING | array_type | ID | VOID;
    def visitData_type(self, ctx: CSlangParser.Data_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOL():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.ID():
            return ClassType(Id(ctx.ID().getText()));
        elif ctx.VOID():
            return VoidType()
        else:
            return self.visit(ctx.array_type());

    # array_type: LSQAB DIGIT RSQAB array_data_type_decl;
    def visitArray_type(self, ctx: CSlangParser.Array_typeContext):
        size = int(ctx.DIGIT().getText())
        eleType = self.visit(ctx.array_data_type_decl())
        return ArrayType(size, eleType);
    
    # array_data_type_decl: INT | FLOAT | BOOL | STRING;
    def visitArray_data_type_decl(self, ctx: CSlangParser.Array_data_type_declContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOL():
            return BoolType()
        else:
            return StringType()

    # super_idlist: (ID | A_ID) COMMA super_idlist | (ID | A_ID);
    def visitSuper_idlist(self, ctx: CSlangParser.Super_idlistContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.A_ID().getText())]
        return [Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.A_ID().getText())] + self.visit(ctx.super_idlist());
    
    # idlist: ID COMMA idlist | ID;
    def visitIdlist(self, ctx: CSlangParser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())];
        return [Id(ctx.ID().getText())] + self.visit(ctx.idlist());
    
    # empty_exprlist: exprprime | ;
    def visitEmpty_exprlist(self, ctx: CSlangParser.Empty_exprlistContext):
        if ctx.getChildCount() == 0:
            return [];
        return self.visit(ctx.exprprime())    
    
    # exprprime: expr COMMA exprprime | expr;
    def visitExprprime(self, ctx: CSlangParser.ExprprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprprime());

    # lit: arraylit | intlit | FLOATLIT | BOOLIT | STRINGLIT | NULL | ID;
    def visitLit(self, ctx:CSlangParser.LitContext):
        if ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()));
        elif ctx.BOOLIT():
            return BooleanLiteral(True if ctx.BOOLIT().getText() == 'true' else False);
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText());
        elif ctx.intlit():
            return self.visit(ctx.intlit());
        elif ctx.NULL():
            return NullLiteral();
        elif ctx.ID():
            return Id(ctx.ID().getText());
        else:
            return self.visit(ctx.arraylit());

    #intlit: ZERO | DIGIT ;
    def visitIntlit(self, ctx: CSlangParser.IntlitContext):
        return IntLiteral(int(ctx.ZERO().getText() if ctx.ZERO() else ctx.DIGIT().getText()))
    
    # arraylit: LSQAB array_decl RSQAB;
    def visitArraylit(self, ctx:CSlangParser.ArraylitContext):
        return ArrayLiteral(self.visit(ctx.array_decl()));
    #array_decl: lit COMMA array_decl | lit;
    def visitArray_decl(self, ctx):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.lit())];
        
        return [self.visit(ctx.lit())] + self.visit(ctx.array_decl());
    
    # array_decl: array_int | array_float | array_bool | array_string;
    # def visitArray_decl(self, ctx:CSlangParser.Array_declContext):
    #     return self.visit(ctx.getChild(0));
    
    # array_int: intlit COMMA array_int | intlit;
    def visitArray_int(self, ctx: CSlangParser.Array_intContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.intlit())];
        
        return [self.visit(ctx.intlit())] + self.visit(ctx.array_int());
    
    # array_float: FLOATLIT COMMA array_float | FLOATLIT;
    def visitArray_float(self, ctx: CSlangParser.Array_floatContext):
        if ctx.getChildCount() == 1:
            return [FloatLiteral(float(ctx.FLOATLIT().getText()))];
        
        return [FloatLiteral(float(ctx.FLOATLIT().getText()))] + self.visit(ctx.array_float());
    
    # array_bool: BOOLIT COMMA array_bool | BOOLIT;
    def visitArray_bool(self, ctx: CSlangParser.Array_boolContext):
        if ctx.getChildCount() == 1:
            return [BooleanLiteral(True if ctx.BOOLIT().getText() == 'true' else False)];
        
        return [BooleanLiteral(True if ctx.BOOLIT().getText() == 'true' else False)] + self.visit(ctx.array_bool());
    
    # array_string: STRINGLIT COMMA array_string | STRINGLIT;
    def visitArray_string(self, ctx: CSlangParser.Array_stringContext):
        if ctx.getChildCount() == 1:
            return [StringLiteral(ctx.STRINGLIT().getText())];
        
        return [StringLiteral(ctx.STRINGLIT().getText())] + self.visit(ctx.array_string());  
    
