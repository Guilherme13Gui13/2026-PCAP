# Conserto : menu de escolhas
'''
jogos = ["Adivinhe o Numero", "Pedra-Papel-Tesoura", "Par ou Impar"]
opcao = int(input("Escolha o jogo(', 2 ou 3): "))
print("Você escolheu:", jogos[opcao])
'''
# O problema é que o computador começa a contar no 0, logo doevemos subtrair 1 de opcao.

jogos = ["Adivinhe o Numero", "Pedra-Papel-Tesoura", "Par ou Impar"]
opcao = int(input("Escolha o jogo(1, 2 ou 3): "))
opcao -= 1
print("Você escolheu:", jogos[opcao])