"""
Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
"""

def calculo_peso(altura):
    peso_ideal = (72.7 * altura) - 58
    print(f'Observando sua altura o peso ideal para você deve ser de: {peso_ideal:.2f} kg')
    
altura = float(input('Digite aqui sua altura para ter uma base do seu peso ideal: '))

calculo_peso(altura)