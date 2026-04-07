'''
Problema: beecrowd | 1001
Data: 2026.04.07
Estudante: Guilherme Antunes de Camargo
'''
# Objetivo: Somar 2 valores e exibir o resultado

# --- ANÁLISE (LIAC) ---
# Entrada: dois números inteiros, cada um em uma linha separada.
# Processamento: Somar A + B e armazenar em X
# Saída: exibir no formato exato "X = valor" (espaços ao redor do =, sem mensagens extras)

# int() - converte o texto lido para um número inteiro
# input() - lê o valor fornecido (digitado pelo BeeCrown)
# int(input{}) - lê e converte em uma única instrução
A = int(input())
B = int(input())

# O enunciado especifica explicitamente as variáveis A, B e X - segir à risca
X = A + B 

# f-string: insere o valor de X Dentro do texto com {}
# Atenção: espaço antes de depois do = é obrigatório conforme o enunciado
print(f"X = {X}")