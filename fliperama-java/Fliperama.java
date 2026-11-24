/*
* Disciplina: 2026-PCAP
* Projeto: MeuApp v5.0 - o Fliperama em Java (aula 33)
* Autor: Guilherme Antunes de Camargo
* LIAC: Menu do Fliperama em Java: metodo que desenham, um que le um numero dentro de uma faixa, e o laco que so para no 0
*
*/
import java.util.Scanner;

public class Fliperama {
    static final String DONO = "GUILHERME";
    static Scanner teclado = new Scanner(System.in);

    static void linha() {
        System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    }

    static void titulo(String texto) {
        linha();
        System.out.println("    " + texto);
        linha();
    }

    static int lerInteiro() {
        int numero = -1; // -1 quer dizer: nao era numero

        if (teclado.hasNextInt()) { // o que vem ai e um numero inteiro?
            numero = teclado.nextInt();
        }
        teclado.nextLine(); // joga fora o resto da linha, com o Enter
        return numero;
    }

    static int lerNumero(String mensagem, int minimo, int maximo) {
        int numero;

        System.out.print(mensagem + ": ");
        numero = lerInteiro();
        while (numero < minimo || numero > maximo) {
            System.out.print("Opcao invalido! Tente de novo: ");
            numero = lerInteiro();
        }
        return numero;
    }

    static void mostrarMenu() {
        linha();
        System.out.println("[1] Adivinhe o Numero");
        System.out.println("[2] Cadastrar jogador");
        System.out.println("[3] Listar jogadores");
        System.out.println("[0] Sair");
        linha();
    }

    public static void main(String[] args) {
        int opcao;

        mostrarMenu();
        opcao = lerNumero("Sua escolha", 0, 3);
        while (opcao != 0) {
            if (opcao == 1) {
                System.out.println("O jogo entra na fase 3.");
            } else if (opcao == 2) {
                System.out.println("O cadastro entra na fase 2.");
            } else {
                System.out.println("A lista entra na fase 2.");
            }
            mostrarMenu();
            opcao = lerNumero("Sua escolha", 0, 3);
        }

        titulo("Ate a proxima!");
    }
}