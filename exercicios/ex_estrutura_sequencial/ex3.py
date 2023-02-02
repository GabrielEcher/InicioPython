"""
Faça um Programa que peça dois números e imprima a soma.
"""
print('O programa irá realizar a soma dos dois numeros que voce informar')

def soma(num1, num2):
    soma = num1 + num2
    return f'A soma dos dois numeros foi: {soma}'

num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))

print(soma(num1, num2))