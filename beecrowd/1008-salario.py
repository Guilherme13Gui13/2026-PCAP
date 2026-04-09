'''
Problema: beecrowd | 1008
Data: 2026.04.09
Estudante: Guilherme Antunes de Camargo
'''
# Objetivo: calcular o salário de um funcionário a partir da quantidade de horas trabalhadas e emití-lo.

# --- ANÁLISE (LIAC) ---
# Entrada: Receber dois números inteiros e um número com duas casas decimais.
# Processamento: Multiplicar a quantidade de horas trabalhadas pelo valor da hora.
# Saída: Emitir dessa forma exatamente "NUMBER = " e "SALARY = U$ ".

# Leitura das entradas:
N = int(input())
H = int(input())
V = float(input())

# Cálculo do salário:
SAL = V * H

# Saída:
print(f"NUMBER = {N}")
print(f"SALARY = U$ {SAL:.2f}")