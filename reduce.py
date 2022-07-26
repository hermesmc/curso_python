"""
Reduce

OBS.: A partir da versão 3 do Python, o reduce não é mais uma versão integrada.
Agora temos de importar para utilizar essa função a partir do modúlo: "functools"

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo
caso, 99% das vezes um loop for é mais legivel.

Para entender o reduce()

- Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

E você tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

Assim como map() e filter(), reduce() recebe dois parâmetros: a função e o iterável.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:

passo1: res1 = f(a1, a2) => Aplica a função nos dois primeiros elementos da coleção e
guarda o resultado.
passo2: res2 = f(res1, a3) => Aplica a função passando o resultado do passo1 mais o
terceiro elemento e guarda o resultado.

Isso é repetido até o final...

## Exemplos

from functools import reduce

dados = [1, 2, 3, 4]

# Para utilizar o reduce é necessário uma função que recebe os dois parâmetros

multip = lambda x, y: x * y

res = reduce(multip, dados)
print(res)

# Refatorando

dados = [1, 2, 3, 4, 5, 6, 7]

res = reduce(lambda x, y: x * y, dados)
print(res)

# O mesmo resultado sem reduce

res = 1
for n in dados:
    res = res * n

print(res)

"""
