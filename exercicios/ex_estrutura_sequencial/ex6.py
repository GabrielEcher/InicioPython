"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área
"""
import math

print("CALCULO DE AREA DE UM CIRCULO...")


def circ_area(raio):
    area = math.pi * (raio ** 2)
    return f'A área do circulo é: {area:.2f}'

raio = float(input('Informe o raio do circulo, e te informaremos a area do mesmo: '))

print(circ_area(raio))

