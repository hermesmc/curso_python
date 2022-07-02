"""
Funções com parâmetro padrão (Default Parameters)

- Funções onde a passagem de parâmetros seja opcional;

# Exemplo

print('Teste de passagem')

print()

# Exemplo (quando uma função precisa receber um parametro(obrigatório)
def quadrado(numero):
    return numero ** 2

print(quadrado(2))
print(quadrado()) # TypeError

# Exemplo, ao colocar um valor padrão, se não for informado, utiliza esse valor

def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(5,3))
print(exponencial(5)) # sem o parametro vai usar o padrão

OBS.: em funções python com valores padrao DEVEM sempre estar no final da declaração

Exemplo:

def teste(num1=2, num2): # Desta forma não vai funcionar
    return num1 * num2

# Exemplo
def soma(num1=0, num2=0): # inicializando as todas tb funciona
    return num1 + num2

print(soma(5, 7))
print(soma(5))
print(soma())

# Exemplo mais complexo

def mostra_informacoes(nome='Heisen', instrutor=False):
    if instrutor:
        if nome == 'Heisen':
            return f'Bem vindo instrutor {nome}'
        return f'Bem vindo instrutor'
    else:
        return f'Bem vindo {nome}'

print(mostra_informacoes('Mauro', True))
print(mostra_informacoes('Mauro'))
print(mostra_informacoes(instrutor=True))
print(mostra_informacoes())

# Exemplo - passando uma funcao como parametro

def soma (num1, num2):
    return num1 + num2

def subtracao (num1, num2):
    return num1 - num2

def mat (num1, num2, fun=soma):
    return fun(num1, num2)

print(mat(5, 6))
print(mat(1, 2, soma))
print(mat(1, 2, subtracao))

# Escopo

# - Variaveis globais
# - Variaveis locais

# Exemplo

prof = 'Hermes' # Variavel prof é global pois não está restrita a uma função

def diz_oi():
    return f' Olá {prof}'

print(diz_oi())

# Exemplo
prof = 'Hermes'

def diz_oi():
    prof = 'José'
    return f' Olá {prof}'

print(diz_oi()) # vai retornar o valor local da funcao
print(prof)     # vai mstrar o valor global

# Exemplo

def diz_oi():
    prof = 'José'
    return f' Olá {prof}'

print(diz_oi())
print(prof) # Aqui dá erro pq a variavel foi declarada dentro da funcao, então só será reconhecida dentro dela

# Exemplo

total = 0

def incrementa():
    total = total + 1 # para uma operação a variavel deve ser iniciada dentro da operação
    return total

print(incrementa())

# Exemplo - arrumando a função anterior

total = 0

def incrementa():
    global total # Aqui indicamos que deve ser utilizada a variavel global
    total = total + 1
    return total

print(incrementa())

# Podemos ter funções declaradas dentro de funções. Tem uma forma especial de escopo de variavel

def fora():
    contador = 0
    def dentro():
        nonlocal contador # indica que a variavel não é global e não é local, está na função anterior
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())
"""



