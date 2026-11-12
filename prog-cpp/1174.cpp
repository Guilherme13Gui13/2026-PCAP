/*
* Disciplina : 2026-PCAP - 1174 Seleção em Vetor I
* Autor: Guiherme Antunes de Camargo
* LIAC: Le 100 numeros reais em um vector, depois mostra com posicao os que são menores ou iguais ao 10, com uma casa decimal.
*/

#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main() {
    vector<double> a;
    double x;
    int i, qtd;

    for (i = 0; i < 100; i++) {
        cin >> x;
        a.push_back(x);
    }

    qtd = a.size();
    cout << fixed << setprecision(1);
    for (i = 0; i < qtd; i++) {
        if(a[i] <= 10) {
            cout << "A[" << i << "] = " << a[i] << endl;
        }
    }

    return 0;
}