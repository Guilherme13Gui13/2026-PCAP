/*
* Disciplina : 2026-PCAP - 1168 LED
* Autor: Guilherme Antunes de Camargo
* LIAC: Calcular o número total de LEds necessários pra exibir um número em um painel de leds.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, i, j, total;
    string num;
    
    cin >> n;

    for (i = 0; i < n; i++) {
        cin >> num;
        total = 0;

        for (j = 0; j < num.size(); j++) {
            if (num[j] == '1') total += 2;
            else if (num[j] =='7') total += 3;
            else if (num[j] =='4') total += 4;
            else if (num[j] == '2' || num[j] == '3' || num[j] == '5') total += 5;
            else if (num[j] == '0' || num[j] == '6' || num[j] == '9') total += 6;
            else if (num[j] == '8') total += 7;
        }

        cout << total << " leds" << endl;
    }

    return 0;
}