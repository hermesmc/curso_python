"""
List Comprehensions
- Utilizando list comprehension nõs podemos gerar novas listas com dados
  processados a partir de outro iterável

# Sintaxe

[dado for dado in iteravel]

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

# Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

# - for numero in numeros (para cada numero da lista numeros)
# - numero * 10 (multiplique o valor da variável numero por 10)

# Exemplo 2

numeros = [1, 2, 3, 4, 5]
res = [numero / 2 for numero in numeros]

print(res)

# Exemplo 3

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]

print(res)

# list comprehension X Loop

# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = [ ]

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List Comprehension
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = [ ]

print([numero * 2 for numero in numeros])

# Exemplo 4

nome = 'Torcida do Flamengo'

print([letra.upper() for letra in nome])

# Exemplo 5

amigos = ['José', 'Maria', 'João', 'Davi', 'Ana']

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

print([caixa_alta(amigo) for amigo in amigos])

# Exemplo 6

print([numero * 3 for numero in range(1, 10)])

# Exemplo 7

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Exemplo 8

print([str(numero) for numero in [1, 2,3 ,4 ,5]])

"""
