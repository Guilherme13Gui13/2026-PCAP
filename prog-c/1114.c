/*
Problema 1114 Beecrowd
2026.10.05
Guilherme Antunes de Camargo
*/

#include <stdio.h> 

int main(){
    int senha;

    scanf("%d",&senha);

    while (senha != 2002) {
        printf("Senha Invalida\n");
        scanf("%d", &senha);
    }

    printf("Acesso Permitido\n");

    return 0;
}