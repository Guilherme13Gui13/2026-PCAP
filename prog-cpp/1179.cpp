/*
* Disciplina : 2026-PCAP - 1179 Preenchimento em Vetor IV
* Autor: Guilherme Antunes de Camargo
* LIAC: Ler 15 numeros inteiros e separa eles em dois vetores de 5 posicoes para pares e impares.
*/

#include <iostream>
using namespace std;

int main() {
    int par[5], impar[5];
    int j, i, p = 0, im = 0, x;

    for (i = 0; i < 15; i++) {
        cin >> x;
        if (x % 2 == 0) {
            par[p] = x;
            p++;
            if (p == 5) {
                for (j = 0; j < 5; j++) {
                    cout << "par[" << j << "] = " << par[j] << endl;
                }
                p = 0;
            }
        } else {
            impar[im] = x;
            im++;
            if (im == 5) {
                for (j = 0; j < 5; j++) {
                    cout << "impar[" << j << "] = " << impar[j] << endl;
                }
                im = 0;
            }
        }
    }
    for (i = 0; i < im; i++) {
        cout << "impar[" << i << "] = " << impar[i] << endl;
    }
    for (i = 0; i < p; i++) {
        cout << "par[" << i << "] = " << par[i] << endl;
    }

    return 0;
}