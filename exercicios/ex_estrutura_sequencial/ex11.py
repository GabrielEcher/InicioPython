"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 A - o produto do dobro do primeiro com metade do segundo .
 B - a soma do triplo do primeiro com o terceiro.
 C - o terceiro elevado ao cubo.
"""

def A(num1, num2):
    produto = (num1 * 2) + (num2 / 2)
    print(f'O Produto do dobro do primeiro número com metade do segundo é: {produto}')
    
def B(num1, num3):
    soma = (num1 * 3) + num3
    print(f'A soma do triplo do primeiro número com o terceiro número é: {soma}')
    
def C(num3):
    cubo = num3 ** 3
    print(f'O cubo do terceiro número é: {cubo}')
    
num1 = int(input("==PRIMEIRO NÚMERO== | Digite um número inteiro:"))
num2 = int(input("==SEGUNDO NÚMERO== | Digite outro número inteiro:"))
num3 = float(input("==TERCEIRO NÚMERO== | Digite um número real: "))

A(num1, num2)
B(num1, num3)
C(num3)
