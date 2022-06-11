"""
Recebendo dados do usuário

input() -> Todo tipo de dados recebido via input é uma string
"""

# Entrada de dados
# print("Qual seu nome: ")
# nome = input()
# print("Em que ano nasceu: ")
# ano = input()

nome = input("Qual seu nome: ")
ano = int(input("Em que ano nasceu: "))

if (ano > 2022):
    print("Você veio do futuro?")
else:
    total = 2022 - ano
    print(f'{nome} tem {total} anos.')
"""
int(ano) está fazendo cast

Cast é a conversão de um tipo de dados para outro
"""

# Exemplo antigo de print - python 2x
# print('%s tem %s anos.' % (nome, idade))

# Exemplo mais novo de print - python 3x
#print('{0} tem {1} anos.' .format (nome, idade))

# Exmplo print mais atual
# print(f'{nome} tem {total} anos.')
