"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
   - Permissão de leitura -> para ler o arquivo
   - Permissão de escrita -> para escrever no arquivo

StringIO -> utilizado para ler e criar arquivos em memória.

# Fazendo import do stringIO
from io import StringIO

mensagem = 'Esta é uma string normal\n'

arquivo = StringIO(mensagem)
# Instrução equivalente ao open

print(arquivo.read())
arquivo.write('Mais uma linha de texto.\n')
arquivo.seek(0)
print(arquivo.read())
"""
