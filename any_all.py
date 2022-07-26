"""
Any e All

All() -> Função booleana que retorna true se todos os elementos do iterável são
verdadeiros ou se o iterável está vazio.


# Exemplo All:

print(all([0, 1, 2, 3, 4, 5])) # Retorna FALSE pq 0 == false

print(all([1, 2, 3, 4, 5])) # Retorna TRUE

print(all([])) # Retorna TRUE

nomes = ['Carla', 'Cristina', 'Camilla', 'Cora', 'Cleide']

print(all(nome[0] == 'C' for nome in nomes)) # Aqui verifico se TODOS os nome começam com a letra 'C'

nomes = ['Carla', 'Cristina', 'Camilla', 'Cora', 'Cleide', 'Deise']

print(all(nome[0] == 'C' for nome in nomes)) # Aqui vai dar FALSE

print(all(letra for letra in 'zxy' if letra in 'aeiou'))

print(all(num for num in [4, 2, 6, 4, 12] if num % 2 == 0))


Any: Função booleana que retorna true se algum dos elementos do iterável são
verdadeiros ou se o iterável está vazio.


print(any([0, 1, 2, 3, 4, 5])) # Retorna True pq pelo menos um é TRUE

print(any([0, 1, 2, 3, 4, 5])) # Retorna True pq pelo menos um é TRUE

nomes = ['Carla', 'Cristina', 'Camilla', 'Cora', 'Cleide', 'Deise']

# Aqui vai dar True pq pelo menos um inicia com eltra D
print(any(nome[0] == 'D' for nome in nomes))

# Nenhum numero é impar resultado FALSE
print(any(num for num in [4, 2, 6, 4, 12] if num % 2 == 1))
"""
