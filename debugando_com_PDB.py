"""
Debugando com PDB

PDB - Python DeBugger

# A utilização de print para debugar é uma prática ruim

def dividindo(a, b):
    print(f'a={a} e b={b}')
    try:
        return (int(a) / int(b))
    except (ValueError,ZeroDivisionError) as err:
        return f'Valor incorreto: {err}'

print(dividindo( 4 , 7))

# Existem formas mais profissionais para debugar utilizando o debugger
# Em Python, podemos fazer isso com diferentes IDEs, como o PyCHarm ou
# utilizando o PDB - Python Debugger


def dividindo(a, b):
    try:
        return int(a) / int(b)
    except (ValueError,ZeroDivisionError) as err:
        return f'Valor incorreto: {err}'

print(dividindo( 4 , 7))

# NO PYCHARM
# Clique com botão direito na coluna a esquerda do código. Deverá aparecer uma bolinha vermelha
# que representa um break point. Para executar clique com botão esquerdo e utilize a função
# debug 'debugando com PDB.

# Você pode monitorar um determinado trecho selecionando ele (no nosso caso aqui o calculo do
# return, clicar com botão direito e selecionar 'add to watches'

# Para ir de um break point para outro use o F8 para próxima instrução e F7 para retornar a anterior

# Usando o PDB

# Exemplo 1

# É necessário importar a biblioteca PDB e usar a função set_trace()

# Comandos básicos do PDB
# l (listar onde estamos)
# n (próxima linha)
# p (imprime variável)
# c (continua a excução - finaliza o debugging)


import pdb

nome = 'Jennifer'
sobrenome = 'Aniston'
pdb.set_trace() # inclusão manual de break point
nome_completo = nome + ' ' + sobrenome
curso = 'Programando com Python'
final = nome_completo + ' faz ourso ' + curso
print(final)

# Exemplo 2

nome = 'Jennifer'
sobrenome = 'Aniston'
import pdb;pdb.set_trace() # inclusão manual de break point
nome_completo = nome + ' ' + sobrenome
curso = 'Programando com Python'
final = nome_completo + ' faz ourso ' + curso
print(final)

# As vezes utilizamos o formato: import pdb;pdb.set_trace() # inclusão manual de break point

# O debug normalimente é utilizado no desenvolvimento. Costumamos realizar os importes de bibliotecas
# no início do arquivo. Por isso no lugar de colocar o import do pdb no início do código, colocamos onde
# vamos utilizá-lo e depois vamos retirar quando o código estiver OK.

# Exemplo 3 - A partir do  Python 3.7 não é mais necessário importar a biblioteca pdb pois a biblioteca
# foi integrada. Chamada breakpoint()

nome = 'Jennifer'
sobrenome = 'Aniston'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programando com Python'
final = nome_completo + ' faz ourso ' + curso
print(final)

# OBS.: Cuidado com conflitos entre nomes de variáveis e comandos do pdb. exemplo

breakpoint()
def soma(l, n, p ,c ):
    return l + n + p + c

print(soma( 1 , 2 , 3 , 4 ))

# Como o nome das variveis são os mesmos dos comandos do pdb, podemos utilizar o comando p
# para imprimrir os comandos das variáveis: p n (por exemplo)

"""

