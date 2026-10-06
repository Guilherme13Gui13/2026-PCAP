/*
Problema 1178 Beecrowd
2026.10.05
Guilherme Antunes de Camargo
*/

#include <stdio.h>

int main() {
    double n[100];
    int i;

    scanf("%lf", &n[0]);

    for (i = 1; i < 100; i++) {
        n[i] = n[i - 1] / 2;
    }

    for (i = 0; i < 100; i++) {
        printf("N[%d] = %.4f\n", i, n[i]);
    }

    return 0; 
}


