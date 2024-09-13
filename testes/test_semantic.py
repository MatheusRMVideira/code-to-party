from testes.base_call import base_call
import json

# Execute tests.py
def semantic():
    simbolos, error = base_call('./testes/input/test_100.txt')
    assert len(error) != 0, 'Não retornou erro, mas devia'
    errors_to_detect = [
        'Linha: 9: O convidado jorge já foi declarado no grupo adulto',
        'Linha: 19: O item coca_cola já existe na categoria atual',
        'Linha: 20: A propriedade unidade_de_medida já foi declarada',
        'Linha: 24: A propriedade quantidade_por_item não é do tipo correto',
        'Linha: 31: O grupo adulto não possui valor atribuido. Declare ele ou utilize a chave global \'*\'',
        'Linha: 28: A propriedade valor_por_item não foi declarada',
        'Linha: 47: A categoria comidas já foi declarada',
        'Linha: 78: O grupo adulto não possui valor atribuido. Declare ele ou utilize a chave global \'*\'']
    assert len(error) == len(errors_to_detect), 'A quantidade de erros retornada é diferente da esperada'
    for e in errors_to_detect:
        assert e in error, f'O erro \'{e}\' não foi retornado, mas deveria'
