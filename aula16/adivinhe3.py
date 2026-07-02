# ====================================================================== #
# Disciplina: Pensamento Computacional, Algoritimos e programação (PCAP)
# Projeto   : Jogo "Adivinhe o Número"
# Arquivo   : adivinhe3.py
# Autor     : Guilherme Antunes de Camargo
# Data      : 28/05/2026
# ====================================================================== #


import random

# === Função para os níveis numéricos (Fácil, Médio, Impossível) ===
def jogar(maximo, chances):
    numero_secreto = random.randint(1, maximo)
    acertou = False

    while chances > 0 and not acertou:
        palpite = int(input("Seu palpite (1 a " + str(maximo) + "): "))

        if palpite == numero_secreto:
            print("Acertou!")
            acertou = True
        elif palpite < numero_secreto:
            print("Muito baixo!")
        else:
            print("Muito alto!")

        chances = chances - 1
        print("Chances restantes:", chances)

    return acertou

# === Nova função: "Nível Tutorial" (somente vogais e 5 chances) ===
def jogar_tutorial(chances):
    vogais = ['A', 'E', 'I', 'O', 'U']
    vogal_secreta = random.choice(vogais) # random.choices(vogais) sorteia um item aleatório da variável vogais.
    acertou = False

    print("Dica: a resposta é uma das vogais")

    while chances > 0 and not acertou:
        palpite = input("Seu palpite (Vogal maíuscula): ").upper().strip() # .upper().strip() pega qualquer texto e transforma em letras maiúsculas, além de deletar qualquer espaço em branco.

        if palpite == vogal_secreta:
            print("Acertou!")
            acertou = True
        else:
            print("Errado! Essa não é a vogal correta...")

            chances = chances - 1
            print("Chances restantes: ", chances)

    return acertou

# === Lista dos níveis numéricos ===
niveis = [
    ["Fácil", 10, 3],
    ["Médio", 100, 5],
    ["Impossível", 1000, 10]
]

# === Menu de escolha de nível ===
print("1 - Tutorial   (Vogais A, E, I, O e U; 5 chances)")
print("2 - Fácil      (1 a 10; 3 chances)")
print("3 - Médio      (1 a 100; 10 chances)")
print("4 - Impossível (1 a 1000; 10 chances)")

opcao = int(input(" Digite 1, 2, 3 ou 4:"))

# === Lógica de direcionamento dos níveis desejados ===
if opcao == 1:
    print("Você escolheu o nível: Tutorial")
    venceu = jogar_tutorial(5)
else:
    nivel = niveis[opcao - 2]
    print("Você escolheu o nível:", nivel[0])
    venceu = jogar(nivel[1], nivel[2])

# === Fim de jogo ===
if not venceu:
    print("Fim de jogo! Tente um nível mais fácil.")