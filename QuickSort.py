import time  # Para medir o tempo de execução
import platform  # Para pegar informações do sistema e da linguagem
import psutil  # Para medir o uso de memória
import statistics  # Para calcular média e mediana
from openpyxl import Workbook  # Para criar a planilha Excel
import os  # Para pegar o hostname e usuário atual
import matplotlib.pyplot as plt
import random  # Para escolher o pivô aleatoriamente

# Função de partição com escolha de pivô aleatório
def partition(numbers, low, high):
    pivot_index = random.randint(low, high)  # Escolhe um pivô aleatório
    numbers[pivot_index], numbers[high] = numbers[high], numbers[pivot_index]  # Troca o pivô com o último elemento
    pivot = numbers[high]
    i = low - 1
    for j in range(low, high):
        if numbers[j] < pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]
    return i + 1

# Função para realizar o Quick Sort
def quick_sort(numbers, low, high):
    if low < high:
        pi = partition(numbers, low, high)
        quick_sort(numbers, low, pi - 1)
        quick_sort(numbers, pi + 1, high)

# Função para ler os números do arquivo
def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]

# Função para salvar os números no arquivo
def write_numbers_to_file(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

# Função para salvar os resultados em uma planilha Excel
def save_to_excel(execution_times, memory_usages, avg_time, median_time, avg_memory, median_memory):
    wb = Workbook()
    ws = wb.active
    ws.title = "Resultados"

    ws.append(["Execução", "Tempo (ms)", "Memória (KB)"])

    for i in range(10):
        ws.append([i + 1, execution_times[i], memory_usages[i]])

    ws.append(["Média", avg_time, avg_memory])
    ws.append(["Mediana", median_time, median_memory])

    wb.save("resultadosPYTHON_QUICK.xlsx")
    print("Resultados salvos em resultadosPYTHON_QUICK.xlsx.")

# Função para gerar os gráficos
def generate_graphs(execution_times, memory_usages, avg_time, median_time, avg_memory, median_memory):
    # Gráfico de Tempo (média)
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, 11), execution_times, label='Tempo de Execução (ms)', color='blue', marker='o')
    plt.axhline(avg_time, color='red', linestyle='--', label=f'Média Tempo: {avg_time:.2f} ms')
    plt.axhline(median_time, color='green', linestyle='--', label=f'Mediana Tempo: {median_time:.2f} ms')
    plt.xlabel('Execuções')
    plt.ylabel('Tempo (ms)')
    plt.title('Tempo de Execução do Quick Sort')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafico_tempo.png')
    plt.show()

    # Gráfico de Memória (média)
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, 11), memory_usages, label='Uso de Memória (KB)', color='blue', marker='o')
    plt.axhline(avg_memory, color='red', linestyle='--', label=f'Média Memória: {avg_memory} KB')
    plt.axhline(median_memory, color='green', linestyle='--', label=f'Mediana Memória: {median_memory} KB')
    plt.xlabel('Execuções')
    plt.ylabel('Memória (KB)')
    plt.title('Uso de Memória do Quick Sort')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafico_memoria.png')
    plt.show()

    # Gráfico Comparativo - Tempo vs Memória
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, 11), execution_times, label='Tempo de Execução (ms)', color='blue', marker='o')
    plt.plot(range(1, 11), memory_usages, label='Uso de Memória (KB)', color='orange', marker='x')
    plt.xlabel('Execuções')
    plt.ylabel('Valores')
    plt.title('Comparativo: Tempo de Execução e Uso de Memória')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafico_comparativo.png')
    plt.show()

# Função principal
def main():
    input_file = "arqG.txt"  # Arquivo de entrada com números para ordenar
    output_file = "PYarq-saida.txt"  # Arquivo de saída com os números ordenados

    print("\n" + "---====---" * 5)
    print("Ordenação por Quick Sort")
    print("Linguagem: Python")
    print("Versão:", platform.python_version())

    print("\nInformações do sistema:")
    print("Sistema:", platform.system())
    print("Processador:", platform.processor())
    print("Arquitetura:", platform.architecture()[0])
    print("Memória RAM total:", psutil.virtual_memory().total // 1024, "KB")
    print("Memória Livre:", psutil.virtual_memory().available // 1024, "KB")
    print("Número de CPUs:", psutil.cpu_count(logical=False))
    print("Hostname:", platform.node())
    print("Usuário Atual:", os.getlogin())
    print("---====---" * 5)

    print("\nLendo os números do arquivo...")
    numbers = read_numbers_from_file(input_file)
    print("Números lidos:", numbers)

    execution_times = []
    memory_usages = []

    print("\nExecutando Quick Sort 10 vezes...")
    for i in range(10):
        start_time = time.time()  # Marca o início do tempo
        start_memory = psutil.Process().memory_info().rss // 1024  # Marca a memória usada no início

        quick_sort(numbers, 0, len(numbers) - 1)

        end_time = time.time()
        end_memory = psutil.Process().memory_info().rss // 1024

        elapsed_time_ms = (end_time - start_time) * 1000  
        memory_used_kb = end_memory - start_memory 

        execution_times.append(elapsed_time_ms)
        memory_usages.append(memory_used_kb)

        print(f"Execução {i + 1}: Tempo = {elapsed_time_ms:.2f} ms, Memória = {memory_used_kb} KB")

    avg_time = statistics.mean(execution_times)
    median_time = statistics.median(execution_times)
    avg_memory = statistics.mean(memory_usages)
    median_memory = statistics.median(memory_usages)

    print("\nSalvando os números ordenados no arquivo...")
    write_numbers_to_file(numbers, output_file)
    print(f"Números ordenados salvos em {output_file}.")

    print("\n" + "---====---" * 5)
    print("Resultados Finais:")
    print(f"Tempo - Média: {avg_time:.2f} ms, Mediana: {median_time:.2f} ms")
    print(f"Memória - Média: {avg_memory} KB, Mediana: {median_memory} KB")
    print("---====---" * 5)

    save_to_excel(execution_times, memory_usages, avg_time, median_time, avg_memory, median_memory)
    generate_graphs(execution_times, memory_usages, avg_time, median_time, avg_memory, median_memory)

if __name__ == "__main__":
    main()
