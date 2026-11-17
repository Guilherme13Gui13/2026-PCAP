/*
* Disciplina : 2026-PCAP - 1234 Sentença Dançante 
* Autor: Guilherme Antunes de Camargo
* LIAC: Tranfomar ua frase em uma sentenca dançante, mudando as letras entre maiusculas e minusculas ignorando os espaços em branco.
*/
#include <iostream>
#include <string>
using namespace std;

int main() {
    int i;
    string s;

    while (getline(cin, s)) {
        int cont = 0;
        for (i = 0; i < s.size(); i++) {
            if (s[i] != ' ') {
                if (cont % 2 == 0) {
                    s[i] = toupper(s[i]);
                } else {
                    s[i] = tolower(s[i]);
                }
                cont++;
            }
        }
        cout << s << endl;
    }
}