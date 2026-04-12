'''
Problema: beecrowd | 1050
Data: 2026.04.12
Estudante: Guilherme Antunes de Camargo
'''
# Objetivo: Ler um código DDD e informar a qual cidade ele pertence.
# --- ANÁLISE (LIAC) ---
# Entrada: Um número inteiro representando o código DDD.
# Processamento: Comparar o DDD lido com cada código na tabela usando if/elif/else
# Saída: Nome da cidade correspondente, ou "DDD não cadastrado" se não encontrado.

# int(input()) - DDD é sempre um número inteiro
DDD = int(input())

# Estrutura if/elif/else: testa cada condição em sequência
# Apenas o primeiro bloco verdadeiro é executado - os demais são ignorados
if DDD == 61: 
     print("Brasilia")
elif DDD == 71: 
     print("Salvador")
elif DDD == 11: 
     print("Sao Paulo")  
elif DDD == 21: 
     print("Rio de Janeiro") 
elif DDD == 32: 
     print("Juiz de Fora") 
elif DDD == 19:
     print("Campinas")  
elif DDD == 27: 
     print("Vitoria") 
elif DDD == 31: 
     print("Belo Horizonte") 
else:
     print("DDD nao cadastrado") # Nenhuma condição acima verdadeira - DDD não está na tabela.                         