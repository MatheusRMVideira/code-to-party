from excel_builder import Excel
from testes.base_call import base_call
import json

# Execute tests.py
def syntax():
    try:
        simbolos, error = base_call('./testes/input/test_2.txt')
    except Exception as e:
        assert e.args[0] == 'Erro sintatico. Simbolo desconhecido: caregoria Linha: 11', 'O erro recebido é diferente do esperado'

    try:
        simbolos, error = base_call('./testes/input/test_3.txt')
    except Exception as e:
        assert e.args[0] == 'Erro sintatico. Simbolo desconhecido: { Linha: 11', 'O erro recebido é diferente do esperado'

    try:
        simbolos, error = base_call('./testes/input/test_4.txt')
    except Exception as e:
        assert e.args[0] == 'Erro sintatico. Simbolo desconhecido: { Linha: 12', 'O erro recebido é diferente do esperado'

    try:
        simbolos, error = base_call('./testes/input/test_5.txt')
    except Exception as e:
        assert e.args[0] == 'Erro sintatico. Simbolo desconhecido: categoria Linha: 11', 'O erro recebido é diferente do esperado'

    try:
        simbolos, error = base_call('./testes/input/test_6.txt')
    except Exception as e:
        assert e.args[0] == 'Erro sintatico. Simbolo desconhecido: } Linha: 58', 'O erro recebido é diferente do esperado'

    try:
        simbolos, error = base_call('./testes/input/test_7.txt')
    except Exception as e:
        assert e.args[0] == 'Erro sintatico. Simbolo desconhecido: 20 Linha: 65', 'O erro recebido é diferente do esperado'

    try:
        simbolos, error = base_call('./testes/input/test_8.txt')
    except Exception as e:
        assert e.args[0] == 'Erro sintatico. Simbolo desconhecido: ABC123 Linha: 44', 'O erro recebido é diferente do esperado'

    try:
        simbolos, error = base_call('./testes/input/test_9.txt')
    except Exception as e:
        assert e.args[0] == 'Erro sintatico. Simbolo desconhecido: categoria Linha: 1', 'O erro recebido é diferente do esperado'
