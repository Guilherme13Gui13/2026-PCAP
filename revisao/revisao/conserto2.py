# Conserto 2: chegagem de idade
'''
idade = int(input("Sua idade: "))
if idade = 18:
    print("Você tem exatamente 18 anos!")
else:
    print("Você não tem 18 anos.")
'''
# O problema está em que você retribui um valor novo a idade, dveria ser "==" em vez de "=".

idade = int(input("Sua idade: "))
if idade == 18:
    print("Você tem exatamente 18 anos!")
else:
    print("Você não tem 18 anos.")