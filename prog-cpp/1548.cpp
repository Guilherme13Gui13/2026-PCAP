/*
* Disciplina : 2026-PCAP - 1548 Fila da Cantina
* Autor: Guilherme Antunes de Camargo
* LIAC: Ler N casos de teste, em cada um M notas, na ordem dos estudantes. Uma fila é reodenada da maior para a menor nota, mostrar quantos estudantes ficaram na mesma posição.
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int na_mesma_posicao(vector<int> &fila) {
    vector<int> ordenada = fila;
    int i, iguais = 0, qtd = fila.size();

    sort(ordenada.begin(), ordenada.end(), greater<int>());

    for (i = 0; i < qtd; i++) {
        if (fila[i] == ordenada[i]) {
            iguais++;
        }
    }
    return iguais;
}

int main() {
    vector<int> fila;
    int n, m, nota, caso, i;

    cin >> n;
    for (caso = 0; caso < n; caso++) {
        fila.clear();
        cin >> m;
        for (i = 0; i < m; i++) {
            cin >> nota;
            fila.push_back(nota);
        }
        cout << na_mesma_posicao(fila) << endl;
    }

    return 0;
}