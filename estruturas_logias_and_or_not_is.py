"""
Estruturas lógias - AND(e) OR(ou) NOT(não) IS(é)

Operdores unários:
   - not

Operadores binários:
   - and, or, is
"""
ativo = input('Valor ATIVO:')
logado = input('Valor LOGADO:')

if ativo.upper() == 'SIM':
    ativo = True
else:
    ativo = False

if logado.upper() == 'SIM':
    logado = True
else:
    logado = False

# AND: as duas condições precisam ser verdadeira para a condição ser atendida
if ativo and logado:
    print('AND - Bem vindo usuário!')
else:
   print('AND - Você precisa ativar sua conta.')

# OR:  basta que somente umas das condições seja verdadeira para a condição ser atendida

if ativo or logado:
    print('OR - Bem vindo usuário!')
else:
   print('OR - Você precisa ativar sua conta.')

# NOT: o valor do booleano é invertido

if not ativo:
    print('NOT - Bem vindo usuário!')
else:
    print('NOT - Você precisa ativar sua conta.')

# IS:
if ativo is False:
    print('IS - Você precisa ativar sua conta.')
else:
    print('IS - Bem vindo usuário!')

if logado is False:
    print('IS - Você precisa logar na sua conta.')
else:
    print('IS - Usuário logado!')

# pode ser utilizado para vaidações:
nome = 'teste'
if nome.isupper():
   print('Maiusculo')
else:
    print('Minusculo')

if nome.isnumeric():
   print('Numerico')
else:
    print('Não numerico')

if nome.isspace():
   print('Espaços')
else:
    print('Não espaço')
