"""
List Comprehension - P2

Podemos adicionar estruturas condicionais lógicas as list comprehension

# Exemplo 1

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# REFATORAR

# Qualquer numero módulo de 2 com resto 0 é considerado FALSE pelo python, logo

pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)
"""

# Exemplo 2 - Aqui cada numero impar será dividido por 2
# e cada numero par será multiplicado por 2

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
res = [numero * 2 if not numero % 2 else numero /2 for numero in numeros]
print(res)
