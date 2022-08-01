"""
Len, Abs, Sum, round

Len(): retorna o tamanho, o número de itens de um iterável.

# Só revisando

print(len('Torcida do Flamengo'))

print(len([1, 2, 3, 4, 5, 6, 7])) # lista

print(len((1, 2, 3, 4, 5, 6))) # set

print(len({1, 2, 3, 4, 5, 6, 7, 8, 9})) #tupla

print(len({'a': 1, 'b': 2, 'c': 3})) #dicionário

print(len(range( 0,20 )))

# No uso da função len() op python faz:

print('Torcida do Flamengo'.__len__())

OBS.: toda função que inicia e termina com dois underlines se chama dunder, no caso dunder len

# ABS

abs(): retorna o valor absoluto de um numero interio ou real. Ou seja, seu valor sem sinalização.

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

print(abs('Teste')) # Gera erro

# Sum

sum() : recebe como parâmetro um iterável podendo receber u valor inicial e retorna soma total dos elementos
incluindo o valor inicial

OBS.: valor inicial default é zero

print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))

print(sum([1.31, 2.45, 3.11, 4.98, 5.7]))

print(sum((1.31, 2.45, 3.11, 4.98, 5.7)))

print(sum({1.31, 2.45, 3.11, 4.98, 5.7}))

print(sum({'a': 1.31, 'b': 2.45, 'c': 3.11, 'd': 4.98, 'e': 5.7}.values()))

print(sum('Torcida do Flamengo')) # não funciona com strings

# Round

round(): retorna um numero arredondado de n digitos. Se a precisão não for informada,
retorna o inteiro mais próximo da entrada.

print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(10.9))

print(round(10.298456349856, 3))

print(round(10.298556349856, 3))

"""
