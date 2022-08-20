"""
Pacotes

"""

from collections import Counter
texto = """John Francis Jackson foi um ás da aviação australiano
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
 durante as campanhas do Norte de África e da Síria-Líbano."""

palavras = texto.split()
# print(palavras)
res = Counter(palavras)
print(res)

# Pegando as cinco palavras que mais aparecem
print(res.most_common(5))