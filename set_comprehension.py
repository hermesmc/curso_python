"""
Set comprehension

Lista = [1, 2, 3, 4]
Set = {1, 2, 3, 4}

#Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

#Exemplo 2

numeros = {X ** 2 for X in range(10)}
print(numeros)
print(type(numeros))

#Exemplo - Gerando um dicionário

numeros = {X: X ** 2 for X in range(10)}
print(numeros)
print(type(numeros))

# Exemplo final - string

palavra = {alfa for alfa in 'Torcida do Flamengo'}
print(palavra)

# dicionario
palavra = {alfa: alfa for alfa in 'Torcida do Flamengo'}
print(palavra)

"""
