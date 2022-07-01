"""
Funções com retorno

# Funcoes que retornam valor

numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno pop: {ret_pop}')

ret_pr = print(numeros)
print(f'Retorno print: {ret_pr}')

# Funcao que não retorna valor

def quadrado_de_7():
    print(7 * 7)

OBS.: quando uma função python não retorna nada seu valor será none

OBS.: funcoes python que retornam valor utilizam a palavra reservada return

def quadrado_de_7():
    return(7 * 7)

OBS.: Não precisamos necessariamente criar uma variavel apra receber o retorno
de uma função. Podemos passar a execução para outras funções

print(quadrado_de_7())

# Refatorando a primeira função

def diz_oi():
    print("Oi!")

diz_oi()

def diz_oi():
    return 'Oi!'

print(f'Pedro diz {diz_oi()}')

OBS.: Sobre a palavra reservada return

1 - Ele finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes retornos;
3 -  Podemos, em uma função, retornar qualquer tipo de dado e até multiplos valores.

# Exemplo 1

def diz_oi():
    print('Executando antes do return')
    return 'OI!'
    print('Executando depois do return')

print(diz_oi())

# Exemplo 2

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'

print(nova_funcao())

# Exemplo 3

def outra_funcao():
    return 2 ,3 , 4, 5

num1, num2, num3, num4 = outra_funcao()

print(num1)
print(num2)
print(num3)
print(num4)

# OU

print(outra_funcao())

# Vamos criar uma função para receber o resultado de jogar uma moeda

def joga_moeda():
    # Gera numeros pseudo-randomicos entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'CARA'
    return 'COROA'

print(joga_moeda())

# Refatorando
from random import random
def joga_moeda():
    # Gera numeros pseudo-randomicos entre 0 e 1
    if random() > 0.5:
        return 'CARA'
    return 'COROA'

print(joga_moeda())

# Erros comuns na utilização de retorno, que na verdade nem são erros, mas codificação desnecessária:

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else: # Não há necessidade desse else
        return False

print(eh_impar())

# Melhor assim:

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False

"""
