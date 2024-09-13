# Generated from Programa.g4 by ANTLR 4.13.2
from typing import List

from antlr4 import *
from antlr_generated.ProgramaVisitor import ProgramaVisitor
from antlr_generated.ProgramaParser import ProgramaParser
from tabela_simbolos import TabelaSimbolos


# This class defines a complete generic visitor for a parse tree produced by ProgramaParser.

class VerificadorSemantico(ProgramaVisitor):
    lista_erros: List[str]

    def __init__(self):
        self.tabela_simbolos = TabelaSimbolos()
        self.lista_erros = []

    def _verificar_erros(self, func, ctx):
        try:
            func(ctx)
        except Exception as e:
            self.lista_erros.append(f'Linha: {ctx.start.line}: {e}')

    def obter_erros(self):
        return self.lista_erros

    # Visit a parse tree produced by ProgramaParser#programa.
    def visitPrograma(self, ctx: ProgramaParser.ProgramaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#convidados.
    def visitConvidados(self, ctx: ProgramaParser.ConvidadosContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#lista_convidados.
    def visitLista_convidados(self, ctx: ProgramaParser.Lista_convidadosContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#conv.
    def visitConv(self, ctx: ProgramaParser.ConvContext):
        self._verificar_erros(self.tabela_simbolos.adiciona_pessoa_grupo, ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#grupo_conv.
    def visitGrupo_conv(self, ctx: ProgramaParser.Grupo_convContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#grupo_conv_global.
    def visitGrupo_conv_global(self, ctx:ProgramaParser.Grupo_conv_globalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#corpo.
    def visitCorpo(self, ctx: ProgramaParser.CorpoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#categorias.
    def visitCategorias(self, ctx: ProgramaParser.CategoriasContext):
        result = self.visitChildren(ctx)
        self._verificar_erros(self.tabela_simbolos.valida_categorias, ctx)
        return result

    # Visit a parse tree produced by ProgramaParser#categoria.
    def visitCategoria(self, ctx: ProgramaParser.CategoriaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#categoria_variavel.
    def visitCategoria_variavel(self, ctx: ProgramaParser.Categoria_variavelContext):
        self._verificar_erros(self.tabela_simbolos.adiciona_categoria, ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#categoria_fixo.
    def visitCategoria_fixo(self, ctx: ProgramaParser.Categoria_fixoContext):
        self._verificar_erros(self.tabela_simbolos.valida_fixo_ja_declarado, ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#itens_variaveis.
    def visitItens_variaveis(self, ctx: ProgramaParser.Itens_variaveisContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#itens_fixos.
    def visitItens_fixos(self, ctx: ProgramaParser.Itens_fixosContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#item_variavel.
    def visitItem_variavel(self, ctx: ProgramaParser.Item_variavelContext):
        self._verificar_erros(self.tabela_simbolos.adiciona_item_categoria, ctx)
        result = self.visitChildren(ctx)
        self._verificar_erros(self.tabela_simbolos.valida_detalhes, ctx)
        return result

    # Visit a parse tree produced by ProgramaParser#item_fixo.
    def visitItem_fixo(self, ctx: ProgramaParser.Item_fixoContext):
        self._verificar_erros(self.tabela_simbolos.adiciona_item_fixo, ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#detalhes_item.
    def visitDetalhes_item(self, ctx: ProgramaParser.Detalhes_itemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#detalhe_item.
    def visitDetalhe_item(self, ctx: ProgramaParser.Detalhe_itemContext):
        self._verificar_erros(self.tabela_simbolos.adiciona_detalhe_item, ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#detalhe_item_valorAtomico.
    def visitDetalhe_item_valorAtomico(self, ctx: ProgramaParser.Detalhe_item_valorAtomicoContext):
        self._verificar_erros(self.tabela_simbolos.valida_tipo_detalhes_item, ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#detalhe_item_valorGrupo.
    def visitDetalhe_item_valorGrupo(self, ctx: ProgramaParser.Detalhe_item_valorGrupoContext):
        self._verificar_erros(self.tabela_simbolos.adiciona_valor_contexto_grupo, ctx)
        result = self.visitChildren(ctx)
        self._verificar_erros(self.tabela_simbolos.valida_grupos_contexto, ctx)
        return result

    # Visit a parse tree produced by ProgramaParser#lista_grupo_conv.
    def visitLista_grupo_conv(self, ctx: ProgramaParser.Lista_grupo_convContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#grupo_valores.
    def visitGrupo_valores(self, ctx: ProgramaParser.Grupo_valoresContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#grupo_valor.
    def visitGrupo_valor(self, ctx: ProgramaParser.Grupo_valorContext):
        self._verificar_erros(self.tabela_simbolos.adiciona_valor_grupo, ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgramaParser#cobrar_conv.
    def visitCobrar_conv(self, ctx: ProgramaParser.Cobrar_convContext):
        self._verificar_erros(self.tabela_simbolos.adiciona_cobrar_contexto, ctx)
        result = self.visitChildren(ctx)
        self._verificar_erros(self.tabela_simbolos.valida_grupos_contexto, ctx)
        return result
