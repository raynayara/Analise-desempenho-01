package src;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        Lista lista = new Lista();

        try (BufferedReader br = new BufferedReader(new FileReader("arq.txt"))) {
            
            String[] valoresIniciais = br.readLine().split(" ");
            for (String valor : valoresIniciais) {
                lista.adicionarNoFinal(Integer.parseInt(valor)); 
            }

            
            int numAcoes = Integer.parseInt(br.readLine().trim());
            for (int i = 0; i < numAcoes; i++) {
                String[] partes = br.readLine().split(" ");
                String acao = partes[0];

                switch (acao) {
                    case "A": 
                        int valorAdicionar = Integer.parseInt(partes[1]);
                        int posicaoAdicionar = Integer.parseInt(partes[2]);
                        lista.adicionar(valorAdicionar, posicaoAdicionar);
                        System.out.println("Ação: Adicionar | Valor: " + valorAdicionar + " | Posição: " + posicaoAdicionar);
                        break;

                    case "R": 
                        int valorRemover = Integer.parseInt(partes[1]);
                        lista.remover(valorRemover);
                        System.out.println("Ação: Remover | Valor: " + valorRemover);
                        break;

                    case "P": 
                        System.out.println("Ação: Imprimir");
                        lista.imprimir();
                        break;

                    default:
                        System.out.println("Ação desconhecida: " + acao);
                }
            }

        } catch (IOException e) {
            System.out.println("Erro ao ler o arquivo: " + e.getMessage());
        }
    }
}
