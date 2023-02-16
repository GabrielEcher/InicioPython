"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


"""

numero = int(input("Digite um número de 1 a 7: "))

if numero == 1:
    print("1 - DOMINGO")
elif numero == 2:
    print("2 - SEGUNDA")
elif numero == 3:
    print("3 - TERÇA")
elif numero == 4:
    print("4 - QUARTA")
elif numero == 5:
    print("5 - QUINTA")
elif numero == 6:
    print("6 - SEXTA")
elif numero == 7:
    print("7 - SABADO")
else:
    print("NUMERO INVÁLIDO")