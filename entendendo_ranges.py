"""
Ranges

- Precisamos conhecer o loop FOR para usar ranges
- Precisamos conhecer o RANGE para trabalhar melhor com loops FOR

Ranges são utilizados para gerar sequencias numéricas não de forma aleatoria,
mas de maneira especificada.

Formas gerais:

# Forma 1
range(valor_de_parada)
OBS.: valor_de_parada não inclusive (início padrão = 0, e passo de 1 em 1)

for num in range(11):
    print(num)

# Forma 2
range(valor_de_inicio, valor_de_parada)
OBS.: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

for num in range(1, 11):
    print(num)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo
OBS.: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

for num in range(1, 11, 2):
    print(num)

# Forma 4 (ingual a 3 inversa)
range(valor_de_inicio, valor_de_parada, passo
OBS.: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)

for num in range(55, 0, -5):
    print(num)

"""
lista = list(range(10))
print(lista)


