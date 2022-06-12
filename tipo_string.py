"""
Tipo String

É do tipo string sempre:
- Estiver entre aspas simples;
- Estiver entre aspas duplas;
- Estiver entre aspas simples triplas;
- Estiver entre aspas duplas triplas;
"""

nome = 'Testando'
print(nome)
print(type(nome))

nome = "Testando"
print(nome)
print(type(nome))

nome = '''Testando'''
print(nome)
print(type(nome))

nome = """Testando"""
print(nome)
print(type(nome))

nome = """Testando
deu certo"""
print(nome)
print(type(nome))

nome = 'Testando'
print(nome.upper())
print(type(nome))

nome = 'Testando'
print(nome.lower())
print(type(nome))

print(nome[0:8])

print(nome[::-1])
