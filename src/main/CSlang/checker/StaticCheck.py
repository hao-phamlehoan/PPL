
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
        self.globalEnv = {}
        
    def visitProgram(self,ast,param):
        return None
    
    def visitVarDecl(self,ast,param):
        return None
    
    def visitConstDecl(self,ast,param):
        return None
    
    def visitClassDecl(self,ast,param):
        return None
    
    def visitMethodDecl(self,ast,param):
        return None
    
    def visitAttributeDecl(self,ast,param):
        return None
    
    def visitIntType(self,ast,param):
        return None
    
    def visitFloatType(self,ast,param):
        return None
    
    def visitBoolType(self,ast,param):
        return None
    
    def visitStringType(self,ast,param):
        return None
    
    def visitVoidType(self,ast,param):
        return None
    
    def visitArrayType(self,ast,param):
        return None
    
    def visitClassType(self,ast,param):
        return None
    
    def visitBinaryOp(self,ast,param):
        return None
    
    def visitUnaryOp(self,ast,param):
        return None
    
    def visitCallExpr(self,ast,param):
        return None
    
    def visitNewExpr(self,ast,param):
        return None
    
    def visitId(self,ast,param):
        return None
    
    def visitArrayCell(self,ast,param):
        return None
    
    def visitFieldAccess(self,ast,param):
        return None
    
    def visitBlock(self,ast,param):
        return None
    
    def visitIf(self,ast,param):
        return None
    
    def visitFor(self,ast,param):
        return None
    
    def visitContinue(self,ast,param):
        return None
    
    def visitBreak(self,ast,param):
        return None
    
    def visitReturn(self,ast,param):
        return None
    
    def visitAssign(self,ast,param):
        return None
    
    def visitCallStmt(self,ast,param):
        return None
    
    def visitIntLiteral(self,ast,param):
        return None
    
    def visitFloatLiteral(self,ast,param):
        return None
    
    def visitBooleanLiteral(self,ast,param):
        return None
    
    def visitStringLiteral(self,ast,param):
        return None
    
    def visitNullLiteral(self,ast,param):
        return None
    
    def visitSelfLiteral(self,ast,param):
        return None 
        
    def visitArrayLiteral(self,ast,param):
        return None 

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
                            Member("@writeIntLn",MType([StaticChecker.inttype],StaticChecker.voidtype),False),
                            ])]
    def check(self):
        self.visit(self.ast,self.io)
        return "successful"

    def visitProgram(self,ast, c):
        env = reduce(lambda a,e: self.visit(e,a), ast.decl,c)
        
    def visitClassDecl(self, ast, c):
        if ast.classname.name in map(lambda x: x.name,c):
            raise Redeclared(Class(),ast.classname.name)
        mem = reduce(lambda a,e: self.visit(e,a) ,ast.memlist,[])
        return [BKClass(ast.classname.name,ast.parentname,mem)]+c

    def visitAttributeDecl(self,ast,c):
        field = self.visit(ast.decl,c) 
        return [field]+c

    def visitVarDecl(self, ast, c):
        if ast.variable.name in map(lambda x: x.name,c):
            raise Redeclared(Attribute(),ast.variable.name)
        return Member(ast.variable.name,ast.varType,True)

    def visitProgram(self,ast,param):
        return None
    
    def visitVarDecl(self,ast,param):
        return None
    
    def visitConstDecl(self,ast,param):
        return None
    
    def visitClassDecl(self,ast,param):
        return None
    
    def visitMethodDecl(self,ast,param):
        return None
    
    def visitAttributeDecl(self,ast,param):
        return None
    
    def visitIntType(self,ast,param):
        return None
    
    def visitFloatType(self,ast,param):
        return None
    
    def visitBoolType(self,ast,param):
        return None
    
    def visitStringType(self,ast,param):
        return None
    
    def visitVoidType(self,ast,param):
        return None
    
    def visitArrayType(self,ast,param):
        return None
    
    def visitClassType(self,ast,param):
        return None
    
    def visitBinaryOp(self,ast,param):
        return None
    
    def visitUnaryOp(self,ast,param):
        return None
    
    def visitCallExpr(self,ast,param):
        return None
    
    def visitNewExpr(self,ast,param):
        return None
    
    def visitId(self,ast,param):
        return None
    
    def visitArrayCell(self,ast,param):
        return None
    
    def visitFieldAccess(self,ast,param):
        return None
    
    def visitBlock(self,ast,param):
        return None
    
    def visitIf(self,ast,param):
        return None
    
    def visitFor(self,ast,param):
        return None
    
    def visitContinue(self,ast,param):
        return None
    
    def visitBreak(self,ast,param):
        return None
    
    def visitReturn(self,ast,param):
        return None
    
    def visitAssign(self,ast,param):
        return None
    
    def visitCallStmt(self,ast,param):
        return None
    
    def visitIntLiteral(self,ast,param):
        return None
    
    def visitFloatLiteral(self,ast,param):
        return None
    
    def visitBooleanLiteral(self,ast,param):
        return None
    
    def visitStringLiteral(self,ast,param):
        return None
    
    def visitNullLiteral(self,ast,param):
        return None
    
    def visitSelfLiteral(self,ast,param):
        return None 
        
    def visitArrayLiteral(self,ast,param):
        return None 