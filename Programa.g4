grammar Programa;

PALAVRAS_CHAVE: 'convidados' | 'categoria' | 'fixo' | 'cobrar_convidados';

PALAVRAS_CHAVE_ITEM: 'unidade_de_medida' | 'quantidade_por_item' | 'valor_por_item' | 'quantidade_por_pessoa';

ABRE_CHAVE: '{';
FECHA_CHAVE: '}';

NUM_REAL: ('0'..'9')+ ('.' ('0'..'9')+)?;

WS: (' ' | '\t' | '\r' | '\n') -> skip;

IDENTIFICADOR: ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;

COMENTARIO: '//' (~('\n'|'\r')*) ('\n' | '\r');

SELETOR_GLOBAL: '*';

Caracter_invalido: .;

programa: convidados corpo EOF;

convidados: 'convidados' ':' ABRE_CHAVE lista_convidados FECHA_CHAVE;

lista_convidados: (conv)+;

conv: IDENTIFICADOR ':' grupo_conv;

grupo_conv: IDENTIFICADOR;

grupo_conv_global: IDENTIFICADOR | SELETOR_GLOBAL;

corpo: (categorias cobrar_conv) | (cobrar_conv categorias);

categorias: (categoria)+;

categoria: categoria_variavel | categoria_fixo;

categoria_variavel: 'categoria' IDENTIFICADOR ':' ABRE_CHAVE itens_variaveis FECHA_CHAVE;

categoria_fixo: 'fixo' ':' ABRE_CHAVE itens_fixos FECHA_CHAVE;

itens_variaveis: (item_variavel)+;

itens_fixos: (item_fixo)+;

item_variavel: IDENTIFICADOR ':' ABRE_CHAVE detalhes_item FECHA_CHAVE;

item_fixo: IDENTIFICADOR ':' NUM_REAL;

detalhes_item: (detalhe_item)+;

detalhe_item: PALAVRAS_CHAVE_ITEM ':' detalhe_item_valor;

detalhe_item_valor
    :
    IDENTIFICADOR  #detalhe_item_valorAtomico
    |
    NUM_REAL #detalhe_item_valorAtomico
    |
    lista_grupo_conv # detalhe_item_valorGrupo
    ;

lista_grupo_conv: ABRE_CHAVE grupo_valores FECHA_CHAVE;

grupo_valores: (grupo_valor)+;

grupo_valor: grupo_conv_global ':' NUM_REAL;

cobrar_conv: 'cobrar_convidados' ':'  lista_grupo_conv;