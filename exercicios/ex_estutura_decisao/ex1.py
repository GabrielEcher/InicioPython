"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))

maior = max(num1, num2)

print(f'O maior número entre {num1} e {num2} é: {maior}')
