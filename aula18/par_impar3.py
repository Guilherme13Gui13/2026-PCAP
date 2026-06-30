# ====================================================================== #
# Disciplina: Pensamento Computacional, Algoritimos e programação (PCAP)
# Projeto   : Jogo "Par ou Ímpar""
# Arquivo   : par_impar2.py
# Autor     : Guilherme Antunes de Camargo
# Data      : 25/06/2026
# ====================================================================== #

jogar_de_novo = "sim"
while jogar_de_novo == "sim":
    pj = 0
    pm = 0
    rodada = 0

    for rodada in range(1,6): #Faz com que o jogo funcione 5 vezes.
         import random

         maquinanumero = random.randint(0, 5) #A máquina escolhe o número
         jogadorpalavra = input("Escolha se desejas par ou ímpar: ").lower().strip()
         jogadornumero = int(input("Escolha seu número (de 0 a 5): "))
         opcoes1 = ["par", "ímpar"] # Depois usaremos para validar as resposta do jogador.
         opcoes2 = [0, 1, 2, 3, 4, 5]

         if jogadorpalavra not in opcoes1:
            print("Jogada inválida! Se atente a grafia das palavras!")
            pm = pm + 1
         elif jogadornumero not in opcoes2:
            print("Jogada inválida! Se atente aos valores correspondentes!")
            pm = pm + 1
         else:
            pm = pm

         def soma(maquinanumero, jogadornumero): #Define se a soma é par ou ímpar.
            c = (maquinanumero + jogadornumero) % 2
            if c == 0:
               return "par"
            else:
               return "ímpar"
         resultado1 = soma(maquinanumero, jogadornumero)

         def ganhador(jogadornumero, jogadorpalavra, pm, pj): #Define o ganhador
             if resultado1 == "par" and jogadorpalavra == "par":
                 pj = pj + 1 #Poderíamos usar pj += 1
                 return "jogador", pm, pj #Como a função não usa as variáveis globais, devemos colocar depois "pm, pj" para identificar que deve-se usar as variáveis globais, poderiamos usar global também.
             elif resultado1 == "ímpar" and jogadorpalavra == "ímpar":
                 pj = pj + 1
                 return "jogador", pm, pj
             elif jogadornumero not in opcoes2: #É capaz que o jogo contabilize duas vezes o ponto da máquina.
                 pm = pm
                 return "máquina", jogadornumero, pm, pj
             elif jogadorpalavra not in opcoes1: #Mesma coisa do elif anterior, eu poderia ter escrito tudo aqui em vez de ter espalhado isso pelo código... Mas deu certo!
                 pm = pm
                 return "máquina", jogadorpalavra, pm, pj
             else:
                 pm = pm + 1
                 return "máquina", pm, pj

         resultado2, pm, pj = ganhador(jogadornumero, jogadorpalavra, pm, pj) #Chama a função.

         if resultado2 == "jogador": #Identifica o ganhador.
             print(f"Você ganhou a rodada {rodada}")
             print(f"Você: {pj} | Máquina: {pm}")
         else:
             print(f"Você perdeu a rodada {rodada}")
             print(f"Você: {pj} | Máquina: {pm}")

    jogar_de_novo = input("Você quer jogar de novo? (sim/não): ") #Se for "sim", o while lá em cima repete tudo.
