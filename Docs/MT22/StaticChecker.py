from Visitor import Visitor
from AST import ArrayType
from AST import IntegerType
from AST import FloatType
from AST import BooleanType
from AST import StringType
from AST import AutoType
from AST import VoidType
from AST import FuncDecl
from AST import WhileStmt
from AST import DoWhileStmt
from AST import ForStmt
from AST import VarDecl
from AST import Id
from AST import ArrayLit
from AST import CallStmt
from AST import BlockStmt
from AST import ParamDecl
from AST import FuncCall

from StaticError import *


class GetENV(Visitor):
    
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        return self.visitProgram(self.ast, [])
    
    def visitFuncDecl(self, ast, param):
        param[0] += [[ast,False]]
        return param

    def visitProgram(self, ast, param):
        param = [[]]
        for decl in ast.decls:
            if type(decl) is FuncDecl:
                param = self.visit(decl, param)
        
        newFunc = FuncDecl("readInteger",IntegerType(),[], None, BlockStmt([]))
        param[0] = param[0] + [[newFunc,False]]
        
        newFunc = FuncDecl("printInteger",VoidType(),[ParamDecl("anArg", IntegerType(), False, False)], None, BlockStmt([]))
        param[0] = param[0] + [[newFunc,False]]
        
        newFunc = FuncDecl("readFloat",FloatType(),[], None, BlockStmt([]))
        param[0] = param[0] + [[newFunc,False]]
        
        newFunc = FuncDecl("printFloat",VoidType(),[ParamDecl("anArg", FloatType(), False, False)], None, BlockStmt([]))
        param[0] = param[0] + [[newFunc,False]]
        
        newFunc = FuncDecl("readBoolean",BooleanType(),[], None, BlockStmt([]))
        param[0] = param[0] + [[newFunc,False]]
        
        newFunc = FuncDecl("printBoolean",VoidType(),[ParamDecl("anArg", BooleanType(), False, False)], None, BlockStmt([]))
        param[0] = param[0] + [[newFunc,False]]
        
        newFunc = FuncDecl("readString",StringType(),[], None, BlockStmt([]))
        param[0] = param[0] + [[newFunc,False]]
        
        newFunc = FuncDecl("printString",VoidType(),[ParamDecl("anArg", StringType(), False, False)], None, BlockStmt([]))
        param[0] = param[0] + [[newFunc,False]]
        
        newFunc = FuncDecl("preventDefault",VoidType(),[], None, BlockStmt([]))
        param[0] = param[0] + [[newFunc,False]]
        
        return param
    
class StaticChecker(Visitor):
    
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        return self.visitProgram(self.ast, [])
    
    def visitIntegerType(self, ast, param):
        return IntegerType(), param
    def visitFloatType(self, ast, param):
        return FloatType(), param
    def visitBooleanType(self, ast, param):
        return BooleanType(), param
    def visitStringType(self, ast, param):
        return StringType(), param
    def visitArrayType(self, ast, param):
        return ArrayType(ast.dimensions, ast.typ), param
    def visitAutoType(self, ast, param):
        return AutoType(), param
    def visitVoidType(self, ast, param):
        return VoidType(), param

    def visitBinExpr(self, ast, param):
    
        e1t, param = self.visit(ast.left, param)
        e2t, param = self.visit(ast.right, param)

        if ast.op in ['+','-','*','/']:
            if type(e1t) is BooleanType or type(e2t) is BooleanType:
                raise TypeMismatchInExpression(ast)
            if type(e1t) is StringType or type(e2t) is StringType:
                raise TypeMismatchInExpression(ast)
            if type(e1t) is ArrayType or type(e2t) is ArrayType:
                raise TypeMismatchInExpression(ast)
            if type(e1t) is VoidType or type(e2t) is VoidType:
                raise TypeMismatchInExpression(ast)
            
            if type(e1t) is AutoType:
                if type(e2t) is IntegerType:
                    for decls in param:
                        for decl in decls:
                            if type(decl) is list and decl[0].name == ast.left.name:
                                decl[0].return_type = e2t
                    return IntegerType(), param
                
                if type(e2t) is FloatType:
                    for decls in param:
                        for decl in decls:
                            if type(decl) is list and decl[0].name == ast.left.name:
                                decl[0].return_type = e2t
                    return FloatType(), param
                
            if type(e2t) is AutoType:
                if type(e1t) is IntegerType:
                    for decls in param:
                        for decl in decls:
                            if type(decl) is list and decl[0].name == ast.right.name:
                                decl[0].return_type = e1t
                    return IntegerType(), param
                
                if type(e1t) is FloatType:
                    for decls in param:
                        for decl in decls:
                            if type(decl) is list and decl[0].name == ast.right.name:
                                decl[0].return_type = e1t
                    return FloatType(), param
                
            if type(e1t) is FloatType or type(e2t) is FloatType:
                return FloatType(), param
            return IntegerType(), param
        if ast.op in ['%']:
            if type(e1t) is IntegerType and type(e2t) is IntegerType:
                return IntegerType(), param
            raise TypeMismatchInExpression(ast)
        if ast.op in ['&&', '||']:
            if type(e1t) is BooleanType and type(e2t) is BooleanType:
                return BooleanType(), param
            raise TypeMismatchInExpression(ast)
        if ast.op in ['::']:
            if type(e1t) is StringType and type(e2t) is StringType:
                return StringType(), param
            raise TypeMismatchInExpression(ast)
        if ast.op in ['<', '>', '<=', '>=']:
            if (type(e1t) is IntegerType or type(e1t) is FloatType) and (type(e2t) is IntegerType or type(e2t) is FloatType):
                return BooleanType(), param
            raise TypeMismatchInExpression(ast)
        if ast.op in ['==', '!=']:
            if (type(e1t) is IntegerType or type(e1t) is BooleanType) and (type(e2t) is IntegerType or type(e2t) is BooleanType):
                return BooleanType(), param
            raise TypeMismatchInExpression(ast)
            
    def visitUnExpr(self, ast, param):
        et, param = self.visit(ast.val, param)
        
        if ast.op in ['-']:
            if type(et) is IntegerType:
                return IntegerType(), param
            if type(et) is FloatType:
                return FloatType(), param
            raise TypeMismatchInExpression(ast)
        if ast.op in ['!']:
            if type(et) is BooleanType:
                return BooleanType(), param
            raise TypeMismatchInExpression(ast)
            
    def visitId(self, ast, param):
        for decls in param:
            for decl in decls:
                if type(decl) is not list and type(decl) is not tuple and decl.name == ast.name:
                    return decl.typ, param
        raise Undeclared(Identifier(), ast.name)
    
    def visitArrayCell(self, ast, param):
        listIndexAccess = ast.cell
        for index in ast.cell:
            typ, param = self.visit(index, param)
            if type(typ) is not IntegerType:
                raise TypeMismatchInExpression(ast)
        
        for decls in param:
            for decl in decls:
                if type(decl) is not list and type(decl) is not tuple and decl.name == ast.name:
                    if type(decl.typ) is ArrayType:
                        if type(decl) is ParamDecl:
                            listElement = None
                        else:
                            listElement = decl.init
                        if listElement is not None:
                            if type(listElement) is ArrayLit:
                                for idList in range(0, len(listIndexAccess)):
                                    listElement = listElement.explist[0]
                                typIdFind, param = self.visit(listElement, param)
                                return typIdFind, param
                            elif type(listElement) is FuncCall:
                                typOf, param = self.visit(listElement, param)
                                lstOfArr = typOf.dimensions
                                if len(listIndexAccess) == len(lstOfArr):
                                    typIdFind, param = self.visit(typOf.typ, param)
                                    return typIdFind, param
                                if len(listIndexAccess) < len(lstOfArr):
                                    typIdFind = ArrayType(lstOfArr[len(listIndexAccess)], typOf.typ)
                                    return typIdFind, param
                        else:
                            if len(decl.typ.dimensions) == len(listIndexAccess):
                                typIdFind = decl.typ.typ
                                return typIdFind, param
                            elif len(decl.typ.dimensions) > len(listIndexAccess):
                                lenTru = len(decl.typ.dimensions) - len(listIndexAccess)
                                newList = []
                                for item in listIndexAccess[::-1]:
                                    if lenTru == 0:
                                        break
                                    lenTru -= 1
                                    newList = [item] + newList
                                typIdFind = ArrayType(newList, decl.typ.typ)
                                return typIdFind, param
                            else:
                                raise TypeMismatchInExpression(ast)
                        # return typIdFind, param
                    else:
                        raise TypeMismatchInExpression(ast) 
                
                if (type(decl) is list or type(decl) is tuple):
                    if type(decl) is list:
                        if decl[0].name == ast.name:
                            raise TypeMismatchInExpression(ast)
                    if type(decl) is tuple:
                        if decl[0] == ast.name:
                            raise TypeMismatchInExpression(ast)
        raise Undeclared(Identifier(), ast.name)
    
    def visitIntegerLit(self, ast, param):
        return IntegerType(), param
    def visitFloatLit(self, ast, param):
        return FloatType(), param
    def visitStringLit(self, ast, param):
        return StringType(), param
    def visitBooleanLit(self, ast, param):
        return BooleanType(), param

    
    def visitArrayLit(self, ast, param):
        listValArr = ast.explist
        
        if not listValArr:
            return ArrayType([0], VoidType()), param
        else:
            typFist, param = self.visit(listValArr[0], param)
        for item in listValArr:
            typeItem, param = self.visit(item, param)
            if type(typeItem) is not type(typFist):
                raise IllegalArrayLiteral(ast)
        
        for i in range(0, len(listValArr)):
            for j in range(i+1, len(listValArr)):
                if type(listValArr[i]) is ArrayLit and type(listValArr[i]) is ArrayLit:
                    item1, param = self.visit(listValArr[i], param)
                    item2, param = self.visit(listValArr[j], param)
                    if type(item1.typ) is not type(item2.typ) or item1.dimensions != item2.dimensions:
                        raise IllegalArrayLiteral(ast)
                    
        dimensions = []
        while type(listValArr[0]) is ArrayLit:
            listValArr = listValArr[0].explist
        
        item, param = self.visit(ast.explist[0], param)
        
        if type(item) is ArrayType:
            dimensions = dimensions + [len(ast.explist)] + item.dimensions
        else:
            dimensions = dimensions + [len(ast.explist)]
            
        typ, param = self.visit(listValArr[0], param)
        if type(typ) is ArrayType:
            return ArrayType(dimensions, typ.typ), param
        else:
            return ArrayType(dimensions, typ), param
    
    def visitFuncCall(self, ast, param):
        flag = True
        flag2 = False
        for decls in param:
            for decl in decls:
                if type(decl) is not list and type(decl) is not tuple and decl.name == ast.name:
                    flag = False
                elif type(decl) is list:
                    if decl[0].name == ast.name:
                        if flag == False:
                            raise TypeMismatchInExpression(ast)
                        if type(decl[0].return_type) is VoidType:
                            raise TypeMismatchInExpression(ast)
                        if len(decl[0].params) != len(ast.args):
                            raise TypeMismatchInExpression(ast)
                        
                        for i in range(0, len(decl[0].params)):
                            typ1, param = self.visit(decl[0].params[i].typ, param)
                            typ2, param = self.visit(ast.args[i], param)
                            if type(typ1) is AutoType and type(typ2) is not AutoType:
                                decl[0].params[i].typ = typ2
                            elif type(typ1) is not AutoType and type(typ2) is AutoType:
                                for items in param:
                                    for item in items:
                                        if type(item) is list:
                                            if ast.args[i].name == item[0].name:
                                                item[0].return_type = typ1
                                        elif type(item) is tuple:
                                            if ast.args[i].name == item[0]:
                                                item[1] = typ1
                                        else:
                                            if ast.args[i].name == item.name:
                                                item.typ = typ1
                                                flag2 = True
                                                break
                                    if flag2:
                                        break
                            elif type(typ1) is FloatType and type(typ2) is IntegerType:
                                continue
                            elif type(typ1) is not type(typ2):
                                raise TypeMismatchInExpression(ast)
                        # param = self.visit(decl[0].body, param)
                        return decl[0].return_type, param
        if ast.name == "super" or ast.name == "preventDefault":
            return VoidType(), param
        raise Undeclared(Function(), ast.name)

    def visitAssignStmt(self, ast, param):
        rhs = ast.rhs
        lhs = ast.lhs
        
        vt, param = self.visit(lhs, param)
        vp, param = self.visit(rhs, param)
        
        
        if type(vp) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(vp) is IntegerType and type(vt) is FloatType:
            return param
        if type(vp) is AutoType or type(vt) is AutoType:
            if type(vp) is AutoType and type(vt) is not AutoType:
                if type(rhs) is VarDecl or type(rhs) is FuncDecl or type(rhs) is Id:
                    flag1 = False
                    for items in param:
                        for item in items:
                            if type(item) is not list and type(item) is not tuple and item.name == rhs.name:
                                if type(item) is FuncDecl:
                                    item.return_type = vt
                                    flag1 =  True
                                    break
                                else:
                                    item.typ = vt
                                    flag1 =  True
                                    break
                        if flag1:
                            break
            if type(vp) is not AutoType and type(vt) is AutoType:
                if type(lhs) is VarDecl or type(lhs) is FuncDecl or type(lhs) is Id:
                    flag1 = False
                    for items in param:
                        for item in items:
                            if type(item) is not list and type(item) is not tuple and item.name == lhs.name:
                                if type(item) is FuncDecl:
                                    item.return_type = vp
                                    flag1 =  True
                                    break
                                else:
                                    item.typ = vp
                                    flag1 =  True
                                    break
                        if flag1:
                            break
            return param
        if type(vp) is not type(vt):
            raise TypeMismatchInStatement(ast)
        return param
    
    def visitBlockStmt(self, ast, param):
        newLst = [[]]
        for item in param[0]:
            if type(item) is tuple:
                newItem = (item[0], item[1], 'BlockStmt')
                newLst = [[newItem]]
        env = newLst + param
        for decl in ast.body:
            env = self.visit(decl, env)
        return param
    
    def visitIfStmt(self, ast, param):
        typ, param = self.visit(ast.cond, param)
        if type(typ) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        newLst = [[]]
        for item in param[0]:
            if type(item) is tuple:
                newItem = (item[0], item[1], 'IfStmt')
                newLst = [[newItem]]
                break
        env = newLst + param
        env = self.visit(ast.tstmt, env)
        
        if ast.fstmt is not None:
            newLst1 = [[]]
            for item in param[0]:
                if type(item) is tuple:
                    newItem = (item[0], item[1], 'ElseStmt')
                    newLst1 = [[newItem]]
                    break
            env = newLst1 + param
            env = self.visit(ast.fstmt, env)
        return param
    
    def visitForStmt(self, ast, param):
        newLst = [[]]
        for item in param[0]:
            if type(item) is tuple:
                newItem = (item[0], item[1], 'ForStmt')
                newLst = [[newItem]]
        env = newLst + param
        typScala, env = self.visit(ast.init.lhs, env)
        if type(typScala) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        env = self.visit(ast.init, env)
        
        typCond, env = self.visit(ast.cond, env)
        if type(typCond) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        
        typUpd, env = self.visit(ast.upd, env)
        if type(typUpd) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        env = self.visit(ast.stmt, env)
        return param
    
    def visitWhileStmt(self, ast, param):
        newLst = [[]]
        for item in param[0]:
            if type(item) is tuple:
                newItem = (item[0], item[1], 'WhileStmt')
                newLst = [[newItem]]
        env = newLst + param
        typ, env = self.visit(ast.cond, env)
        if type(typ) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        env = self.visit(ast.stmt, env)
        return param
    
    def visitDoWhileStmt(self, ast, param):
        newLst = [[]]
        for item in param[0]:
            if type(item) is tuple:
                newItem = (item[0], item[1], 'DoWhileStmt')
                newLst = [[newItem]]
        env = newLst + param
        typ, env = self.visit(ast.cond, env)
        if type(typ) is BooleanType:
            raise TypeMismatchInStatement(ast)
        env = self.visit(ast.stmt, env)
        return param
    
    def visitBreakStmt(self, ast, param):
        flag = False
        for decls in param:
            for decl in decls:
                if type(decl) is tuple:
                    if decl[2] == 'ForStmt' or decl[2] == 'WhileStmt' or decl[2] == 'Dowhile':
                        flag = True
                        break
            if flag:
                break
        if flag == False:
            raise MustInLoop(ast)
        return param
                    
    def visitContinueStmt(self, ast, param):
        flag = False
        for decls in param:
            for decl in decls:
                if type(decl) is tuple:
                    if decl[2] == 'ForStmt' or decl[2] == 'WhileStmt' or decl[2] == 'Dowhile':
                        flag = True
                        break
            if flag:
                break
        if flag == False:
            raise MustInLoop(ast)
        return param
    
    def visitReturnStmt(self, ast, param):
        flag1 = False
        if ast.expr is None:
            typ1 = VoidType()
        else:
            typ1, param = self.visit(ast.expr, param)
        for decl in param[0]:
            if type(decl) is tuple:
                typ2 = decl[1]
                if type(typ2) is AutoType:
                    for i in range(0, len(param)):
                        for j in range(0, len(param[i])):
                            if type(param[i][j]) is tuple:
                                if param[i][j][0] == decl[0]:
                                    newTup = (param[i][j][0], typ1, decl[2])
                                    param[i][j] = newTup
                            if type(param[i][j]) is list:
                                if param[i][j][0].name == decl[0]:
                                    param[i][j][0].return_type = typ1
                    param.pop(0)
                    return param
                elif type(typ1) is IntegerType and type(typ2) is FloatType:
                    param.pop(0)
                    return param
                elif type(typ1) is not type(typ2):
                    raise TypeMismatchInStatement(ast)
                else:
                    param.pop(0)
                    return param
        
    def visitCallStmt(self, ast, param):
        flag1 = False
        flag = True
        flag2 = False
        for decls in param:
            for decl in decls:
                if type(decl) is not list and type(decl) is not tuple and decl.name == ast.name:
                    flag = False
                elif type(decl) is list and decl[0].name == ast.name:
                    if flag == False:
                        raise TypeMismatchInExpression(ast)
                    if len(decl[0].params) != len(ast.args):
                        raise TypeMismatchInExpression(ast)
                    for i in range(0, len(decl[0].params)):
                        
                        typ1, param = self.visit(decl[0].params[i].typ, param)
                        typ2, param = self.visit(ast.args[i], param)
                        if type(typ1) is AutoType and type(typ2) is not AutoType:
                            decl[0].params[i].typ = typ2
                        elif type(typ1) is not AutoType and type(typ2) is AutoType:
                            for items in param:
                                for item in items:
                                    if type(item) is list:
                                        if ast.args[i].name == item[0].name:
                                            item[0].return_type = typ1
                                    elif type(item) is tuple:
                                        if ast.args[i].name == item[0]:
                                            item[1] = typ1
                                    else:
                                        if ast.args[i].name == item.name:
                                            item.typ = typ1
                                            flag2 = True
                                            break
                                if flag2:
                                    break
                        elif type(typ1) is FloatType and type(typ2) is IntegerType:
                            continue
                        elif type(typ1) is ArrayType and type(typ2) is ArrayType:
                            if typ1.dimensions != typ2.dimensions or type(typ1.typ) is not type(typ2.typ):
                                raise TypeMismatchInStatement(ast)
                        elif type(typ1) is not type(typ2):
                            raise TypeMismatchInStatement(ast)
                    flag1 = True
                    break
            if flag1:
                break
        if flag1 == False:
            if ast.name != "super" and ast.name != "preventDefault":
                raise Undeclared(Function(), ast.name)
            if ast.name == "super" or ast.name == "preventDefault":
                if ast.name == "super":
                    if not ast.args:             
                        for decl in param[0]:
                            if type(decl) is list:
                                if ast.inherit == decl[0].name:
                                    if decl[0].params:
                                        raise TypeMismatchInStatement(ast)
                                    else:
                                        pass
                    else:
                        for decl in param[0]:
                            if type(decl) is list:
                                if ast.inherit == decl[0].name:
                                    if len(decl[0].params) != len(ast.args):
                                        raise TypeMismatchInStatement(ast)
                                        
                                    for i in range(0, len(decl[0].params)):
                                        typ1, param = self.visit(decl[0].params[i].typ, param)
                                        typ2, param = self.visit(ast.args[i], param)
                                        if type(typ1) is AutoType and type(typ2) is not AutoType:
                                            decl[0].params[i].typ = typ2
                                        elif type(typ1) is not AutoType and type(typ2) is AutoType:
                                            for items in param:
                                                for item in items:
                                                    if type(item) is list:
                                                        if ast.args[i].name == item[0].name:
                                                            item[0].return_type = typ1
                                                    elif type(item) is tuple:
                                                        if ast.args[i].name == item[0]:
                                                            item[1] = typ1
                                                    else:
                                                        if ast.args[i].name == item.name:
                                                            item.typ = typ1
                                                            flag2 = True
                                                            break
                                                if flag2:
                                                    break
                                        elif type(typ1) is FloatType and type(typ2) is IntegerType:
                                            continue
                                        elif type(typ1) is not type(typ2):
                                            raise TypeMismatchInStatement(ast)
                                        
                elif ast.name == "preventDefault":
                    if ast.args:
                        raise TypeMismatchInStatement(ast)
        return param

    def visitVarDecl(self, ast, param):

        for decl in param[0]:
            if type(decl) is list:
                if ast.name == decl[0].name:
                    if decl[1] == True:
                        raise Redeclared(Variable(), ast.name)
                    else:
                        decl[1] = True
            elif type(decl) is not tuple and decl.name == ast.name:
                raise Redeclared(Variable(), ast.name)

        if ast.init is None:
            typ, param = self.visit(ast.typ, param)
            if type(typ) is AutoType:
                raise Invalid(Variable(), ast.name)
            param[0] += [ast]
            return param
        else:
            
            typInit, param = self.visit(ast.init, param)
            typ, param = self.visit(ast.typ, param)
                  
            if type(typ) is type(typInit):
                if type(typ) is ArrayType:
                    if type(typ.typ) is type(typInit.typ) and typ.dimensions == typInit.dimensions:
                        param[0] += [ast]
                        return param
                    else: 
                        raise TypeMismatchInVarDecl(ast) 
                else:
                    param[0] += [ast]
                    return param
            elif type(typ) is AutoType:
                ast.typ = typInit
                param[0] += [ast]
                return param
            elif type(typInit) is AutoType:
                for decls in param:
                    for decl in decls:
                        if type(decl) is list and decl[0].name == ast.init.name:
                            if type(decl[0].return_type) is AutoType:
                                decl[0].return_type = typ
                param[0] += [ast]
                return param
            elif type(typInit) is IntegerType and type(typ) is FloatType:
                param[0] += [ast]
                return param
            else:
                raise TypeMismatchInVarDecl(ast)
            
    def visitParamDecl(self, ast, param):
        for decl in param[0]:
            if type(decl) is not list and type(decl) is not tuple and decl.name == ast.name:
                raise Redeclared(Parameter(), ast.name)
        param[0] += [ast]
        return param
            
    def visitFuncDecl(self, ast, param):
        for decl in param[0]:
            if type(decl) is list:
                if decl[0].name == ast.name:
                    if decl[1] == False:
                        decl[1] = True
                    else:
                        raise Redeclared(Function(), ast.name)
        
        env = [[(ast.name, ast.return_type,'FuncDecl')]] + param
        
        if ast.inherit is not None:
        
            flag1 = False
            for decl in param[0]:
                if type(decl) is list and ast.inherit == decl[0].name:
                    flag1 = True
                    break
            if flag1 == False:
                    raise Undeclared(Function(), ast.inherit)
            for decl in ast.params:
                env = self.visit(decl, env)
                
            for decl in param[0]:
                if type(decl) is list:
                    if ast.inherit == decl[0].name:
                        for para in decl[0].params:
                            if para.inherit == True:
                                for namePara in env[0]:
                                    if type(namePara) is not list and type(namePara) is not tuple and namePara.name == para.name:
                                        raise Invalid(Parameter(), namePara.name)
                                env[0] += [para]
            listBlock = ast.body.body
        
            if not listBlock:
                for decl in param[0]:
                    if type(decl) is list:
                        if ast.inherit == decl[0].name:
                            if decl[0].params:
                                raise InvalidStatementInFunction(ast.name)
            else:
                if type(listBlock[0]) is CallStmt:
                    if listBlock[0].name == "super" or listBlock[0].name == "preventDefault":
                        if listBlock[0].name == "super":
                            if not listBlock[0].args:             
                                for decl in param[0]:
                                    if type(decl) is list:
                                        if ast.inherit == decl[0].name:
                                            if decl[0].params:
                                                raise TypeMismatchInExpression("")
                                            else:
                                                pass
                            else:
                                for decl in param[0]:
                                    if type(decl) is list:
                                        if ast.inherit == decl[0].name:
                                            if len(decl[0].params) != len(listBlock[0].args):
                                                if len(decl[0].params) < len(listBlock[0].args):
                                                    raise TypeMismatchInExpression(listBlock[0].args[len(decl[0].params)])
                                                if len(decl[0].params) > len(listBlock[0].args):
                                                    raise TypeMismatchInExpression("")
                                                raise TypeMismatchInStatement(listBlock[0])
                                            for i in range(0, len(decl[0].params)):
                                                typ1, param = self.visit(decl[0].params[i].typ, param)
                                                typ2, param = self.visit(listBlock[0].args[i], param)
                                                if type(typ1) is AutoType and type(typ2) is not AutoType:
                                                    decl[0].params[i].typ = typ2
                                                elif type(typ1) is not AutoType and type(typ2) is AutoType:
                                                    for items in param:
                                                        for item in items:
                                                            if type(item) is list:
                                                                if listBlock[0].args[i].name == item[0].name:
                                                                    item[0].return_type = typ1
                                                            elif type(item) is tuple:
                                                                if listBlock[0].args[i].name == item[0]:
                                                                    item[1] = typ1
                                                            else:
                                                                if listBlock[0].args[i].name == item.name:
                                                                    item.typ = typ1
                                                                    flag2 = True
                                                                    break
                                                        if flag2:
                                                            break
                                                elif type(typ1) is FloatType and type(typ2) is IntegerType:
                                                    continue
                                                elif type(typ1) is not type(typ2):
                                                    raise TypeMismatchInExpression(listBlock[0].args[i])
                                            
                        elif listBlock[0].name == "preventDefault":
                            if listBlock[0].args:
                                raise TypeMismatchInStatement(listBlock[0])
                else:            
                    for decl in param[0]:
                        if type(decl) is list:
                            if ast.inherit == decl[0].name:
                                if decl[0].params:
                                    raise InvalidStatementInFunction(ast.name)
                                else:
                                    pass       
        else:                   
            for decl in ast.params:
                env = self.visit(decl, env)
        for decl in ast.body.body:
            env = self.visit(decl, env)
        return param

    def visitProgram(self, ast, param):
        
        param = GetENV(ast).visit(ast,param)
        
        for i in range(0, len(param[0])):
            for j in range(i + 1, len(param[0])):
                if type(param[0][i]) is list  and type(param[0][j]) is list:
                    if param[0][i][0].name == param[0][j][0].name:
                        raise Redeclared(Function(), param[0][j][0].name)
        for decl in ast.decls:
            param = self.visit(decl, param)
        flag = False
        for decls in param:
            for decl in decls:
                if type(decl) is list:
                    if decl[0].name == 'main' and decl[0].params == []:
                        if type(decl[0].return_type) is VoidType:
                            flag = True
        if flag == False:
            raise NoEntryPoint()