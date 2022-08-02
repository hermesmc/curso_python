"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

#def printf(texto):
#    return print(texto)

printf('Teste')

# Erros mais comuns

SyntaxError -> Ocorre quando Python encontra um erro de sintaxe, ou seja, você escreveu algo que o não
é reconhecido como parte da linguagem.

# Aqui faltam os parênteses depois do nome da função:

def funcao:
    print('Teste')

# Uso errado de palavra reservada

None = 1

NameError -> Oocrre quando uma variavel ou função não foi definida

Exemplo:

# O nome "teste" não foi definido.
print(teste)

#Função "teste" não foi definida
teste()

#Variavel local sendo usada fora do contexto
a = 20
if a > 100:
    msg = "Maior que 100"

print(msg)

TypeError -> Ocorre quando uma função/oeração /ação é aplicada a um tipo errado.

# A função len não pode ser utilizada com numerico. Ele verifica o tamanho de strings
print(len(5))

# Tentar concatenar uma string e uma lista vazia
print('Teste' + [])

IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de
dado indexado usando um indice inválido.

# Tentando acessar o elemento que não existe na lista
lista = ['a']
print(lista[5])

ValueError -> Ocorre quando uma função ou operação built-in recebe um argumento com tipo corretp
mas valor inapropriado.

#Tentando converter uma string para inteiro
print(int('teste'))

KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave inválida(inexistente)

# Tentar acessar a chave 'z' quando o dicionário não a possui
dic = {'a': 1}
print(dic['z'])

AttibuteError -> Ocorre quando uma variável não tem um atributo ou função

# A função sort() é usada SOMENTE em listas. Seu uso em tuplas gera um erro de atributo
tupla = (34, 6, 12 , 8, 9)
print(tupla.sort())

IndentationErro -> Ocorre quando a indentação está errada

#Após a definição da função é esperado a identação padrão de 4 espaços e não
#foi respeitado
def nova():
print('teste')

#Dentro do laço for a indentação também é esperada

x = 10
for i in x:
print(x)

OBS.: Exceptions e erros são sinônimos

"""
