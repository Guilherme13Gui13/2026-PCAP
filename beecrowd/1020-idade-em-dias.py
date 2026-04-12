'''
Problema: beecrowd | 1020
Data: 2026.04.12
Estudante: Guilherme Antunes de Camargo
'''
# Objetivo: Ler um valor inteiro em dias e transformar em anos, meses e dias.

# --- ANÁLISE (LIAC) ---
# Entrada: Um número inteiro N representando dias totais.
# Processamento: Extrair anos, meses e dias restantes por divisão inteira e módulo.
# Saída: No formato ano(s), mes(es) e dia(s) em linhas separadas.

N = int(input())
a = N // 365
N = N % 365
m = N // 30
d = N % 30
print(f"{a} ano(s)")
print(f"{m} mes(es)")
print(f"{d} dia(s)")