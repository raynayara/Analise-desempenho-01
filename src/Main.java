package src;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        Lista lista = new Lista();

        try (BufferedReader br = new BufferedReader(new FileReader("arq.txt"))) {
            
            // Leitura dos valores iniciais e adição na lista
            for (String valor : br.readLine().split(" ")) {
                lista.adicionar(Integer.parseInt(valor));
            }
            
            // Leitura e processamento das ações
            int numAcoes = Integer.parseInt(br.readLine().trim());
            for (int i = 0; i < numAcoes; i++) {
                String[] partes = br.readLine().split(" ");
                String acao = partes[0];

                switch (acao) {
                    case "A":
                        lista.adicionar(Integer.parseInt(partes[1]));
                        System.out.println("Ação: Adicionar | Valor adicionado: " + partes[1]);
                        break;
                    case "R":
                        lista.remover(Integer.parseInt(partes[1]));
                        System.out.println("Ação: Remover | Valor removido: " + partes[1]);
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
