# 🔢 Par ou Ímpar
​
Jogo de Par ou Ímpar feito em Python na disciplina PCAP (Aula 18).
Você joga contra o computador em uma melhor de 5 rodadas, com placar, estatística e histórico de partidas.
​
## ▶️ Como jogar
1. Abra o terminal na pasta do jogo.
2. Rode: python par_impar4.py
3. A cada rodada, escolha a aposta (par ou ímpar) e um número de 0 a 5.
4. Ao fim das 5 rodadas, o programa mostra o placar final. Se quiser jogar novamente só escrever no terminal "sim".
​
## ⚙️ Como funciona (resumo)
Os pontos da máquina (pm) e os pontos do jogador (pj) são definidos.
A lista do histórico é criada.
Tudo é indentado pelo while.
tudo é indentado pelo for.
A cada rodada o computador sorteia um número (random.randint) e lê o seu.
A aposta é limpa (.lower().strip()) e validada (in) antes de usar.
A soma dos dois números define a paridade com o operador % (resto).
Uma função decide quem venceu e o programa soma os pontos das 5 rodadas.
​O jogo mostra a opção de jogar novamente.
Caso não, ele mostra o histórico de partidas.


## 🧠 O que eu pratiquei
- Operador de resto (%): descobrir se a soma é par ou ímpar
- Funções (def/return): isolar a regra do jogo (quem venceu)
- random.randint: sortear o número da máquina
- int(input()): ler o número do jogador
- Métodos de texto (.lower().strip()) e validação com in: tratar a aposta
- Repetição (for): jogar as 5 rodadas e manter o placar
- Repetição (while): repetir o programa se o jogador escrever sim.
​
## 🎯 Autoavaliação
Conceito pretendido: A
​
Justificativa (cite arquivo e linha de cada critério):
- O jogo funciona ............: par_impar4.py, linhas 9 a 88
- Funções e operador % .......: par_impar4.py, linha 34 (def/return, soma % 2)
- Documentação e Git .........: este README + commits no GitHub
- Extensão/originalidade .....: par_impar4.py, linha 10 e 11 (criei a opção de poder jogar novamente e criei uma estatística/histórico de jogadas). Obs.: Começa nessas linhas e se desenvolve a medida que o jogo funciona. Caso queira ver cada uma das versão anteriores a final veja par_impar.py, par_impar2.py e par_impar3.py.
​
Autor: Guilherme Antunes de Camargo