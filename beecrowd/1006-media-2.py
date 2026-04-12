'''
Problema: beecrowd | 1006
Data: 2026.04.09
Estudante: Guilherme Antunes de Camargo
'''
# Objetivo: Ler três notas diferentes e calcular a média ponderada.

# --- ANÁLISE (LIAC) ---
# Entrada: Três notas com ponto flutuante A, B e C (cada uma em uma linha).
# Processamento: Média Ponderada = (A * 2 + B * 3 + C * 5) / 10
# Saída: Exibir o resultado no formato exato "MEDIA = valor" com uma casa decimal.

A = float(input())
B = float(input())
C = float(input())

media = (A * 2 + B * 3 + C * 5) / 10

print(f"MEDIA = {media:.1f}")
