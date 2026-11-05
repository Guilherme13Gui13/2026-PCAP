/*
* Disciplina : 2026-PCAP
* Problema : beecrowd 1551 - Frase completa
* Autor: Guiherme Antunes de Camargo
* LIAC: ler uma frase e determinar se a frase possui todas a letras do alfabeto, ou mais da metade, identificando se ela é completa quae completa ou mal elaborada.
*/
#include <iostream>
#include <string>
using namespace std;

int conta_letras(string frase) {
    int total = 0, i, tam = frase.size();
    char letra;
    bool achou;

    for (letra = 'a'; letra <= 'z'; letra++) {
        achou = false;
        for (i = 0; i < tam; i++) {
            if (frase[i] == letra) {
                achou = true;
            }
        }
        if (achou) {
            total++;
        }
    }
    return total;
}

int main() {
    int n, i, letras;
    string frase;

    cin >> n;
    cin.ignore();
    for (i = 0; i < n; i++) {
        getline(cin, frase);
        letras = conta_letras(frase);
        if (letras == 26) {
            cout << "frase completa" << endl;
        } else if (letras >= 13) {
            cout << "frase quase completa" << endl;
        } else {
            cout << "frase mal elaborada" << endl;
        }
    }

    return 0;
}