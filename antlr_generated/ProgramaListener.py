# Generated from Programa.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ProgramaParser import ProgramaParser
else:
    from ProgramaParser import ProgramaParser

# This class defines a complete listener for a parse tree produced by ProgramaParser.
class ProgramaListener(ParseTreeListener):

    # Enter a parse tree produced by ProgramaParser#programa.
    def enterPrograma(self, ctx:ProgramaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by ProgramaParser#programa.
    def exitPrograma(self, ctx:ProgramaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by ProgramaParser#convidados.
    def enterConvidados(self, ctx:ProgramaParser.ConvidadosContext):
        pass

    # Exit a parse tree produced by ProgramaParser#convidados.
    def exitConvidados(self, ctx:ProgramaParser.ConvidadosContext):
        pass


    # Enter a parse tree produced by ProgramaParser#lista_convidados.
    def enterLista_convidados(self, ctx:ProgramaParser.Lista_convidadosContext):
        pass

    # Exit a parse tree produced by ProgramaParser#lista_convidados.
    def exitLista_convidados(self, ctx:ProgramaParser.Lista_convidadosContext):
        pass


    # Enter a parse tree produced by ProgramaParser#conv.
    def enterConv(self, ctx:ProgramaParser.ConvContext):
        pass

    # Exit a parse tree produced by ProgramaParser#conv.
    def exitConv(self, ctx:ProgramaParser.ConvContext):
        pass


    # Enter a parse tree produced by ProgramaParser#grupo_conv.
    def enterGrupo_conv(self, ctx:ProgramaParser.Grupo_convContext):
        pass

    # Exit a parse tree produced by ProgramaParser#grupo_conv.
    def exitGrupo_conv(self, ctx:ProgramaParser.Grupo_convContext):
        pass


    # Enter a parse tree produced by ProgramaParser#grupo_conv_global.
    def enterGrupo_conv_global(self, ctx:ProgramaParser.Grupo_conv_globalContext):
        pass

    # Exit a parse tree produced by ProgramaParser#grupo_conv_global.
    def exitGrupo_conv_global(self, ctx:ProgramaParser.Grupo_conv_globalContext):
        pass


    # Enter a parse tree produced by ProgramaParser#corpo.
    def enterCorpo(self, ctx:ProgramaParser.CorpoContext):
        pass

    # Exit a parse tree produced by ProgramaParser#corpo.
    def exitCorpo(self, ctx:ProgramaParser.CorpoContext):
        pass


    # Enter a parse tree produced by ProgramaParser#categorias.
    def enterCategorias(self, ctx:ProgramaParser.CategoriasContext):
        pass

    # Exit a parse tree produced by ProgramaParser#categorias.
    def exitCategorias(self, ctx:ProgramaParser.CategoriasContext):
        pass


    # Enter a parse tree produced by ProgramaParser#categoria.
    def enterCategoria(self, ctx:ProgramaParser.CategoriaContext):
        pass

    # Exit a parse tree produced by ProgramaParser#categoria.
    def exitCategoria(self, ctx:ProgramaParser.CategoriaContext):
        pass


    # Enter a parse tree produced by ProgramaParser#categoria_variavel.
    def enterCategoria_variavel(self, ctx:ProgramaParser.Categoria_variavelContext):
        pass

    # Exit a parse tree produced by ProgramaParser#categoria_variavel.
    def exitCategoria_variavel(self, ctx:ProgramaParser.Categoria_variavelContext):
        pass


    # Enter a parse tree produced by ProgramaParser#categoria_fixo.
    def enterCategoria_fixo(self, ctx:ProgramaParser.Categoria_fixoContext):
        pass

    # Exit a parse tree produced by ProgramaParser#categoria_fixo.
    def exitCategoria_fixo(self, ctx:ProgramaParser.Categoria_fixoContext):
        pass


    # Enter a parse tree produced by ProgramaParser#itens_variaveis.
    def enterItens_variaveis(self, ctx:ProgramaParser.Itens_variaveisContext):
        pass

    # Exit a parse tree produced by ProgramaParser#itens_variaveis.
    def exitItens_variaveis(self, ctx:ProgramaParser.Itens_variaveisContext):
        pass


    # Enter a parse tree produced by ProgramaParser#itens_fixos.
    def enterItens_fixos(self, ctx:ProgramaParser.Itens_fixosContext):
        pass

    # Exit a parse tree produced by ProgramaParser#itens_fixos.
    def exitItens_fixos(self, ctx:ProgramaParser.Itens_fixosContext):
        pass


    # Enter a parse tree produced by ProgramaParser#item_variavel.
    def enterItem_variavel(self, ctx:ProgramaParser.Item_variavelContext):
        pass

    # Exit a parse tree produced by ProgramaParser#item_variavel.
    def exitItem_variavel(self, ctx:ProgramaParser.Item_variavelContext):
        pass


    # Enter a parse tree produced by ProgramaParser#item_fixo.
    def enterItem_fixo(self, ctx:ProgramaParser.Item_fixoContext):
        pass

    # Exit a parse tree produced by ProgramaParser#item_fixo.
    def exitItem_fixo(self, ctx:ProgramaParser.Item_fixoContext):
        pass


    # Enter a parse tree produced by ProgramaParser#detalhes_item.
    def enterDetalhes_item(self, ctx:ProgramaParser.Detalhes_itemContext):
        pass

    # Exit a parse tree produced by ProgramaParser#detalhes_item.
    def exitDetalhes_item(self, ctx:ProgramaParser.Detalhes_itemContext):
        pass


    # Enter a parse tree produced by ProgramaParser#detalhe_item.
    def enterDetalhe_item(self, ctx:ProgramaParser.Detalhe_itemContext):
        pass

    # Exit a parse tree produced by ProgramaParser#detalhe_item.
    def exitDetalhe_item(self, ctx:ProgramaParser.Detalhe_itemContext):
        pass


    # Enter a parse tree produced by ProgramaParser#detalhe_item_valorAtomico.
    def enterDetalhe_item_valorAtomico(self, ctx:ProgramaParser.Detalhe_item_valorAtomicoContext):
        pass

    # Exit a parse tree produced by ProgramaParser#detalhe_item_valorAtomico.
    def exitDetalhe_item_valorAtomico(self, ctx:ProgramaParser.Detalhe_item_valorAtomicoContext):
        pass


    # Enter a parse tree produced by ProgramaParser#detalhe_item_valorGrupo.
    def enterDetalhe_item_valorGrupo(self, ctx:ProgramaParser.Detalhe_item_valorGrupoContext):
        pass

    # Exit a parse tree produced by ProgramaParser#detalhe_item_valorGrupo.
    def exitDetalhe_item_valorGrupo(self, ctx:ProgramaParser.Detalhe_item_valorGrupoContext):
        pass


    # Enter a parse tree produced by ProgramaParser#lista_grupo_conv.
    def enterLista_grupo_conv(self, ctx:ProgramaParser.Lista_grupo_convContext):
        pass

    # Exit a parse tree produced by ProgramaParser#lista_grupo_conv.
    def exitLista_grupo_conv(self, ctx:ProgramaParser.Lista_grupo_convContext):
        pass


    # Enter a parse tree produced by ProgramaParser#grupo_valores.
    def enterGrupo_valores(self, ctx:ProgramaParser.Grupo_valoresContext):
        pass

    # Exit a parse tree produced by ProgramaParser#grupo_valores.
    def exitGrupo_valores(self, ctx:ProgramaParser.Grupo_valoresContext):
        pass


    # Enter a parse tree produced by ProgramaParser#grupo_valor.
    def enterGrupo_valor(self, ctx:ProgramaParser.Grupo_valorContext):
        pass

    # Exit a parse tree produced by ProgramaParser#grupo_valor.
    def exitGrupo_valor(self, ctx:ProgramaParser.Grupo_valorContext):
        pass


    # Enter a parse tree produced by ProgramaParser#cobrar_conv.
    def enterCobrar_conv(self, ctx:ProgramaParser.Cobrar_convContext):
        pass

    # Exit a parse tree produced by ProgramaParser#cobrar_conv.
    def exitCobrar_conv(self, ctx:ProgramaParser.Cobrar_convContext):
        pass



del ProgramaParser