import random
# === Função para os níveis numéricos (Fácil, Médio, Impossível) ===
def jogar(maximo, chances):
    numero_secreto = random.randint(1, maximo)
    acertou = False

    while chances > 0 and not acertou:
        palpite = int(input("Seu palpite(1 a " + str(maximo) + "): "))

        if palpite == numero_secreto:
            print("Acertou!")
            acertou = True
        elif palpite < numero_secreto:
            print("Muito baixo!")
        else:
            print("Muito Alto!")

            chances = chances - 1
            print("Chances restantes:", chances)

        return acertou
    
    # === Nova Função: exclusiva para o nível "Tutorial", somente vogais === #
def jogar_tutorial(chances):
    vogais = ['A', 'E', 'I', 'O', 'U']
    vogal_secreta = random.choice(vogais)
    acertou = False

    print("O segredo é uma das vogais, escreva-as maiúsculas")

# .upper().strip() remove espaços e transorma a letra em maiúscula.
    while chances > 0 and not acertou:
        palpite = input("Seu palpite (Vogal maiúscula): ").upper().strip()

        if palpite == vogal_secreta:
            print("Acertou!")
            acertou = True
        else:
            print("Errado! Essa não é a vogal secreta.")

            chances = chances - 1
            print("Chances restantes:", chances)

    return acertou

# === Lista de níveis numéricos === #
# [nome, maximo, chances]
niveis = [
    ["Fácil", 10, 3],
    ["Médio", 100, 5],
    ["Impossível", 1000, 10]
]

# === Menu de escolha de nível === #
print("1 - Tutorial   (Vogais maiúculas, 5 chance)")
print("2 - Fácil      (1 a 10, 3 chances)")
print("3 - Médio      (1 a 100, 3 chances)")
print("4 - Impossível (1 a 1000, 3 chances)")
opcao = int(input("Dígite 1, 2, 3 ou 4: "))

# === Lógica para direionar o nível desejado === #
if opcao == 1:
    print("Você escolheu o nível: Tutorial")
    venceu = jogar_tutorial(5) # Inicia o tutorial com 5 chances.
else:
    # Como o usuário escolheu a opção 2, 3 ou 4, subtraímos 2 para apontar corretamente para os indices 0, 1 ou 2 da lista dos níveis.
    nivel = niveis[opcao -2]
    print(" Você esolheu o nível:", nivel[0])
    venceu = jogar(nivel[1], nivel[2])

# === Fim de Jogo === #
if not venceu:
    print("Fim de Jogo! Tente um nível mais fácil.")