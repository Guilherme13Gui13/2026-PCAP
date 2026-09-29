/* 
Problema 1037 Beecrowd
2026.09.29
Guilherme Antunes de Camargo
*/

#include <stdio.h>

int main() {
    int a, b;

    scanf("%d %d", &a, &b);

    if (a % b == 0 || b % a == 0) {
        printf("Sao Multiplos\n");
    } else {
        printf("Nao sao Multiplos\n");
    }

    return 0;
}