/*
* Disciplina : 2026-PCAP
* Problema : beecrowd 1011 - Esfera
* Autor: Guiherme Antunes de Camargo
* LIAC: Calcular o volume de uma esfera multiplicando (4.0 / 3.0) por pi e pelo raio ao cubo, forçando a divisão em ponto flutuante.
*/
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int r;
    double volume;

    cin >> r;
    volume = (4 / 3.0) * 3.14159  * r * r * r;
    cout << fixed << setprecision(3);
    cout << "VOLUME = " << volume << endl;

    return 0;
}