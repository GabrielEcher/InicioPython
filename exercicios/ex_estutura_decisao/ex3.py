"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

gen = input("Digite M para Masculino, ou F para Feminino: ")

if gen == 'M' or gen == 'm':
    print("MASCULINO")

elif gen == 'F' or gen == 'f':
    print("FEMININO")

else:
    print("Sexo Inválido")