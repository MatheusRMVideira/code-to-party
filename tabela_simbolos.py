from typing import Dict, List, Union, Optional

from antlr_generated.ProgramaLexer import ProgramaLexer

propriedades_verificar = {'unidade_de_medida': [ProgramaLexer.IDENTIFICADOR],
                          'quantidade_por_item': [ProgramaLexer.NUM_REAL],
                          'valor_por_item': [ProgramaLexer.NUM_REAL],
                          'quantidade_por_pessoa': [ProgramaLexer.NUM_REAL]
                          }


class TabelaSimbolos:
    grupos: Dict[str, List[str]]
    itens_variaveis: Dict[str, Dict]
    cobrar: Dict[str, str]
    itens_fixos: Dict[str, str]

    contexto_atual: Optional[Dict[str, str]]

    def __init__(self):
        self.grupos = {}
        self.itens_variaveis = {}
        self.itens_fixos = {}
        self.cobrar = {}

        self.contexto_atual = None

    def _identificador_do_parent(self, ctx, profundidade: int):
        temp_ctx = ctx
        for i in range(0, profundidade):
            temp_ctx = temp_ctx.parentCtx
        return temp_ctx.IDENTIFICADOR().getText()

    def adiciona_pessoa_grupo(self, ctx):
        grupo = ctx.grupo_conv().IDENTIFICADOR().getText()
        pessoa = ctx.IDENTIFICADOR().getText()
        if grupo not in self.grupos:
            self.grupos[grupo] = []
        if pessoa in self.grupos[grupo]:
            raise ValueError(f'O convidado {pessoa} já foi declarado no grupo {grupo}')
        self.grupos[grupo].append(pessoa)

    def adiciona_categoria(self, ctx):
        categoria = ctx.IDENTIFICADOR().getText().lower()
        if categoria in self.itens_variaveis:
            raise ValueError(f'A categoria {categoria} já foi declarada')
        self.itens_variaveis[categoria] = {}

    def adiciona_item_categoria(self, ctx):
        categoria = self._identificador_do_parent(ctx, profundidade=2)
        item = ctx.IDENTIFICADOR().getText().lower()
        if item in self.itens_variaveis[categoria]:
            raise ValueError(f'O item {item} já existe na categoria atual')
        self.itens_variaveis[categoria][item] = {}

    def adiciona_detalhe_item(self, ctx):
        categoria = self._identificador_do_parent(ctx, profundidade=4)
        item = self._identificador_do_parent(ctx, profundidade=2)
        detalhe = ctx.PALAVRAS_CHAVE_ITEM().getText()
        if detalhe in self.itens_variaveis[categoria][item]:
            raise ValueError(f'A propriedade {detalhe} já foi declarada')
        self.itens_variaveis[categoria][item][detalhe] = None

    def valida_tipo_detalhes_item(self, ctx):
        categoria = self._identificador_do_parent(ctx, profundidade=5)
        item = self._identificador_do_parent(ctx, profundidade=3)
        detalhe = ctx.parentCtx.PALAVRAS_CHAVE_ITEM().getText()
        valor_tipo = ctx.getChild(0).getSymbol().type
        valor = ctx.getChild(0).getText()
        tipo = propriedades_verificar[detalhe]
        if valor_tipo not in tipo:
            raise ValueError(f'A propriedade {detalhe} não é do tipo correto')
        self.itens_variaveis[categoria][item][detalhe] = valor

    def adiciona_valor_contexto_grupo(self, ctx):
        categoria = self._identificador_do_parent(ctx, profundidade=5)
        item = self._identificador_do_parent(ctx, profundidade=3)
        detalhe = ctx.parentCtx.PALAVRAS_CHAVE_ITEM().getText()
        self.itens_variaveis[categoria][item][detalhe] = {}
        self.contexto_atual = self.itens_variaveis[categoria][item][detalhe]

    def adiciona_valor_grupo(self, ctx):
        nome = ctx.grupo_conv_global().getText()
        valor = ctx.NUM_REAL().getText()
        if nome not in self.grupos and nome != '*':
            raise ValueError(f'O grupo {nome} não foi declarado em convidados')
        self.contexto_atual[nome] = valor

    def valida_detalhes(self, ctx):
        categoria = self._identificador_do_parent(ctx, profundidade=2)
        item = self._identificador_do_parent(ctx, profundidade=0)
        propriedades = self.itens_variaveis[categoria][item]
        for k in propriedades_verificar.keys():
            if k not in propriedades:
                raise ValueError(f'A propriedade {k} não foi declarada')

    def adiciona_cobrar_contexto(self, ctx):
        self.contexto_atual = self.cobrar

    def adiciona_item_fixo(self, ctx):
        item = ctx.IDENTIFICADOR().getText()
        valor = ctx.NUM_REAL().getText()
        self.itens_fixos[item] = valor

    def valida_grupos_contexto(self, ctx):
        if '*' not in self.contexto_atual:
            for grupo in self.grupos:
                if grupo not in self.contexto_atual:
                    raise ValueError(
                        f'O grupo {grupo} não possui valor atribuido. Declare ele ou utilize a chave global \'*\'')

    def valida_categorias(self, ctx):
        if not self.itens_fixos:
            raise ValueError(f'A categoria fixo não foi declarada.')

    def recuperar_simbolos(self):
        return {'grupos': self.grupos,
                'itens_variaveis': self.itens_variaveis,
                'cobrar': self.cobrar,
                'itens_fixos': self.itens_fixos}
