"""
Tipo float

Tipos -> real, decimal

OBS: 0 Separados de casas decimais na programação é com ponto e não com vírgula
"""

# Errado do ponto de vista float, mas correto no ponto de vista tuple
valor = 1, 44
print(valor)

# Correto
valor = 1.44
print(valor)
print(type(valor))

# Dupla atribuição
valor1, valor2 = 1, 3.44
print(valor1)
print(valor2)
print(type(valor1))
print(type(valor2))

# Podemos converter um float para um int
"""
Convertendo float para inteiro se perde precisão nos dados
"""
res = int(valor)
print(res)
print(type(res))