/*
* Disciplina : 2026-PCAP
* Problema : beecrowd 1332 - one two three
* Autor: Guiherme Antunes de Camargo
*/
#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, i;
    string s;

    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> s;
        if (s.size() == 5) {
            cout << 3 << endl;
        } else if ((s[0] == 'o' && s[1] == 'n' ) || (s[0] == 'o' && s[2] == 'e') || (s[1] == 'n' && s[2] == 'e')) {
            cout << 1 << endl;
        } else {
            cout << 2 << endl;
        }
    }

    return 0;
}