/*
* Disciplina : 2026-PCAP - 2137 A biblioteca so senhor severino
* Autor: Guilherme Antunes de Camargo
* LIAC: ler códigos de livro e depois ordenar todos em ordem crescente mostrando linha por linha.
*/

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int i, n;
    string livros[1005];

    while (cin >> n) {
        for (i = 0; i < n; i++) {
            cin >> livros[i];
        }
        sort(livros, livros + n);

        for (i = 0; i < n; i++) {
            cout << livros[i] << endl;
        }
    }

    return 0;
}
