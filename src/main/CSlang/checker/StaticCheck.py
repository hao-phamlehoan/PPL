
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
            env += self.visit(mem, env)
        return [BKClass(name,ast.parentname,env)]
        

    def visitMethodDecl(self,ast,o):
            
        if ast.name.name != 'constructor' and ast.name.name in map(lambda x: x.name, o): 
            raise Redeclared(Method(), ast.name.name)
        typ = ast.returnType
        params = ast.param 
        local =  []
        paramtyp = []
        for param in params:
            if param.variable.name in local:
                raise Redeclared(Parameter(), param.variable.name)
            local += [param.variable.name]
            paramtyp += [param.varType]
        if ast.name.name == 'constructor':
            for mem in o:
                if mem.name == ast.name.name and mem.typ.partype == paramtyp:
                    raise Redeclared(Method(), ast.name.name)
        return [Member(ast.name.name,MType(paramtyp,typ),False)]
    
    def visitAttributeDecl(self,ast,o):
        return [self.visit(ast.decl, o)]
    
    def visitVarDecl(self,ast,o):
        if ast.variable.name in map(lambda x: x.name,o):
            raise Redeclared(Attribute(),ast.variable.name)
        return Member(ast.variable.name,ast.varType,True)
    
    def visitConstDecl(self,ast,o):
        if ast.constant.name in map(lambda x: x.name,o):
            raise Redeclared(Attribute(),ast.constant.name)
        return Member(ast.constant.name,ast.constType,False)
    
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
        if ast.classname.name in map(lambda x: x.name, o):
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
            if type(mem) is MethodDecl:
                self.visit(mem, o)
        

    def visitAttributeDecl(self,ast,o): pass
    
    def visitMethodDecl(self,ast,o):
        self.visit(ast.body, (ast.param, o, ast.returnType))  

    def visitVarDecl(self, ast, o):
        return None
        # if ast.variable.name in map(lambda x: x.name,o):
        #     raise Redeclared(Attribute(),ast.variable.name)
        # return Member(ast.variable.name,ast.varType,True)
    
    def visitConstDecl(self,ast,o):
        return None
    
    def visitIntType(self,ast,o):
        return IntType(), o
    
    def visitFloatType(self,ast,o):
        return FloatType(), o
    
    def visitBoolType(self,ast,o):
        return BoolType(), o
    
    def visitStringType(self,ast,o):
        return StringType(), o
    
    def visitVoidType(self,ast,o):
        return VoidType(), o
    
    def visitArrayType(self,ast,o):
        return ArrayType(ast.size, ast.eleType), o
    
    def visitClassType(self,ast,o):
        if ast.classname.name in map(lambda x: x.name, o):
            return ClassType(ast.classname), o
        raise Undeclared(Class(), ast.classname.name)
        
    
    def visitBinaryOp(self,ast,o):
        return None
    
    def visitUnaryOp(self,ast,o):
        return None
    
    def visitCallExpr(self,ast,o):
        return None
    
    def visitNewExpr(self,ast,o):
        return None
    
    def visitId(self,ast,o):
        return None
    
    def visitArrayCell(self,ast,o):
        return None
    
    def visitFieldAccess(self,ast,o):
        return None
    
    def visitBlock(self,ast,o):
        return None
    
    def visitIf(self,ast,o):
        return None
    
    def visitFor(self,ast,o):
        return None
    
    def visitContinue(self,ast,o):
        return None
    
    def visitBreak(self,ast,o):
        return None
    
    def visitReturn(self,ast,o):
        return None
    
    def visitAssign(self,ast,o):
        return None
    
    def visitCallStmt(self,ast,o):
        return None
    
    def visitIntLiteral(self,ast,o):
        return IntType(), o
    
    def visitFloatLiteral(self,ast,o):
        return FloatType(), o
    
    def visitBooleanLiteral(self,ast,o):
        return BoolType(), o
    
    def visitStringLiteral(self,ast,o):
        return StringType(), o
    
    def visitNullLiteral(self,ast,o):
        return NullLiteral(), o
    
    def visitSelfLiteral(self,ast,o):
        return SelfLiteral(), o
        
    def visitArrayLiteral(self,ast,o):
        return None 