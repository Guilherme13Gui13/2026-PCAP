# Conserto 5: trecho do "Par ou Ímpar" (Aula 18)
'''
def soma_jogadas(minha, da_maquina):
    total = minha +da_maquina
pontos = soma_jogadas(3, 4)
print("A soma das jogadas foi:", pontos)
'''
# O problema é que não tem o return.

def soma_jogadas(minha, da_maquina):
    total = minha +da_maquina
    return total
pontos = soma_jogadas(3, 4)
print("A soma das jogadas foi:", pontos)