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

    public void adicionar(int data){
        Node novo = new Node(data);
        if (this.head == null){
           this.head = novo; 
        }else{
            Node aux = this.head;
            while(aux.prox != null){
                aux = aux.prox;
            }
            aux.prox = novo;
        }

    } 

    public void imprimir(){
        Node aux = this.head;
        while(aux != null){
            System.out.println(aux.data);
            aux = aux.prox;
        }
    }

    public void remover(int data){
        if (this.head == null){
            return;
        }
        if (this.head.data == data){
            this.head = this.head.prox;
            return;
        }
        Node aux = this.head;
        while(aux.prox != null){
            if (aux.prox.data == data){
                aux.prox = aux.prox.prox;
                return;
            }
            aux = aux.prox;
        }

    }

}