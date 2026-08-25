# ===========================================
# Arquivo:    main.py
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      Guilherme Antunes de Camargo
# Data:       2026.08.04
# Conceitos:  escrever depopois
# ===========================================

# Importar funções de arquivos
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from modulos import ler_opcao
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores
from parimpar import jogar_parimpar

NOMES_DOS_JOGOS = ['Adivinhe o Numero', 'Perda-Papel-Tesoura', 'Par ou Impar']
vezes_jogado = carregar_placar()
jogadores = carregar_jogadores()
def mostrar_placar():
    titulo('PLACAR')
    for i in range(3):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')
              
NOME_DO_DONO = "GUILHERME"
OPCOES = ["0", "1", "2", "3", "4"]

while True:
    titulo("FLIPERAMA DO " + NOME_DO_DONO)
    print("1 - Jogo Adivinhe o Número")
    print("2 - Jogo PEDRA-PAPEL-TESOURA")
    print("3 - Jogo Par ou Ímpar")
    print("4 - Jogadores")
    print("0 - Sair do Fliperama")
    linha()
    opcao = ler_opcao("Escolha uma opção", OPCOES)

    if opcao == "0":
        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        titulo("Até a próxima!")
        break

    if opcao == '4':
        menu_jogadores(jogadores)
    else:
        indice = int(opcao) - 1
        vezes_jogado[indice] = vezes_jogado[indice] + 1

        if opcao == '1':
            jogar_adivinhe()
        elif opcao == '2':
            jogar_ppt()
        elif opcao == "3":
            jogar_parimpar()

    input('Pressione Enter para voltar ao menu...')

    '''
    elif opcao == "1":
        jogar_adivinhe()
    elif opcao == "2":
        jogar_ppt()
    indice = int(opcao) - 1
    vezes_jogado[indice] = vezes_jogado[indice] + 1
    '''