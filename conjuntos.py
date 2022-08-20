"""
Conjuntos

- Conjuntos, em qualquer linguagem de programação, estão fazendo referencia aos conjuntos da matemática.

- Aqui no Python os conjuntos sao chamdos de Sets. Da mesma forma que na matemática:
- Sets não possuem valores duplicados;
- Sets não possuem valores ordenados;
- Sets não possuem indices.

São bons para ser utilizados quando precisamos armazenar elementos mas não importamos com a ordenação deles.

Os conjuntos são referenciados cm {}

Diferença entra conjuntos e mapas:
- Mapas tem chave e valor;
- Conjuntos tem apenas valores.

# Definindo um conjunto:
# Forma 1
conjunto = set({1, 2, 3, 5, 6, 7, 8, 9, 9})
print(conjunto)
print(type(conjunto))

# Ao incluir itens duplicados o conjunto não os armazenará, mas não vai gerar erros

#Forma 2 (mais comum)

conjunto = {1, 2, 3, 4, 5, 7, 1, 2}
print(conjunto)
print(type(conjunto))

conjunto = set("Torcida do Flamengo")
print(conjunto)
print(type(conjunto))

lista = [1, 2, 3, 4, 56, 7, 8, 1, 2, 3, 8]
print(lista)
print(set(lista))

tupla = (1, 3, 4, 656, 8, 9, 1, 3)
print(tupla)
print(type(tupla))
print(set(tupla))

conjunto = {1, 2, 3, 4, 5, 7, 1, 2}

# Localizando um valor no conjunto
if 3 in conjunto:
    print('localizou o 3')
else:
    print('Não localizou o 3')

# Importante lembrar que não temos valores duplicados e nem ORDEM

dados = [56, 7, 9, 44, 1, 2, 3, 4, 5, 7, 1, 2]

lista = (list(dados))

# Importante lembrar que não temos valores duplicados e nem ORDEM
print(f'Lista: {lista} com {len(lista)} elementos')
print(type(lista))

tupla = (tuple(dados))
print(f'Tupla: {tupla} com {len(tupla)} elementos')
print(type(tupla))

dicionario = {}.fromkeys(lista, 'dict')
print(f'Tupla: {dicionario} com {len(dicionario)} elementos')
print(type(dicionario))

conjunto = (set(dados))
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')
print(type(conjunto))

# Nos conjuntos, os tipos dos dados não precisam ser obrigatoriamente iguais

# Usos interessantes com sets(conjuntos)

cidades = ('Guará 1', 'Guará 2', 'Sobradinho', 'Gama', 'Guará 1', 'Asa Sul', 'Gama')
print(cidades)
print(len(cidades))

# Sem repetir
print(set(cidades))
print(len(set(cidades))

# Adicionando elementos em um conjunto
conjunto = {1, 2, 3, 5}
conjunto.add(7)
conjunto.add(7) # a duplicidade na inclusão não gera erro, simplesmente é ignorada
print(conjunto)

# Removendo
conjunto = {1, 2, 3, 5}

#Forma 1
conjunto.remove(5)
print(conjunto)
# não retorna valor removido
ret = conjunto.remove(3)
print(ret)


# Caso o valor que queremos remover não seja encontrado, dá erro
conjunto.remove(5)
print(conjunto)



#Forma 2
conjunto = {1, 2, 3, 5}
conjunto.discard(2)
print(conjunto)

# Caso o valor que queremos remover não seja encontrado, não ocorre erro
conjunto.discard(5)
print(conjunto)

# Copiando conjuntos (deep e shalow)

s = {1, 2, 3, 4}
print(s)
print(type(s))

# Forma 1 (deep copy)
novo = s.copy()
print(novo)
print(type(novo))

novo.add(8)
print(f'S: {s}')
print(f'novo: {novo}')

# Forma 2 (shalow copy)

s = {1, 2, 3, 4}
novo = s

print(novo)
print(type(novo))

novo.add(8)
print(f'S: {s}')
print(f'novo: {novo}')

# Podemos remover TODOS os itens de um conjunto

s = {1, 2, 3, 4}

print(f'Antes do clear: {s}')
s.clear()
print(f'Depois do clear: {s}')

# Métodos matemáticos de conjunto

estudante_python = {'Mário', 'Sérgio', 'Luciana', 'Ruth', 'Oto'}
estudante_java = {'Maria', 'Leandro', 'Ruth', 'Zeca'}

# juntar todos os alunos em um unico programa
#Forma 1 - Union

unico = estudante_java.union(estudante_python)
print(unico)

# Forma 2 - caracter pipe |
unicos2 = estudante_python | estudante_java
print(unicos2)

# Saber qual valor se repete

# Forma 1 - intersection

inter = estudante_python.intersection(estudante_java)
print(inter)

# Forma 2 - &

inter = estudante_python & estudante_java
print(inter)

# Saber qual valor não se repete

# Forma 1 - diference

somente_python = estudante_python.difference(estudante_java)
somente_java = estudante_java.difference(estudante_python)

print(f'Estudantes somente em Python: {somente_python}')
print(f'Estudantes somente em Java: {somente_java}')

# Soma, maior valor, minimo valor e tamanho (somente para valores inteiros ou reais
s = set((range(10)))
print(s)
print(type(s))

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
"""
s = set((range(10)))
print(s)
print(type(s))

print(sum(s))
print(max(s))
print(min(s))
print(len(s))