# TERMO

Jogo autoral do meu fliperama. Abre pela opcao [4] do menu.
Autor: Guilherme Antunes de Camargo

## A regra

O jogador deve escolher uma palavra de 5 letras, o sistema valida ela com ler_texto e conta a quantidade certa de letras. em seguida o sistema vê se quais letras da palavra escolhida estão na posição certa ou errada ou se não existem na palavra secreta. 
## Como jogar

1. Dentro da pasta `fliperama`, rode `python3 main.py`.
2. Escolha a opcao `[4]` no menu.
3. Escolha uma palavra e a partir das dicas tente descobrir a palavra secreta.

## O que eu reusei do projeto, e onde

| Peca | De qual modulo | Onde eu uso | Para que serve ali |
|---|---|---|---|
| `titulo()` | `telas.py` | `termo.py`, linha [30] | desenha a testeira do jogo |
| `linha()` | `telas.py` | `termo.py`, linha [29] | fecha a tela no fim da partida |
| `ler_numero()` | `modulos.py` | `termo.py`, linha [N] | pede o numero e recusa fora do intervalo |
| contagem da partida | `placar.py` | `main.py`, linha [N] | soma 1 em `vezes_jogado` a cada partida |

## Exemplo de execucao

```
Escolha uma opção: 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                           Termo                            
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INSTRUÇÕES:
Nesse jogo você deverá adivinhar uma palavra secreta.
O computador falará se cada uma das letras está na posição 
certa, fora de ordem ou se não existe. Bom jogo !
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Escolha sua palavra de 5 letras sem acento ortográfico: Jesus
A letra J não existe na palavra secreta...
A letra e está no lugar errado.
A letra s não existe na palavra secreta...
A letra u não existe na palavra secreta...
A letra s não existe na palavra secreta...
Escolha sua palavra de 5 letras sem acento ortográfico: 
```

## O que ainda nao funciona

- Contagem de partidas...
