"""
Sorted

OBS.: Não confundir com a função sort() que já foi vista em listas. O sort() só funciona em listas.
Podemos utilizar o sorted() com qualquer iterável. Ele serve para ordenar elementos.

# Ordenação convencional de listas

lista = [6, 4, 5, 2, 3, 9, 1, 8, 7]
print(lista)
lista.sort()
print(lista)

# E o sort() só funciona com listas


# Usando Sorted

numeros = [6, 4, 5, 2, 3, 9, 1, 8, 7]
print(sorted(numeros))

tupla = (33, 55, 11, 22)
print(sorted(tupla))

Sets = {323, 515, 171, 232}
print(sorted(Sets))

# OBS.: O retorno da função sorted() sempre será uma lista

numeros = [6, 4, 5, 2, 3, 9, 1, 8, 7]
print(sorted(numeros))
print(sorted(numeros, reverse=True)) # Ordenação inversa

print(tuple(sorted(numeros))) # Convertendo para tupla
print(set(sorted(numeros)))   # Convertendo para set

# Podemos usar em coisas mais complexas

usuarios = [
    {"username": "Manuel", "tweets": ["Eu gosto de balinhas", "Eu não gosto de chcolate"]},
    {"username": "Antonia", "tweets": ["Eu gosto de Gin"]},
    {"username": "Carmem", "tweets": [], "cor": 'Amarelo'},
    {"username": "João", "tweets": ["Eu fui dormir"], "cor": 'Amarelo', "Musica": 'Rock'},
    {"username": "Luis", "tweets": ["Vi Maria hoje", "Trabalhei muito", "Hj tá pago"]},
    {"username": "Julia", "tweets": [], "cor": 'Preta'}
]

print(usuarios)

# print(sorted(usuarios)) => para dicionários devemos informar a chave para que ele consiga ordenar

print(sorted(usuarios, key=len))

#Ordenando pelo nome do usuário

print(sorted(usuarios, key=lambda usuario: usuario["username"]))

#Ordenando pela quantidade de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

# Exemplo gracinha do Hermes

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 123},
    {'titulo': 'Back in Black', 'tocou': 59},
    {'titulo': 'Master of Puppets', 'tocou': 44},
    {'titulo': 'War Pigs', 'tocou': 85}
]
condicao = False
ordem_tocada = sorted(musicas, key=lambda musica: musica['tocou'], reverse=condicao)

# Imprimindo do menor para o maior
print(ordem_tocada)

# Imprimindo do maior para o menor
condicao = True
print(ordem_tocada)

"""




