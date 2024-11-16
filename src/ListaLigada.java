package src;

class Node {
    int data;
    Node prox;

    Node(int data) {
        this.data = data;
        this.prox = null;
    }
}

class Lista {
    Node head;

    public Lista() {
        this.head = null;
    }

    public void adicionar(int data, int posicao) {
        Node novo = new Node(data);

        
        if (posicao < 0) {
            System.out.println("Posição inválida.");
            return;
        }

        
        if (posicao == 0) {
            novo.prox = this.head;
            this.head = novo;
            return;
        }

        
        Node aux = this.head;
        int contador = 0;

        while (aux != null && contador < posicao - 1) {
            aux = aux.prox;
            contador++;
        }

        
        if (aux == null) {
            System.out.println("Posição maior que o tamanho da lista.");
            return;
        }

        
        novo.prox = aux.prox;
        aux.prox = novo;
    }

    public void adicionarNoFinal(int data) {
        Node novo = new Node(data);

        
        if (this.head == null) {
            this.head = novo;
            return;
        }

       
        Node aux = this.head;
        while (aux.prox != null) {
            aux = aux.prox;
        }

        
        aux.prox = novo;
    }

    public void imprimir() {
        Node aux = this.head;
        if (aux == null) {
            System.out.println("A lista está vazia.");
            return;
        }

        while (aux != null) {
            System.out.print(aux.data);
            if (aux.prox != null) { 
                System.out.print(" -> ");
            }
            aux = aux.prox;
        }
        System.out.println();
    }

    public void remover(int data) {
        if (this.head == null) {
            System.out.println("A lista está vazia. Nada a remover.");
            return;
        }

        if (this.head.data == data) {
            this.head = this.head.prox;
            return;
        }

        Node aux = this.head;
        while (aux.prox != null) {
            if (aux.prox.data == data) {
                aux.prox = aux.prox.prox;
                return;
            }
            aux = aux.prox;
        }

        System.out.println("Valor " + data + " não encontrado na lista.");
    }
}
