"""
Navegação

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
"""

import os


