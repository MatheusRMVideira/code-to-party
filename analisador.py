from typing import Dict

from antlr4 import FileStream, CommonTokenStream

from antlr_generated.ProgramaLexer import ProgramaLexer
from antlr_generated.ProgramaParser import ProgramaParser
from error import LexerErrorHandler, ParserErrorHandler
from verificador_semantico import VerificadorSemantico


class Analisador:
    input_stream: FileStream
    lexer: ProgramaLexer
    parser: ProgramaParser


    def __init__(self, input_file: str):
        self.input_stream = FileStream(input_file, encoding='utf8')
        self.lexer = ProgramaLexer(self.input_stream)

        tokens = CommonTokenStream(self.lexer)
        self.parser = ProgramaParser(tokens)
        self.semantico = VerificadorSemantico()

        self.lexer.removeErrorListeners()
        self.parser.removeErrorListeners()

        self.lexer.addErrorListener(LexerErrorHandler)
        self.parser.addErrorListener(ParserErrorHandler)

    def executar(self) -> Dict:
        tree = self.parser.programa()
        self.semantico.visitPrograma(tree)
        return self.semantico.tabela_simbolos.recuperar_simbolos()

    def obter_erros(self):
        return self.semantico.obter_erros()