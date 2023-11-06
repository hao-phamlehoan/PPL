# Generated from e:/231/PPL/Assignment/Assignment3/initial/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,1,1,1,1,5,1,20,8,1,10,1,12,1,23,9,1,1,1,1,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,1,1,0,7,8,32,
        0,9,1,0,0,0,2,15,1,0,0,0,4,26,1,0,0,0,6,32,1,0,0,0,8,10,3,2,1,0,
        9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,13,1,0,0,
        0,13,14,5,0,0,1,14,1,1,0,0,0,15,16,5,1,0,0,16,17,5,9,0,0,17,21,5,
        2,0,0,18,20,3,4,2,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,
        22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,3,0,0,25,3,1,0,0,
        0,26,27,5,4,0,0,27,28,5,9,0,0,28,29,5,5,0,0,29,30,3,6,3,0,30,31,
        5,6,0,0,31,5,1,0,0,0,32,33,7,0,0,0,33,7,1,0,0,0,2,11,21
    ]

class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'{'", "'}'", "'var'", "':'", 
                     "';'", "'int'", "'void'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INTTYPE", 
                      "VOIDTYPE", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_memdecl = 2
    RULE_cslangtype = 3

    ruleNames =  [ "program", "classdecl", "memdecl", "cslangtype" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    INTTYPE=7
    VOIDTYPE=8
    ID=9
    WS=10
    ERROR_CHAR=11
    UNCLOSE_STRING=12
    ILLEGAL_ESCAPE=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def classdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ClassdeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ClassdeclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.classdecl()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 13
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def memdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.MemdeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.MemdeclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_classdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassdecl" ):
                listener.enterClassdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassdecl" ):
                listener.exitClassdecl(self)




    def classdecl(self):

        localctx = CSlangParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(CSlangParser.T__0)
            self.state = 16
            self.match(CSlangParser.ID)
            self.state = 17
            self.match(CSlangParser.T__1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 18
                self.memdecl()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(CSlangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def cslangtype(self):
            return self.getTypedRuleContext(CSlangParser.CslangtypeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_memdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemdecl" ):
                listener.enterMemdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemdecl" ):
                listener.exitMemdecl(self)




    def memdecl(self):

        localctx = CSlangParser.MemdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(CSlangParser.T__3)
            self.state = 27
            self.match(CSlangParser.ID)
            self.state = 28
            self.match(CSlangParser.T__4)
            self.state = 29
            self.cslangtype()
            self.state = 30
            self.match(CSlangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CslangtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(CSlangParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(CSlangParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_cslangtype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCslangtype" ):
                listener.enterCslangtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCslangtype" ):
                listener.exitCslangtype(self)




    def cslangtype(self):

        localctx = CSlangParser.CslangtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cslangtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





