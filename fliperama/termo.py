# ===========================================
# Arquivo:    termo.py
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      Guilherme Antunes de Camargo
# Data:       2026.08.30
# Conceitos:  escrever depopois
# ===========================================

import random
from telas import linha, titulo
from modulos import ler_texto

# Única parte do código em que usei IA, pedi para fazer uma lista de 100 palavras todas com 5 letras e sem acento.
palavras_termo = [
    "termo", "amigo", "carro", "festa", "figos", "sagaz", "negro", "exito", "sabor", "poder",
    "fazer", "assim", "caros", "sobre", "muito", "nosso", "grupo", "tempo", "corpo", "falar",
    "saber", "trave", "pedir", "olhar", "dever", "tomar", "comer", "beber", "andar", "parar",
    "subir", "desce", "abrir", "fecha", "girar", "jogar", "puxar", "vista", "morar", "viver",
    "vence", "perde", "sonho", "morte", "livro", "ponto", "campo", "porto", "noite", "vento",
    "chuva", "nuvem", "fundo", "pedra", "terra", "prata", "fruta", "bicho", "porta", "regua",
    "canto", "metro", "linha", "fazer", "santo", "sinal", "marca", "troca", "passo", "prosa",
    "certo", "gravo", "mudar", "plano", "claro", "breve", "duros", "moles", "vazio", "cheio",
    "prato", "copos", "garfo", "facas", "mesas", "caixa", "pasta", "folha", "lapiz", "chave",
    "carne", "peixe", "leite", "arroz", "milho", "tinta", "ferro", "ouros", "prata", "couro"
]

def instrucoes():
    linha()
    titulo('Termo')
    linha()
    print("INSTRUÇÕES:")
    print("Nesse jogo você deverá adivinhar uma palavra secreta.")
    print("O computador falará se cada uma das letras está na posição ")
    print("certa, fora de ordem ou se não existe. Bom jogo !")
    linha()

def escolha_palavra():
    posicao_lista = random.randint(0, 99)
    palavra_secreta = []
    palavra_secreta.append(palavras_termo[posicao_lista])
    letras = list(palavra_secreta[0]) 
    return letras

def validacao_dobrada():
    palavra_jogador = list(ler_texto("Escolha sua palavra de 5 letras sem acento ortográfico"))
    while len(palavra_jogador) != 5:
        palavra_jogador = list(ler_texto("Palavra inválida... Digite outra: "))
    return palavra_jogador

def certo_ou_errado(a1, a2):
    certos_e_errados = ["N"] * 5
    secreta_copia = list(a1)
    chute_copia = list(a2)

    for i in range(5):
        if chute_copia[i] == secreta_copia[i]:
            certos_e_errados[i] = "S"
            secreta_copia[i] = None 

    for i in range(5):
        if certos_e_errados[i] != "S" and chute_copia[i] in secreta_copia:
            certos_e_errados[i] = "O"
            secreta_copia[secreta_copia.index(chute_copia[i])] = None

    return certos_e_errados

def analise(a2, a3):
    for i in range(0, 5):
        if (a3[i]) == "S":
            print(f"A letra {a2[i]} está no lugar certo!")
        elif (a3[i]) == "O":
            print(f"A letra {a2[i]} está no lugar errado.")
        else:
            print(f"A letra {a2[i]} não existe na palavra secreta...")

def jogar_termo():
    instrucoes()
    tentativas = 0
    a1 = escolha_palavra()
    
    a4 = 0
    
    while a4 < 5:
        a2 = validacao_dobrada()
        a3 = certo_ou_errado(a1, a2) 
        analise(a2, a3)
        tentativas += 1
        a4 = a3.count("S") # count conta quantas vezes "S" aparece na lista a3
        
    print(f"\nParabéns! Você acertou a palavra em {tentativas} tentativa(s)!")


'''
a1 = escolha_palavra()
a2 = validacao_dobrada()

def certo_ou_errado(a1, a2):
    certos_e_errados = []
    for i in range(0, 5):
        if (a2[i]) == (a1[i]):
            certos_e_errados.append("S")
        elif (a2[i]) == (a1[0]) or (a2[i]) == (a1[1]) or (a2[i]) == (a1[2]) or (a2[i]) == (a1[3]) or (a2[i]) == (a1[4]):
            certos_e_errados.append("O")
        else:
            certos_e_errados.append("N")
    return certos_e_errados

a3 = certo_ou_errado(a1, a2)

def analise(a2, a3):
    for i in range(0, 5):
        if (a3[i]) == "S":
            print(f"A letra {a2[i]} está no lugar certo!")
        elif (a3[i]) == "O":
            print(f"A letra {a2[i]} está no lugar errado.")
        else:
            print(f"A letra {a2[i]} não exite na palavra secreta...")

def jogar_termo():
    instrucoes()
    tentativas = 0
    
    escolha_palavra()
    validacao_dobrada()
    analise(a1, a2)
    tentativas += 1
    a4 = a3.count("S")
    while a4 < 5:
        validacao_dobrada()
        certo_ou_errado(a1, a2)
        analise(a2, a3)
        tentativas += 1
    print(f"Você descobriu a palavra secreta {a1} em {tentativas} tentativas.")

jogar_termo()

# Corrigir erros: não tem introdução, muito mal feita a introdução, aceita espaços vazios como palavra, não está análisando corretammebte'''