"""
Módulo Collections - Deque

O Deque é uma lista de alta performance

"""

# Importação

from collections import deque

#Criando deques

deq = deque("Flamengo")

print(deq)
print(type(deq))
print(deq.index('F'))

# Adicionando elementos

# No final da lista
deq.append('W')
print(deq)
print(deq.index('F'))


# A esquerda da lista(início)
deq.appendleft('Z')
print(deq)
print(deq.index('F'))

# Removendo itens

# Remove o ultimo elemento
deq.pop()
print(deq)
print(deq.index('F'))

# Remove o primeiro elemento
deq.popleft()
print(deq)
print(deq.index('F'))