"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""

print("CALCULO DO SALARIO, CONSIDERANDO VALOR POR HORA E HORAS TRABALHADAS")

def salario(valor_hora, horas):
    salario_mes = valor_hora * horas
    return f'O seu salário no fim do mês será: {salario_mes}'

valor_hora = float(input("Quantos R$ você ganha por hora? "))
horas = float(input("Quantas horas você trabalha em um mês? "))

print(salario(valor_hora, horas))
