"""
Mapas - Conhecidos em Python como dicionários

Dicionários são representados em Python por chaves {}

receita = {'jan': 100, 'fev': 200, 'mar':300}

print(receita)
print(type(receita))
print('------------------------------------')

# Interar com dicionários
# Mostrando a chave
for chave in receita:
    print(chave)

print('------------------------------------')
# Mostrando o valor
for chave in receita:
    print(receita[chave])

print('--------------')
# OU

for chave in receita.keys():
    print(receita[chave])

print('------------------------------------')
# Mostrando a chave e o valor
for chave in receita:
    print(f'{chave} : {receita[chave]}')

print('------------------------------------')
# Recebendo a chave
chave = receita.keys()

print(chave)

# Acessando valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários

for chave, valor in receita.items():
    print(f'Chave = {chave} e Valor = {valor}')

# Soma, valor máximo, mínimo e tamanho

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))

# Soma, valor máximo, mínimo e tamanho

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))

"""






