/*
* Disciplina : 2026-PCAP
* Problema : beecrowd 1002 - Área do Círculo
* Autor: Guiherme Antunes de Camargo
* LIAC:  Calcular a área multiplicando pi pelo raio ao quadrado com variáveis double, definindo a precisão em 4 casas decimais com fixed e setprecision(4).
*/
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double r, area;
    
    cin >> r;
    
    area = 3.14159 * r * r;
    
    cout << fixed << setprecision(4);
    cout << "A=" << area << endl;
    
    return 0;
}