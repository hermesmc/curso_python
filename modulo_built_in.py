"""
Módulos built in são módulos integrados, já vem instalados no Python, mas não são carrgeados em memória.
Devem ser carregados conforme a necessidade do programa.

Utilizando alias para módulos ou funções

o módulo random recebeu "rdm" como seu alias

import random as rdm
print(rdm.random())

# Podemos inportar todas as funções de um módulo utilizando o asterisco. Assim não precisamos
# informar nem o alias nem o nome do módulo

from random import *
print(random())

# Importando todo o módulo

import random
print(random.random())

# Utilizando alias para módulos/funções

from random import randint as rdi
print(rdi(5, 89))

# Duas funções com alias

from random import randint as rdi, random as rdm
print(rdi(5, 89))
print(rdm())

# Costumamos utilizar tuple para colocar multiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(3, 7))
lista = ['Torcida', ' do ', 'Flamengo']
shuffle(lista)
print(lista)
print(choice('Torcida'))

Lista de módulos do Python

https://docs.python.org/3/py-modindex.html

"""

