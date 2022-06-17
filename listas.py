"""
Listas

LIstas em Python funcionam como vetores/matrizes (arrays em outras linguagens), com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

- Dinâmico: Não possui tamaanho fixo, ou seja podemos criar a lista e ir adicionando elementos;
- Qualquer tipo de dado: não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.

As listas em python são representadas por colchetes []

teste = [1, 8, 3, 4]
# print(teste)

teste2 = ['A', 'T', 'W', 'Q', 'S']
print(teste2)

teste3 = []
print(teste3)

teste4 = list(range(11))
print(teste4)

teste5 = list('Torcida do Flamengo')
print(teste5)

# Podemos checar se determinado elemento está em uma lista:
valor_correto = False
valor = ' '
while not valor_correto:
    if valor.isnumeric():
        valor_correto = True
        valor = int(valor)
    else:
        valor = input("Digite o valor para checagem: ")

if valor in teste:
    print(f'Elemento {valor} encontrado')
else:
    print(f'{valor} não foi encontrado')

# Ordenamento de listas
lista1 = [1, 99, 33, 21, 72, 98, 5, 23, 69, 44, 102]
lista1.sort()
print(f'Lista ordenada: {lista1}')

lista2 = list('Torcida do Flamengo')
lista2.sort()
print(lista2)

# Podemos facilmente saber o numero de ocorrências em uma lista
print(lista2.count('a'))

# Inserindo mais valores a lista pré-existente
print(teste)
teste.append(42) # adicionando com APPEND: adiciona um elemento por vez
print(teste)

# Inserindo uma lista em uma lista
teste.append([1, 8])
print(teste)
print(teste.count(1))

# Inserindo multiplos dados em uma lista
teste.extend([12, 13, 14]) # extend só aceita incluir mais de um elemento
print(teste)

# Podemos inserir um elemento informando o indice, ou seja, onde ele será incluído na lista
lista1.insert(2, 999)
print(lista1)

# Podemos juntar varias listas
lista1 = list(range(6))
lista2 = list('Torcida do Flamengo')
lista3 = lista1 + lista2
print(lista3)

ou

lista1.extend(lista2)
print(lista1)

# Invertendo a ordem de uma lista
lista1.reverse()
print(lista1)

OU

print(lista1[::-1])

# Copiando listas
lista4 = lista1.copy()
print(lista1)

# Sabendo o tamanho de uma lista
tamanho = len(lista1)
print(tamanho)

# Removendo o ultimo elemento de uma lista retornando este elemento
print(lista1.pop())
print(lista1)

# Remove um elemento pelo indice
lista1.pop(2)

OBS.: se tentar remover um elemento de uma posição que não existe será retornado erro

# removendo todos os elementos
lista1.clear()
print(lista1)

# podemos repetir elementos em uma lista
lista1 = lista1 * 5
print(lista1)

# Convertendo string em lista

# Exemplo 1
texto = 'Torcida do Flamengo'
lista2 = list(texto)
print(lista2)

lista2 = texto.split()
print(lista2)

OBS.: Por padrão o split separa os elementos pelo 'espaço' entre elas

# Informando qual o separador que o split deve obedecer

# Exemplo 2
texto = 'Torcida;do;Flamengo'
lista2 = list(texto)
print(lista2)

lista2 = texto.split(';')
print(lista2)

# Convertendo lista em string

lista = ["Torcida", "do", "Flamengo"]
print(lista)

# Abaixo estamos juntando os elementos da lista em uma
# string e separando pelo espaço(poderia ser ; por exemplo

texto = ' '.join(lista)
print(texto)

texto = ';'.join(lista)
print(texto)

# exemplo 2 - utilizando while

carrinho = []
produto = ''
while  produto!= 'sair':
    print('Adicione um produto na lista ou digite sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 6
num2 = 7
num3 = 8
num4 = 9
num5 = 0

numeros = [num1, num2, num3, num4, num5]
print(numeros)
"""
