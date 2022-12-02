"""
Sorted

OBS: Não é igual a função sort(), ele só funciona em listas.
Podemos utilizar o sorted() com qualquer iterável
Serve para ordenar elementos

# Exemplo

numeros = {1, 6, 10, 9} # Retorna uma lista, independente de qual tipo de iterável
print(numeros)
print(sorted(numeros)) # A lista original se mantém intacta
print(numeros)

numeros = [5, 8, 4, 10]
print(numeros)
print(set(sorted(numeros))) # Podemos escolher também qual tipo de iterável gerará

# Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True))

# Utilizando o sorted() para coisas mais complexas
usuarios = [
    {'username': 'Gabriel', 'tweets': ["Eu gosto de gatos"]},
    {'username': 'Joao', 'tweets': ["Eu gosto de cachorros"]},
    {'username': 'Henrique', 'tweets': []},
    {'username': 'Antonio', 'tweets': []},
    {'username': 'Gian', 'tweets': ["Eu gosto de papagaios", "Vou sair hoje"]},
    {'username': 'Gabriele', 'tweets': []}
]
# Ordenando por username - ORDEM ALFABÉTICA
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
"""

musicas = [
    {"titulo": "Can you feel my heart", "tocou": 2},
    {"titulo": "Numb", "tocou": 4},
    {"titulo": "In the end", "tocou": 1},
    {"titulo": "Something in the way", "tocou": 7},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))                                         

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))  