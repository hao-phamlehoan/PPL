
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils, MType
from StaticError import *
from functools import reduce
import copy


class Member:
    def __init__(self,n,t,isMu=False):
        self.name = n
        self.typ = t
        self.isMu = isMu
    def __str__(self):
        return "Member("+self.name+","+str(self.typ)+","+str(self.kind)+","+str(self.isMu)+")"

class BKClass:
    def __init__(self,n,p,m):
        self.name = n
        self.parent = p
        self.member = m
    def __str__(self):
        return "Class("+self.name+","+(self.parent if type(self.parent) == str else "None" if self.parent is None else self.parent.name)+",["+",".join(str(i) for i in self.member) +"])"

class GetEnv(BaseVisitor,Utils):
    def __init__(self):
        self.globalEnv = []
        
    def visitProgram(self,ast,o):
        o = []
        for decl in ast.decl:
            o += self.visit(decl, o)
        return o
        
    def visitClassDecl(self,ast,o):
        name = ast.classname.name 
        for decl in o:
            if name == decl.name:
                raise Redeclared(Class(), name)
        parent = ast.parentname
        if parent:
            found = False
            for decl in o:
                if parent.name == decl.name:
                    found = True
                    break
            if not found:
                raise Undeclared(Class(), parent)
        env = []
        for mem in ast.memlist:
            env += self.visit(mem, (env, o))
        return [BKClass(name, parent, env)]
        
    def visitMethodDecl(self,ast,o):
        if ast.name.name != 'constructor' and ast.name.name in map(lambda x: x.name, o[0]): 
            raise Redeclared(Method(), ast.name.name)
        typ = self.visit(ast.returnType, o[0])
        params = ast.param 
        local =  []
        paramtyp = []
        for param in params:
            if param.variable.name in local:
                raise Redeclared(Parameter(), param.variable.name)
            local += [param.variable.name]
            paramtyp += [self.visit(param.varType, o)]
        if ast.name.name == 'constructor':
            for mem in o[0]:
                if mem.name == ast.name.name and mem.typ.partype == paramtyp:
                    raise Redeclared(Method(), ast.name.name)
        return [Member(ast.name.name,MType(paramtyp,typ),False)]
    
    def visitAttributeDecl(self,ast,o):
        return [self.visit(ast.decl, o)]
    
    def visitVarDecl(self,ast,o):
        if ast.variable.name in map(lambda x: x.name, o[0]):
            raise Redeclared(Attribute(),ast.variable.name)
        return Member(ast.variable.name,self.visit(ast.varType, o),True)
    
    def visitConstDecl(self,ast,o):
        if ast.constant.name in map(lambda x: x.name, o[0]):
            raise Redeclared(Attribute(),ast.constant.name)
        return Member(ast.constant.name,self.visit(ast.constType, o),False)
    
    def visitIntType(self,ast,o):
        return IntType()
    
    def visitFloatType(self,ast,o):
        return FloatType()
    
    def visitBoolType(self,ast,o):
        return BoolType()
    
    def visitStringType(self,ast,o):
        return StringType()
    
    def visitVoidType(self,ast,o):
        return VoidType()
    
    def visitArrayType(self,ast,o):
        return ArrayType(ast.size, ast.eleType)
    
    def visitClassType(self,ast,o):
        if ast.classname.name in map(lambda x: x.name, o[1]):
            return ClassType(ast.classname)
        raise Undeclared(Class(), ast.classname.name)

class StaticChecker(BaseVisitor,Utils):
    inttype = IntType()
    floattype = FloatType()
    voidtype = VoidType()
    booltype = BoolType()
    stringtype = StringType() 
    def __init__(self,ast):
        self.ast = ast
        self.io = [BKClass("io",None,[
                            Member("@readInt",MType([],StaticChecker.inttype),False),
                            Member("@writeInt",MType([StaticChecker.inttype],StaticChecker.voidtype),False),
                            Member("@readFloat",MType([],StaticChecker.floattype),False),
                            Member("@writeFloat",MType([StaticChecker.floattype],StaticChecker.voidtype),False),
                            Member("@readBool",MType([],StaticChecker.booltype),False),
                            Member("@writeBool",MType([StaticChecker.booltype],StaticChecker.voidtype),False),
                            Member("@readStr",MType([],StaticChecker.stringtype),False),
                            Member("@writeStr",MType([StaticChecker.stringtype],StaticChecker.voidtype),False),
                            ])]
    
    def check(self):
        self.visit(self.ast,self.io)
        return "successful"
    
    def recurVisit(self, field, parent_name, o):
        for classdecl in o[1]:
            if parent_name == classdecl.name:
                for mem in classdecl.member:
                    if field == mem.name:
                        return (mem.typ, 'var' if mem.isMu else 'const')
                if mem.parent:
                    return self.recurVisit(field, mem.parent.name, o)
        return None
        
    def visitProgram(self,ast, o):
        env = GetEnv().visit(ast, None)
        found = False
        for e in env:
            if e.name == 'Program':
                for mem in e.member:
                    if mem.name == '@main' and type(mem.typ) is MType:
                        if mem.typ.partype == [] and type(mem.typ.rettype) is VoidType:
                            found = True
        if not found:
            raise NoEntryPoint()
        
        o += env
        for classdecl in ast.decl:
            self.visit(classdecl, o)
        # return reduce(lambda a,e: self.visit(e,a), ast.decl,o)
        
    def visitClassDecl(self, ast, o):
        for mem in ast.memlist:
            self.visit(mem, (o, ast.classname.name))
        
    def visitAttributeDecl(self,ast,o): 
        local = []
        self.visit(ast.decl, (local, o[0], o[1], None, None))
    
    def visitMethodDecl(self,ast,o):
        paramlist = ast.param 
        local = []
        for param in paramlist:
            local += [(param.variable.name, self.visit(param.varType, o), 'var')]
        self.visit(ast.body, (local, o[0], o[1], ast.returnType, None))  

    def visitVarDecl(self, ast, o):
        name = ast.variable.name
        typ = self.visit(ast.varType, o)
        if o[3]:
            if name in map(lambda x: x[0], o[0][0]):
                Redeclared(Variable(), name)   
        if ast.varInit is not None:
            value = self.visit(ast.varInit, (o[0], o[1], o[2], o[3], o[4]))  
            if type(typ) is not type(value[0]):
                if not(type(typ) is FloatType and type(value[0]) is IntType):
                    raise TypeMismatchInDeclaration(ast)
                if not(type(typ) is ClassType and type(value[0]) is NullLiteral):
                    raise TypeMismatchInDeclaration(ast)
                
            if type(typ) is ClassType:
                if typ.classname.name != value[0].classname.name:
                    raise TypeMismatchInDeclaration(ast)
                if type(typ) is ArrayType:
                    if typ.size != value[0].size:
                        raise TypeMismatchInDeclaration(ast)
                    if type(typ.eleTyp) is not type(value[0].eleTyp):
                        if not(type(typ.eleTyp) is FloatType and type(value[0].eleTyp) is IntType):
                            raise TypeMismatchInDeclaration(ast)
        if o[3]:
            o[0][0] += [(name, typ, 'var')]
    
    def visitConstDecl(self,ast,o):
        name = ast.variable.name
        typ = self.visit(ast.varType, o)
        if o[3]:
            if name in map(lambda x: x[0], o[0][0]):
                Redeclared(Constant(), name)   
        if ast.varInit is not None:
            value = self.visit(ast.varInit, (o[0], o[1], o[2], o[3], o[4]))  
            if type(typ) is not type(value[0]):
                if not(type(typ) is FloatType and type(value[0]) is IntType):
                    raise TypeMismatchInDeclaration(ast)
                if not(type(typ) is ClassType and type(value[0]) is NullLiteral):
                    raise TypeMismatchInDeclaration(ast)
                
            if type(typ) is ClassType:
                if typ.classname.name != value[0].classname.name:
                    raise TypeMismatchInDeclaration(ast)
                if type(typ) is ArrayType:
                    if typ.size != value[0].size:
                        raise TypeMismatchInDeclaration(ast)
                    if type(typ.eleTyp) is not type(value[0].eleTyp):
                        if not(type(typ.eleTyp) is FloatType and type(value[0].eleTyp) is IntType):
                            raise TypeMismatchInDeclaration(ast)
        else:
            raise TypeMismatchInDeclaration(ast)
        if o[3]:
            o[0][0] += [(name, typ, 'const')]
            
    def visitBinaryOp(self,ast,o):
        e1t, kindl = self.visit(ast.left, o)
        e2t, kindr = self.visit(ast.right, o)

        if ast.op in ['+','-','*']:
            if (type(e1t) is IntType or type(e1t) is FloatType) and (type(e2t) is IntType or type(e2t) is FloatType):
                if type(e1t) is FloatType or type(e2t) is FloatType:
                    return (FloatType(), 'const')
                else:
                    return (IntType(), 'const')
            raise TypeMismatchInExpression(ast)
        if ast.op in ['/']:
            if type(e1t) is FloatType and type(e2t) is FloatType:
                return (FloatType(), 'const')
            raise TypeMismatchInExpression(ast)
        if ast.op in ['%', '\\']:
            if type(e1t) is IntType and type(e2t) is IntType:
                return (IntType(), 'const')
            raise TypeMismatchInExpression(ast)
        if ast.op in ['&&', '||']:
            if type(e1t) is BoolType and type(e2t) is BoolType:
                return (BoolType(), 'const')
            raise TypeMismatchInExpression(ast)
        if ast.op in ['^']:
            if type(e1t) is StringType and type(e2t) is StringType:
                return (StringType(), 'const')
            raise TypeMismatchInExpression(ast)
        if ast.op in ['<', '>', '<=', '>=']:
            if (type(e1t) is IntType or type(e1t) is FloatType) and (type(e2t) is IntType or type(e2t) is FloatType):
                return (BoolType(), 'const')
            raise TypeMismatchInExpression(ast)
        if ast.op in ['==', '!=']:
            if (type(e1t) is IntType or type(e1t) is BoolType) and (type(e2t) is IntType or type(e2t) is BoolType):
                return (BoolType(), 'const')
            raise TypeMismatchInExpression(ast)
            
    def visitUnaryOp(self,ast,o):
        body = self.visit(ast.body, o)
        
        if ast.op in ['-']:
            if type(body[0]) is IntType:
                return (IntType(), 'const')
            if type(body[0]) is FloatType:
                return (FloatType(), 'const')
            raise TypeMismatchInExpression(ast)
        if ast.op in ['!']:
            if type(body[0]) is BoolType:
                return (BoolType(), 'const')
            raise TypeMismatchInExpression(ast)
    
    def visitNewExpr(self,ast,o):
        for decl in o[1]:
            if ast.classname.name == decl.name:
                for mem in decl.member:
                    if mem.name == 'constructor':
                        method = mem.typ 
                        paramlist = [self.visit(param, o) for param in ast.param]
                        if len(paramlist) != len(method.partype):
                            raise TypeMismatchInExpression(ast)
                        for i in range(0, len(paramlist)):
                            if type(paramlist[i][0]) is type(method.partype[i][0]):
                                if type(paramlist[i][0]) is ClassType:
                                    if paramlist[i][0].classname.name != method.partype[i][0].classname.name:
                                        raise TypeMismatchInExpression(ast)
                                if type(paramlist[i][0]) is ArrayType:
                                    if paramlist[i][0].size != method.partype[i][0].size:
                                        raise TypeMismatchInExpression(ast)
                                    if type(paramlist[i][0].eleTyp) is not type(method.partype[i][0].eleTyp):
                                        if not(type(paramlist[i][0].eleTyp) is IntType and type(method.partype[i][0].eleTyp) is FloatType):
                                            raise TypeMismatchInExpression(ast)
                            elif not(type(paramlist[i][0]) is IntType and type(method.partype[i][0]) is FloatType):
                                raise TypeMismatchInExpression(ast)
                        return (ClassType(ast.classname), 'const')
                raise TypeMismatchInExpression(ast)
        raise Undeclared(Class(), ast.classname.name)
        
    def visitId(self,ast,o):            
        for i in o[0]:
            for j in i:
                if ast.name ==  j[0]:
                    return (j[1], j[2])
        raise Undeclared(Identifier(), ast.name)
    
    def visitArrayCell(self,ast,o):
        arrType = self.visit(ast.arr, o)
        idxType = self.visit(ast.idx, o)
        if type(idxType[0]) is not IntType or type(arrType[0]) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        return arrType
    
    def visitFieldAccess(self,ast,o):
        obj = self.visit(ast.obj, o)
        name = ''
        if type(obj[0]) is ClassType:
            name = obj.classname.name
        elif type(obj[0]) is SelfLiteral:
            name = o[2]
        else:
            raise TypeMismatchInExpression(ast)
        for decl in o[1]:
            if name == decl.name:
                for mem in decl.member:
                    if mem.name == ast.fieldname.name:
                        return (mem.typ, 'var' if mem.isMu else 'const')
                inheritance = None
                if decl.parent:
                    inheritance = self.recurVisit(ast.fieldname.name, decl.parent.name, o)
                if inheritance:
                    return inheritance
                raise Undeclared(Attribute(), ast.fieldname.name)
        raise Undeclared(Class(), name)
    
    def visitBlock(self,ast,o):
        stmtlist = ast.stmt 
        local = [[]] + o[0]
        for stmt in stmtlist:
            self.visit(stmt, (local, o[1], o[2], o[3], o[4]))
    
    def visitIf(self,ast,o):
        local = o[0]
        if ast.preStmt: 
            local = [[]] + local
            for stmt in ast.preStmt:
                self.visit(stmt, (local, o[1], o[2], o[3], o[4]))
        conType = self.visit(ast.expr, (local, o[1], o[2], o[3], o[4]))
        if type(conType[0]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, (local, o[1], o[2], o[3], o[4]))
        if ast.elseStmt: 
            self.visit(ast.elseStmt, (local, o[1], o[2], o[3], o[4]))
        
    def visitFor(self,ast,o):
        self.visit(ast.initStmt, (o[0], o[1], o[2], o[3], o[4]))
        exprType = self.visit(ast.exprStmt, (o[0], o[1], o[2], o[3], o[4]))
        if type(exprType) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.postStmt, (o[0], o[1], o[2], o[3], o[4]))
        self.visit(ast.loop, (o[0], o[1], o[2], o[3], 'for'))
    
    def visitAssign(self,ast,o):
        lhs = self.visit(ast.lhs, o)
        exp = self.visit(ast.exp, o)
        if lhs[1] == 'const':
            raise CannotAssignToConstant(ast)
        if type(lhs[0]) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(lhs[0]) is not type(exp[0]):
            if not(type(lhs[0]) is FloatType and type(exp[0]) is IntType):
                raise TypeMismatchInStatement(ast)
        elif type(lhs[0]) is ClassType:
            if lhs[0].classname.name != exp[0].classname.name:
                raise TypeMismatchInExpression(ast)
        elif type(lhs[0]) is ArrayType:
            if lhs[0].size != exp[0].size:
                raise TypeMismatchInExpression(ast)
            if type(lhs[0].eleTyp) is not type(exp[0].eleTyp):
                if not(type(lhs[0].eleTyp) is FloatType and type(exp[0].eleTyp) is IntType):
                    raise TypeMismatchInStatement(ast)
    
    def visitCallStmt(self,ast,o):
        methodname = ast.method.name 
        name = ''
        if ast.obj:
            obj = self.visit(ast.obj, o)
            if type(obj[0]) is ClassType:
                name = obj.classname.name
            elif type(obj[0]) is SelfLiteral:
                name = o[2]
            else:
                raise TypeMismatchInStatement(ast)
        else:
            name = o[2]
            
        for decl in o[1]:
            if name == decl.name:
                method = None
                for mem in decl.member:
                    if mem.name == methodname and type(mem.typ) is MType:
                        method = mem.typ 
                inheritance = None
                if decl.parent:
                    inheritance = self.recurVisit(methodname, decl.parent.name, o)
                if inheritance and type(inheritance[0]) is MType:
                    method = inheritance[0]
                else:
                    raise Undeclared(Method(), name)
                if type(method.rettype) is not VoidType:
                    raise TypeMismatchInStatement(ast)
                paramlist = [self.visit(param, o) for param in ast.param]
                if len(paramlist) != len(method.partype):
                    raise TypeMismatchInStatement(ast)
                for i in range(0, len(paramlist)):
                    if type(paramlist[i][0]) is type(method.partype[i][0]):
                        if type(paramlist[i][0]) is ClassType:
                            if paramlist[i][0].classname.name != method.partype[i][0].classname.name:
                                raise TypeMismatchInStatement(ast)
                        if type(paramlist[i][0]) is ArrayType:
                            if paramlist[i][0].size != method.partype[i][0].size:
                                raise TypeMismatchInStatement(ast)
                            if type(paramlist[i][0].eleTyp) is not type(method.partype[i][0].eleTyp):
                                if not(type(paramlist[i][0].eleTyp) is IntType and type(method.partype[i][0].eleTyp) is FloatType):
                                    raise TypeMismatchInStatement(ast)
                    elif not(type(paramlist[i][0]) is IntType and type(method.partype[i][0]) is FloatType):
                        raise TypeMismatchInStatement(ast)
        raise Undeclared(Class(), name)
        
    def visitCallExpr(self,ast,o):
        methodname = ast.method.name 
        name = ''
        if ast.obj:
            obj = self.visit(ast.obj, o)
            if type(obj[0]) is ClassType:
                name = obj.classname.name
            elif type(obj[0]) is SelfLiteral:
                name = o[2]
            else:
                raise TypeMismatchInExpression(ast)
        else:
            name = o[2]
            
        for decl in o[1]:
            if name == decl.name:
                for mem in decl.member:
                    if mem.name == methodname and type(mem.typ) is MType:
                        method = mem.typ 
                inheritance = None
                if decl.parent:
                    inheritance = self.recurVisit(methodname, decl.parent.name, o)
                if inheritance and type(inheritance[0]) is MType:
                    method = inheritance[0]
                else:
                    raise Undeclared(Method(), name)
                if type(method.rettype) is VoidType:
                    raise TypeMismatchInExpression(ast)
                paramlist = [self.visit(param, o) for param in ast.param]
                if len(paramlist) != len(method.partype):
                    raise TypeMismatchInExpression(ast)
                for i in range(0, len(paramlist)):
                    if type(paramlist[i][0]) is type(method.partype[i][0]):
                        if type(paramlist[i][0]) is ClassType:
                            if paramlist[i][0].classname.name != method.partype[i][0].classname.name:
                                raise TypeMismatchInExpression(ast)
                        if type(paramlist[i][0]) is ArrayType:
                            if paramlist[i][0].size != method.partype[i][0].size:
                                raise TypeMismatchInExpression(ast)
                            if type(paramlist[i][0].eleTyp) is not type(method.partype[i][0].eleTyp):
                                if not(type(paramlist[i][0].eleTyp) is IntType and type(method.partype[i][0].eleTyp) is FloatType):
                                    raise TypeMismatchInExpression(ast)
                    elif not(type(paramlist[i][0]) is IntType and type(method.partype[i][0]) is FloatType):
                        raise TypeMismatchInExpression(ast)
                raise Undeclared(Method(), name)
        raise Undeclared(Class(), name)
    
    def visitContinue(self,ast,o):
        if not o[4]:
            raise MustInLoop(ast)
    
    def visitBreak(self,ast,o):
        if not o[4]:
            raise MustInLoop(ast)
    
    def visitReturn(self,ast,o):           
        if ast.expr:
            typeReturn = self.visit(ast.expr, o)
            if type(o[3]) is not type(typeReturn[0]):
                if not (type(o[3]) is FloatType and type(typeReturn[0]) is IntType):
                    return TypeMismatchInStatement(ast)   
            else:
                if type(o[3]) is ClassType:
                    if o[3].classname.name != typeReturn[0].classname.name:
                        raise TypeMismatchInStatement(ast)
                if type(o[3]) is ArrayType:
                    if o[3].size != typeReturn[0].size:
                        raise TypeMismatchInStatement(ast)
                    if type(o[3].eleTyp) is not type(typeReturn[0].eleTyp):
                        if not(type(o[3].eleTyp) is FloatType and type(typeReturn[0].eleTyp) is IntType):
                            raise TypeMismatchInStatement(ast)
        else:
            if type(o[3]) is not VoidType:
                return TypeMismatchInStatement(ast)        
    
    def visitIntLiteral(self,ast,o):
        return (IntType(), 'const')
    
    def visitFloatLiteral(self,ast,o):
        return (FloatType(), 'const')
    
    def visitBooleanLiteral(self,ast,o):
        return (BoolType(), 'const')
    
    def visitStringLiteral(self,ast,o):
        return (StringType(), 'const')
    
    def visitNullLiteral(self,ast,o):
        return (NullLiteral(), 'const')
    
    def visitSelfLiteral(self,ast,o):
        return (SelfLiteral(), 'const')
        
    def visitArrayLiteral(self,ast,o):
        temp = list(map(lambda x: self.visit(x, o), ast.value))
        default = temp[0][0]
        for typeofElement in temp:
            if type(typeofElement[0]) is not type(default):
                raise IllegalArrayLiteral(ast)
        return (ArrayType(len(temp), default), 'const')
    
    def visitIntType(self,ast,o):
        return IntType()
    
    def visitFloatType(self,ast,o):
        return FloatType()
    
    def visitBoolType(self,ast,o):
        return BoolType()
    
    def visitStringType(self,ast,o):
        return StringType()
    
    def visitVoidType(self,ast,o):
        return VoidType()
    
    def visitArrayType(self,ast,o):
        return ArrayType(ast.size, ast.eleType)
    
    def visitClassType(self,ast,o):
        if ast.classname.name in map(lambda x: x.name, o[1]):
            return ClassType(ast.classname)
        raise Undeclared(Class(), ast.classname.name)
    