num = int(input("Informe um número entre 1 e 10:  "))
while num < 1 or num > 10:
    num = int(input("Informe um número entre 1 e 10:  "))
print(f"Tabuada de {num}")
for n in range(1, 11):
    res = num * n
    print(f"{num} x {n} = {res}")
