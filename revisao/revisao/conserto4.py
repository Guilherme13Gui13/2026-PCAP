# Conserto 4: trecho do "Pedra-Papel-Tesoura" (Aula 17)
'''
jogada = input("pedra, papel ou tesoura? ")
if jogada == "pedra" or jogada == "papel" or jogada == "tesoura":
    print("Jogada válida!", jogada)
else:
    print("Jogada inválida!")
'''
# Deemos criar uma lista que contenha todas as opções aceitáveis ou podemos adicionar .lower.strip depois do input(...)

jogada = input("pedra, papel ou tesoura? ").lower().strip()
if jogada == "pedra" or jogada == "papel" or jogada == "tesoura":
    print("Jogada válida!", jogada)
else:
    print("Jogada inválida!")