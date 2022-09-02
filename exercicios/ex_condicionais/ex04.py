import math

num = int(input("Digite um número e calcularei sua raíz e o quadrado dele: "))

if num <= 0:
    print("Aceito apenas números negativos para fazer as resoluções!!")
else:
    rqd = math.sqrt(num)
    qdr = num ** 2
    print(f"A raíz quadrada de {num} é {rqd}\nE o {num} elevado ao quadrado é {qdr}")
