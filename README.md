# Python
Pasta para estudos sobre Python

<h2>Instalação Windows</h2>

Instalação básica:
- Java JDK (lembrar de incluir no path o caminho C:\Program Files\Java\jdk-11.0.7\bin
- Python versão mais recente
- Pycharm

Verifique se o Java e Python foram instalados via prompt de comando: 
- java --version 
- python --version
- pip --version (gerenciador de pacotes python)

Atualizar o PIP:
- pip install --upgrade pip (utilize o cmd como administrador)

Instalar pacotes do PIP:
- pip install virtualenv virtualenvwrapper-win

Criar nova variável de ambiente para seu usuário(necessária para utilizar ferramentas para ambientes virtuais - criados na pasta do usuário):
- Clique em NOVO;
- Nome da variável: WORKON_HOME
- Valor da variável: c:\Users\herme\Envs

Para testar se a variavel nova está funcionando: 
- cmd;
- comando: echo %WORKON_HOME%
- deve retornar o valor da variável que foi estabelecido.

Criando ambiente virtual:
- cmd;
- mkvirtualenv guppe

Depois de instalar o PyCharm, entrar nele e criar novo projeto:
- Se já havia criado o ambiente virtual, coloque o mesmo nome do ambiente virtual: C:\Users\herme\PycharmProjects\ <b>guppe</b>
- Se não criou:

![inicio_pycharm](https://user-images.githubusercontent.com/49697760/172600809-2e3da281-a3a8-4fa0-80ba-06f2bc4946fc.jpg)

Veja que o nome colocado no fim do endereço em location será o mesmo do ambiente virtual. O ideal é que seja feito assim.

<h2>Instalação Linux</h2>

a) Instalar as dependências

sudo apt install build-essential zlib1g-dev libjpeg-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev sqlite3 liblzma-dev curl libbz2-dev

b) Baixar o fonte do Python

c) Descompactar o Python baixado

d) Com o terminal aberto no diretório do fonte executar:

	./configure --enable-optimizations --with-ensurepip=install

e) Compilar com o comando:

	make -j 2

f) Instalar com o comando:

	sudo make altinstall
	
g) Verifique se foi instalado com o comando:

	python3.x --version

	pip3.x --version

<h2>Ambiente Virtual</h2>

A razão para utilização de ambientes virtuais no desenvolvimento python é a possibilidade de ter versões diferentes de bibliotecas e do próprio python em diferentes projetos na mesma máquina sem que um interfira no outro.

<h2>PEP8 - Boas práticas</h2>

Style Guide for Python Code

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica

[1] - Utilize Camel Case para nomes de classes;

ex.:

class Calculador e não class calculadora

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

ex.:

def soma_dois():<br>
&nbsp;&nbsp;&nbsp;&nbsp;pass

numero_par = 4

[3] - Utilize 4 espaços para identação! (NÃO use tab)

if 'a' in 'banana'<br>
&nbsp;&nbsp;&nbsp;&nbsp;print("tem")

[4] - Linhas em branco
- Separar funções e definições de classes com duas linhas em branco;
- Metodos dentro de uma classe devem se separados por uma linha em branco

[5] - Imports
- Imports devem ser sempre feitos em linhas separadas

ex. errado:<br>
import sys, os

ex. certo:<br>
import sys<br>
import os

- Não há problema em utilizar:<br>
from types import StrigType, ListType

Para vários pacotes:<br>
from types import (<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;StringType,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ListType,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SetType,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OutroType<br>
)

- Os imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
antes de constantes e variáveis globais.

[6] - Espaçoes entre expressões e instruções

- Não faça:

funcao( algo[ 1 ], {outro: 2 } )

- Faça:

funcao(algo[1], {outro: 2}) 

- Não faça

x              = 1<br>
y              = 2<br>
variavel_longa = 3<br>

- Não faça

x = 1<br>
y = 2<br>
variavel_longa = 3<br>

[7] - Termine sempre uma instrução com uma nova linha

Deixe sempre uma linha em branco no final do programa
