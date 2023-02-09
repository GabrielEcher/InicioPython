"""
Faça um Programa que leia três números e mostre o maior deles.
"""

num1 = float(input('DIGITE UM NÚMERO: '))
num2 = float(input('DIGITE UM NÚMERO: '))
num3 = float(input('DIGITE UM NÚMERO: '))

maior = max(num1, num2, num3)

print(f'O maior número dos 3 digitados é: {maior:.0f}')