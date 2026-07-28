# Conserto 3: contagem de rodadas
'''
contador = 1
while contador <= 5:
    print("Rodada", contador)
print("Fim de Jogo!")
'''
# O problema está em que sempre repetirá porque o valor contido em contador não muda, deve ser adicionado contador += 1.
# Tive que mudar para !=, pois queremos que mostre até a rodada 5, e tiive que colocar antes do while o print(...) para printar Rodada 1.
contador = 1
print("Rodada", contador)
while contador != 5:
    contador += 1
    print("Rodada", contador)
print("Fim de Jogo!")