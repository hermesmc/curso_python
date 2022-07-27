"""
Generator expression

Em aulas anteriores vimos:
- List comprehension;
- Dictionary comprehension;
- Set comprehension.

Nõa vimos:
- Tuple comprehension

Não vimos pq se chamam generations

Ele utiliza menos recursos da maquina

nomes = ['Carlos', 'Carla', 'Camilla', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes])


# Poderiamos ter feito da seuinte forma

nomes = ['Carlos', 'Carla', 'Camilla', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))

# List comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Pra que serve o getsizeof: retorna quantidade de bytes
# em memoria do objeto passado em parâmetro
from sys import getsizeof

# Mostra quantos bytes a string "Flamengo" ocupa em memória
print(getsizeof('Flamengo'))

print(getsizeof('Torcida do Flamengo'))

print(getsizeof(82))

print(getsizeof(8435342))

print(getsizeof(True))

# Mostrando que o Generator gasta menos memória
from sys import getsizeof

list_comp = getsizeof([x * 10 for x in range(1000)])

set_comp = getsizeof({x * 10 for x in range(1000)})

dict_comp = getsizeof({x: x * 10 for x in range(1000)})

gen = getsizeof(x * 10 for x in range(1000))

print(list_comp)
print(set_comp)
print(dict_comp)
print(gen)

# Eu posso iterar no generation expression? SIM

gen = (x * 10 for x in range(10))
print(gen)

for num in gen:
    print(num)

"""

