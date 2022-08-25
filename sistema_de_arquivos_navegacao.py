"""
Sistema de Arquivos - Navegação

Para fazer uso de manipulação de arquivos do SO precisamos importar e fazer uso do módulo OS.

os -> Operating System

import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente.
# Retorna o caminho absolutp
caminho = os.getcwd() # Atual: /home/hermes/PycharmProjects/guppe
print(caminho)

# chdir() -> para mudar o diretorio

os.chdir('..')
caminho = os.getcwd() # Agora: /home/hermes/PycharmProjects
print(caminho)

os.chdir('..')
caminho = os.getcwd() # Agora: /home/hermes
print(caminho)

os.chdir('..')
caminho = os.getcwd() # Agora: /home
print(caminho)

os.chdir('..')
caminho = os.getcwd() # Agora: /
print(caminho)

os.chdir('..')
caminho = os.getcwd() # Agora: /
print(caminho)

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('/home/geek/')) # Linux

print(os.path.isabs('c:\\home\\geek ')) # Windows

# name -> Identificando o sistema operacional

print(os.name) # posix = Linux/Mac e nt para Windows

# Para mais detalhes do SO

print(os.uname())

import sys - > aqui mostra o nome do SO

print(sys.platform)

# Acessando uma pasta

caminho = os.getcwd()
print(caminho) # /home/hermes/PycharmProjects/guppe

res = os.path.join(caminho, 'geek')
os.chdir(res)

print(os.getcwd()) # /home/hermes/PycharmProjects/guppe/geek

# O comando os.path.join recebe dois parâmetros sendo o primeiro um caminho e o segundo o que será
# acrescentado ao caminho

# Podemos listar os diretórios com listdir()


caminho = os.listdir('/etc')
quantidade = len(os.listdir('/etc'))
print(caminho)
print(quantidade)


# Mais detalhes da pasta scandir()

scanner = os.scandir('/etc')

caminho = list(os.scandir('/etc'))
print(caminho)
print('-------------------------------------')
print(caminho[0].name)         # nome do arquivo
print(caminho[0].inode())      # Identificador do node
print(caminho[0].is_dir())     # Se é um diretório
print(caminho[0].is_file())    # Se é um arquivo
print(caminho[0].is_symlink()) # É um symlink
print(caminho[0].path)         # Caminho até o arquivo
print(caminho[0].stat())       # Estatísticas sobre o arquivo

# Depois de usar o scandir(), devemos fechá-la
scanner.close()

"""

