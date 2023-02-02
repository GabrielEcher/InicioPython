"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

def menu_inicial():
    print('CALCULO DE PESO IDEAL CONFORME A ALTURA')
    print('DIGITE 1 PARA SEXO MASCULINO')
    print('DIGITE 2 PARA SEXO FEMININO')
    

def peso_homem():
    altura = float(input('Digite aqui sua altura para ter uma base do seu peso ideal: '))
    peso_ideal = (72.7 * altura) - 58
    print(f'Observando sua altura o peso ideal para você deve ser de: {peso_ideal:.2f} kg')

def peso_mulher():
    altura = float(input('Digite aqui sua altura para ter uma base do seu peso ideal: '))
    peso_ideal = (62.1* altura) - 44.7
    print(f'Observando sua altura o peso ideal para você deve ser de: {peso_ideal:.2f} kg')
    
if __name__ == '__main__':
    menu_inicial()
    sexo = int(input("DIGITE O NÚMERO RESPECTIVO PARA SEU SEXO: "))
    
    if sexo == 1:
        peso_homem()
    
    if sexo == 2:
        peso_mulher()
        
    
    
    
