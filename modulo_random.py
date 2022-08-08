"""
Módulo Random e o que são módulos.

- São outros arquivos Python.

Random - possui várias funções para geração de números pseudo-aleatórios.

# OBS.: Existem duas formas de utilização do módulo random.

# Forma 1 - importando todo o módulo(não recomendado)

import random

# Ao realizar o import de todo o módulo, todas as funções, atributos, classes e
 propriedades que estiverem dentro do módulo ficarão disponíveis(em memória)

# Se você souber quais funções utilizará deste módulo, esta não seria a forma ideal.


import random

print(random.random())

# a função random() gera um numero pseudo-aleatório entre 0 e 1. Para utilizar a
# função random(), informamos o nome do pacote e o nome da função. Uma coisa é o
# pacote e outra é a função.


# Forma 2 - importando uma função específica do módulo - Forma recomendada

from random import random

# No import acima estamos falando do mmódulo random, importando a função random

for i in range(0, 9):
    print(random())

# uniform() -> Gerar numeros pseudo-aleatórios entre os intervalos estabelecidos

from random import uniform

for i in range(0, 9):
    print(uniform(3, 7))  # o 7 não está incluído

# randint() -> Gerar numeros INTEIROS pseudo-aleatórios entre os intervalos estabelecidos

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')  # o 61 não está incluído

# choice() -> mostra um valor aleatório entre um iterável.

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

# shuffle() -> tem como objetivo embaralhar dados

from random import shuffle

cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for i in range(10):
    shuffle(cartas)
    print(cartas)
    print(cartas.pop())

"""






