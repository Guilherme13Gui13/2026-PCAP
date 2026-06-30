# ====================================================================== #
# Disciplina: Pensamento Computacional, Algoritimos e programação (PCAP)
# Projeto   : Jogo "Par ou Ímpar""
# Arquivo   : par_impar2.py
# Autor     : Guilherme Antunes de Camargo
# Data      : 25/06/2026
# ====================================================================== #

jogar_de_novo = "sim"
historico_partidas = [] #Lista que guarda o histórico das partidas.
while jogar_de_novo == "sim":
    pj = 0
    pm = 0
    rodada = 0

    for rodada in range(1,6): #Faz com que o jogo funcione 5 vezes.
         import random

         maquinanumero = random.randint(0, 5) #A máquina escolhe o número
         jogadorpalavra = input("Escolha se desejas par ou ímpar: ").lower().strip()
         jogadornumero = int(input("Escolha seu número (de 0 a 5): "))
         opcoes1 = ["par", "ímpar"] # Depois usaremos para validar as resposta do jogador.
         opcoes2 = [0, 1, 2, 3, 4, 5]

         '''if jogadorpalavra not in opcoes1:
            print("Jogada inválida! Se atente a grafia das palavras!")
            pm = pm + 1
         elif jogadornumero not in opcoes2:
            print("Jogada inválida! Se atente aos valores correspondentes!")
            pm = pm + 1
         else:
            pm = pm''' #Essa parte dá erro...

         def soma(maquinanumero, jogadornumero): #Define se a soma é par ou ímpar.
            c = (maquinanumero + jogadornumero) % 2
            if c == 0:
               return "par"
            else:
               return "ímpar"
         resultado1 = soma(maquinanumero, jogadornumero)

         def ganhador(jogadornumero, jogadorpalavra): #Define o ganhador
             global pm, pj
             if jogadorpalavra not in opcoes1:
                 pm = pm + 1 #Poderíamos usar pm += 1
                 return "inválido"
             elif jogadornumero not in opcoes2:
                 pm = pm + 1
                 return "inválido"
             elif resultado1 == "par" and jogadorpalavra == "par":
                 pj = pj + 1
                 return "jogador"
             elif resultado1 == "ímpar" and jogadorpalavra == "ímpar":
                 pj = pj + 1
                 return "jogador"
             else:
                 pm = pm + 1
                 return "máquina"

         resultado2 = ganhador(jogadornumero, jogadorpalavra) #Chama a função.
         dados_da_rodada = f"Rodada {rodada}: Jogador ({jogadornumero}) VS Máquina ({maquinanumero}) -> Ganhador: {resultado2}"
         historico_partidas.append(dados_da_rodada) #Preenche a lista com os dados.

         if resultado2 == "jogador": #Identifica o ganhador.
             print(f"Você ganhou a rodada {rodada}")
             print(f"Você: {pj} | Máquina: {pm}")
         elif resultado2 == "inválido": #Identifica erros por parte do jogador
             print(f"Jogada inválida! Você perdeu a rodada {rodada}...")
             print(f"Você: {pj} | Máquina: {pm}")
         else:
             print(f"Você perdeu a rodada {rodada}")
             print(f"Você: {pj} | Máquina: {pm}")

    jogar_de_novo = input("Você quer jogar de novo? (sim/não): ") #Se for "sim", o while lá em cima repete tudo.
print("Obrigado por jogar! ;)")
print("\n" + "="*20 + " ESTATÍSTICA GERAL " + "="*20) #Começa a estatística e o histórico.
print(f"Total de Vitórias do Jogador: {pj}")
print(f"Total de Vitórias da Máquina: {pm}")

total_rodadas = len(historico_partidas) #Lê a quantidade de caracteres.
if total_rodadas > 0:
    porcentagem_jogador = (pj / total_rodadas) * 100
    print(f"Aproveitamento do Jogador: {porcentagem_jogador:.1f}%")

print("\n" +"="*20 + " HISTÓRICO DE JOGADAS " + "="*17)
for partida in historico_partidas: #Laço de repetição que passa por cada jogo salvo na lista
    print(partida) #Printa as informações da lista
print("="*59)