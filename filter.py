"""
Filter

Serve para filtar dados de uma determinada coleção.

valores = 1, 2, 3, 4, 5, 6, 7, 8

media = (sum(valores) / len(valores))
print(media)

# boblioteca para trabalhar com dados estatísticos
import statistics

dados = [1.3, 4.1, 3.2, 6.1, 0.9]

# Calculando a media com a função mean()

media = statistics.mean(dados)
print(media)

# OBS.: Assim como a função map(), a função filter() recebe dois parâmetros
# sendo uma função e um iterável

res = filter(lambda x: x > statistics.mean(dados), dados)
print(list(res))

# Retirar dados faltantes
paises = ['', 'Argentina', 'Bolivia', '', 'Peru', '', '' , 'Equador', ' Colombia']

res = filter(lambda x: x != '', paises)
print(list(res))

#Refatorando
res2 = filter(None, paises)
print(list(res2))

"""


