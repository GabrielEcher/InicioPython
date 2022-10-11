"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a 
função integrada open()

open() -> Na forma mais simples de utilização, nós passamos apenas um
parâmetro de entrada, que é o caminho para o arquivo a ser lido. Essa função
retorna um __io.TextIoWrapper e é com ele que trabalhamos então

# OBS: Por padrão, a função open() abre o arq para leitura. Este arquivo
deve existir, se não teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r -> Modo de Leitura. r -> read()
"""
# Exemplo 

arquivo = open('texto.txt', encoding= 'UTF-8')

#print(arquivo)
#print(type(arquivo))

# Para ler o conteúdo de seu arquivo após a abertura, devemos utilizar a função
# read()

print(arquivo.read())

# OBS: O python, utiliza o recurso para trabalhar com arquivos chamado cursor.
# o cursor funciona como o cursor quando estamos escrevendo