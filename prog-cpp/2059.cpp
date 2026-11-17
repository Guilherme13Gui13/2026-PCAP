/*
* Disciplina : 2026-PCAP - 2059 Par, Impar ouu roubo
* Autor: Guilherme Antunes de Camargo
* LIAC: Determinar um ganhador do jogo, considerando a escolha do playe, a soma dos numeros e o roubo e a acusação.
*/

#include <iostream>
using namespace std;

int main() {
    int p, j1, j2, r, a;
    cin >> p >> j1 >> j2 >> r >> a;

    if (r == 1 && a == 1) {
        cout << "Jogador 2 ganha!" << endl;
    } else if (r == 1 && a == 0) {
        cout << "Jogador 1 ganha!" << endl;
    } else if (r == 0 && a == 1) {
        cout << "Jogador 1 ganha!" << endl;
    } else {
        if ((j1 + j2) % 2 == 0 && p == 1) {
            cout << "Jogador 1 ganha!" << endl;
        } else if ((j1 + j2) % 2 != 0 && p == 0) {
            cout << "Jogador 1 ganha!" << endl;
        } else {
            cout << "Jogador 2 ganha!" << endl;
        }
    }

    return 0;
}
