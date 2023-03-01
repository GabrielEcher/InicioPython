"""
Set comprehension
# Exemplos
numeros = {num for num in range(1, 5)}
print(numeros)
"""


# Outro exemplo

numeros = {x ** 2 for x in range(10)}
print(numeros)

# DESAFIO: Faça uma alteração na estrutura acima, para gerar um dicionário

numeros = {x: x ** 2 for x in range(10)}
print(numeros)


letras = {letra for letra in 'Geek University'}
print(letras)
