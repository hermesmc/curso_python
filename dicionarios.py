"""
Dicionários - são coleções do tipo chave/valor. O valor da chave não pode ser repetida.
O valor pode ser repetido

Exemplo:

paises = {'br': 'Brasil', 'us': 'Estados Unidos', 'uk': 'Reino Unido'}
print(paises)
print(type(paises))

# Trazendo só chaves:
print(paises.keys())

# Trazendo só valores:
print(paises.values())

# Acessando pela chave informada
print(paises['br'])

# Acessando via GET (recomendado)

print(paises.get('br'))
print(paises.get('ru'))

pais = paises.get('pt')

if pais:
    print('País encontrado: ' + pais)
else:
    print('Não foi encontrado')

# Valor padrão - Mais elegante:

pais = paises.get('br', 'Não encontrado')
print('País encontrado: ' + pais)

# Incluindo valores ao dicionário

# Forma 1
paises['pt'] = 'Portugal'
print(paises)

# Forma 2

paises.update({'fr': 'França'})
print(paises)

# Atualizando dados em um dicionário
# Forma 1

paises['uk'] = 'Inglaterra'
print(paises)

#Forma 2
paises.update({'br': 'BRASIL'})
print(paises)

# Removendo dados de um dicionário
# Forma 1

ret = paises.pop('br')
print(ret)
print(paises)

# OBS.: Ao remover ele pode retornar o valor que está sendo removido

# Forma 2 - Forma mais comum

del paises['us']
print(paises)

# OBS.: Neste caso não retorna o valor que está sendo removido

# Montando um carrinho de compras com listas
carrinho = []

produto1 = ["PlayStation 4", 1 , 4000.00]
produto2 = ["Controle Wirelees", 2 , 300.00]
produto3 = ["Minecraft", 1 , 168.00]

carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)

print(carrinho)
print(type(carrinho))

# Montando um carrinho de compras com tuplas

carrinho = []

produto1 = ("PlayStation 4", 1 , 4000.00)
produto2 = ("Controle Wirelees", 2 , 300.00)
produto3 = ("Minecraft", 1 , 168.00)

carrinho = (produto1, produto2, produto3)

print(carrinho)
print(type(carrinho))

# Montando um carrinho de compras com dicionários

carrinho = []

produto1 = {'nome': 'PlayStation 4', 'qtd': 1 , 'vlr' : 4000.00}
produto2 = {'nome': 'Controle Wirelees', 'qtd': 2 , 'vlr' : 300.00}
produto3 = {'nome': 'Minecraft', 'qtd': 1 , 'vlr' : 168.00}

carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)

print(produto1)
print(type(produto1))

print(carrinho)
print(type(carrinho))

# Metodos de dicionários

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# limpar um dicionário

d.clear()
print(d)
print(type(d))

# Copiando um dicionário para outro
# Forma 1 (deepCopy)

novo = d.copy()
novo['d'] = 4
print(novo)
print(type(novo))

# Forma 2 (ShallowCopy

novo = d
print(novo)
novo['d'] = 4
print(novo)
print(d) # Veja que incluiu aqui também
print(type(novo))

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O metodo fromkeys recebe dois parâmetros: um iterável e um valor
# Para cada valor iterável uma chave e irá atribuir a essa chave o valor informado

"""

