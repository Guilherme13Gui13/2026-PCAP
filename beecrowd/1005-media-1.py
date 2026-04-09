'''
Problema: beecrowd | 1005
Data: 2026.04.09
Estudante: Guilherme Antunes de Camargo
'''
# Objetivo: Ler duas notas com pesos diferentes e calcular a média ponderada.

# --- ANÁLISE (LIAC) ---
# Entrada: Duas notas com ponto flutuante A e B (cada uma em uma linha).
# Processamento: Média Ponderada = (A * 3.5 + B * 7.5) / 11.
# Saída: Exibir o resultado no formato exato "MEDIA = valor" com cinco casas decimais.

# float(input()) - notas podem ter casa decimais (ex. 5.0, 7.1).
A = float(input())
B = float(input())

# Nota A tem peso 3.5 e nota B tem peso 7.5
# A soma dos pesos é 11 - divide-se por 11 para obter a média ponderada.
media = (A * 3.5 + B * 7.5) / 11

# :.5f dentro da f-string - formata o número com exatamente 5 casas decimais.
# O enunciado exige espaço antes e depois do = - seguir À risca 
print(f"MEDIA = {media:.5f}")