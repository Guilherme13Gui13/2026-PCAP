# ====================================================================== #
# Disciplina: Pensamento Computacional, Algoritimos e programação (PCAP)
# Projeto   : Jogo "Pedra-Papel-Tesoura""
# Arquivo   : ppt.py
# Autor     : Guilherme Antunes de Camargo
# Data      : 16/06/2026
# ====================================================================== #

import random

# === Sub-rotina: define o resultado e UMA rodada e devolve um texto === #
def resultado(jogador, maquina):
    if jogador == maquina:
        return "empate"
        
    # Dicionário onde a CHAVE ganha dos elementos da LISTA
    regras = {
        "pedra": ["tesoura", "lagarto"],
        "papel": ["pedra", "spock"],
        "tesoura": ["papel", "lagarto"],
        "lagarto": ["spock", "papel"],
        "spock": ["tesoura", "pedra"]
    }
    
    # Se a máquina estiver na lista de coisas que o jogador vence:
    if maquina in regras[jogador]:
        return "jogador"
        
    return "maquina" # Nenhum caso acima -> vitória da máquina.

# === Programa Principal === #
# 1. Expandindo as opções do jogo:
opcoes = ["pedra", "papel", "tesoura", "lagarto", "spock"]

# 2. Loop prinicipal para repetir o jogo inteiro caso o usuário queira.
while True:
    pontos_jogador = 0
    pontos_maquina = 0

    print("\n============== JOGO INICIADO ==============") # O \n pula uma linha.
    # Loop das 5 rodadas
    for rodada in range(1, 6):
        print(f"\n --- Rodada {rodada} ---")
        jogada_maquina = random.choice(opcoes)

        # Leitura enxuta: Ler + .lower() + .strip() em uma linha só
        jogada_jogador = input("Sua jogada (pedra, papel, tessoura, lagarto, spock): ").lower().strip()

        if jogada_jogador not in opcoes:
            print("Inválido! Você perde a rodada.")
            pontos_maquina += 1
        else:
            print(f"Máquina escolheu: {jogada_maquina}")
            quem = resultado(jogada_jogador, jogada_maquina)

            if quem == "empate":
                print("Empate!")
            elif quem == "jogador":
                print("Você ganhou a rodada!")
                pontos_jogador += 1
            else:
                print("A máquina ganhou a rodada!")
                pontos_maquina += 1

    # Fim de jogo (Placar Final)
    print("\n============== RESULTADO FINAL ==============")
    print(f"Placar final -> Você: {pontos_jogador} | Máquina {pontos_maquina}")
    if pontos_jogador > pontos_maquina:
        print("Você ganhouuuuuuuuuuuuuuuuu!")
    elif pontos_jogador < pontos_maquina:
        print("Você perdeuuuuuuuuuuuuuuuuuuuuu!")
    else:
        print("Você empatouuuuuuuuuuuuuuuuuuuuuuu!")

    # 3. Pergunta se quer jogar de novo:
    jogar_de_novo = input("\nDeseja jogar novamente? (s/n): ").lower().strip()
    if jogar_de_novo != 's': # != se for diferente de 's' retona True, se não False
        print("\nObrigado por jogar! Até maissssssssssssssssssssssssss.")
        break # Sai do loop "while True" e encerra o programa