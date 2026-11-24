# Fliperama em C++ (MeuApp v4.0)

## O que e
E um fliperama que possui um jogo, onde voce pode pode cadastrar jogadores e jogar usando eles o jogo adivinhe o numero

## Como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama
./fliperama

## Arquivos
- fliperama.cpp: E o arquivo que guarda o codigo do jogo
- jogadores.csv: E o arquivo que guarda os jogadores (primeira coluna) e as partidas jogadas (segunda coluna), e com base nele que se pode jogar com o mesmo jogador.

## C x C++: o que mudou
| O que | No fliperama.c (linha) | No fliperama.cpp (linha) |
|---|---|---|

| guardar um jogador | strcpy(apelidos[qtd], novo) (l. 74) | apelidos.push_back(novo) (l. 98)), 

| comparar apelidos | strcmp(apelidos[i], procurado) == 0 (l. 52) | apelidos[i] == procurado(l. 57) |

| a funcao que cadastra | int cadastrar(char apelidos[][TAM_APELIDO], int partidas[], int qtd) (l. 59) | void cadastrar(vector<string> &apelidos, vector<int> &partidas) (l. 87)

## O que o C++ decidiu por mim
Em C, eu precisava definir um tamanho fixo de jogadores, ja em C++ o vector aumenta sozinho conforme novos jogadores entram.

## Autoavaliacao
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|

| 1. Estrutura, compilacao e Git |estrutura |A| todo o código segue a estrutura que o prof passou fliperama.cpp |

| 2. Cadastro: vectors e referencia |vectors|A|linhas 87 a 143 fliperama.cpp|

| 3. Jogo e partidas |jogo|A|linhas 115 a 144 fliperama.cpp|

| 4. Persistencia |Persistencia|B|linhas 157 a 182, o jogo salva tudo antes de desligar fliperama.cpp|

| 5. Documentacao e comparacao |Documentação|A|linhas 1 a 39 README.md|