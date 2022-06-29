"""
Definindo funções

- Funções são pequenas partes do código que fazem tarefas específicas;
- Pode ou não receber dados de entrada e retornar uma saída;
- Muito uteis para tarefas repetitivas;

OBS.: Se você escrever uma função que realiza várias tarefas dentro dela,
é bom fazer uma verificação para simplificá-la.

Já autilizamos várias funções como:
- print()
- len()
- max()
- min()
- count()
- dentre outras...

# DRY - Don´t repeat yourself - Não se repita

# Exemplo de utilização de funções

cores = ['vermelho', 'verde', 'azul', 'amarelo', 'rosa']

# Usando uma função integrada (Built-in) do Python

print(cores)

# Função que não recebe parâmetros

cores.clear()
print(cores)

# Como definir funcoes

EM Python a forma geral para definição de funções:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:
- nome_da_funcao sempre com letras minúsculas e separadas por underline;
- parâmetros de entrada são opcionais e, caso mais de um, separados por vírgulas;
- bloco da função é onde o processamento da função acontece;

OBS.: Para definir uma função usamos a palavra reserva "def".

# Definindo funcoes

def diz_oi():
    print("Oi")

diz_oi()


def diz_oi(nome):
    print(f"Oi {nome}")

diz_oi('José')
"""



