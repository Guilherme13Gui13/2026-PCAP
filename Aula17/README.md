# ✊✋✌️ Pedra-Papel-Tesoura
​
Jogo de Pedra-Papel-Tesoura feito em Python na disciplina PCAP (Aula 17).
Você joga contra o computador em uma melhor de 5 rodadas, com placar.
​
## ▶️ Como jogar
1. Abra o terminal na pasta do jogo.
2. Rode: python ppt.py (se esjar a versão inalterada)
2.1 Rode: python pptls.py (se desejar a versão nova)
3. A cada rodada, digite pedra, papel, tesoura, lagarto ou spock.
3.1 Pedra ganha de tesoura e lagarto; papel ganha de pedra e spock; tesoura ganha de papel e lagarto; lagarto ganha de spock e papel; spock ganha de tesoura e pedra.
4. Ao fim das 5 rodadas, o programa mostra o placar final.
5. Em seguida, ele te pergunta se queres jogar novamente.
​
## ⚙️ Como funciona (resumo)
A cada rodada o computador sorteia uma jogada (random.choice) e lê a sua.
O texto digitado é limpo (.lower().strip()) e validado (in) antes de comparar.
Uma sub-rotina decide quem venceu e o programa soma os pontos das 5 rodadas.
​
## 🧠 O que eu pratiquei
- Strings e métodos de texto: .lower() e .strip() para limpar o que foi digitado
- Validação com in: aceitar só pedra, papel ou tesoura
- Comparação de textos (==): descobrir empate e vitórias
- random.choice: sortear a jogada da máquina
- Repetição (for): jogar as 5 rodadas e manter o placar
- Sub-rotinas (def/return): isolar a regra do jogo
- While True: serve para repetir o jogo caso a pessoa queira jogar novamente.
​
## 🎯 Autoavaliação
Conceito pretendido: A (nova versão, a pptls.py))
​
Justificativa (cite arquivo e linha de cada critério):
- O jogo funciona ............: pptls.py, linhas 9 a 79
- Trabalho com texto .........: pptls.py, linha 47 (.lower().strip(), in, ==)
- Documentação e Git .........: este README + commits no GitHub
- Extensão/originalidade .....: pptls.py, linhas 16 a 29 (adição do lagarto e do spock), (obs.: na realidade, todas as linhas tem algumas alterações), linhas 75 a 79 (adição definitiva se a pessoa quer jogar novamente)

​
Autor: Guilherme Antunes de Camargo