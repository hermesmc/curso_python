"""
Bloco With

Sequencia que vimos até agora:
1 - Abrir o arquivo;
2 - Manipular o arquivo;
3 - Fechar o arquivo.

O bloco With é utilizado para criar um contexto de trabalho onde os
recursos utilziados são  fechados apos o bloco with.

OBS.: Forma mais utilizada para leitura e manipulação de arquivos:
# Exemplo

with open('texto.txt') as arquivo:
    print(arquivo.readlines())

# O próprio contexto criado pelo with abre(quando é utilizado) e fecha(quando encerrado) o arquivo

"""

