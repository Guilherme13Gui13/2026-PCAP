/*
Problema 1000 Beecrowd
2026.09.29
Guilherme Antunes de Camargo
*/

#include <stdio.h>

int main(){
    int n, i;

    scanf("%d", &n);

    for (i = 1; i <= 10; i++){
        printf("%d x %d = %d\n", i, n, i * n);
    }

    return 0;

}