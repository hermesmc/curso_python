"""
**KWargs - ele é só mais uma parâmetro, mas diferente do *args, que coloca valores extras em uma tupla, o **kwargs
           exige que utilizemos parâmentros nomeados e transforma esses parâmetros extras em um dicionário.

Poderíamos chamr esse parametro de qualquer nome: **qualquercoisa, mas por convenção chamamos de **kwargs

Exemplo 1

def cores_favoritas(**kwargs):
    print(type(kwargs))
    print(kwargs)

cores_favoritas(marcos='verde', jose='azul', joel='marron')

Melhorando

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', jose='azul', joel='marron')


#OBS.: Os parâmetros *args e **kwargs não são obrigatórios

cores_favoritas()
cores_favoritas(marcos='verde', jose='azul', joel='marron')

Exemplo 2

def cumprimento_especial(**kwargs):
    if 'torcida' in kwargs and kwargs['torcida'] == 'Flamengo':
         return 'Você é muito especial.'
    elif 'torcida' in kwargs:
        return f"Torcida do {kwargs['torcida']}! Eca"
    return 'Não sei quem vc é...'

print(cumprimento_especial())
print(cumprimento_especial(torcida='Flamengo'))
print(cumprimento_especial(torcida='Fluminense'))

# Nas nossas funções podemos ter (NESTA ORDEM):
- Parâmetros obrigatórios
- Args
- Parâmetros defaul (não obrigatórios)
- kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos ')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)
    print('------------------------')

minha_funcao(8, 'Julia')
minha_funcao(18, 'Maria', 4, 5, 3, solteiro=True)
minha_funcao(38, 'José', 9, 4, 1, java=False, python=True)

# Porquê é importante manter essa ordem???

# Ordem correta
def minha_funcao(a, b, *args, solteiro='Solto', **kwargs):
     return [a, b, args, solteiro, kwargs]

print(minha_funcao(1, 2, 3, sobrenome='Silva', cargo='Instrutor'))

# Ordem errada

def minha_funcao(a, b, solteiro='Solto', *args, **kwargs):
    return [a, b, solteiro, args, kwargs]

print(minha_funcao(1, 2, 3, sobrenome='Silva', cargo='Instrutor'))

# Desempacotar com kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'André','sobrenome': 'Silva'}

print(mostra_nomes(**nomes))

def soma_numeros(a, b, c):
    return a+b+c

lista = [1, 5, 3]
tupla = (6, 3, 4)
conjunto = {6, 2, 9}
dicionario = dict(a=6, b=2, c=9)

print(soma_numeros(*lista))
print(soma_numeros(*tupla))
print(soma_numeros(*conjunto))

# O nome das chaves em um dicionário deve ser iguais aos da função
print(soma_numeros(**dicionario))

# Exemplo diferente
dicionario = dict(x=6, b=2, z=9)
print(soma_numeros(**dicionario)) #TypeError
"""
