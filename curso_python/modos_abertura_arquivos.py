"""
Modos de abertura de arquivos:

r -> Abre para leitura - padrão
w -> Abre para a escrita (sobrescreve caso o arquivo já exista)
x -> Abre para escrita somente se o arquivo não existir - caso o arquivo exista gera FileExistsError
a -> Abre para escrita, adicionando conteúdo ao final do arquivo
+ -> Abre para o modo de atualização, Leitura e escrita

http://docs.python.org/3/library/functions.html#open

# Exemplo x:
try:
    with open('n_existe.txt', 'x', encoding='UTF-8') as arquivo:
        arquivo.write('Teste de conteúdo')
except:
    print('O arquivo já existe')

# Exemplo a:

with open('frutas.txt', 'a', encoding='UTF-8') as arq:

    while True:
        fruta = input('Informe uma fruta ou digite sair:')
        if fruta != 'sair':
            arq.write(fruta + '\n')
        else:
            break
"""

with open('NOVO1.txt', 'r+', encoding='UTF-8') as arquivo:
    arquivo.seek(0)
    arquivo.write('Novo topo\n')
    arquivo.write('Nova linha\n')
    arquivo.write('Mais uma linha\n')
    
