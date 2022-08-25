"""
Sistema de arquivos - Manipulação


import os

# descobrindo se uma arquivo ou diretório existe

# Arquivos
print(os.path.exists('arquivo.txt')) # Não localizou - FALSE
print(os.path.exists('fruta.txt')) # Localizou - TRUE

# Diretórios - relativos
print(os.path.exists('geek')) # Localizou - TRUE
print(os.path.exists('geek/university')) # Localizou - TRUE
print(os.path.exists('maria')) # Não localizou - FALSE

# Diretórios - absolutos(desde a raiz)
print(os.path.exists('/home/hermes/PycharmProjects/guppe/geek')) # Localizou - TRUE
print(os.path.exists('/home/hermes')) # Localizou - TRUE
print(os.path.exists('maria')) # Não localizou - FALSE

# Criando arquivos

# Forma 1
open('arquivo_teste.txt', 'w').close()

# Forma 2
open('arquivo_teste2.txt', 'a').close()

# Forma 3
with open('arquivo_teste3.txt', 'w') as arquivo:
    pass

# Forma 4 - MELHOR FORMA DE CRIAR ARQUIVOS

os.mknod('arquivo_teste4.txt')

os.mknod('/home/hermes/PycharmProjects/guppe/arquivo_teste5.txt')

# OBS1.: Se estiver utilizando no MAC-OS pode ocorre um erro de permissão
# OBS2.: Se o arquivo já existir, retornará erro de FileExistsError

# Criando pastas

os.mkdir('teste')

os.mkdir('teste')
# OBS.: Se a pasta já existir, retornará erro de FileExistsError

os.mkdir('/etc/teste')
# Se não tiver permissão para criar a pasta retornará PermissionError

# Não é possível criar varias pastas ao mesmo tempo. Devem ser criadas uma a uma

os.mkdir('templates/university/geek') # Retornou FileNotFoundError pq a pasta templates não existe

# Pode ser feito assim

os.mkdir('templates')
os.mkdir('templates/university')
os.mkdir('templates/university/geek')

OU

os.makedirs('templates2/university/geek')

"""

import os

# Criando pastas



