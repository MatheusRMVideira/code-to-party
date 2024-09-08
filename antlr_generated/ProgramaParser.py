# Generated from Programa.g4 by ANTLR 4.13.2
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
        4,1,15,149,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,4,2,56,
        8,2,11,2,12,2,57,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,74,8,6,1,7,4,7,77,8,7,11,7,12,7,78,1,8,1,8,3,8,83,8,
        8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,
        4,11,99,8,11,11,11,12,11,100,1,12,4,12,104,8,12,11,12,12,12,105,
        1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,4,15,119,
        8,15,11,15,12,15,120,1,16,1,16,1,16,1,16,1,17,1,17,1,17,3,17,130,
        8,17,1,18,1,18,1,18,1,18,1,19,4,19,137,8,19,11,19,12,19,138,1,20,
        1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,0,0,22,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,1,2,0,12,12,14,14,136,
        0,44,1,0,0,0,2,48,1,0,0,0,4,55,1,0,0,0,6,59,1,0,0,0,8,63,1,0,0,0,
        10,65,1,0,0,0,12,73,1,0,0,0,14,76,1,0,0,0,16,82,1,0,0,0,18,84,1,
        0,0,0,20,91,1,0,0,0,22,98,1,0,0,0,24,103,1,0,0,0,26,107,1,0,0,0,
        28,113,1,0,0,0,30,118,1,0,0,0,32,122,1,0,0,0,34,129,1,0,0,0,36,131,
        1,0,0,0,38,136,1,0,0,0,40,140,1,0,0,0,42,144,1,0,0,0,44,45,3,2,1,
        0,45,46,3,12,6,0,46,47,5,0,0,1,47,1,1,0,0,0,48,49,5,1,0,0,49,50,
        5,2,0,0,50,51,5,8,0,0,51,52,3,4,2,0,52,53,5,9,0,0,53,3,1,0,0,0,54,
        56,3,6,3,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,
        0,58,5,1,0,0,0,59,60,5,12,0,0,60,61,5,2,0,0,61,62,3,8,4,0,62,7,1,
        0,0,0,63,64,5,12,0,0,64,9,1,0,0,0,65,66,7,0,0,0,66,11,1,0,0,0,67,
        68,3,14,7,0,68,69,3,42,21,0,69,74,1,0,0,0,70,71,3,42,21,0,71,72,
        3,14,7,0,72,74,1,0,0,0,73,67,1,0,0,0,73,70,1,0,0,0,74,13,1,0,0,0,
        75,77,3,16,8,0,76,75,1,0,0,0,77,78,1,0,0,0,78,76,1,0,0,0,78,79,1,
        0,0,0,79,15,1,0,0,0,80,83,3,18,9,0,81,83,3,20,10,0,82,80,1,0,0,0,
        82,81,1,0,0,0,83,17,1,0,0,0,84,85,5,3,0,0,85,86,5,12,0,0,86,87,5,
        2,0,0,87,88,5,8,0,0,88,89,3,22,11,0,89,90,5,9,0,0,90,19,1,0,0,0,
        91,92,5,4,0,0,92,93,5,2,0,0,93,94,5,8,0,0,94,95,3,24,12,0,95,96,
        5,9,0,0,96,21,1,0,0,0,97,99,3,26,13,0,98,97,1,0,0,0,99,100,1,0,0,
        0,100,98,1,0,0,0,100,101,1,0,0,0,101,23,1,0,0,0,102,104,3,28,14,
        0,103,102,1,0,0,0,104,105,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,
        0,106,25,1,0,0,0,107,108,5,12,0,0,108,109,5,2,0,0,109,110,5,8,0,
        0,110,111,3,30,15,0,111,112,5,9,0,0,112,27,1,0,0,0,113,114,5,12,
        0,0,114,115,5,2,0,0,115,116,5,10,0,0,116,29,1,0,0,0,117,119,3,32,
        16,0,118,117,1,0,0,0,119,120,1,0,0,0,120,118,1,0,0,0,120,121,1,0,
        0,0,121,31,1,0,0,0,122,123,5,7,0,0,123,124,5,2,0,0,124,125,3,34,
        17,0,125,33,1,0,0,0,126,130,5,12,0,0,127,130,5,10,0,0,128,130,3,
        36,18,0,129,126,1,0,0,0,129,127,1,0,0,0,129,128,1,0,0,0,130,35,1,
        0,0,0,131,132,5,8,0,0,132,133,3,38,19,0,133,134,5,9,0,0,134,37,1,
        0,0,0,135,137,3,40,20,0,136,135,1,0,0,0,137,138,1,0,0,0,138,136,
        1,0,0,0,138,139,1,0,0,0,139,39,1,0,0,0,140,141,3,10,5,0,141,142,
        5,2,0,0,142,143,5,10,0,0,143,41,1,0,0,0,144,145,5,5,0,0,145,146,
        5,2,0,0,146,147,3,36,18,0,147,43,1,0,0,0,9,57,73,78,82,100,105,120,
        129,138
    ]

class ProgramaParser ( Parser ):

    grammarFileName = "Programa.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'convidados'", "':'", "'categoria'", 
                     "'fixo'", "'cobrar_convidados'", "<INVALID>", "<INVALID>", 
                     "'{'", "'}'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "PALAVRAS_CHAVE", "PALAVRAS_CHAVE_ITEM", 
                      "ABRE_CHAVE", "FECHA_CHAVE", "NUM_REAL", "WS", "IDENTIFICADOR", 
                      "COMENTARIO", "SELETOR_GLOBAL", "Caracter_invalido" ]

    RULE_programa = 0
    RULE_convidados = 1
    RULE_lista_convidados = 2
    RULE_conv = 3
    RULE_grupo_conv = 4
    RULE_grupo_conv_global = 5
    RULE_corpo = 6
    RULE_categorias = 7
    RULE_categoria = 8
    RULE_categoria_variavel = 9
    RULE_categoria_fixo = 10
    RULE_itens_variaveis = 11
    RULE_itens_fixos = 12
    RULE_item_variavel = 13
    RULE_item_fixo = 14
    RULE_detalhes_item = 15
    RULE_detalhe_item = 16
    RULE_detalhe_item_valor = 17
    RULE_lista_grupo_conv = 18
    RULE_grupo_valores = 19
    RULE_grupo_valor = 20
    RULE_cobrar_conv = 21

    ruleNames =  [ "programa", "convidados", "lista_convidados", "conv", 
                   "grupo_conv", "grupo_conv_global", "corpo", "categorias", 
                   "categoria", "categoria_variavel", "categoria_fixo", 
                   "itens_variaveis", "itens_fixos", "item_variavel", "item_fixo", 
                   "detalhes_item", "detalhe_item", "detalhe_item_valor", 
                   "lista_grupo_conv", "grupo_valores", "grupo_valor", "cobrar_conv" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    PALAVRAS_CHAVE=6
    PALAVRAS_CHAVE_ITEM=7
    ABRE_CHAVE=8
    FECHA_CHAVE=9
    NUM_REAL=10
    WS=11
    IDENTIFICADOR=12
    COMENTARIO=13
    SELETOR_GLOBAL=14
    Caracter_invalido=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def convidados(self):
            return self.getTypedRuleContext(ProgramaParser.ConvidadosContext,0)


        def corpo(self):
            return self.getTypedRuleContext(ProgramaParser.CorpoContext,0)


        def EOF(self):
            return self.getToken(ProgramaParser.EOF, 0)

        def getRuleIndex(self):
            return ProgramaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = ProgramaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.convidados()
            self.state = 45
            self.corpo()
            self.state = 46
            self.match(ProgramaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConvidadosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRE_CHAVE(self):
            return self.getToken(ProgramaParser.ABRE_CHAVE, 0)

        def lista_convidados(self):
            return self.getTypedRuleContext(ProgramaParser.Lista_convidadosContext,0)


        def FECHA_CHAVE(self):
            return self.getToken(ProgramaParser.FECHA_CHAVE, 0)

        def getRuleIndex(self):
            return ProgramaParser.RULE_convidados

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConvidados" ):
                listener.enterConvidados(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConvidados" ):
                listener.exitConvidados(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConvidados" ):
                return visitor.visitConvidados(self)
            else:
                return visitor.visitChildren(self)




    def convidados(self):

        localctx = ProgramaParser.ConvidadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_convidados)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ProgramaParser.T__0)
            self.state = 49
            self.match(ProgramaParser.T__1)
            self.state = 50
            self.match(ProgramaParser.ABRE_CHAVE)
            self.state = 51
            self.lista_convidados()
            self.state = 52
            self.match(ProgramaParser.FECHA_CHAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_convidadosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conv(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramaParser.ConvContext)
            else:
                return self.getTypedRuleContext(ProgramaParser.ConvContext,i)


        def getRuleIndex(self):
            return ProgramaParser.RULE_lista_convidados

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_convidados" ):
                listener.enterLista_convidados(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_convidados" ):
                listener.exitLista_convidados(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_convidados" ):
                return visitor.visitLista_convidados(self)
            else:
                return visitor.visitChildren(self)




    def lista_convidados(self):

        localctx = ProgramaParser.Lista_convidadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_lista_convidados)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self.conv()
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==12):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConvContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(ProgramaParser.IDENTIFICADOR, 0)

        def grupo_conv(self):
            return self.getTypedRuleContext(ProgramaParser.Grupo_convContext,0)


        def getRuleIndex(self):
            return ProgramaParser.RULE_conv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConv" ):
                listener.enterConv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConv" ):
                listener.exitConv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConv" ):
                return visitor.visitConv(self)
            else:
                return visitor.visitChildren(self)




    def conv(self):

        localctx = ProgramaParser.ConvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_conv)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(ProgramaParser.IDENTIFICADOR)
            self.state = 60
            self.match(ProgramaParser.T__1)
            self.state = 61
            self.grupo_conv()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Grupo_convContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(ProgramaParser.IDENTIFICADOR, 0)

        def getRuleIndex(self):
            return ProgramaParser.RULE_grupo_conv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrupo_conv" ):
                listener.enterGrupo_conv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrupo_conv" ):
                listener.exitGrupo_conv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrupo_conv" ):
                return visitor.visitGrupo_conv(self)
            else:
                return visitor.visitChildren(self)




    def grupo_conv(self):

        localctx = ProgramaParser.Grupo_convContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_grupo_conv)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(ProgramaParser.IDENTIFICADOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Grupo_conv_globalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(ProgramaParser.IDENTIFICADOR, 0)

        def SELETOR_GLOBAL(self):
            return self.getToken(ProgramaParser.SELETOR_GLOBAL, 0)

        def getRuleIndex(self):
            return ProgramaParser.RULE_grupo_conv_global

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrupo_conv_global" ):
                listener.enterGrupo_conv_global(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrupo_conv_global" ):
                listener.exitGrupo_conv_global(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrupo_conv_global" ):
                return visitor.visitGrupo_conv_global(self)
            else:
                return visitor.visitChildren(self)




    def grupo_conv_global(self):

        localctx = ProgramaParser.Grupo_conv_globalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_grupo_conv_global)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not(_la==12 or _la==14):
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


    class CorpoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def categorias(self):
            return self.getTypedRuleContext(ProgramaParser.CategoriasContext,0)


        def cobrar_conv(self):
            return self.getTypedRuleContext(ProgramaParser.Cobrar_convContext,0)


        def getRuleIndex(self):
            return ProgramaParser.RULE_corpo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCorpo" ):
                listener.enterCorpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCorpo" ):
                listener.exitCorpo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCorpo" ):
                return visitor.visitCorpo(self)
            else:
                return visitor.visitChildren(self)




    def corpo(self):

        localctx = ProgramaParser.CorpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_corpo)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.categorias()
                self.state = 68
                self.cobrar_conv()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.cobrar_conv()
                self.state = 71
                self.categorias()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CategoriasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def categoria(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramaParser.CategoriaContext)
            else:
                return self.getTypedRuleContext(ProgramaParser.CategoriaContext,i)


        def getRuleIndex(self):
            return ProgramaParser.RULE_categorias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCategorias" ):
                listener.enterCategorias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCategorias" ):
                listener.exitCategorias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCategorias" ):
                return visitor.visitCategorias(self)
            else:
                return visitor.visitChildren(self)




    def categorias(self):

        localctx = ProgramaParser.CategoriasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_categorias)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 75
                self.categoria()
                self.state = 78 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CategoriaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def categoria_variavel(self):
            return self.getTypedRuleContext(ProgramaParser.Categoria_variavelContext,0)


        def categoria_fixo(self):
            return self.getTypedRuleContext(ProgramaParser.Categoria_fixoContext,0)


        def getRuleIndex(self):
            return ProgramaParser.RULE_categoria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCategoria" ):
                listener.enterCategoria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCategoria" ):
                listener.exitCategoria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCategoria" ):
                return visitor.visitCategoria(self)
            else:
                return visitor.visitChildren(self)




    def categoria(self):

        localctx = ProgramaParser.CategoriaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_categoria)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.categoria_variavel()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.categoria_fixo()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Categoria_variavelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(ProgramaParser.IDENTIFICADOR, 0)

        def ABRE_CHAVE(self):
            return self.getToken(ProgramaParser.ABRE_CHAVE, 0)

        def itens_variaveis(self):
            return self.getTypedRuleContext(ProgramaParser.Itens_variaveisContext,0)


        def FECHA_CHAVE(self):
            return self.getToken(ProgramaParser.FECHA_CHAVE, 0)

        def getRuleIndex(self):
            return ProgramaParser.RULE_categoria_variavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCategoria_variavel" ):
                listener.enterCategoria_variavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCategoria_variavel" ):
                listener.exitCategoria_variavel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCategoria_variavel" ):
                return visitor.visitCategoria_variavel(self)
            else:
                return visitor.visitChildren(self)




    def categoria_variavel(self):

        localctx = ProgramaParser.Categoria_variavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_categoria_variavel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(ProgramaParser.T__2)
            self.state = 85
            self.match(ProgramaParser.IDENTIFICADOR)
            self.state = 86
            self.match(ProgramaParser.T__1)
            self.state = 87
            self.match(ProgramaParser.ABRE_CHAVE)
            self.state = 88
            self.itens_variaveis()
            self.state = 89
            self.match(ProgramaParser.FECHA_CHAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Categoria_fixoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRE_CHAVE(self):
            return self.getToken(ProgramaParser.ABRE_CHAVE, 0)

        def itens_fixos(self):
            return self.getTypedRuleContext(ProgramaParser.Itens_fixosContext,0)


        def FECHA_CHAVE(self):
            return self.getToken(ProgramaParser.FECHA_CHAVE, 0)

        def getRuleIndex(self):
            return ProgramaParser.RULE_categoria_fixo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCategoria_fixo" ):
                listener.enterCategoria_fixo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCategoria_fixo" ):
                listener.exitCategoria_fixo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCategoria_fixo" ):
                return visitor.visitCategoria_fixo(self)
            else:
                return visitor.visitChildren(self)




    def categoria_fixo(self):

        localctx = ProgramaParser.Categoria_fixoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_categoria_fixo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(ProgramaParser.T__3)
            self.state = 92
            self.match(ProgramaParser.T__1)
            self.state = 93
            self.match(ProgramaParser.ABRE_CHAVE)
            self.state = 94
            self.itens_fixos()
            self.state = 95
            self.match(ProgramaParser.FECHA_CHAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Itens_variaveisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item_variavel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramaParser.Item_variavelContext)
            else:
                return self.getTypedRuleContext(ProgramaParser.Item_variavelContext,i)


        def getRuleIndex(self):
            return ProgramaParser.RULE_itens_variaveis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItens_variaveis" ):
                listener.enterItens_variaveis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItens_variaveis" ):
                listener.exitItens_variaveis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItens_variaveis" ):
                return visitor.visitItens_variaveis(self)
            else:
                return visitor.visitChildren(self)




    def itens_variaveis(self):

        localctx = ProgramaParser.Itens_variaveisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_itens_variaveis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 97
                self.item_variavel()
                self.state = 100 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==12):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Itens_fixosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item_fixo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramaParser.Item_fixoContext)
            else:
                return self.getTypedRuleContext(ProgramaParser.Item_fixoContext,i)


        def getRuleIndex(self):
            return ProgramaParser.RULE_itens_fixos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItens_fixos" ):
                listener.enterItens_fixos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItens_fixos" ):
                listener.exitItens_fixos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItens_fixos" ):
                return visitor.visitItens_fixos(self)
            else:
                return visitor.visitChildren(self)




    def itens_fixos(self):

        localctx = ProgramaParser.Itens_fixosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_itens_fixos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.item_fixo()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==12):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Item_variavelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(ProgramaParser.IDENTIFICADOR, 0)

        def ABRE_CHAVE(self):
            return self.getToken(ProgramaParser.ABRE_CHAVE, 0)

        def detalhes_item(self):
            return self.getTypedRuleContext(ProgramaParser.Detalhes_itemContext,0)


        def FECHA_CHAVE(self):
            return self.getToken(ProgramaParser.FECHA_CHAVE, 0)

        def getRuleIndex(self):
            return ProgramaParser.RULE_item_variavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem_variavel" ):
                listener.enterItem_variavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem_variavel" ):
                listener.exitItem_variavel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem_variavel" ):
                return visitor.visitItem_variavel(self)
            else:
                return visitor.visitChildren(self)




    def item_variavel(self):

        localctx = ProgramaParser.Item_variavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_item_variavel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(ProgramaParser.IDENTIFICADOR)
            self.state = 108
            self.match(ProgramaParser.T__1)
            self.state = 109
            self.match(ProgramaParser.ABRE_CHAVE)
            self.state = 110
            self.detalhes_item()
            self.state = 111
            self.match(ProgramaParser.FECHA_CHAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Item_fixoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(ProgramaParser.IDENTIFICADOR, 0)

        def NUM_REAL(self):
            return self.getToken(ProgramaParser.NUM_REAL, 0)

        def getRuleIndex(self):
            return ProgramaParser.RULE_item_fixo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem_fixo" ):
                listener.enterItem_fixo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem_fixo" ):
                listener.exitItem_fixo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem_fixo" ):
                return visitor.visitItem_fixo(self)
            else:
                return visitor.visitChildren(self)




    def item_fixo(self):

        localctx = ProgramaParser.Item_fixoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_item_fixo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(ProgramaParser.IDENTIFICADOR)
            self.state = 114
            self.match(ProgramaParser.T__1)
            self.state = 115
            self.match(ProgramaParser.NUM_REAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Detalhes_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def detalhe_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramaParser.Detalhe_itemContext)
            else:
                return self.getTypedRuleContext(ProgramaParser.Detalhe_itemContext,i)


        def getRuleIndex(self):
            return ProgramaParser.RULE_detalhes_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetalhes_item" ):
                listener.enterDetalhes_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetalhes_item" ):
                listener.exitDetalhes_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetalhes_item" ):
                return visitor.visitDetalhes_item(self)
            else:
                return visitor.visitChildren(self)




    def detalhes_item(self):

        localctx = ProgramaParser.Detalhes_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_detalhes_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 117
                self.detalhe_item()
                self.state = 120 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Detalhe_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PALAVRAS_CHAVE_ITEM(self):
            return self.getToken(ProgramaParser.PALAVRAS_CHAVE_ITEM, 0)

        def detalhe_item_valor(self):
            return self.getTypedRuleContext(ProgramaParser.Detalhe_item_valorContext,0)


        def getRuleIndex(self):
            return ProgramaParser.RULE_detalhe_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetalhe_item" ):
                listener.enterDetalhe_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetalhe_item" ):
                listener.exitDetalhe_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetalhe_item" ):
                return visitor.visitDetalhe_item(self)
            else:
                return visitor.visitChildren(self)




    def detalhe_item(self):

        localctx = ProgramaParser.Detalhe_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_detalhe_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ProgramaParser.PALAVRAS_CHAVE_ITEM)
            self.state = 123
            self.match(ProgramaParser.T__1)
            self.state = 124
            self.detalhe_item_valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Detalhe_item_valorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProgramaParser.RULE_detalhe_item_valor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Detalhe_item_valorAtomicoContext(Detalhe_item_valorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProgramaParser.Detalhe_item_valorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFICADOR(self):
            return self.getToken(ProgramaParser.IDENTIFICADOR, 0)
        def NUM_REAL(self):
            return self.getToken(ProgramaParser.NUM_REAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetalhe_item_valorAtomico" ):
                listener.enterDetalhe_item_valorAtomico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetalhe_item_valorAtomico" ):
                listener.exitDetalhe_item_valorAtomico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetalhe_item_valorAtomico" ):
                return visitor.visitDetalhe_item_valorAtomico(self)
            else:
                return visitor.visitChildren(self)


    class Detalhe_item_valorGrupoContext(Detalhe_item_valorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProgramaParser.Detalhe_item_valorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lista_grupo_conv(self):
            return self.getTypedRuleContext(ProgramaParser.Lista_grupo_convContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetalhe_item_valorGrupo" ):
                listener.enterDetalhe_item_valorGrupo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetalhe_item_valorGrupo" ):
                listener.exitDetalhe_item_valorGrupo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetalhe_item_valorGrupo" ):
                return visitor.visitDetalhe_item_valorGrupo(self)
            else:
                return visitor.visitChildren(self)



    def detalhe_item_valor(self):

        localctx = ProgramaParser.Detalhe_item_valorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_detalhe_item_valor)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = ProgramaParser.Detalhe_item_valorAtomicoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(ProgramaParser.IDENTIFICADOR)
                pass
            elif token in [10]:
                localctx = ProgramaParser.Detalhe_item_valorAtomicoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(ProgramaParser.NUM_REAL)
                pass
            elif token in [8]:
                localctx = ProgramaParser.Detalhe_item_valorGrupoContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.lista_grupo_conv()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_grupo_convContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRE_CHAVE(self):
            return self.getToken(ProgramaParser.ABRE_CHAVE, 0)

        def grupo_valores(self):
            return self.getTypedRuleContext(ProgramaParser.Grupo_valoresContext,0)


        def FECHA_CHAVE(self):
            return self.getToken(ProgramaParser.FECHA_CHAVE, 0)

        def getRuleIndex(self):
            return ProgramaParser.RULE_lista_grupo_conv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_grupo_conv" ):
                listener.enterLista_grupo_conv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_grupo_conv" ):
                listener.exitLista_grupo_conv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_grupo_conv" ):
                return visitor.visitLista_grupo_conv(self)
            else:
                return visitor.visitChildren(self)




    def lista_grupo_conv(self):

        localctx = ProgramaParser.Lista_grupo_convContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lista_grupo_conv)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(ProgramaParser.ABRE_CHAVE)
            self.state = 132
            self.grupo_valores()
            self.state = 133
            self.match(ProgramaParser.FECHA_CHAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Grupo_valoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def grupo_valor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramaParser.Grupo_valorContext)
            else:
                return self.getTypedRuleContext(ProgramaParser.Grupo_valorContext,i)


        def getRuleIndex(self):
            return ProgramaParser.RULE_grupo_valores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrupo_valores" ):
                listener.enterGrupo_valores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrupo_valores" ):
                listener.exitGrupo_valores(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrupo_valores" ):
                return visitor.visitGrupo_valores(self)
            else:
                return visitor.visitChildren(self)




    def grupo_valores(self):

        localctx = ProgramaParser.Grupo_valoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_grupo_valores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 135
                self.grupo_valor()
                self.state = 138 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==12 or _la==14):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Grupo_valorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def grupo_conv_global(self):
            return self.getTypedRuleContext(ProgramaParser.Grupo_conv_globalContext,0)


        def NUM_REAL(self):
            return self.getToken(ProgramaParser.NUM_REAL, 0)

        def getRuleIndex(self):
            return ProgramaParser.RULE_grupo_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrupo_valor" ):
                listener.enterGrupo_valor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrupo_valor" ):
                listener.exitGrupo_valor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrupo_valor" ):
                return visitor.visitGrupo_valor(self)
            else:
                return visitor.visitChildren(self)




    def grupo_valor(self):

        localctx = ProgramaParser.Grupo_valorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_grupo_valor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.grupo_conv_global()
            self.state = 141
            self.match(ProgramaParser.T__1)
            self.state = 142
            self.match(ProgramaParser.NUM_REAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cobrar_convContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_grupo_conv(self):
            return self.getTypedRuleContext(ProgramaParser.Lista_grupo_convContext,0)


        def getRuleIndex(self):
            return ProgramaParser.RULE_cobrar_conv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCobrar_conv" ):
                listener.enterCobrar_conv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCobrar_conv" ):
                listener.exitCobrar_conv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCobrar_conv" ):
                return visitor.visitCobrar_conv(self)
            else:
                return visitor.visitChildren(self)




    def cobrar_conv(self):

        localctx = ProgramaParser.Cobrar_convContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_cobrar_conv)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ProgramaParser.T__4)
            self.state = 145
            self.match(ProgramaParser.T__1)
            self.state = 146
            self.lista_grupo_conv()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





