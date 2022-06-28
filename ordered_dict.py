"""
Módulo Collections - Ordered dict

https://docs.python.org/3/library/collections.html#collections.OrderedDict

É um dicionário que nos garante a ordem de inserção dos elementos

* Vantagem = PERFORMANCE

# Em um dicionário a ordem de inserção não é garantida
dicionario = {'e': 5, 'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dicionario)
dicionario['z'] = 9
dicionario['f'] = 6
print(dicionario)
print(type(dicionario))

# Fazendo import
from collections import OrderedDict

dic = OrderedDict(dicionario)

for chave, valor in dic.items():
    print(f'Chave={chave} - Valor: {valor}')

# Entendendo a diferença entre Dict e Ordered Dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # Aqui a ordem não importa

dict3 = OrderedDict(dict1)
dict4 = OrderedDict(dict2)

print(dict3 == dict4) # Aqui a ordem importa
"""
