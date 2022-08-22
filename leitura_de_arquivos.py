"""
Leitura de arquivos

Para ler  o conteúdo de um arquivo em Python, utilizamos a função integrada open(), que significa literalmente abrir.

open() -> A forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que neste caso é o caminho do
arquivo a ser lido. Essa função retorna um __io.TextIOWrapper e é com ela que trabalhamos então.

documentação: https://docs.python.org/3/library/functions.html#open

OBS.: Por padrão a função open abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o erro
FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>

mode='r' => Modo de leitura (read)

# Exemplo

arquivo = open('texto.txt')
print(arquivo)
print(type(arquivo))

print('----------------------------------')
# Para a leitura do arquivo devemos usar a função read()

print(arquivo.read())
# O Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor funciona como o cursor
# quando estamos escrevendo.

print(arquivo.read())
# sendo assim esse segundo print não vai retornar nada

# A função read() lê todo o conteúdo do arquivo.

ret = arquivo.read()
print(type(ret))

"""


