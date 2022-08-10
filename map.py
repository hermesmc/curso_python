"""
Map

Com o map fazemos o mapeamento de valores para função.

import math

def area(r):
    # calculo area de um circulo com raio "r"
    return math.pi * (r ** 2)


print(area(2))
print(area(3))

raios = [2, 3, 5, 7.1, 10, 40]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Utilizando map
# Map é uma função que recebe dois parâmetros: o primeiro é uma função e o segundo um iterável

areas = map(area, raios)
print(list(areas))

# Utilizando map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: após utilizar a função map, após a utilização do primeiro resultado ele zera.

# mais um exemplo - cidades e temperaturas em graus celsius

cidades = [('Berlin', 28),('Madri', 23),('Paris', 19),('Tokio', 22),('São Paulo', 25),
           ('Londres', 22), ('Buenos Aires', 20)]

print(cidades)

# convertendo para fahrenheit - f = 9/5 * c + 32

c_para_f = lambda dado: (dado[0], round(9/5 * dado[1] + 32))
print(list(map(c_para_f, cidades)))
"""

cidades = [('Berlin', 28),('Madri', 23),('Paris', 19),('Tokio', 22),('São Paulo', 25),
           ('Londres', 22), ('Buenos Aires', 20)]

print(cidades)

# convertendo para fahrenheit - f = 9/5 * c + 32

c_para_f = lambda dado: (dado[0], round(9/5 * dado[1] + 32))
print(list(map(c_para_f, cidades)))

