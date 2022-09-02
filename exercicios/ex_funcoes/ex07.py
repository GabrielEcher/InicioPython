"""
Função que receba uma temperatura em graus Celsius e retorne-a convertida em graus 
Fahrenheit. 
fórmula = F = C * (9.0/5.0) + 32.0
"""

from lib2to3.pytree import convert


C = float(input("Digite a temperatura em graus Celsius: "))

def converter_F(C):
    fahrenheit = C * (9.0/5.0) + 32.0
    return f'A temperatura {C} C° convertida para Fahrenheit fica {fahrenheit} F°'


print(converter_F(C))
    