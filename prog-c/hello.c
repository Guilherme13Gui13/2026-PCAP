/* Comentário de Bloco
Programa: Hello.c
Data: 2026.09.22
Autor: Guilherme Antunes de Camargo
*/

// Importa biblioteca padrão de entrada e saída
#include <stdio.h>

// Define a função principal do tipo int
int main(){
    // prinf == Saída --> Mostra na Tela 
    //"entre aspas == texto" 
    // comando se encerra com ;
    printf("Hello, World!\n");

    // Receber dois valores e somar e mostar o resultado

    // Declarar a variável
    int num1=0, num2=0, soma=0;
    printf("Digite dois valores separados por vírgula: ");
    scanf("%d %d", &num1, &num2);
    
    soma = num1 + num2;
    printf("O resultado é: %d\n", soma);

    // indica que chegou ao fim da função == retornando 0
    return 0;
}

/*
Para compilar ==
gcc <nome-do-arquivo> -o <nome-do-programa>

Para executar ==
./nome-do-programa
*/
