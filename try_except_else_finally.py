"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

- Toda entrada deve ser tratada

OBS.: A funçãdo usuário é destruir seu sistema

A utilização de ELSE e FINALLY não são comuns

# Exemplo 1

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou {num}')

# Exemplo 2

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou {num}')
finally:
    print('Executou finally')

print(f'Fim do bloco  ')

# O bloco finally é sempre executado, independente de exceção ou não.

# O finally é utilizado para fechar ou desalocar recursos

# Exemplo 3

def dividir(a, b):
    return (a / b)

try:
    num1 = int(input('Informe o primeiro número: '))
except ValueError:
    print('Digite um número válido')
else:
   try:
       num2 = int(input('Informe o segundo número : '))
   except ValueError:
       print('Digite um número válido')
   else:
      print(f'Resultado: {dividir(num1, num2)}')

# Refatorando

# Você é reponsável pelas entradas das suas funções. Então trate-as

def dividindo(a, b):
    try:
        return (int(a) / int(b))
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possivel dividir um valor por ZERO.'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número : ')

print(dividindo(num1, num2))

# Tratamento de erro genérico

def dividindo(a, b):
    try:
        return (int(a) / int(b))
    except
        return 'VAlor incorreto.'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número : ')

print(dividindo(num1, num2))

# Tratamento de erro semi-genérico

def dividindo(a, b):
    try:
        return (int(a) / int(b))
    except (ValueError,ZeroDivisionError) as err:
        return f'Valor incorreto: {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número : ')

print(dividindo(num1, num2))
"""




