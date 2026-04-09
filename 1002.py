'''
Problema: beecrowd | 1002
Data: 2026.04.07
Estudante: Guilherme Antunes de Camargo
'''
# Objetivo: Calcular a área do cículo a partir da fórmula dada e depois exibir o resultado.

# --- ANÁLISE (LIAC) ---
# Entrada: um número de ponto flutuante, o R.
# Processamento: calcular a área a partir da fórmula e guardar o resultado em AREA.
# Saída: mostrar "A=", dessa forma e exibir o resultado

# Leitura do raio como número decimal
R = float(input())

pi = 3.14159

AREA = R ** 2 * pi

print(f"A={AREA:.4f}")
