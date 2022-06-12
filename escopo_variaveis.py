"""
Escopo de variaveis

Dois casos de escopo
1 - Variáveis globais: são reconhecidas em todo o programa

2 - Variáveis locais: são reconhecidas apenas no bloco onde são declaradas

Para declarar variáveis no python fazemos:

nome_da_variável = valor_da_variável

Python é uma liguagem de tipágem dinâmica, ou seja, quando declaramos uma
variável, não precisamos determinar o tipo dela. O tipo é inferido quando
é atribuído um valor a mesma
"""

numero = 42
print(numero)
print(type(numero))

if numero > 10:
    novo = numero + 10
    print(novo)

print(novo)
