# Generated from e:/231/PPL/Assignment/Assignment3/initial/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete listener for a parse tree produced by CSlangParser.
class CSlangListener(ParseTreeListener):

    # Enter a parse tree produced by CSlangParser#program.
    def enterProgram(self, ctx:CSlangParser.ProgramContext):
        pass

    # Exit a parse tree produced by CSlangParser#program.
    def exitProgram(self, ctx:CSlangParser.ProgramContext):
        pass


    # Enter a parse tree produced by CSlangParser#classdecl.
    def enterClassdecl(self, ctx:CSlangParser.ClassdeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#classdecl.
    def exitClassdecl(self, ctx:CSlangParser.ClassdeclContext):
        pass


    # Enter a parse tree produced by CSlangParser#memdecl.
    def enterMemdecl(self, ctx:CSlangParser.MemdeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#memdecl.
    def exitMemdecl(self, ctx:CSlangParser.MemdeclContext):
        pass


    # Enter a parse tree produced by CSlangParser#cslangtype.
    def enterCslangtype(self, ctx:CSlangParser.CslangtypeContext):
        pass

    # Exit a parse tree produced by CSlangParser#cslangtype.
    def exitCslangtype(self, ctx:CSlangParser.CslangtypeContext):
        pass



del CSlangParser