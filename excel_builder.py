from ctypes import c_ushort
from typing import Dict

import xlsxwriter


class Excel:
    workbook: xlsxwriter.Workbook

    def __init__(self, output_path: str, simbolos: Dict):
        self.workbook = xlsxwriter.Workbook(output_path)
        self.worksheet = self.workbook.add_worksheet('Visão Geral')
        self.worksheet_itens = self.workbook.add_worksheet('Itens por grupo')
        self.simbolos = simbolos
        self.bold = self.workbook.add_format({'bold': True})
        self.format = {
            'moeda': self.workbook.add_format({"num_format": "R$#,###"}),
            'float': self.workbook.add_format({"num_format": "#,###"}),
        }

        self._escreve_convidados()
        self._escreve_itens_por_grupo()
        self._escreve_itens_variaveis()
        self._escreve_itens_fixos()
        self._escreve_custos()

    def salvar(self):
        self.worksheet.autofit()
        self.worksheet.autofit()
        self.workbook.close()

    def _formatar_nomes(self, texto: str):
        return texto.replace('_', ' ').capitalize()

    def _escreve_convidados(self):
        self.worksheet.merge_range('B2:E2', 'Convidados', self.bold)

        # Escreve tabela de grupos
        if 'grupos' not in self.simbolos:
            grupos = []
        else:
            grupos = [self._formatar_nomes(x) for x in self.simbolos['grupos'].keys()]
        total_grupos = len(grupos)
        self.worksheet.add_table(f'B4:B{4 + total_grupos}',
                                 options={
                                     "data": [[x] for x in grupos],
                                     "name": "grupos",
                                     "columns": [{"header": "Grupos"}],
                                     "autofilter": 0
                                 })
        convidados = []
        for grupo, v in self.simbolos['grupos'].items():
            grupo_formatado = self._formatar_nomes(grupo)
            for pessoa in v:
                pessoa_formatado = self._formatar_nomes(pessoa)
                convidados.append([pessoa_formatado, grupo_formatado])

        total_convidados = len(convidados)
        self.worksheet.add_table(f'D4:E{4 + total_convidados + 1}',
                                 options={
                                     "data": convidados,
                                     "name": "convidados",
                                     "total_row": 1,
                                     "columns": [{"header": "Nome", "total_string": "Total"},
                                                 {"header": "Grupo", "total_function": "count"}]
                                 })

    def _escreve_itens_por_grupo(self):
        if 'itens_variaveis' not in self.simbolos:
            itens_variaveis = {}
        else:
            itens_variaveis = self.simbolos['itens_variaveis']
        row = 1
        column = 1
        for categoria, itens_categoria in itens_variaveis.items():
            categoria_formatado = self._formatar_nomes(categoria)
            for item, propriedades in itens_categoria.items():
                item_formatado = self._formatar_nomes(item)
                self.worksheet_itens.write(row, column, f'{categoria_formatado} - {item_formatado}')
                row += 1
                if isinstance(propriedades['quantidade_por_pessoa'], dict):
                    data = [
                        [self._formatar_nomes(grupo) if grupo != '*' else 'TODOS', float(quantidade)] for grupo, quantidade in
                        propriedades['quantidade_por_pessoa'].items()
                    ]
                else:
                    data = [['TODOS', float(propriedades['quantidade_por_pessoa'])]]

                total_grupos = len(data)
                self.worksheet_itens.add_table(row, column, row + total_grupos + 1, column + 3,
                                               options={
                                                   "data": data,
                                                   "total_row": 1,
                                                   "name": f"quantidade_{categoria}_{item}",
                                                   "columns": [
                                                       {"header": "Grupo",
                                                        },
                                                       {
                                                           "header": "Quant. por pessoa",
                                                       },
                                                       {
                                                           "header": "Pessoas no grupo",
                                                           "formula": '=IF([@Grupo]="TODOS",SUMPRODUCT(--(ISNA(MATCH(convidados[Grupo],[Grupo],0)))),COUNTIF(convidados[Grupo],[@Grupo]))',
                                                           "total_string": "Total"
                                                       },
                                                       {
                                                           "header": "Total Grupo",
                                                           "formula": "=VALUE([@[Quant. por pessoa]])*[@[Pessoas no grupo]]",
                                                           "total_function": "sum"
                                                       },
                                                   ]
                                               })
                row = row + total_grupos + 3

    def _escreve_itens_variaveis(self):
        self.worksheet.merge_range('G2:M2', 'Itens variáveis', self.bold)
        if 'itens_variaveis' not in self.simbolos:
            itens_variaveis = {}
        else:
            itens_variaveis = self.simbolos['itens_variaveis']
        row = 4
        for k, v in itens_variaveis.items():
            # Escreve o nome da categoria
            categoria = self._formatar_nomes(k)
            self.worksheet.write(f'G{row}', categoria, self.bold)
            row += 1
            itens = []
            for item, propriedades in v.items():
                itens.append([
                    self._formatar_nomes(item),
                    propriedades['unidade_de_medida'],
                    float(propriedades['quantidade_por_item']),
                    float(propriedades['valor_por_item'])
                ])

            self.worksheet.add_table(f'G{row}:M{row + len(itens) + 1}',
                                     options={
                                         "data": itens,
                                         "name": f"itens_{k}",
                                         "total_row": 1,
                                         "columns": [
                                             {"header": "Nome"},
                                             {"header": "Unidade de medida"},
                                             {"header": "Quantidade por item"},
                                             {"header": "Valor por item"},
                                             {
                                                 "header": "Quantidade",
                                                 "formula": f'=IFERROR(INDIRECT(SUBSTITUTE("quantidade_{k}_REPLACE[[#Totals],[Total Grupo]]", "REPLACE", LOWER(SUBSTITUTE([@Nome], " ", "_")))), INDIRECT(SUBSTITUTE("quantidade_{k}_REPLACE[[#Totals];[Total Grupo]]", "REPLACE", LOWER(SUBSTITUTE([@Nome], " ", "_")))))'
                                             },
                                             {
                                                 "header": "Quantidade de unidades",
                                                 "formula": '=CEILING.MATH([@Quantidade]/[@[Quantidade por item]])',
                                                 "total_string": "Total"
                                             },
                                             {
                                                 "header": "Valor total",
                                                 "formula": '=[@[Quantidade de unidades]]*[@[Valor por item]]',
                                                 "total_function": "sum"
                                             },
                                         ]
                                     })
            row += len(itens) + 3
        print('a')

    def _escreve_itens_fixos(self):
        self.worksheet.merge_range('O2:P2', 'Itens fixos', self.bold)
        if 'itens_fixos' not in self.simbolos:
            itens_fixos = {}
        else:
            itens_fixos = self.simbolos['itens_fixos']
        itens = []
        for item, valor in itens_fixos.items():
            itens.append([
                self._formatar_nomes(item),
                float(valor)
            ])
        self.worksheet.add_table(f'O4:P{4 + len(itens) + 1}',
                                 options={
                                     "data": itens,
                                     "name": f"itens_fixos",
                                     "total_row": 1,
                                     "columns": [
                                         {
                                             "header": "Nome",
                                             "total_string": "Total"
                                         },
                                         {
                                             "header": "Valor",
                                             "total_function": "sum"
                                         },
                                     ]
                                 })

    def _escreve_custos(self):
        self.worksheet.merge_range('R2:V2', 'Cobrar', self.bold)

        self.worksheet.write('R4', 'Total', self.bold)
        total_string_list = []
        for var in self.simbolos['itens_variaveis'].keys():
            total_string_list.append(f"itens_{var}[[#Totals],[Valor Total]]")
        total_string_list.append('itens_fixos[[#Totals],[Valor]]')
        total_string = "=SUM(" + ', '.join(total_string_list) + ")"
        self.worksheet.write_formula('S4', total_string)
        if 'cobrar' not in self.simbolos:
            custos = {}
        else:
            custos = self.simbolos['cobrar']
        data = []
        for grupo, porcentagem in custos.items():
            data.append([
                self._formatar_nomes(grupo) if grupo != "*" else "TODOS",
                float(porcentagem)
            ])

        self.worksheet.add_table(f'R6:V{6 + len(data) + 1}',
                                 options={
                                     "data": data,
                                     "name": f"custos_grupos",
                                     "total_row": 1,
                                     "columns": [
                                         {
                                             "header": "Grupo",
                                             "total_string": "Total"
                                         },
                                         {
                                             "header": "Porcentagem",
                                             "total_function": "sum"
                                         },
                                         {
                                             "header": "Valor total",
                                             "total_function": "sum",
                                             "formula": "=[@[Porcentagem]]/100*S4"
                                         },
                                         {
                                             "header": "Quant. pessoas",
                                             "total_function": "sum",
                                             "formula": '=IF([@Grupo]="TODOS",SUMPRODUCT(--(ISNA(MATCH(convidados[Grupo],[Grupo],0)))),COUNTIF(convidados[Grupo],[@Grupo]))'
                                         },
                                         {
                                             "header": "Valor por pessoa",
                                             "formula": "=[@[Valor total]]/[@[Quant. pessoas]]"
                                         }
                                     ]
                                 })
        row = 6 + len(data) + 3
        self.worksheet.write(f'R{row}', 'Custo não alocado', self.bold)
        self.worksheet.write_formula(f'S{row}', '=S4-custos_grupos[[#Totals],[Valor total]]')