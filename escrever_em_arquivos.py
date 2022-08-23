"""
Escrever em arquivos


OBS.: Ao abrir um arquivo para leitura, não podemos efetuar a escrita. Da mesma forma, se for aberto
para escreta, não pode ser lido.

# Exemplo de escrita, usando modo W = WRITE

with open("novo.txt", 'w') as arquivo:
    arquivo.write('Escrever em arquivos é muito fácil.\n')
    arquivo.write('Incluimos quantas linhas quisermos\n')
    arquivo.write('Ultima linha\n')

# Lendo só pra testar
with open('novo.txt') as arquivo:
    print(arquivo.readlines())

# Exemplo forma tradicional não pythonica

arquivo = open("test.txt", "w")
arquivo.write('Escrever em arquivos é muito fácil.\n')
arquivo.write('Incluimos quantas linhas quisermos\n')
arquivo.write('Ultima linha\n')
arquivo.close()

with open('test.txt') as arquivo:
    print(arquivo.readlines())

# Exemplo 3

with open('test2.txt', 'w') as arquivo:
    arquivo.write('Torcida do Flamengo\n' * 1000)

with open('test2.txt') as arquivo:
    print(arquivo.readlines())

# Escrevendo dados recebidos pelo usuário em arquivo

with open("fruta.txt", 'w') as arquivo:
    while True:
        fruta = input("Escreva uma fruta ou digite sair: ")
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break

with open('fruta.txt') as arquivo:
    print(arquivo.readlines())


"""

