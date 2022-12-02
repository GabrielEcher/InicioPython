"""
Módulo Collection - Named Tuple

#Recap tuple

tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> São tuples diferenciadas onde especificamos um nome para a mesma e também
parâmetros
"""
from collections import namedtuple

#PRECISAMOS DEFINIR O NOME E PARÂMETROS

# Forma 1 - Declaração Named Tuple
cachorro1 = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - ==

cachorro = namedtuple('cachoro', ['idade', 'raça', 'nome'])

ray = cachorro(idade=2, raça='pinscher', nome='ted')

#Acessando os dados

# Forma 1 -
print(ray)
print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2 - (melhor)

print(ray.idade)
print(ray.raça)
print(ray.nome)

print(ray.index('pinscher'))

print(ray.count('pinscher'))