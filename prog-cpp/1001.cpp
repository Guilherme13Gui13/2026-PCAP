/*
* Disciplina : 2026-PCAP
* Problema : beecrowd 1001 - Extremamente Basico
* Autor: Guiherme Antunes de Camargo
* LIAC: Le dois inteiros A e B, um por linha. Imprime a soma no formato "X = soma", com espaços em volta do sinal de igual.
*/
#include <iostream>

int main() {
    int a, b;

    std::cin >> a >> b;
    std::cout << "X = " << a + b << std::endl;

    return 0;
}