"""
Loop for

Loop: estrutura de repetição
For: Uma dessas estruturas

Tabela de emaojis unicode:
https://apps.timwhitlock.info/emoji/tables/unicode
"""
nome = 'Torcida do Flamengo'
lista = [1, 5, 3, 4, 9, 7, 8]
numeros = range(0, 7) # no range o valor final não é inclusivo

for letra in nome:
    print(letra)
print('==================================')

for letra in nome:
    print(letra, end='')

print()
print('==================================')
# Outra forma

for indice, letra in enumerate(nome):
    print(letra)

print('==================================')
# descartando o [indice
for _, letra in enumerate(nome):
    print(letra)

print('==================================')
# descartando a letra
for indice, _ in enumerate(nome):
    print(indice)
"""
for numero in lista:
    print(numero)
"""
print('==================================')
for unidade in numeros:
    #print(unidade)
    print(lista[unidade])

# Emoji original = U+1F602
# Emoji modificado = U0001F602

emoji = '\U0001F602'

for num in range(1,11):
    print(emoji * num)

