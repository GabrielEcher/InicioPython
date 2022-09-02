"""
Função que receba dois números e retorne qual deles é o maior
"""

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

def verif_maior():
    if num1 > num2:
        return f'{num1} é maior que {num2}'
    else:
        return f'{num2} é maior que {num1}'
    
print(verif_maior())