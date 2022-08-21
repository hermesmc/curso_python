def funcao1():
    print('Torcida do Flamengo - primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('primeiro.py está sendo executado diretamente.')
else:
    print(f'primeiro.py está sendo importado. {__name__}')
