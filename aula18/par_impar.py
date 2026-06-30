# ====================================================================== #
# Disciplina: Pensamento Computacional, Algoritimos e programação (PCAP)
# Projeto   : Jogo "Par ou Ímpar""
# Arquivo   : par_impar.py
# Autor     : Guilherme Antunes de Camargo
# Data      : 25/06/2026
# ====================================================================== #

import random

pj = 0
pm = 0 

    maquina = random.randint(0, 5)
    jogadorpalavra = input("Escolha se desejas par ou ímpar: ").lower()
    jogadornumero = int(input("Escolha seu número (de 1 a 5): "))
    opcoes = ["par", "ímpar"]

    if jogadorpalavra not in opcoes:
        print("Jogada inválida! Se atente a grafia das palavras!")
    
    c = soma((jogadornumero + maquina) % 2)

    def soma(c):
        if c == 0:
            return "par"
        else:
            return "impar"

    def resultado(jogador, maquina):
        if soma == "par" and jogadorpalavra == "par":
            print("Você venceu")
            return "jogador"
        elif soma == "impar" and jogadorpalavra == "ímpar":
            print("Você venceu")
            return "jogador"
        elif jogadorpalavra not in opcoes:
            print("Jogada inválida! Se atente a grafia das palavras!")
            return "maquina"
        else:
            print("Você perdeu")
            return "maquina"
    
    if resultado == "jogador":
        pj += 1
    else:
        pm += 1
    print(f"Você: {pj} pontos | Máquina {pm} pontos")