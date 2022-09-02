import math

n = int(input(f"Digite um número: "))

if n <= 0:
    print("Número inválido!!")
else:
    rqd = math.sqrt(n)
    print(f"A raíz quadrada de {n} é: {rqd}")
