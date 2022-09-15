"""
Map

- Fazemos o mapeamento de valores para função

import math

def area(r):
    #Calcula a area de um cirulo com raio 'r' 
    return math.pi * (r ** 2)

#print(area(3.5))

raios = [2, 5, 7, 1, 0.3, 10, 40]

areas = []
for r in raios:
    areas.append(((area)(r)))
    
#print(areas)

# Map é uma função que recebe 2 parametros, o 1° é a função e o 2° um iterável

areas = map(area, raios) # Mapeia uma função para um iterável
print(list(areas))

# Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: APÓS UTILIZAR A FUNÇÃO map(), DEPOIS DA PRIMEIRA UTILIZAÇÃO DO RESULTADO
# ELE ZERA;

# FIXAÇÃO - Map

# Temos dados iteráveis:

# dados: a1, a2, .... an

# Temos uma função:
# f(x)

# Utilizamos a função map(f, dados) onde map irá mapear cada elemento e 
# aplicar a fumção
"""

# Exemplos

cidades = [('Anta Gorda', 27), ('Encantado', 45), ('Muçum', 25), ('NY', 5) ]

print(cidades)

# Lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades))) # (FUNÇÃO, ITERÁVEL)