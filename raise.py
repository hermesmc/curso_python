"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS.: Raise não é uma função. É uma palavra reservada assim como def ou qualquer outra em Python.

Simplificando: pense no raise como sendo algo útil para que possamos criar nossas proprias exceções
e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro('mensagem de erro')

raise ValueError('Valor incorreto')

OBS.: O ise, assim como return, finaliza a função. Ou seja, nada após o raise é executado.

Exemplo 1

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("O texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("A cor precisa ser uma string")
    print(f'O texto: "{texto}" será impresso na cor {cor}')

# Execução OK
#colore('Teste de texto', 'amarelo')

# Execução com erro
colore('Teste de texto', 4)

# Exemplo 1 refatorado

def colore(texto, cor):
    cores = ('vermelhor', 'preto', 'azul', 'amarelo')
    if type(texto) is not str:
        raise TypeError("O texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("A cor precisa ser uma string")
    elif cor not in cores:
        raise ValueError(f'A cor informada "{cor}" é inválida')
    print(f'O texto: "{texto}" será impresso na cor {cor}')

# Execução OK
colore('Teste de texto', 'vermelha')

"""
