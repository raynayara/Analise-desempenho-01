const fs = require('fs'); // Módulo para manipular arquivos
const os = require('os'); // Módulo para obter informações sobre o sistema operacional

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

function bubbleSort(numbers) {
    let n = numbers.length; 
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (numbers[j] > numbers[j + 1]) {
                let temp = numbers[j];
                numbers[j] = numbers[j + 1];
                numbers[j + 1] = temp;
            }
        }
    }
}

function readNumbersFromFile(filename) {
    const data = fs.readFileSync(filename, 'utf8'); 
    return data.split('\n').filter(line => line.trim() !== '').map(Number);
}

function saveNumbersToFile(filename, numbers) {
    const data = numbers.join('\n'); 
    fs.writeFileSync(filename, data, 'utf8'); 
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
    const inputFile = 'arqG.txt'; 
    const outputFile = 'JSarq.saida.txt'; 
    const iterations = 10; 

    let executionTimes = []; 
    let memoryUsages = []; 

    console.log('---===---===---===---===---===---===---===---===---');
    console.log('Ordenação por Bubble Sort');
    console.log(`Linguagem: JavaScript (Node.js)`); 
    console.log(`Versão: ${process.version}`);
    console.log('---===---===---===---===---===---===---===---===---');
    
    showMachineConfig();
    
    console.log(`\nExecutando Bubble Sort ${iterations} vezes...\n`);

    let sortedNumbers; 

    for (let i = 0; i < iterations; i++) {
        const numbers = readNumbersFromFile(inputFile); 

        const startTime = Date.now(); // Marca o tempo de início
        const startMemory = process.memoryUsage().heapUsed / 1024; // Obtém o uso inicial de memória

        bubbleSort(numbers);

        if (i === iterations - 1) {
            sortedNumbers = numbers;
        }

        const endTime = Date.now();
        const endMemory = process.memoryUsage().heapUsed / 1024;

        const timeTaken = endTime - startTime; 
        const memoryUsed = endMemory - startMemory; 

        console.log(`Execução ${i + 1}: Tempo = ${timeTaken} ms, Memória = ${memoryUsed.toFixed(2)} KB`);

        executionTimes.push(timeTaken); 
        memoryUsages.push(memoryUsed); 
    }

    saveNumbersToFile(outputFile, sortedNumbers);
    console.log(`Números ordenados salvos em: ${outputFile}`);

    const timeMean = calculateMean(executionTimes);
    const timeMedian = calculateMedian(executionTimes);
    const memoryMean = calculateMean(memoryUsages);
    const memoryMedian = calculateMedian(memoryUsages);

    console.log('\n---===---===---===---===---===---===---===---===---');
    console.log("Resultados Finais:");
    console.log(`Tempo - Média: ${timeMean.toFixed(2)} ms, Mediana: ${timeMedian.toFixed(2)} ms`);
    console.log(`Memória - Média: ${memoryMean.toFixed(2)} KB, Mediana: ${memoryMedian.toFixed(2)} KB`);
    console.log('---===---===---===---===---===---===---===---===---\n');
}

main();
