# ===========================================
# Arquivo:    main.py
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      Guilherme Antunes de Camargo
# Data:       2026.08.18
# Conceitos:  escrever depopois
# ===========================================

from random import randint
from telas import titulo, linha
from modulos import ler_opcao, ler_numero
import random


JOGADAS1 = [ "Par", "Ímpar"]
JOGADAS2 = ['0', '1', '2', '3', '4', '5']

def mostrar_jogadas1():
    print("Veja as opções e escolha uma delas:")
    print("[0] Par")
    print("[1] Ímpar")

def mostrar_jogadas2():
    print("Escolha um número de 0 a 5.")

def eh_par_ou_impar(jogador2, computador2):
    soma = (jogador2 + computador2) % 2
    if soma == 0:
        return "par"
    else:
        return "impar"

def placar(pontos_jogador, pontos_maquina):
    print("Quem fizer dois primeiro ganha. O placar está assim:")
    print(f"Você tem {pontos_jogador} pontos.")
    print(f"O computador tem {pontos_maquina} pontos.")

def jogar_parimpar():
    titulo("Par ou Ímpar")
    pontos_jogador = 0
    pontos_maquina = 0

    while pontos_jogador < 2 and pontos_maquina < 2:
        mostrar_jogadas1()
        jogador1 = int(ler_opcao("Sua jogada: ", ['0', '1']))
        if jogador1 == 1:
            computador1 = 0
        else:
            computador1 = 1

        mostrar_jogadas2()
        jogador2 = int(ler_opcao("Sua jogada: ", ['0', '1', '2', '3', '4', '5']))
        computador2 = randint(0, 5)
        resultado1 = eh_par_ou_impar(jogador2, computador2)
        if resultado1 == "par" and jogador1 == 0:
            pontos_jogador += 1
            print(f"Você jogou {JOGADAS1[jogador1]} e a máquina jogou {JOGADAS1[computador1]}")
            print(f"Você escolheu {JOGADAS2[jogador2]} e a maquina jogou {computador2}")
            print("~~~~~~~~~~~~~~~~~~~~~~~ Você Ganhou! ~~~~~~~~~~~~~~~~~~~~~~~")
        elif resultado1 == "impar" and jogador1 == 1:
            pontos_jogador += 1
            print(f"Você jogou {JOGADAS1[jogador1]} e a máquina jogou {JOGADAS1[computador1]}")
            print(f"Você escolheu {JOGADAS2[jogador2]} e a maquina jogou {computador2}")
            print("~~~~~~~~~~~~~~~~~~~~~~~ Você Ganhou! ~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            pontos_maquina += 1
            print(f"Você jogou {JOGADAS1[jogador1]} e a máquina jogou {JOGADAS1[computador1]}")
            print(f"Você escolheu {JOGADAS2[jogador2]} e a maquina jogou {computador2}")
            print("~~~~~~~~~~~~~~~~~~~~~~~ Você Perdeu! ~~~~~~~~~~~~~~~~~~~~~~~")
        placar(pontos_jogador, pontos_maquina)
        linha()





'''
def jogar_parimpar():
    titulo("Par ou Ímpar")
    pontos_jogador = 0
    pontos_maquina = 0
    while pontos_jogador < 2 and pontos_maquina < 2:
        opcao_palavra()
        jogadorpalavra = int(ler_opcao("Sua jogada: ", ['0', '1']))
        if jogadorpalavra == "0":
            maquinapalavra = "1"
        else:
            maquinapalavra = "0"
        opcao_numero()
        jogadornumero = int(ler_numero("Seu número: ", [0, 1, 2, 3, 4, 5]))
        maquinanumero = random.randint(0, 5)
        c = (jogadornumero + maquinanumero) % 2
        if c == 0:
            return "par"
        else:
            return "ímpar"

def parouimpar():
    global jogador_palavra, maquina_palavra, jogadornumero, maquinanumero
    opcao_palavra()
    jogadorpalavra = int(ler_opcao("Sua jogada: ", ['0', '1']))
    if jogadorpalavra == "0":
        maquinapalavra = "1"
    else:
        maquinapalavra = "0"
    opcao_numero()
    jogadornumero = int(ler_numero("Seu número: ", [0, 1, 2, 3, 4, 5]))
    maquinanumero = random.randint(0, 5)
    c = (jogadornumero + maquinanumero) % 2
    if c == 0:
        return "par"
    else:
        return "ímpar"

def ganhador():
    a = parouimpar()
    if jogador_palavra == "0" and a == 0:
        print("Você ganhou!!")

'''