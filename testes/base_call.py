from analisador import Analisador


def base_call(file_path):
    lexer = Analisador(file_path)
    simbolos = lexer.executar()
    # Caso possua erros semanticos, enviar todos de uma vez
    erros = lexer.obter_erros()
    return simbolos, erros