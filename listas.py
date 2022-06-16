"""
Listas

LIstas em Python funcionam como vetores/matrizes (arrays em outras linguagens), com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

- Dinâmico: Não possui tamaanho fixo, ou seja podemos criar a lista e ir adicionando elementos;
- Qualquer tipo de dado: não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.

As listas em python são representadas por colchetes []
"""
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

