# ===========================================
# Arquivo:    telas.py
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      Guilherme Antunes de Camargo
# Data:       2026.08.04
# Conceitos:  escrever depopois
# ===========================================

# Definição da Moldura Caracteres e Tamanho
CAR = "~"
TAM = 60 # Largura

# Função para desenhar um linha na tela
def linha():
    print(CAR * TAM)

# Função para desenhar um texto entre linhas
def titulo(texto):
    linha()
    print(texto.center(TAM))
    linha()
