"""
Função que recebe os valores de a e b e calcule o valor da hipotenusa sendo a formula:
H =  raiz quadrada de a² + b² 
"""
import math
a = int(input("Digite o valor do cateto A: "))
b = int(input("Digite o valor do cateto B: "))

def calc_hipotenusa(a, b):
    hipotenusa = math.sqrt(a ** 2 + b ** 2)
    return f'A hipotenusa dos dois catetos é: {hipotenusa}'

print(calc_hipotenusa(a, b))