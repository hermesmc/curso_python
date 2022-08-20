"""
Módulos externos

Utilizamos o gerenciador de pacotes pytho chamado PIP - Python Installer Package

Para conhecer todos os pacotes oficiais no link abaixo:
https://pypi.org

Pacotes:

Colorama: utilizado para permitir a impressão de textos coloridos no terminal

from colorama import init, Fore, Back, Style

init()

print(Fore.RED + "Torcida do Flamengo")
print("Teste")

print(Style.RESET_ALL)

print(Back.GREEN + "Torcida do Flamengo")

print(Style.RESET_ALL)
print("Teste")

"""

import pydf
pdf = pydf.generate_pdf('<h1>Torcida do Flamengo</h1>')
with open('test_hermes_doc.pdf', 'wb') as f:
    f.write(pdf)

