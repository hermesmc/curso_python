"""
Seek e Cursors

seek() -> é utilizada para movimentar o cursor dentro do arquivo. Ela recebe um parâmetro que indica onde
queremos colocar o cursor.

arquivo = open('texto.txt')
print(arquivo.read())
arquivo.seek(25)
print(arquivo.read())

readline() -> Função que lê o arquivo linha a linha

arquivo = open('texto.txt')
ret = arquivo.readline()
print(ret.split())

print(arquivo.readlines())

OBS.: Quando abrimos um arquivo com open(), é criada uma conexão entre o arquivo aberto e o programa.
Essa conexão é chamada de streaming. Ao finalizar a utilização do arquivo. Para isso devemos usar a função close().


Passos para utilizar um arquivo:


1 - Abrir o arquivo
2 - Trabalhar com o arquivo;
3 - Fechar o arquivo.

# Quantidade de linhas

# 1
arquivo = open('texto.txt')

# 2
linhas = len(arquivo.readlines())
print(linhas)

# Verifica se o arquivo está aberto ou fechado
print(arquivo.closed)

# 3
arquivo.close()


# Verifica se o arquivo está aberto ou fechado
print(arquivo.closed)

OBS.: Se tentarmos manipular um arquivo fechado, será gerado um ValueError

# Imprime somente os primeiros 18 caracteres

arquivo = open('texto.txt')
print(arquivo.read(18))

"""

