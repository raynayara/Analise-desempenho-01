const fs = require('fs'); // Para manipular arquivos de texto
const os = require('os'); // Para informações do sistema
const xlsx = require('xlsx'); // Para manipular planilhas Excel

// Função para ordenar os números usando Quick Sort
function quickSort(numbers) {
    if (numbers.length <= 1) {
        return numbers;
    }
    const pivot = numbers[0];
    const left = numbers.slice(1).filter(num => num <= pivot);
    const right = numbers.slice(1).filter(num => num > pivot);
    return [...quickSort(left), pivot, ...quickSort(right)];
}

// Função para ler números do arquivo
function readNumbersFromFile(filename) {
    const data = fs.readFileSync(filename, 'utf8');
    return data.split('\n').filter(line => line.trim() !== '').map(Number);
}

// Função para calcular média
function calculateMean(values) {
    return values.reduce((sum, val) => sum + val, 0) / values.length;
}

// Função para calcular mediana
function calculateMedian(values) {
    values.sort((a, b) => a - b);
    const mid = Math.floor(values.length / 2);
    return values.length % 2 === 0 ? (values[mid - 1] + values[mid]) / 2 : values[mid];
}

// Função principal
async function main() {
    const inputFile = 'arqTEST03.txt';
    const outputExcelFile = 'resultadosJAVASCRIPT_QUICK.xlsx';
    const iterations = 10; // Número de vezes que o algoritmo será executado

    // Variáveis para guardar os resultados
    let executionTimes = [];
    let memoryUsages = [];

    console.log('Ordenação por Quick Sort');
    console.log(`Linguagem: JavaScript (Node.js)`);
    console.log(`Versão: ${process.version}`);
    console.log(`Executando Quick Sort ${iterations} vezes...\n`);

    for (let i = 0; i < iterations; i++) {
        const numbers = readNumbersFromFile(inputFile);

        // Medição de tempo e memória inicial
        const startTime = Date.now();
        const startMemory = process.memoryUsage().heapUsed / 1024;

        // Ordena os números usando Quick Sort
        quickSort(numbers);

        // Medição de tempo e memória final
        const endTime = Date.now();
        const endMemory = process.memoryUsage().heapUsed / 1024;

        // Calcula tempo e memória utilizados
        const timeTaken = endTime - startTime;
        const memoryUsed = endMemory - startMemory;

        console.log(`Execução ${i + 1}: Tempo = ${timeTaken} ms, Memória = ${memoryUsed.toFixed(2)} KB`);

        executionTimes.push(timeTaken);
        memoryUsages.push(memoryUsed);
    }

    // Calcula média e mediana
    const timeMean = calculateMean(executionTimes);
    const timeMedian = calculateMedian(executionTimes);
    const memoryMean = calculateMean(memoryUsages);
    const memoryMedian = calculateMedian(memoryUsages);

    console.log("\nResultados Finais:");
    console.log(`Tempo - Média: ${timeMean.toFixed(2)} ms, Mediana: ${timeMedian.toFixed(2)} ms`);
    console.log(`Memória - Média: ${memoryMean.toFixed(2)} KB, Mediana: ${memoryMedian.toFixed(2)} KB`);

    // Cria planilha com os resultados
    const workbook = xlsx.utils.book_new();
    const worksheetData = [
        ["Execução", "Tempo (ms)", "Memória (KB)"],
        ...executionTimes.map((time, index) => [index + 1, time, memoryUsages[index]]),
        [],
        ["Média", timeMean.toFixed(2), memoryMean.toFixed(2)],
        ["Mediana", timeMedian.toFixed(2), memoryMedian.toFixed(2)]
    ];
    const worksheet = xlsx.utils.aoa_to_sheet(worksheetData);
    xlsx.utils.book_append_sheet(workbook, worksheet, "Resultados");
    xlsx.writeFile(workbook, outputExcelFile);

    console.log(`Planilha com resultados salva em: ${outputExcelFile}`);
}

main();
