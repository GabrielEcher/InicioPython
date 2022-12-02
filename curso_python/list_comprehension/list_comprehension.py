"""
List comprehension
- Podemos gerar nosvas listas com dados processados a partir de outro 
iterável.
# Sintaxe da List Comprehension
[dado - for dado in iterável]
# Exemplos
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)
Para entender melhor o que está acontecendo devemos dividir a expressão
em duas partes
- A primeira parte: for numero in numeros
- A segunda parte: numero * 10
res = [numero / 2 for numero in numeros]
print(res)
def funao(valor):
    return valor * valor
res = [funao(numero) for numero in numeros]
print(res)
# List comprehension em loops
# Loop comum
numeros = [1, 2, 3, 4, 5]
 
#print(numeros_dobrados)
# Loop list comprehension
print([numero * 2 for numero in numeros])
"""

# Outros exemplos

# 1

nome = 'Gabriel Echer'

print([letra.upper() for letra in nome])

# 2
 
def caixa_alta(nome):
    nome = nome.title()
    return nome

amigos = ['gabi', 'dudu', 'henrique']

print([caixa_alta(amigo) for amigo in amigos])

# 3

print([numero * 3 for numero in range(1, 10)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
 
print([str(numero) for numero in [1, 2, 3, 4, 5]])