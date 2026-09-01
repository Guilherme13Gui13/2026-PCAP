# Fliperama do Guilherme 

Um fliperama de terminal com quatros jogos, placar que não esquece e cadastro de jogadores. Projeto da disciplina PCAP, 1º. ano do Técnico em Informática do IFPR.

## O que ele faz

- Quatro jogos pelo menu: Adivinhe o Número, Pedra-Papel-Tesoura, Par ou Ímpar e Termo.
- Placar que conta quantas vezes cada jogo foi jogado e continua contando depois de fechar o programa.
- Cadastro de jogadores: cadastrar, listar, alterar e excluir.

## Como rodar

'''
cd fliperama
python3 main.py
'''

## Os arquivos

- 'main.py' - o gabinete: menu,placar e chamadas
- 'telas.py' - ferramentas visuais
- 'modulos.py' - ferramentas de lógica: as três funções que perguntam e conferem
- 'placar.py' - quantas partidas cada jogo teve
- 'jogadores.py' - quem são os jogadores
- 'adivinhe.py', 'ppt.py', 'parimpar.py', 'termo.py' - um arquivo por jogo
- 'placar.csv' e 'jogadores.csv' - os dados, que nascem sozinhos

A função 'ler_texto' ficou no 'modulos.py' ,porque, assim como 'ler_opcao' e 'ler_numero' ela serve para os jogos, sendo uma função universal.

## De onde ele veio

- Aula 20: os quatros jogos viraram um programa só, com módulos e menu
- Aula 21: entrou o Pedra-Papel_Tesoura e o placar passou a sobreviver
- Aula 22: entrou o cadastro de jogadores, com as quatro operações
- Aula 23: campo em branco barrado e o projeto documentado

## O que ainda não funciona

- Nome com vírgula quebra a linha do arquivo, porque a vírgula é o separador
- O apelido aceita apelido com espaços em branco

## Autoavaliacao

Conceito que eu acho que a minha entrega vale: B

### Mapa do projeto: onde esta cada coisa

| O que | Arquivo | Funcao |
|---|---|---|
| Adivinhe o Numero | `adivinhe.py` | `jogar_adivinhe` |
| Pedra-Papel-Tesoura | `ppt.py` | `jogar_ppt` |
| Par ou Impar | `parimpar.py` | `jogar_parimpar` |
| Termo | `termo.py` | `jogar_meujogo` |
| Cadastro de jogadores | `jogadores.py` | `menu_jogadores` |
| Ranking Top 10 | `jogadores.py` | `listar` |
| Placar que sobrevive | `placar.py` | `salvar_placar`, `carregar_placar` |

### Criterio por criterio: o nivel e a prova

| Criterio | Nivel | Onde esta a prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura e registro | C | [arquivo, linha] |
| 2. As quatro operacoes | C | [jogadores.py, 33] |
| 3. Busca e indice | A | [jogadores.py, 64] |
| 4. Persistencia e primeira execucao | C | [jogadores.py] |
| 5. Documentacao e autoavaliacao | A | [README.md e README-termo.md] |
| 6. Jogo autoral e reuso | A | [termo.py, linhas 10 - 91] |

### Usei IA?

Sim, professor, usei IA, usei para que ela criasse uma lista com 100 palavras seguindo alguns critérios para o jogo termo, também usei em uma daa funções do mesmo jogo, caso queria ver versões anteriores dos projetos sempre deixo entre '''''' para que você possa ver.

## Considerações finais

Professor, não sei o por quê, mas estou tendo erros com a função salvar_jogadores do jogadores.py, essa função sempre funcionou, mas agora não está mais... fiz o que pude, espero tirar pelo menos C pelo esforço, desculpa...