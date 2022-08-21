"""
Pacotes:

Módulo -> é apenas um arquivo python que pode ter diversas funções para utilizarmos;

Pacote -> é um diretório que contém uma coleção de módulos.

OBS.: Nas versões do Puthon 2.x, um pacote Python deveria ter  dentro dele um arquivo chamado __init__.py;
Nas versões do Python 3.X, não é mai obrigatória a utilização deste arquivo, mas normalmente ainda é utilizado
para manter a compatibilidade.

# Exemplo 1

from geek import geek1, geek2

from geek.university import geek3, geek4

print(geek1.pi)
print(geek1.funcao1(4, 6))

print(geek2.curso)
print(geek2.funcao2())

print(geek4.funcao4())
print(geek3.funcao3())

# Exemplo 2

from geek.geek1 import funcao1
from geek.university.geek4 import funcao4

print(funcao1(7, 3))
print(funcao4())

"""


