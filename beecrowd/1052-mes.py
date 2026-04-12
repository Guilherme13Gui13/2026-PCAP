'''
Problema: beecrowd | 1052
Data: 2026.04.12
Estudante: Guilherme Antunes de Camargo
'''
# Objetivo: Ler um número inteiro e exibir qual mês ele é.

# --- ANÁLISE (LIAC) ---
# Entrada: Um número inteiro representando o número do mês.
# Processamento: Comparar o número na tabela usando if/elif/else
# Saída: Nome do mês em inglês com a primeira letra maiúscula correspondente.

mes = int(input())
if mes == 1: 
    print("January")
elif mes == 2: 
    print("February")
elif mes == 3:
    print("March")
elif mes == 4: 
    print("April")   
elif mes == 5: 
    print("May")   
elif mes == 6: 
    print("June")   
elif mes == 7: 
    print("July")
elif mes == 8: 
    print("August")
elif mes == 9: 
    print("September") 
elif mes == 10:
    print("October")   
elif mes == 11: 
    print("November")   
else:
    print("December")         