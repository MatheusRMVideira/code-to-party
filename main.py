import os
import sys
from analisador import Analisador
from excel_builder import Excel


# PARA EXECUTAR O GERADOR DO ANTLR
# java -cp "C:\Users\matheus\Downloads\antlr-4.13.2-complete.jar" org.antlr.v4.Tool -Dlanguage=Python3 -o antlr_generated Programa.g4

def main(args):
    # Valida os argumentos do programa
    if len(args) != 2:
        sys.exit('Uso: python3 main.py <input-file> <output-file>')

    if not os.path.isfile(args[0]):
        sys.exit(f'Arquivo de entrada: {os.path.abspath(args[0])} não existe')

    if os.path.isfile(args[1]):
        sys.exit(f'Arquivo de saida: {os.path.abspath(args[1])} já existe')

    # Inicia o analisador
    lexer = Analisador(args[0])
    simbolos = lexer.executar()
    # Caso possua erros semanticos, enviar todos de uma vez
    erros = lexer.obter_erros()
    if erros:
        sys.exit('\n'.join(erros))
    # Gera o output, feito depois do erros para não gerar o arquivo incompleto
    excel = Excel(args[1], simbolos)
    excel.salvar()



if __name__ == '__main__':
    main(sys.argv[1:])
