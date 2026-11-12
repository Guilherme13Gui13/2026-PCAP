/*
* Disciplina : 2026-PCAP - 1173 Array Fill I
* Autor: Guilherme Antunes de Camargo
* LIAC: Ler um inteiro e guardar ele em N[0], depois preencher as posicoes de 1 a 9 com o valor dobrado da posicao anterior.
*/

#include <iostream>
#include <vector>
using namespace std;

void preencher(vector<int> &n, int primeiro) {
    int i;

    n.push_back(primeiro);
    for (i = 1; i < 10; i++) {
        n.push_back(n[i - 1] * 2);
    }
}

void mostrar(vector<int> &n) {
    int i, qtd = n.size();

    for (i = 0; i < qtd; i++) {
        cout <<"N[" << i << "] = " << n[i] << endl;
    }
}

int main() {
    vector<int> n;
    int primeiro;

    cin >> primeiro;
    preencher(n, primeiro);
    mostrar(n);

    return 0;
}