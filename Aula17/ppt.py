# ====================================================================== #
# Disciplina: Pensamento Computacional, Algoritimos e programação (PCAP)
# Projeto   : Jogo "Pedra-Papel-Tesoura""
# Arquivo   : ppt.py
# Autor     : Guilherme Antunes de Camargo
# Data      : 16/06/2026
# ====================================================================== #

import random

# Tudo isso já vem pronto da v1 e v2: sotear, ler e limpar a jogada
opcoes = ["pedra", "papel", "tesoura"]
jogada_maquina = random.choice(opcoes)

entrada = input("Sua jogada (pedra, papel ou tesoura): ")
jogada_jogador = entrada.lower().strip() # tudo minúsculo e sem espaços nas pontas
print("Você jogou:", jogada_jogador, "| Máquina:", jogada_maquina)

# Decidimos o resultado COMPARANDO as duas jogadas (textos)
# A ORDEM dos testes importa: 1º inválida, 2º empate, depois as vitórias
if jogada_jogador not in opcoes:
    print("Jogada Inválida! Digite pedra, papel ou tesoura.")
elif jogada_jogador == jogada_maquina: # mesma jogda dos dois?
    print("Empate! Os dois jogaram", jogada_maquina)
# As três (e únicas) formas de o JOGADOR vencer - a regra clássica
elif jogada_jogador == "pedra" and jogada_maquina == "tesoura":
    print("Você venceu! Pedra quebra tesoura.")
elif jogada_jogador == "papel" and jogada_maquina == "pedra":
    print("Você venceu! Papel embrulha pedra.")
elif jogada_jogador == "tesoura" and jogada_maquina == "papel":
    print("Você venceu! Tesoura corta papel.")
else: # não caiu em nenhuma bitória acima -> sobra máquina
    print("A máquina venceu! Ela jogou", jogada_maquina)
# fazer v4 e v5.