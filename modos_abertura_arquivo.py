"""
Modos de abertura arquivo

r -> abre para leitura - padrão
w -> abre para escrita. Sobreescreve caso o arquivo já exista
x -> abre para escrita somente se o arquivo não existir. Caso exista gera FileExistError
a -> abre para escrita acrescentando no fim do arquivo quando existir. SEMPRE.

http://docs.python.org/3/library/function.html#open

# Exemplo modo "X"
try:
    with open('test2.txt', 'x') as arquivo:
        arquivo.write('Torcida do Flamengo\n' * 1000)
except FileExistsError:
    print("Arquivo já existe")

with open('test2.txt') as arquivo:
    print(arquivo.readlines())

# Exemplo modo "a"
with open("fruta.txt", 'a') as arquivo:
    while True:
        fruta = input("Escreva uma fruta ou digite sair: ")
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break

with open('fruta.txt') as arquivo:
    print(arquivo.readlines())

# Exemplo incluindo no início do arquivo

with open('outro.txt', 'a') as arquivo:
    arquivo.seek(0)
    arquivo.write('Teste de inclusão no início-1.\n')
    arquivo.write('Teste de inclusão no início-2.\n')
    arquivo.write('Teste de inclusão no início-3.\n')

# Esse exemplo não funciona

with open('outro.txt', 'r+') as arquivo:
    arquivo.seek(0)
    arquivo.write('Teste de inclusão no início-6.\n')
    arquivo.write('Teste de inclusão no início-2.\n')
    arquivo.write('Teste de inclusão no início-3.\n')

"""



