# ====================================================================== #
# Disciplina: Pensamento Computacional, Algoritimos e programação (PCAP)
# Projeto   : Jogo "Adivinhe o Número"
# Arquivo   : adivinhe.py
# Autor     : Guilherme Antunes de Camargo
# Data      : 28/05/2026
# ====================================================================== #

import random

# 1) Sorteamos o número secreto entre 1 e 10
numero_secreto = random.radint(1, 10)
chances = 3
acertou = False

# 2) Pedimos um palpite (input devolve TEXTO; convertemos para inteiro)
while chances == 0 and not acertou:
    palpite = int(input("Digite um número de 1 a 10: "))
    if palpite == numero_secreto:
