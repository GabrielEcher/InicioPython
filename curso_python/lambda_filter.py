"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção


import statistics # Biblioteca para trabalhar com dados estatisticos

# Dados coletados de algum sensor

dados = [1.3, 2.7, 0.8, 4.1, 4.8, -0.1]

# Calculando a media dos dados utilizando a função mean()

media = statistics.mean(dados)

print(media)

# OBS: Assim como a função map(), a filter(), recebe dois parâmetros, sendo
# uma função e um iterável

res = filter(lambda x: x > media, dados)
print(list(res)) # Valor só fica na memória até ele ser usado a primeira vez

paises = ['', 'Argentina', 'Brasil', '', 'Chile', 'Noruega', '']

res = filter(None, paises) # Remove os espaços em branco de uma lista

print(list(res))

# Ou

res2 = filter(lambda pais: len(pais) > 0, paises)
print(list(res2))

# Diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável, e retorna um objeto mapeando a função
#para cada elemento do iterável

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas
# os elementos de acordo com a função

# Exemplo mais complexo

usuarios = [
    {'username': 'Gabriel', 'tweets': ["Eu gosto de gatos"]},
    {'username': 'Joao', 'tweets': ["Eu gosto de cachorros"]},
    {'username': 'Henrique', 'tweets': []},
    {'username': 'Antonio', 'tweets': []},
    {'username': 'Gian', 'tweets': ["Eu gosto de papagaios", "Vou sair hoje"]},
    {'username': 'Gabriele', 'tweets': []}
]
#print(usuarios)

# Forma 1:
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

print(inativos)

# Forma 2:
inativos = list(filter(lambda usuario: not usuario['tweets', usuarios]))
"""

# Como combinar filter()  com map()

nomes = ['Vanessa', 'Ana', 'Maria']
# Devemos criar uma lista contendo "Sua instrutora é" + nome, desde que tenho menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)