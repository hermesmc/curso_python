"""
Listas alinhadas (Nested lists)

Algumas linhagugens de programação prossuem estruturas de dados chamadas de arrays:
- Unidimensionais (arrays/vetores);
- Multidimensionais(matrizes);

Em Python temos as listas:

numeros = [1, 4, 7, 4, 9, 3]
numeros = ['a', 4.76, 'nome', 4, True, 3]

# Exemplos:

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # matrix 3x3

print(listas)
print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0][1]) # acessando o número 2
print(listas[1][2]) # acessando o número 6
print(listas[2][0]) # acessando o número 7

# Iterando com loops em uma lista alinhada

for lista in listas:
    for num in lista:
       print(num)

# Usando lista comprehension:

[[print(valor) for valor in lista] for lista in listas]

# Outros Exemplos:

# Gerando uma matrix 3 x 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1,4)]
print(tabuleiro)

# Gerando jogadas para jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais

print([['*' for i in range(1,4)] for j in range (1,4 )])

"""
