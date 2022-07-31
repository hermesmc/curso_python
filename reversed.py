"""
Reversed

OBS.: Não confunda com a função reverse() estudadas nas listas.

lista = [2, 4, 6, 8, 9, 3, 1]
lista.reverse()
print(lista)

# tupla = (2, 4, 6, 8, 9, 3, 1)
# tupla.reverse()
# print(tupla)

# A função reverse() não funciona com nenhum tipo que não seja lista

A função reversed retorna um iterável chamado list reverset iterator

tupla = (2, 4, 6, 8, 9, 3, 1)
# Conversão para lista
print(list(reversed(tupla)))

# Conversão para conjunt(set)
print(tuple(reversed(tupla)))

# Conversão para conjunt(set) OBS. em conjunto s não definimos a ordem dos elementos
print(set(reversed(tupla)))

# Podemos iterar sobre o reversed

for letra in reversed('Torcida do Flamengo'):
   print(letra, end='')

print('-----------------------------------')

# Sem usar for
print(''.join(list(reversed('Torcida do Flamengo'))))

# Outra forma, mais simples
print('Torcida do Flamengo'[::-1])

print('-----------------------------------')

# Podemos também utilizar o reversed() para fazer loop reverso
for n in reversed(range(0, 30)):
    print(n)

# podemos fazer o reverse no proprio range
for n in range(9, -1, -1):
    print(n)

"""

