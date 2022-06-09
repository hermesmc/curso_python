"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica

[1] - Utilize Camel Case para nomes de classes;

ex.:

class Calculador e não class calculadora

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

ex.:

def soma_dois():
    pass

numero_par = 4

[3] - Utilize 4 espaços para identação! (NÃO use tab)

if 'a' in 'banana'
    print("tem")

[4] - Linhas em branco
- Separar funções e definições de classes com duas linhas em branco;
- Metodos dentro de uma classe devem se separados por uma linha em branco

[5] - Imports
- Imports devem ser sempre feitos em linhas separadas

ex. errado:
import sys, os

ex. certo:
import sys
import os

* Não há problema em utilizar:
from types import StrigType, ListType

Para vários pacotes:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Os imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
antes de constantes e variáveis globais.

[6] - Espaçoes entre expressões e instruções

# Não faça:

funcao( algo[ 1 ], {outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça

x              = 1
y              = 2
variavel_longa = 3

# Não faça

x = 1
y = 2
variavel_longa = 3

[7] - Termine sempre uma instrução com uma nova linha

Deixe sempre uma linha em branco no final do programa

"""
import this
