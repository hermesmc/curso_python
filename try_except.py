"""
O bloc try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
Previnindo assim qu o programa pare de funcionar e que o usuário receba mensagens
de erro inexperadas.

A forma geral mais simples é:

try:
    //execução problematica
except:
    //o que deve ser feito em caso de problemas

# Exemplo 1 - tratando um erro genérico

try:
    teste()
except:
    print('Deu algum "pobrema".')

# Exemplo 2 - tratando um erro genérico

try:
    len(5)
except:
    print('Deu "oto pobrema".')

OBS.: tratar erro de forma genérica não é a melhor forma de tratamento de erros.
O ideal é sempre tratar de forma expecifica.

# Exemplo 3 - Trartando um erro específico

try:
    teste()
except NameError:
    print('A função é inexistente.')

Aqui pega apenas NameError

try:
    len(5)
except TypeError:
    print('A função é inexistente.')

Aqui pega apenas TypeError

# Exemplo 4 - Com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'Foi gerado o seguinte erro: {err}.')

# Podemos efetuar diversos tratamentos de erro de uma vez
try:
    len(5)
except NameError as erra:
    print(f'Foi gerado o seguinte erro: {erra}.')
except TypeError as errb:
    print(f'Foi gerado o seguinte erro: {errb}.')

try:
    print('teste'[9])
except NameError as erra:
    print(f'Foi gerado o seguinte erro: {erra}.')
except TypeError as errb:
    print(f'Foi gerado o seguinte erro: {errb}.')
except:
    print(f'Foi gerado um erro diferente.')

# Outro exemplo

def pegavalor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return 'Chave não localizada.'
    except TypeError:
        return 'Dados de entrada informados são inválidos.'

dic = {'nome': 'Flamengo'}

print(pegavalor(dic, 'game'))

print(pegavalor(7, 'game'))

"""
