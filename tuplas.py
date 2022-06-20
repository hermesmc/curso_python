"""
Tuplas - tuple

1 - As tuplas são representadas por parenteses ou sem;
2 - As tuplas são imutáveis. Toda operação gera uma nova tupla
3 - Tuplas são definidas pelo uso do parênteses e não dos parenteses

tupla = (9, 2, 3, 4, 5, 6, 7)
print(tupla)
print(type(tupla))

tupla2 = 9, 2, 3, 4, 5, 6, 7
print(tupla2)
print(type(tupla2))

# Tuplas com 1 elemento (definida pelo uso da virgula e não do parenteses

tupla3 = (3) # não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (3, ) # é uma tupla
print(tupla4)
print(type(tupla4))

# Podemos gerar tuplas dinamicamente com Range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
tupla = "Torcida do Flamengo", "José Geraldo"
Maria, Mario = tupla # O numero de elementos e de variáveis para desempacotar deve ser sempre igual

print(tupla)
print(type(tupla))

print(Maria)
print(type(Maria))
print(Mario)
print(type(Mario))

# Metodos para adição e remoção de elementos em tuplas não existem.

# Soma, máximo, mínimo e tamanho funcionam
tupla = tuple(range(11))
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenando valores de tuplas

tupla = 1, 2, 3
print(tupla)

tupla2 = 4, 5, 6
print(tupla2)

tupla = tupla + tupla2 # As tuplas são imutáveis, mas podemos sobreescrever
print(tupla)
print(tupla2)

# Localizando valores em tuplas
tupla = tuple(range(11))

valor = '4'
if valor in tupla:
    print(valor + " - valor localizado")
else:
    print(valor + " achou não")

valor = '34'
if valor in tupla:
    print(valor + " - valor localizado")
else:
    print(valor + " achou não")

# Localizando valores em tuplas
tupla = 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho'
print(tupla.index('março'))

# Slicing
print(tupla[0:6:2])

# Porquê utilizar tuplas?
- São mais rápidas do que listas
- Deixam seu código mais seguro

"""






