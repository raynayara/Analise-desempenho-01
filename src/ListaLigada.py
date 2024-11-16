class Node:
    def __init__(self, data):
        self.data = data
        self.prox = None


class Lista:
    def __init__(self):
        self.head = None

    def adicionar(self, data, posicao):
        novo = Node(data)

        # Posição inválida
        if posicao < 0:
            print("Posição inválida.")
            return

        # Insere na cabeça
        if posicao == 0:
            novo.prox = self.head
            self.head = novo
            return

        # Insere em uma posição específica
        aux = self.head
        contador = 0

        while aux is not None and contador < posicao - 1:
            aux = aux.prox
            contador += 1

        # Posição ultrapassa o tamanho da lista
        if aux is None:
            print("Posição maior que o tamanho da lista.")
            return

        # Inserir o novo nó
        novo.prox = aux.prox
        aux.prox = novo

    def adicionar_no_final(self, data):
        novo = Node(data)

        # Se a lista estiver vazia
        if self.head is None:
            self.head = novo
            return

        # Percorre a lista até o último nó
        aux = self.head
        while aux.prox is not None:
            aux = aux.prox

        aux.prox = novo

    def imprimir(self):
        aux = self.head
        if aux is None:
            print("A lista está vazia.")
            return

        elementos = []
        while aux is not None:
            elementos.append(aux.data)
            aux = aux.prox

        print(" -> ".join(map(str, elementos)))

    def remover(self, data):
        # Se a lista estiver vazia
        if self.head is None:
            print("A lista está vazia. Nada a remover.")
            return

        # Remove o primeiro elemento, se for o caso
        if self.head.data == data:
            self.head = self.head.prox
            return

        # Percorre a lista para encontrar o elemento
        aux = self.head
        while aux.prox is not None:
            if aux.prox.data == data:
                aux.prox = aux.prox.prox
                return
            aux = aux.prox

        print(f"Valor {data} não encontrado na lista.")
