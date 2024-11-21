import time  # Para medir o tempo de execução
import platform  # Para pegar informações do sistema e da linguagem
import psutil  # Para medir o uso de memória
import statistics  # Para calcular média e mediana
from openpyxl import Workbook  # Para criar a planilha Excel

# Função para ordenar os números usando Quick Sort
def quick_sort(numbers, low, high):
    if low < high:
        # Encontra o ponto de partição
        pi = partition(numbers, low, high)

        # Ordena as duas partes
        quick_sort(numbers, low, pi - 1)
        quick_sort(numbers, pi + 1, high)

# Função para partição do array
def partition(numbers, low, high):
    pivot = numbers[high]
    i = low - 1
    for j in range(low, high):
        if numbers[j] < pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]
    return i + 1

# Função para ler os números do arquivo
def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        # Lê os números e transforma cada linha em um número inteiro
        return [int(line.strip()) for line in file]

# Função para salvar os números ordenados em um arquivo
def write_numbers_to_file(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")  # Escreve cada número em uma nova linha

# Função para salvar os resultados na planilha
def save_to_excel(execution_times, memory_usages, avg_time, median_time, avg_memory, median_memory):
    # Cria uma nova planilha
    wb = Workbook()
    ws = wb.active
    ws.title = "Resultados2"

    # Cabeçalhos das colunas
    ws.append(["Execução", "Tempo (ms)", "Memória (KB)"])

    # Adiciona os tempos e as memórias de cada execução
    for i in range(10):
        ws.append([i + 1, execution_times[i], memory_usages[i]])

    # Adiciona as médias e medianas
    ws.append(["Média", avg_time, avg_memory])
    ws.append(["Mediana", median_time, median_memory])

    # Salva a planilha no arquivo
    wb.save("resultadosPYTHON_QUICK.xlsx")
    print("Resultados salvos em resultados.xlsx.")

def main():
    # Nome dos arquivos
    input_file = "arqTEST03.txt"  # Arquivo de entrada
    output_file = "arq-saida.txt"  # Arquivo de saída

    # Mostra informações da linguagem
    print("ordenação por Quick Sort")
    print("Linguagem: Python")
    print("Versão:", platform.python_version())

    # Mostra informações do sistema
    print("\nInformações do sistema:")
    print("Sistema:", platform.system())
    print("Processador:", platform.processor())
    print("Memória RAM total:", psutil.virtual_memory().total // 1024, "KB")

    # Lê os números do arquivo de entrada
    print("\nLendo os números do arquivo...")
    numbers = read_numbers_from_file(input_file)
    print("Números lidos:", numbers)

    # Variáveis para armazenar os tempos e memórias das execuções
    execution_times = []
    memory_usages = []

    # Rodar o algoritmo 10 vezes e coletar os tempos e memórias
    print("\nExecutando Quick Sort 10 vezes...")
    for i in range(10):
        # Medir o tempo de execução e a memória usada
        start_time = time.time()  # Marca o início do tempo
        start_memory = psutil.Process().memory_info().rss // 1024  # Marca a memória usada no início

        # Ordena os números usando Quick Sort
        quick_sort(numbers, 0, len(numbers) - 1)

        # Marca o fim do tempo e da memória usada
        end_time = time.time()
        end_memory = psutil.Process().memory_info().rss // 1024

        # Calcula o tempo e memória utilizados nessa execução
        elapsed_time_ms = (end_time - start_time) * 1000  # Tempo em milissegundos
        memory_used_kb = end_memory - start_memory  # Memória usada em KB

        # Adiciona os resultados às listas
        execution_times.append(elapsed_time_ms)
        memory_usages.append(memory_used_kb)

        print(f"Execução {i + 1}: Tempo = {elapsed_time_ms:.2f} ms, Memória = {memory_used_kb} KB")

    # Calcula média e mediana para o tempo e a memória
    avg_time = statistics.mean(execution_times)
    median_time = statistics.median(execution_times)
    avg_memory = statistics.mean(memory_usages)
    median_memory = statistics.median(memory_usages)

    # Salva os números ordenados no arquivo de saída
    print("\nSalvando os números ordenados no arquivo...")
    write_numbers_to_file(numbers, output_file)
    print(f"Números ordenados salvos em {output_file}.")

    # Mostra os resultados finais
    print("\nResultados Finais:")
    print(f"Tempo - Média: {avg_time:.2f} ms, Mediana: {median_time:.2f} ms")
    print(f"Memória - Média: {avg_memory} KB, Mediana: {median_memory} KB")

    # Salva os resultados na planilha Excel
    save_to_excel(execution_times, memory_usages, avg_time, median_time, avg_memory, median_memory)

# Inicia o programa
if __name__ == "__main__":
    main()
