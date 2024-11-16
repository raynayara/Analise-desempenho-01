from ListaLigada import Lista  


def processar_arquivo(caminho_arquivo):
    lista = Lista()

    try:
        with open(caminho_arquivo, "r") as arquivo:
            # Leitura dos valores iniciais e adição na lista
            valores_iniciais = list(map(int, arquivo.readline().split()))
            for valor in valores_iniciais:
                lista.adicionar_no_final(valor)

            # Imprime a lista inicial antes de qualquer operação
            print("Lista inicial: ", end="")
            lista.imprimir()

            # Leitura e processamento das ações
            num_acoes = int(arquivo.readline().strip())
            for _ in range(num_acoes):
                partes = arquivo.readline().split()
                acao = partes[0]

                if acao == "A":  # Adicionar
                    valor = int(partes[1])
                    posicao = int(partes[2])
                    lista.adicionar(valor, posicao)
                    print(f"Ação: Adicionar | Valor: {valor} | Posição: {posicao}")

                elif acao == "R":  # Remover
                    valor = int(partes[1])
                    lista.remover(valor)
                    print(f"Ação: Remover | Valor: {valor}")

                elif acao == "P":  # Imprimir
                    print("Ação: Imprimir")
                    lista.imprimir()

                else:
                    print(f"Ação desconhecida: {acao}")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")


if __name__ == "__main__":
    caminho = "arq.txt"  # Substitua pelo caminho correto do arquivo
    processar_arquivo(caminho)
