"""
Módulo Collections - Counter(Contador)

Collections -> High-performance Countainer Date

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter
que é paredcido com um dicionário, contendo como chave o elemento da lista passada como
parâmetro e como valor e quantidade de ocorrências desse elemento.

# Utilizando o counter
from collections import Counter

# Exemplo 1
#podemos utilizar qualquer iterável
lista = [1, 2, 2, 3, 3, 3, 1, 1, 1, 5, 4, 20, 32, 88, 32, 56, 81, 31]
print(lista)
print(type(lista))

# Utilizando o counter
res = Counter(lista)
print(res)
print(type(res))

# Veja que para cada elemento da lista o Counter trouxe a quantidade
# de vezes que ele se repete colocando como chave cada um desses elementos
# e como valor essa quantidade

# Exemplo 2

from collections import Counter
print(Counter('Torcida do Flamengo'))

# Pegando as cinco palavras que mais aparecem
texto = John Francis Jackson foi um ás da aviação australiano
e comandante de esquadrão durante a Segunda Guerra Mundial.
Jackson foi creditado com oito vitórias aéreas e liderou o
Esquadrão N.º 75 durante a Batalha de Port Moresby em 1942.
Nascido em Brisbane, era criador de gado e empresário que operava
o seu próprio avião particular quando ingressou na Reserva da Real
Força Aérea Australiana (RAAF) em 1936. Chamado para o serviço
activo após a eclosão da guerra em 1939, serviu no Esquadrão N.º
23 na Austrália antes de ser destacado para o Médio Oriente em
novembro de 1940. Como piloto de caça no Esquadrão N.º 3 ele
pilotou aviões Gloster Gladiator, Hawker Hurricane e P-40 Tomahawk
 durante as campanhas do Norte de África e da Síria-Líbano.

palavras = texto.split()
# print(palavras)
res = Counter(palavras)
print(res)

# Pegando as cinco palavras que mais aparecem
print(res.most_common(5))
"""

