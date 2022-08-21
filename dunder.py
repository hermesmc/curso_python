"""
Dunder Name & Dunder Main

Dunder significa = dobble under

Dunder name -> __name__

Dunder main -> __main__

Em python são utilizados para criar funções, atributos, propriedades, etc utilizando o double under para não gerar
conflito com o nome desses elementos na programação.

Ex.:

Na linguagem C, temos um programa da seguinte forma:

int main(){

   return 0;

}

Na linguagem Java, temos um programa da seguinte forma:

public static void main(String[] args){

}

Na linguagem Python, se executarmos um módulo Python direto na linha de comando, internamente
o Python atribuirá a variavel __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.

lista = [1, 2, 3, 4 , 5, 6, 7]
print(soma_impares(lista))

tupla = 1, 2, 3, 4 , 5, 6, 7
print(soma_impares(tupla))

"""

import primeiro
import segundo