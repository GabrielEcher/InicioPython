"""
Escrevendo em arquivos CSV

writerow() -> Escreve uma linha

#writer: gera um objeto para que possamos escrever em um arquivo
#csv, utilizamos o método writerow(), este metodo recebe uma lista

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título','Gênero', 'Duração'])
    
    while filme != 'sair':
        filme = input("Informe o nome do filme: ")
        if filme != 'sair':
            genero = input("Informe o gênero: ")
            duracao = input("Informe a duração (em minutos): ")
            escritor_csv.writerow([filme, genero, duracao])
"""

# DictWriter

from csv import DictWriter

with open('filmes.csv', 'w', newline='', encoding='UTF-8') as arquivo:
    cabecalho = ["Titulo", "Gênero", "Duração"]
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    
    while filme != 'sair':
        
        filme = input("Informe o nome do filme: ")
        
        if filme != 'sair':
            genero = input("Informe o gênero: ")
            duracao = input("Informe a duração (em minutos): ")
            escritor_csv.writerow({"Titulo": filme, "Gênero": genero, "Duração": duracao})