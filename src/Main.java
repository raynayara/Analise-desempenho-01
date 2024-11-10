package src;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        Lista lista = new Lista();

        try (BufferedReader br = new BufferedReader(new FileReader("arq.txt"))) {
            
            for (String valor : br.readLine().split(" ")) {
                lista.adicionar(Integer.parseInt(valor));
            }
            
            int numAcoes = Integer.parseInt(br.readLine().trim());
            for (int i = 0; i < numAcoes; i++) {
                String[] partes = br.readLine().split(" ");
                switch (partes[0]) {
                    case "A":
                        lista.adicionar(Integer.parseInt(partes[1]));
                        break;
                    case "R":
                        lista.remover(Integer.parseInt(partes[1]));
                        break;
                    case "P":
                        lista.imprimir();
                        break;
                }
            }

        } catch (IOException e) {
            System.out.println("Erro ao ler o arquivo: " + e.getMessage());
        }
    }
}

