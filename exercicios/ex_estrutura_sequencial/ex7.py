"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

print("PROGRAMA QUE CALCULA A AREA DO DE UM QUADRADO E MOSTRA O DOBRO DA AREA PARA O USUARIO")

def calc(base, altura):
    area = (base * altura) * 2
    return f'O dobro da área desse quadrado é: {area}'

base = float(input('Informe a base do quadrado: '))
altura = float(input('Informe a altura do quadrado: '))

print(calc(base, altura))

