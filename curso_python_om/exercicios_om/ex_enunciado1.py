"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    
    if numero_int % 2 == 0:
        print(f'O {numero_int} é par')
    else:
        print(f'O {numero_int} é impar')

else:
    print('Você não digitou um número inteiro')