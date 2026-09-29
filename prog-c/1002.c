/*
Problema 1002 Beecrowd
2026.09.22
Guilherme Antunes de Camargo
*/

#include <stdio.h>

int main(){
    double raio=0, area=0, n= 3.14159;
    scanf("%lf", &raio);
    area = n * (raio*raio);
    printf("A=%.4lf\n", area);
    return 0;
}