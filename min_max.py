"""
Min e Max


min() = retorna o menor valor em um iterável ou o menor de dois ou mais elementos
max() = retorna o maior valor em um iterável ou o maior de dois ou mais elementos

lista = [1, 5, 98, 32, 2, 56, 300]

print(max(lista))
print(min(lista))

tupla = [3, 5, 98, 32, 2, 56, 299]

print(max(tupla))
print(min(tupla))

conj = {3, 5, 98, 32, 2, 56, 299}

print(max(conj))
print(min(conj))

print('-----------------------------------')
dicionario = {1: 3, 2: 5, 3: 98, 4: 32, 5: 2, 6: 56, 7: 299}

print(max(dicionario.keys()))
print(min(dicionario.keys()))
print(max(dicionario.values()))
print(min(dicionario.values()))

print('-----------------------------------')
print(max(3, 67))

# Faça um programa que receba dois valores do usuário e mostre o maior

val1 = int(input('Informe um valor: '))
val2 = int(input('Informe outro valor: '))

print(f'O maior é: ', max(val1, val2))
print(f'O menor é: ', min(val1, val2))

# Qual o maior/menor TAMANHO dos nomes

nomes = ['Anna', 'Ana', 'Daniele', 'José', 'Roberto', 'Zacarias', 'Rinovaldo']

print(max(nomes, key=lambda tamanho: len(tamanho)))
print(min(nomes, key=lambda tamanho: len(tamanho)))

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 223},
    {'titulo': 'Back in Black', 'tocou': 159},
    {'titulo': 'Master of Puppets', 'tocou': 44},
    {'titulo': 'War Pigs', 'tocou': 95}
]


print(max(musicas, key=lambda tamanho: tamanho['tocou']))
print(min(musicas, key=lambda tamanho: tamanho['tocou']))
print('-----------------------------------')
print(max(musicas, key=lambda tamanho: len(tamanho['titulo'])))
print(min(musicas, key=lambda tamanho: len(tamanho['titulo'])))

# Imprimindo somento o titulo
print('-----------------------------------')
print(max(musicas, key=lambda tamanho: tamanho['tocou'])['titulo'])
print(min(musicas, key=lambda tamanho: tamanho['tocou'])['titulo'])


# Como encontrar a musica mais tocada e menos sem lambda e max/min
# Veja o trabalho que dá sem essas funções: max() e min()

maior = 0
for musica in musicas:
    if musica['tocou'] > maior:
        maior = musica['tocou']

for tocar in musicas:
    if tocar['tocou'] == maior:
        nome_musica = tocar['titulo']

print(f'Tocou mais: ', nome_musica)

menor = 10000000
for musica in musicas:
    if musica['tocou'] < menor:
        menor = musica['tocou']

for tocar in musicas:
    if tocar['tocou'] == menor:
        nome_musica = tocar['titulo']

print(f'Tocou menos: ', nome_musica)

maior = 0
menor = 100000000
for musica in musicas:
    if musica['tocou'] > maior:
        maior = musica['tocou']
        nome_musica1 = musica['titulo']
    if musica['tocou'] < menor:
        menor = musica['tocou']
        nome_musica2 = musica['titulo']

print(f'Tocou mais: ', nome_musica1)
print(f'Tocou menos: ', nome_musica2)

"""

