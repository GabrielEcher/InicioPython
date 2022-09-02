import math


num = int(input("Digite um número e farei o logaritmo do mesmo: "))

if num > 0:
    log = math.log10(num)
    print(f"O logaritmo desse número é {log}")
elif num <= 0:
    print("Número inválido")
else:
    print("Por favor digite um número")
