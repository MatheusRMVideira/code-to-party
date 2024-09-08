from antlr4.error.ErrorListener import ErrorListener


class ParserErrorHandler:
    @staticmethod
    def syntaxError(recognizer, offending, line, column, msg, e):
        simbolo = offending.text
        if simbolo == '<EOF>':
            simbolo = 'EOF'
        raise Exception(f'Erro sintatico. Simbolo desconhecido: {simbolo} Linha: {line}')

class LexerErrorHandler(ErrorListener):
    def syntaxError(self, recognizer, offending, line, column, msg, e):
        simbolo = str(e).split("(")[1][1]
        raise Exception(f'Erro sintatico. Simbolo: {simbolo} Linha: {line}')