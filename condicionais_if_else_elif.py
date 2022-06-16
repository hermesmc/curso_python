"""
Estruturas condicionais - IF ELSE ELIF


"""
ano = ' '
ano_correto = False
while not ano_correto:
    if ano.isnumeric():
        ano_correto = True
        ano2 = int(ano)
    else:
        ano = input("Digite o ano atual: ")

idade = ' '
idade_correta = False
while not idade_correta:
    if idade.isnumeric():
        idade_correta = True
        idade2 = int(idade)
    else:
        idade = input("Digite o ano que você nasceu: ")

idade2 = ano2 - idade2

if idade2 < 18:
    print("==> Menor de idade")
elif idade2 == 18:
    print("==> igual 18")
elif idade2 == 19:
    print("==> igual 19")
elif idade2 == 20:
    print("==> igual 20")
else:
    print("==> Pode entrar")
