"""
min e max
max() -> retorna o maior valor em um iterável ou o maior de dois ou mais elementos
# Exemplos
lista = [12, 15, 32, 88, 111]
print(max(lista))
dicionario = {'a': 12, 'b': 15, 'c': 32, 'd': 88, 'f': 111}
print(max(dicionario.values()))
# Faça um programa que receba dois valores do usuario e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(max(val1, val2))
min() -> retorne o menor valor em um iterável ou o menor de dois ou mais elementos
# Exemplos
lista = [12, 15, 32, 88, 111]
print(min(lista))
dicionario = {'a': 12, 'b': 15, 'c': 32, 'd': 88, 'f': 111}
print(min(dicionario.values()))
# Faça um programa que receba dois valores do usuario e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(min(val1, val2))
# Outros exemplos
nomes = ['Ana', 'Joao', 'Gabriel', 'Max']
print(max(nomes)) # Retorna o maior conforme a primeira letra seguindo a ordem alfabética
print(min(nomes)) # Retorna o menor conforme a primeira letra seguindo a ordem alfabética
print(max(nomes, key=lambda nome: len(nome))) # Retorna o nome com mais letras da lista
print(min(nomes, key=lambda nome: len(nome))) # Retorna o nome com menos letras da lista
"""

musicas = [
    {"titulo": "Can you feel my heart", "tocou": 2},
    {"titulo": "Numb", "tocou": 4},
    {"titulo": "In the end", "tocou": 1},
    {"titulo": "Something in the way", "tocou": 7},
]

print(max(musicas, key=lambda musica: musica["tocou"]))
print(min(musicas, key=lambda musica: musica["tocou"]))


# PRINTANDO APENAS O TITULO DA MUSICA 
print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])
print(min(musicas, key=lambda musica: musica["tocou"])["titulo"])

# Como encontrar a musica mais tocada e a menos tocada sem usar max(), min() ou lambda

maxi = 0

for musica in musicas:
    if musica['tocou'] > maxi:
        maxi = musica['tocou']
        
for musica in musicas:
    if musica['tocou'] == maxi:
        print(musica['titulo'])


mini = 99999

for musica in musicas:
    if musica['tocou'] < mini:
        maxi = musica['tocou']
        
for musica in musicas:
    if musica['tocou'] == mini:
        print(musica['titulo'])