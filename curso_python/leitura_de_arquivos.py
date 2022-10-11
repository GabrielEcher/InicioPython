"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a 
função integrada open()

open() -> Na forma mais simples de utilização, nós passamos apenas um
parâmetro de entrada, que é o caminho para o arquivo a ser lido. Essa função
retorna um __io.TextIoWrapper e é com ele que trabalhamos então

# OBS: Por padrão, a função open() abre o arq para leitura. Este arquivo
deve existir, se não teremos o erro FileNotFoundError

"""
# Exemplo 

arquivo = open('texto.txt')

print(arquivo)
print(type(arquivo))