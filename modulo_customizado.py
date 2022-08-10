"""
Módulos customizados

Como módulos python nada mais são do que arquivos puthon, então todos os programas(arquivos)
que criamos este curso são módulos python prontos para serem utilizados.

# foi importada a função soma_impares() do módulo funcoes_com_parametro
from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5]))

# Importar todo o módulo. Temos acesso a todos os elementos do módulo

import funcoes_com_parametro as fcp

print(fcp.tupla)
print(fcp.lista)

# Outro exemplo

from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))

"""

