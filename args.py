"""
Args - Entendendo *Args

- O *args é um parâmetro de entrada como outro quanlquer.
Isso significa que você poderá chamar de qualquer coisa,
desde que comece com asterisco.

Exemplo: *xis

Mas por convenção, urilizamos *args para defini-lo.

O que é o "args"

O parâmetro "arps" utilizado em uma função, coloca os valores
extras informados com entrada em uma tupla. Então desde já
lembre-se que tuplas são imutáveis.

# Exemplo

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(5, 7, 2))

# print(soma_todos_numeros(3, 9)) # TypeError

# print(soma_todos_numeros(3, 6, 7, 2)) #TypeError

# Entendendo o args

#def soma_todos_numeros(*args):
#    total = 0
#    for numero in args:
#       total = total + numero
#    return total

#OU

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 7, 4))
print(soma_todos_numeros(1, 9, 2, 5))

# Outros exemplo de utilização do args

def verifica_info(*args):
    if 'Torcida do' in args and 'Flamengo' in args:
        return 'Bem vindo'
    else:
        return 'Não é bem vindo'

print(verifica_info())
print(verifica_info(1, True, 'Torcida do', 'Flamengo'))
print(verifica_info(1, 'Flamengo', 4.888, 'Torcida do'))

"""

def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 7, 4))

numeros = [5, 2, 8, 4, 9, 5, 7]

# print(soma_todos_numeros(numeros)) => Aqui dá erro

# Para reseolver este problema use o desempacotador

print(soma_todos_numeros(*numeros))

# O asterisco m serve para que informemos ao python
# que estamo passando uma coleção de dados. Desta forma
# ele saberá que deve antes desempacotar esses dados.
# funciona tanto com listas quanto com tuplas. Dicionários não.




