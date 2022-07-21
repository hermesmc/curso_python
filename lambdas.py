"""
Utilizando lambdas

Conhecidas por exepressões lambdas, ou lambdas, são funções sem nome, ou seja, funções anonimas.

# Função em Python

def soma(a, b):
    return a + b

# Exemplo
def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Refatorando a função (Lambda)

lambda x: 3 * x + 1

# Como usar a função lambda

calc = lambda x: 3 * x + 1

print(calc(4))

# Podemos ter expressões lambdas com várias entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('HERmes', 'marUYama'))

# Com lambdas podemos ter nenhume, uma ou varias entradas, como em funções:

amar = lambda: 'Como não amar Python?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: x ** y

tres = lambda x, y, z: (x - y)/ z

print(amar())
print(uma(5))
print(duas( 3, 2))
print(tres(100, 10, 5))

# Outro exemplo

autores = ['Machado de Assis', 'Guimarães Rosa', 'Eça de Queiroz', 'Ariano Suassuna', 'Cecilia Meireles',
           'Zélia Gatai', 'J K Rowling']
print(autores)

# Como ordenar pelo Sobrenome?

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower(),reverse=False)
print(autores)

# sort = vai ordenar conforme o critério key
# Em sobrenome.split(' ')[-1].lower():
# .split(' ') = o Python vai separar cada parte do nome por espaço
# [-1] = vai pegar o ultimo nome separado
# lower() = vai deixar todos minúsculos para ordenar

# Função quadrática
# exemplo f(x) = 2x² + 5x + 3
#f(x) = a * x **2 +  2 + b * x + c

# definindo a função

def geradora_funcao_quadratica(a, b, c):
    # Retorna a função f(x) = a*x**2 + b*x + c
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 1, 3)
# Aqui se x = 1
print(teste(1))

# Aqui se x = 0, seria o normal
print(teste(0))

"""


