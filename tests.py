from testes.test_semantic import semantic
from testes.test_syntax import syntax
from testes.test_success import success


def run_all_tests():
    errors = []
    try:
        success()
    except Exception as e:
        errors.append(f'O teste sucesso falhou com o erro: {type(e)} {e}')

    try:
        syntax()
    except Exception as e:
        errors.append(f'O teste de sintaxe falhou com o erro: {type(e)} {e}')

    try:
        semantic()
    except Exception as e:
        errors.append(f'O teste de semantica falhou com o erro: {type(e)} {e}')

    if len(errors) > 0:
        raise Exception('; '.join(errors))

    print('Testes executados com sucesso!')

if __name__ == '__main__':
    run_all_tests()