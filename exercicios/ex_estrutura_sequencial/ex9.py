"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)
"""

print("CONVERSOR DE FAHRENHEIT PARA GRAUS CELSIUS...")

def conversor(f):
    c = 5* ((f - 32) / 9)
    return f'Os graus {f} F° em Celsius são: {c:.2f} C°'

f = float(input('Digite os graus em Fahrenheit: '))

print(conversor(f))