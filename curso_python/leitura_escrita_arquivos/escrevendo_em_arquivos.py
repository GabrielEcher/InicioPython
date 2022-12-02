"""
Escrevendo em arquivos

OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler
da mesma forma se abrirmos um arquivo para escrita, não podemos lê-lo somente escrever nele

OBS: Ao abrir um arquivo com o 'w', o arquivo é criado no SO

# Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write(), 
esta função recebe uma string como parâmetro, caso contrário teremos TypeError

# Exemplos de escrita - modo w - write

with open('novo.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Alterando dados.\n')
    arquivo.write('outros ,Podemos colocar quantas linhas a gente quer\n')
    arquivo.write('Esta é a ultima linha')

# Escrevendo várias vezes uma mesma palavra em um arquivo

with open('test.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Echer\n' * 1000)
"""
with open('frutas.txt', 'w', encoding='UTF-8') as arq:

    while True:
        fruta = input('Informe uma fruta ou digite sair:')
        if fruta != 'sair':
            arq.write(fruta + '\n')
        else:
            break
