from os.path import exists
from telas import titulo, linha
from modulos import ler_opcao, ler_texto

ARQUIVO = 'fliperama/jogadores.csv'


# ================================================================
# ARQUIVO : jogadores.py (pasta fliperama)
# DISCIPLINA : Pensamento Computacional, Algoritimos e Programação
# (2026-PCAP)
# AULA : 22 - MauApp v2.0: o cadastro de jogadores
# AUTOR : Guilherme Antunes de Camargo
# Revisado : Aula 23 - validação de campo vazio e documentação
# CONCEITOS : Registro como lista de campos, cadastro como lista
# de listas, cadastrar, listar, bucar, alterar, excluir, persistencia
# em arquivo .csv
# ================================================================
#
# O QUE ESTE ARQUIVO É
#       A quarta gaveta do projeto. O telas.py cuida do que aparee,
#       o modulos.py cuida do que o programa pergunta, o placar.py
#       cuida de quantas partidas cada jogo teve, e o jogadores.py
#       cuida de quem jogou
#
# O REGISTRO 
#       Cada jogador e uma lista de três campos, sempre nest ordem:
#           indice 0 -> apelido | 1 -> nome | 2 -> partidas
#       E o cadastro e uma lista dessas listas.
# ================================================================


def cadastrar(jogadores):
    ''' 
Pergunta apelido e nome e acrescenta um jogador ao cadastro.
Não devolve nada: o cadastro muda no lugar.
'''
    titulo('NOVO JOGADOR')

    apelido = ler_texto('Apelido (sem espaços)').lower()
    nome = ler_texto('Nome completo')

    novo = [apelido, nome, '0']
    jogadores.append(novo)

    print('Jogador ' + apelido + ' cadastrado.')
    linha()


def listar(jogadores):
    titulo('TOP 10 JOGADORES')

    if len(jogadores) == 0:
        print('Nenhum jogador cadastrado ainda.')
    else:
        ranking = sorted(jogadores, key=lambda j: int(j[2]), reverse=True)

        for i in range(len(ranking[:10])):
            print(str(i + 1).rjust(2) + '. ' + ranking[i][0].ljust(6) + ' | ' + ranking[i][1].ljust(18) + ' | ' + ranking[i][2].rjust(3) + ' partidas')

    linha()


def buscar(jogadores, apelido):
    '''
    Procura um apelido no cadastro e diz ONDE ele esta.

    Parametros:
        jogadores (list) - o cadastro inteiro.
        apelido (str) - o apelido procurado, em minúsculas.

    Retorno:
        Int - a posição do jogador na lista, ou -1 se não achar.
    '''
    for i in range(len(jogadores)):
        if jogadores[i][0] == apelido:
            return i

    return -1


def alterar(jogadores):
    listar(jogadores)

    apelido = ler_texto('Apelido de quem vai mudar de nome: ').lower()
    i = buscar(jogadores, apelido)

    if i == -1:
        print('Não achei ninguém com esse apelido.')
    else:
        print('Nome atual: ' + jogadores[i][1])
        jogadores[i][i] = ler_texto('Nome novo: ').strip()
        print('Pronto. Agora e ' + jogadores[i][i] + '.')

    linha()


def excluir(jogadores):
    '''
    Recebe como parametro o jogadores e busca qual deles vai ser excluido e qual nome entra no lugar.
    '''    
    listar(jogadores)

    apelido = input('Apelido de quem vai sair do cadastro: ').strip().lower()
    i = buscar(jogadores, apelido)

    if i == -1:
        print('Não achei ninguém com esse apelido.')
    else:
        print('Vou apagar o cadastro de ' + jogadores[i][1] + '.')
        print('[1] Confirmar')
        print('[2] Deixar com está')
        certeza = ler_opcao('Sua escolha', ['1', '2'])

        if certeza == '1':
            jogadores.pop(i)
            print('Cadastro apagado.')
        else:
            print('Nada foi apagado')

    linha()


def salvar_jogadores(jogadores):
    arquivo = open(ARQUIVO, 'w')

    for jogador in jogadores:
        arquivo.write(jogador[0] + ',' + jogador[1] + ',' + jogador[2] + '\n')

    arquivo.close()


def carregar_jogadores():
    if not exists(ARQUIVO):
        return []

    arquivo = open(ARQUIVO, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    lidos = []
    for linha_lida in linhas:
        campos = linha_lida.strip().split(',')
        lidos.append(campos)

    return lidos


def menu_jogadores(jogadores):
    while True:
        titulo('CADASTRO DE JOGADORES')
        print('[1] Casdastrar jogador')
        print('[2] Listar jogador')
        print('[3] Alterar nome')
        print('[4] Excluir jogador')
        print('[0] Voltar ao fliperama')
        linha()

        opcao = ler_opcao('Sua escolha', ['0', '1', '2', '3', '4'])

        if opcao == '0':
            break
        elif opcao == '1':
            cadastrar(jogadores)
        elif opcao == '2':
            listar(jogadores)
        elif opcao == '3':
            alterar(jogadores)
        else:
            excluir(jogadores)

# --- BANCADA DE TESTE --- #
jogadores = carregar_jogadores()
listar(jogadores)


























