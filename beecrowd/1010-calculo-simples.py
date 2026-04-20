'''
Problema: beecrowd | 1010
Data: 2026.04.20
Estudante: Guilherme Antunes de Camargo
'''
# Objetivo: Ler código, quantidade e valor unitário (float).

# --- ANÁLISE (LIAC) ---
# Entrada: Duas linhas; cada uma com código (int), quantidade (int) e valor.
# Processamento: Total = (qtd1 * val1) + (qtd2 * val2)
# Saída: "VALOR A PAGAR: R$ valor" com 2 casas decimais.

# Lê a primeira linha e separa os tr~es valores inteiros pelo espaço.
cod1, qtd1, val1 = input().split()

# Converte individualmente para inteiro e valor unitário para float.
qtd1 = int(qtd1)
val1 = float(val1)

# Lê a segunda linha e separa os três valores pelo espaço.
cod2, qtd2, val2 = input().split()

# Converte quantidade para inteiro e vaor unitário para float.
qtd2 = int(qtd2)
val2 = float(val2)

# Calcula o valor total: subtotal da peça 1 + subtotal da peça 2 =
total = (qtd1 * val1) + (qtd2 * val2)

# Exibe o resultado no formato exato exigido pelo enunciado.
print(f"VALOR A PAGAR: R$ {total:.2f}")