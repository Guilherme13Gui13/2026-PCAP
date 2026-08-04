# Desafio bônus: contagem regressiva (este tem 2 erros!)
'''
def contagem_regressiva(inicio):
    while inicio > 0:
        print(inicio)
    print("Já!")

contagem_regressiva("5")
'''
# O 5 está sendo lido com str e falta o início -= 1, se deve aparecer o 5 devemos colocar antes de while print(inicio) e se não deve aparecer o 0 devemos mudar de "> 0" para "> 1"

def contagem_regressiva(inicio):
    print(inicio)
    while inicio > 1:
        inicio -= 1
        print(inicio)
    print("Já!")

contagem_regressiva(5)