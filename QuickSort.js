const fs = require('fs'); // Para manipular arquivos de texto
const os = require('os'); // Para informações do sistema
const xlsx = require('xlsx'); // Para manipular planilhas Excel

function showMachineConfig() {
    console.log('Configurações da Máquina');
    console.log(`Sistema Operacional: ${os.type()} ${os.release()}`);
    console.log(`Plataforma: ${os.platform()}`);
    console.log(`Arquitetura: ${os.arch()}`);
    console.log(`Memória Total: ${(os.totalmem() / (1024 ** 2)).toFixed(2)} MB`);
    console.log(`Memória Livre: ${(os.freemem() / (1024 ** 2)).toFixed(2)} MB`);
    console.log(`Número de CPUs: ${os.cpus().length}`);
    console.log(`Hostname: ${os.hostname()}`);
    console.log(`Usuário atual: ${os.userInfo().username}`);
    console.log('---===---===---===---===---===---===---===---===---');
}

function quickSort(numbers) {
    if (numbers.length <= 1) {
        return numbers;
    }
    const pivot = numbers[0];
    const left = numbers.slice(1).filter(num => num <= pivot);
    const right = numbers.slice(1).filter(num => num > pivot);
    return [...quickSort(left), pivot, ...quickSort(right)];
}

//ler os números do arquivo
function readNumbersFromFile(filename) {
    const data = fs.readFileSync(filename, 'utf8');
    return data.split('\n').filter(line => line.trim() !== '').map(Number);
}

function calculateMean(values) {
    return values.reduce((sum, val) => sum + val, 0) / values.length;
}

function calculateMedian(values) {
    values.sort((a, b) => a - b);
    const mid = Math.floor(values.length / 2);
    return values.length % 2 === 0 ? (values[mid - 1] + values[mid]) / 2 : values[mid];
}

async function main() {
    const inputFile = 'arqTEST03.txt';
    const outputExcelFile = 'resultadosJAVASCRIPT_QUICK.xlsx';
    const iterations = 10; 

    let executionTimes = [];
    let memoryUsages = [];

    console.log('\n---===---===---===---===---===---===---===---===---');
    console.log('Ordenação por Quick Sort');
    console.log(`Linguagem: JavaScript (Node.js)`);
    console.log(`Versão: ${process.version}`);
    showMachineConfig();
    console.log(`Executando Quick Sort ${iterations} vezes...\n`);

    for (let i = 0; i < iterations; i++) {
        const numbers = readNumbersFromFile(inputFile);

        const startTime = Date.now();
        const startMemory = process.memoryUsage().heapUsed / 1024;

        quickSort(numbers);

        const endTime = Date.now();
        const endMemory = process.memoryUsage().heapUsed / 1024;

        const timeTaken = endTime - startTime;
        const memoryUsed = endMemory - startMemory;

        console.log(`Execução ${i + 1}: Tempo = ${timeTaken} ms, Memória = ${memoryUsed.toFixed(2)} KB`);

        executionTimes.push(timeTaken);
        memoryUsages.push(memoryUsed);
    }

    const timeMean = calculateMean(executionTimes);
    const timeMedian = calculateMedian(executionTimes);
    const memoryMean = calculateMean(memoryUsages);
    const memoryMedian = calculateMedian(memoryUsages);

    console.log("\nResultados Finais:");
    console.log(`Tempo - Média: ${timeMean.toFixed(2)} ms, Mediana: ${timeMedian.toFixed(2)} ms`);
    console.log(`Memória - Média: ${memoryMean.toFixed(2)} KB, Mediana: ${memoryMedian.toFixed(2)} KB`);

    // Salva os resultados em uma planilha Excel
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
