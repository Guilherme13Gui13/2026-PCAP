# Conserto 1: trecho do "Adivinhe o número" (Aula 16)
'''
print("=== ADIVINHE O NÚMERO ===")
segredo = 7
palpite = input("Digite um número de 1 a 10: ")
if palpite == segredo:
    print("Acertou")
else:
    print("Errou! O segredo era", segredo)
'''
# O problema está no input, ele está naturalmente no str, e como o segredo é int devemos só colocar int na frente.

print("=== ADIVINHE O NÚMERO ===")
segredo = 7
palpite = int(input("Digite um número de 1 a 10: "))
if palpite == segredo:
    print("Acertou")
else:
    print("Errou! O segredo era", segredo)