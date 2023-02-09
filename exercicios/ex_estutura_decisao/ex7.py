"""
Faça um Programa que leia três números e mostre o maior  e o menor deles.
"""

num1 = float(input('DIGITE UM NÚMERO: '))
num2 = float(input('DIGITE UM NÚMERO: '))
num3 = float(input('DIGITE UM NÚMERO: '))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f'O maior número dos 3 digitados é: {maior:.0f}')
print(f'O menor número dos 3 digitados é: {menor:.0f}')