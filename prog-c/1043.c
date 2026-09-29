/*
Problema 1000 Beecrowd
2026.09.29
Guilherme Antunes de Camargo
*/
#include <stdio.h>

int main() {
    float a, b, c;

    scanf("%f %f %f",&a, &b, &c);


    if (a < b + c && b < a + c && c < a + b) {
        printf("Perimetro = %.1f\n", a + b + c);
    } else {
        printf("Area = %.1f\n", ((a + b) * c) / 2.0);
    }

    return 0;
}