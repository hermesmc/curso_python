"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

Recap tupla

tupla = (1, 2, 3)
print(tupla)
print(type(tupla))

Named Tuple -> São tuplas diferenciadas onde especificamos um nome
para a mesma e também parâmetros

"""
# Importando
from collections import namedtuple

# Forma 1 - declaração

cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - declaração

cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3 - declaração

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando

xando = cachorro(idade=2, raça='Dalmata', nome='Xandó')
print(xando)

# Forma 1
print(xando[0])
print(xando[1])
print(xando[2])

print('=====================')
# Forma 2
print(xando.idade)
print(xando.raça)
print(xando.nome)

print('=====================')
print(xando.index('Dalmata'))
print(xando.count('Dalmata'))
