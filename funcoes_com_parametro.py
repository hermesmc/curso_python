"""
Funções com parâmetro (de entrada)

- Funções que recebem dados para serem processados

Se pensarmos em um programa qualquer, temos:

Entrada -> Processamento -> Saída

Se formos pensar em funções, sabemos que podemos ter funções:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não saída;
- Não possuem entrada, mas possuem saída;
- Possuem entrada e saída.

# Refatorando uma função

def quadrado(numero):
    # return numero*numero
    return numero ** 2

print(quadrado(7))
print(quadrado(6))
print(quadrado(9))

print(quadrado( )) # TypeError

def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidade')
    print('Muitos anos de vida')
    print('Viva o aniversariante!!!')

# Refatorando

def cantar_parabens(nome):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidade')
    print('Muitos anos de vida')
    print(f'Viva {nome}!!!')

cantar_parabens('José')

# Funções podem ter "n" parâmetros de entrada
# POdemos receber quantos parâmetros quantos forem necessários

# Exemplo

def soma(a, b):
    return a+b
print(soma(1, 5))

def funcao(a, b, c):
    return (a + b) * c
print(funcao(3, 5, 2))
print(funcao(3, 5, 'Maria '))

# OBS.: Se a quantidade de parametros informada for errada, vai dar TypeError

# nomeando parâmetros

def nome_completo(nome, sobrenome):
    return (f'Seu nome completo é {nome} {sobrenome}')

print(nome_completo('José', 'Arimatéia'))

# Diferença entre parâmetros e Argumentos:
# Parâmentos são variaveis declaradas na definição de uma função
# argumentos são dados informados na execução de uma função

# erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4 , 5, 6, 7]
print(soma_impares(lista))

tupla = 1, 2, 3, 4 , 5, 6, 7
print(soma_impares(tupla))

"""

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4 , 5, 6, 7]
print(soma_impares(lista))

tupla = 1, 2, 3, 4 , 5, 6, 7
print(soma_impares(tupla))