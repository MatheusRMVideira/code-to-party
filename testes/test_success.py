from testes.base_call import base_call
import json

# Execute tests.py
def success():
    simbolos, error = base_call('./testes/input/test_1.txt')
    assert len(error) == 0, 'Retornou erro e não devia'
    simbolos_json = json.dumps(simbolos).replace(' ', '')
    with open('./testes/output/test_1.json', 'r') as f:
        out_json = f.read().replace('\n', '').replace(' ', '')
    assert simbolos_json == out_json, 'Os simbolos são diferentes do esperado'

    return simbolos, error