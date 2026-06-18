from random import randint

n = int(randint(6, 10))
lista = []

for i in range (1, n+1, 1):
    lista.append(randint(1, 100))

for i in range (n - 1, 0, -1):
    if lista[i] > lista[i-1]:






