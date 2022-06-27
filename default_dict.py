"""
Módulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recap dicionários

dicionario = {'Curso':'Programação em Python'}
print(dicionario)
print(dicionario['Curso'])
print(type(dicionario))

print(dicionario['Outro']) # ???

Default Dict: ao informar uma chave que não existe, não retorna erro como no dicionário normal

OBS.: Lambda são funções sem nomes que podem ou não receber parâmetros de entrada e retorno de valores.

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 'Pesquisa')
print(dicionario)

dicionario['Curso'] = 'Programação em Python'

print(dicionario)
print(dicionario['Curso'])
print(dicionario['Outro'])
print(dicionario)

"""
