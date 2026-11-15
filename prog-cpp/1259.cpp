/*
* Disciplina : 2026-PCAP - 1259 Pares e Impares Ordenados
* Autor: Guilherme Antunes de Camargo
* LIAC: Ler N e depois N inteiros. Imprime os pares em ordem crescente e depois os impares em ordem decrescente, linha por linha.
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

void mostrar(vector<int> &v) {
    int i , qtd = v.size();

    for (i = 0; i < qtd; i++) {
        cout << v[i] << endl;
    }
}

int main() {
    vector <int> pares, impares;
    int n, x, i;

    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> x;
        if (x % 2 == 0) {
            pares.push_back(x);
        } else {
            impares.push_back(x);
        }
    }

    sort(pares.begin(), pares.end());
    sort(impares.begin(), impares.end(), greater<int>());

    mostrar(pares);
    mostrar(impares);

    return 0;
}