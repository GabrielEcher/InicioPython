"""
Lendo arquivos CSV

CSV - Comma Separated Values - Valores Separados por Vírgula


# Separador por vírgula
1, 2, 3, 4, 5, 6

# Separador por ponto e vírgula

"gabriel"; "echer"; "estudo"

# Separador por espaço

1 2 3 4 5 6

O IDEAL É TER UM PADRÃO DE SEPARADOR


# Possível de se trabalhar mas não é o ideal (trabalhoso)

with open('lutadores.csv', encoding='UTF-8') as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[3:]
    print(dados)

A linguagem python possui duas formas diferentes para ler dados em arquivos
CSV

- reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
- dict reader -> Permite que iteremos sobre as linhas do arquivo CSV como ordered dicts

# READER

with open('lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]}, nasceu em {linha[1]}, e mede {linha[2]}')

from csv import DictReader

with open('lutadores.csv', encoding='UTF-8') as arquivo:
   leitor_csv = DictReader(arquivo)
   for linha in leitor_csv:
       # Cada linha é um ordered dict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']}, e mede {linha['Altura (em cm)']}")
"""

# COM OUTRO SEPARADOR
from csv import DictReader

with open('lutadores.csv', encoding='UTF-8') as arquivo:
   leitor_csv = DictReader(arquivo, delimiter=';')
   for linha in leitor_csv:
       # Cada linha é um ordered dict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']}, e mede {linha['Altura (em cm)']}")

