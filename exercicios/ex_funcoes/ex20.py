"""
Faça um algoritmo que receba um número inteiro positivo n e calcule seu fatorial n!
"""

numero = int(input("Fatorial de: ") )


def fatorial(numero):
    resultado = 1
    for n in range(1,numero+1):
     resultado *= n
    return resultado

print(fatorial(numero))