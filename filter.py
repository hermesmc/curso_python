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

#OU

res = filter(lambda x: len(x) > 0, paises)
print(list(res))

#Refatorando
res2 = filter(None, paises)
print(list(res2))

#  A diferença entre MAP e FILTER:
# map() -> Recebe dois parametros, uma função e um iterável e retorna um objeto mapeando a função
# para cada elemento do iterável

# filter() -> Recebe dois parametros, uma função e um iterável e retorna um objeto filtrando apenas
# os elementos de acordo com a função

# Então cada item iterado que entra na função map retorna ao chamador, na função filter, que retorna
# de forma booleana, retornam somente os true( ou false)

usuarios = [
    {"username": "Manuel", "Tweets": ["Eu gosto de balinhas", "Eu não gosto de chcolate"]},
    {"username": "Antonia", "Tweets": ["Eu gosto de Gin"]},
    {"username": "Carmem", "Tweets": []},
    {"username": "João", "Tweets": ["Eu fui dormir"]},
    {"username": "Luis", "Tweets": ["Vi Maria hoje", "Trabalhei muito", "Hj tá pago"]},
    {"username": "Julia", "Tweets": []}
]

# OBJETIVO: filtar os inativos no Tweeter (sem nenhum tweet)

print(usuarios)
inativos = list(filter(lambda usuario: len(usuario['Tweets']) == 0, usuarios))
print(inativos)


# inativos = list(filter(lambda uusario: len(usuario['Tweets']) == 0, usuarios))
print(list(filter(lambda usuario: len(usuario['Tweets']) == 0, usuarios)))

# REFATORANDO

inativos = list(filter(lambda usuario: not usuario['Tweets'], usuarios))
ativos = list(filter(lambda usuario: usuario['Tweets'], usuarios))
print(inativos)
print(ativos)

usuarios = [
    {"username": "Manuel", "Tweets": ["Eu gosto de balinhas", "Eu não gosto de chcolate"]},
    {"username": "Antonia", "Tweets": ["Eu gosto de Gin"]},
    {"username": "Carmem", "Tweets": []},
    {"username": "João", "Tweets": ["Eu fui dormir"]},
    {"username": "Luis", "Tweets": ["Vi Maria hoje", "Trabalhei muito", "Hj tá pago"]},
    {"username": "Julia", "Tweets": []}
]

# OBJETIVO: filtar os inativos no Tweeter (sem nenhum tweet)

print(usuarios)
inativos = list(filter(lambda usuario: len(usuario['Tweets']) == 0, usuarios))
print(inativos)


# inativos = list(filter(lambda uusario: len(usuario['Tweets']) == 0, usuarios))
print(list(filter(lambda usuario: len(usuario['Tweets']) == 0, usuarios)))

# REFATORANDO

inativos = list(filter(lambda usuario: not usuario['Tweets'], usuarios))
ativos = list(filter(lambda usuario: usuario['Tweets'], usuarios))
print(ativos)

# Combinando FILTER e MAP

nomes = ['Vanessa', 'Mariana', 'Roberta', 'Jussara', 'Anna', 'Bia']

#Devemos criar uma lista contendo: "Sua instrutora é: + nome", desde que cada
# nome tenha menor de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é: {nome}.', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

"""

usuarios = [
    {"username": "Manuel", "Tweets": ["Eu gosto de balinhas", "Eu não gosto de chcolate"]},
    {"username": "Antonia", "Tweets": ["Eu gosto de Gin"]},
    {"username": "Carmem", "Tweets": []},
    {"username": "João", "Tweets": ["Eu fui dormir"]},
    {"username": "Luis", "Tweets": ["Vi Maria hoje", "Trabalhei muito", "Hj tá pago"]},
    {"username": "Julia", "Tweets": []}
]

inativos = list(filter(lambda usuario: not usuario['Tweets'], usuarios))
ativos = list(filter(lambda usuario: usuario['Tweets'], usuarios))
print(ativos)
