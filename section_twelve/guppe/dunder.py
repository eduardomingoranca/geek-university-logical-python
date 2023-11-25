"""
Dunder Name  e Dunder Main

Dunder -> Doble Under

Dunder Name -> __name__

Dunder Main -> __main__

Em Python, sao utilizados dunder para criar funcoes, atributos, propriedades e etc utilizando
Double Under para nao gerar conflito com os nomes desses elementos na programacao.

# Na linguagem C, temos um programa da seguinte forma:

int main(){
   return 0;
}


# Na linuagem Java, temos um programa da seguinte forma:

public static void main(String[] args) {

}

# Em Python, se executarmos um modulo Python diretamente na linha de comando, internamente
o Python atribuira a variavel __name__ o valor __main__ indicando que este modulo eh o
modulo de execucao principal.


Main -> Significa principal.

from funcoes_com_parametro import soma_impares


print(soma_impares([1, 2, 3, 4, 5, 6]))
"""

import primeiro
import segundo
