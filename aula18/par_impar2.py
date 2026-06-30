# ====================================================================== #
# Disciplina: Pensamento Computacional, Algoritimos e programação (PCAP)
# Projeto   : Jogo "Par ou Ímpar""
# Arquivo   : par_impar2.py
# Autor     : Guilherme Antunes de Camargo
# Data      : 25/06/2026
# ====================================================================== #

pj = 0
pm = 0
rodada = 0

for rodada in range(1,6):
     import random

     maquinanumero = random.randint(0, 5)
     jogadorpalavra = input("Escolha se desejas par ou ímpar: ").lower().strip()
     jogadornumero = int(input("Escolha seu número (de 1 a 5): "))
     opcoes1 = ["par", "ímpar"]
     opcoes2 = [1, 2, 3, 4, 5]

     if jogadorpalavra not in opcoes1:
          print("Jogada inválida! Se atente a grafia das palavras!")
          pm = pm + 1
     elif jogadornumero not in opcoes2:
          print("Jogada inválida! Se atente aos valores correspondentes!")
          pm = pm + 1
     else:
          pm = pm

     def soma(maquinanumero, jogadornumero):
          c = (maquinanumero + jogadornumero) % 2
          if c == 0:
               return "par"
          else:
               return "ímpar"
     resultado1 = soma(maquinanumero, jogadornumero)

     def ganhador(jogadorpalavra, pm, pj):
          if resultado1 == "par" and jogadorpalavra == "par":
                pj = pj + 1
                return "jogador", pm, pj
          elif resultado1 == "ímpar" and jogadorpalavra == "ímpar":
               pj = pj + 1
               return "jogador", pm, pj
          else:
                pm = pm + 1
                return "máquina", pm, pj

     resultado2, pm, pj = ganhador(jogadorpalavra, pm, pj)

     if resultado2 == "jogador":
          print(f"Você ganhou a rodada {rodada}")
          print(f"Você: {pj} | Máquina: {pm}")
     else:
          print(f"Você perdeu a rodada {rodada}")
          print(f"Você: {pj} | Máquina: {pm}")