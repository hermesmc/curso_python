"""
Zip

zip(): cria um iterável chamado zip object que agrega elementos de cada
um dos iteráveis passado cocmo entrada em pares

lista1 = [1, 3, 5]
lista2 = [2, 4, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# sempre podemos gerar uma lista, tupla, set ou dicionário
# Lista
print(list(zip1))
# Tupla
zip1 = zip(lista1, lista2)
print(tuple(zip1))
# Set
zip1 = zip(lista1, lista2)
print(set(zip1))
# Dicionary
zip1 = zip(lista1, lista2)
print(dict(zip1))

print('-----------------')
# Zip utiliza como paramer o menor tamanho de iterável.
lista3 = [4, 2, 7, 9, 4, 5]
zip2 = zip(lista1, lista2, lista3)
print(list(zip2))

# Podemos usar diferentes iteráveis com zip

lista = [6, 7, 8, 9, 10]
tupla = (1, 2, 3, 4, 5)
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zip3 = zip(lista, tupla, dicionario.values())
print(list(zip3))

# Lista de tuplas

dados = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
print(list(zip(*dados)))

# Pegando nome do aluno e sua maior nota e sua media
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Pedro', 'Maria', 'Carla']

maior = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
media = {dado[0]: ((dado[1] + dado[2])/2) for dado in zip(alunos, prova1, prova2)}

print(maior)
print(media)

# refatorando com map

maior = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(maior))

"""
