"""
Docstrings - Documentando funções

OBS.: Podemos ter acesso a documentação de uma função em Python
utilizando a propriedade especial "__doc__"

POdemos ainda fazer acesso a documentoação com 
a função "help"

# Exemplos

def diz_oi():
    #  Função simples que retona string OI
    return "OI"

print(diz_oi.__doc__)

"""

def exponencial(numero, potencia=2):
    """
    Função que retorna a potência de dois numeros sendo que o padrão da potencia, caso não informado, é 2
    :param numero: Numero que desejamos saber a potência
    :param potencia: Valor da potência, caso não informado por padrão será 2
    :return: Retorno do cálculo da potência
    """
    return numero ** potencia

print(exponencial.__doc__)
print(exponencial(3,3))


