/*
* Disciplina : 2026-PCAP
* Problema : beecrowd 2165 - twitting
* Autor: Guiherme Antunes de Camargo
* LIAC: Le uma linha de texto (pode ter espaços). Se tiver até 140 caracteres imprime "TWERT"; se tiver mais, "MUTE!".
*/
#include <iostream>
#include <string>
using namespace std;

int main() {
    string texto;

    getline(cin, texto);
    if (texto.size() <= 140) {
        cout << "TWEET" << endl;
    } else {
        cout << "MUTE" << endl;
    }

    return 0;
}