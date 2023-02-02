"""
Faça um Programa que converta metros para centímetros.
"""

print("CONVERSOR DE METROS PARA CENTÍMETROS...")

def conversor(metros):
    cm = metros * 100
    return f'O valor de {metros} em cm é: {cm}'

metros = int(input('Informe o valor em metros: '))

print(conversor(metros))
