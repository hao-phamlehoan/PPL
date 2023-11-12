class GetEnv(Visitor):
    def visitProgram(self,ctx:Program,o:object): 
        o = []
        for decl in ctx.decl:
            o = self.visit(decl, o)
        return o

    def visitClassDecl(self,ctx:ClassDecl,o:object):
        env = []
        for mem in ctx.mem: 
            env = self.visit(mem, env)
        if ctx.parent != '':     
            for mem in o:
                if ctx.parent == mem[0]:
                    return o + [(ctx.name, ctx.parent, env)]
            raise UndeclaredClass(ctx.parent)
        return o + [(ctx.name, ctx.parent, env)]

    def visitVarDecl(self,ctx:VarDecl,o:object):
        for decl in o:
            if decl.name == ctx.name:
                raise RedeclaredField(ctx.name)
        return o + [ctx]

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        for decl in o:
            if decl.name == ctx.name:
                raise RedeclaredMethod(ctx.name)
        return o + [ctx]

class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        o = GetEnv().visit(ctx, o)
        for classdecl in ctx.decl:
            self.visit(classdecl, o)

    def visitClassDecl(self,ctx:ClassDecl,o:object):
        for mem in ctx.mem:
            if type(mem) is FuncDecl:
                self.visit(mem, o)

    def visitVarDecl(self,ctx:VarDecl,o:object): pass

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        local = ctx.param + ctx.body[0]
        for expr in ctx.body[1]:
            self.visit(expr, (local, o))

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitClassType(self,ctx:ClassType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        for decl in o[0]:
            if decl.name == ctx.name:
                return decl.typ
        raise UndeclaredIdentifier(ctx.name)
        
    #exp: expr, field: str
    def visitFieldAccess(self,ctx:FieldAccess,o:object): 
        typ = self.visit(ctx.exp, o)#m.a -> classtypea in x
        if type(typ) is ClassType:
            #look up in o[1] if there are class x and fieald a in x
            type_info = None
            found = False
            for classdecl in o[1]:
                if typ.name == classdecl[0]:
                    type_info = classdecl
                    found = True
                    break
            # not exists raise exception 
            if not found: raise UndeclaredClass(typ.name)
            for mem in type_info[2]:
                if ctx.field == mem.name:
                    return mem.typ
                if type_info[1] != '':
                    reVisit = self.recurVisit(ctx, type_info[1], o)
                    if reVisit:
                        return reVisit.typ
            raise UndeclaredField(ctx.field)
        
    def recurVisit(self, ctx, parent_name, o: object):
        type_info = None
        found = False
        for classdecl in o[1]:
            if parent_name == classdecl[0]:
                type_info = classdecl
                found = True
                break
        if not found: raise UndeclaredClass(parent_name)
        for mem in type_info[2]:
            if ctx.field == mem.name:
                return mem
            if type_info[1] != '':
                return self.recurVisit(ctx, type_info[1], o)
            else:
                return None
