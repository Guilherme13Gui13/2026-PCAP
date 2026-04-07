'''
Problema: beecrowd | 1011
Data: 2026.04.07
Estudante: Guilherme Antunes de Camargo
'''
# Objetivo: calcular o volume da esfera a partir do raio e mostrar o resultado.

# --- ANÁLISE (LIAC) ---
# Entrada: um número de ponto flutuante, o R.
# Processamento: calcular o volume a partir da fórmula.
# Saída: mostrar "VOLUME = ", dessa forma.

# float() - converte o valor lido para um número decimal (ponto flutuante)
R = float(input())
pi = 3.14159

# 4.0/3 garante a divisão decimal (não inteira)
# R**3 - R elevado ao cubo
V = (4.0 / 3) * pi * R ** 3

# :.3f - formata o número com 3 cass decimais
print(f"VOLUME = {V:.3f}")


