'''
REVISÃO DE PYTHON - Aula 19 | PCAP 2026
Guilherme Antunes de Camargo | 28/07/2026

1. Variáveis e tipos de dados
A variável guarda um dado que pode ser posteriormente usado eplo programa. Divide-se em 4 tipos
idade = 16, tipo int números inteiros
altura = 1.60, tipo float números decimais
A = True, tipo bool True ou False
nome = "Ana", tipo str só texto

2. Operadores
Realizam operações, comparações e lógicas entre nas variáveis
A = 10, = atribuição
10 + 1, soma
10 - 1, diferença ou subtração
10 * 2, multiplicação
10 / 2, divisão
10 ** 2, potenciação e radiciacão (exponenciação)
10 // 3, divisão inteira, volta int
10 % 3, resto da divisão inteira, volta int
10 == 10, verifica se um valor é igual a outro, volta True ou False
10 != 9, verifica se um valor é diferente de outro, volta True ou False
10 > 2 e suas variações (>, <, >=, <=), volta True ou False
and, operador lógico que retórna true ou false se duas afirmações são verdadeiras (como esse também existe o or (ou) e o not que inverte True para false e false para true)

3. Entrada de dados
input() é responsável por receber dados pelo usuário.

4. saída de dados
print() é respinsável por exibir informações no terminal.

5. Estrutura de repetição
for, repete quantas vezes for pedido
while, serve como um enquanto, enquanto uma afirmação for true ele vai repetir o código

6. Estrutura de condição
if, elif, servem como um "se", se tal afirmação (condição) for true eles vão realizar o que estiver indentado, o else serve como um se não então, se o if e else não forem true o que estiver no else vai ser executado.

'''

# Sistema que serve para identificar se cada um dos quatros números inseridos pelo jogador são ou não múltiplos de 3

for i in range(1, 5):
    a = int(input("Escolha seu número: "))
    b = a % 3
    if b == 0:
        print(f"O número {a} é múltiplo de três.")
    else:
        print(f"O número {a} não é múltiplo de três.")
    