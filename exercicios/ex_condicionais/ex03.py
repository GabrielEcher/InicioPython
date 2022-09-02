import math

num = int(input("Digite um número: "))

if num > 0:
    rqd = math.sqrt(num)
    print(f"A raíz quadrada de {num} é {rqd}")
else:
    qdr = num ** 2
    print(f"O quadrado de {num} é {qdr}")
