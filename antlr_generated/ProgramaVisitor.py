# Generated from Programa.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ProgramaParser import ProgramaParser
else:
    from ProgramaParser import ProgramaParser

# This class defines a complete generic visitor for a parse tree produced by ProgramaParser.

class ProgramaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ProgramaParser#programa.
    def visitPrograma(self, ctx:ProgramaParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#convidados.
    def visitConvidados(self, ctx:ProgramaParser.ConvidadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#lista_convidados.
    def visitLista_convidados(self, ctx:ProgramaParser.Lista_convidadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#conv.
    def visitConv(self, ctx:ProgramaParser.ConvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#grupo_conv.
    def visitGrupo_conv(self, ctx:ProgramaParser.Grupo_convContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#grupo_conv_global.
    def visitGrupo_conv_global(self, ctx:ProgramaParser.Grupo_conv_globalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#corpo.
    def visitCorpo(self, ctx:ProgramaParser.CorpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#categorias.
    def visitCategorias(self, ctx:ProgramaParser.CategoriasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#categoria.
    def visitCategoria(self, ctx:ProgramaParser.CategoriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#categoria_variavel.
    def visitCategoria_variavel(self, ctx:ProgramaParser.Categoria_variavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#categoria_fixo.
    def visitCategoria_fixo(self, ctx:ProgramaParser.Categoria_fixoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#itens_variaveis.
    def visitItens_variaveis(self, ctx:ProgramaParser.Itens_variaveisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#itens_fixos.
    def visitItens_fixos(self, ctx:ProgramaParser.Itens_fixosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#item_variavel.
    def visitItem_variavel(self, ctx:ProgramaParser.Item_variavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#item_fixo.
    def visitItem_fixo(self, ctx:ProgramaParser.Item_fixoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#detalhes_item.
    def visitDetalhes_item(self, ctx:ProgramaParser.Detalhes_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#detalhe_item.
    def visitDetalhe_item(self, ctx:ProgramaParser.Detalhe_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#detalhe_item_valorAtomico.
    def visitDetalhe_item_valorAtomico(self, ctx:ProgramaParser.Detalhe_item_valorAtomicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#detalhe_item_valorGrupo.
    def visitDetalhe_item_valorGrupo(self, ctx:ProgramaParser.Detalhe_item_valorGrupoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#lista_grupo_conv.
    def visitLista_grupo_conv(self, ctx:ProgramaParser.Lista_grupo_convContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#grupo_valores.
    def visitGrupo_valores(self, ctx:ProgramaParser.Grupo_valoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#grupo_valor.
    def visitGrupo_valor(self, ctx:ProgramaParser.Grupo_valorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramaParser#cobrar_conv.
    def visitCobrar_conv(self, ctx:ProgramaParser.Cobrar_convContext):
        return self.visitChildren(ctx)



del ProgramaParser