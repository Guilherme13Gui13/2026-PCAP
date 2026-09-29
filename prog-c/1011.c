/*
int == Inteiros Positivos e Negativos == %d
float == Casas decimais == %f
double == Ponto Flutuante de dupla precisão == %lf
*/
/*
Problema 1011 Beecrowd
2026.09.22
Guilherme Antunes de Camargo
*/

#include <stdio.h>

int main(){
    double r=0, v=0;
    scanf("%lf", &r);
    v = (4.0/3.0)*3.14159*(r*r*r);
    printf("VOLUME = %.3lf\n", v);
    return 0;
}