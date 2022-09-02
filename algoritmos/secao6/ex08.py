n1 = int(input("Digite um número: "))

if n1 % 2 == 0:
    if n1 > 0:
        print(f"O {n1} é par e positivo")
    else:
        print(f"O {n1} é par e negativo")
else:
    if n1 > 0:
        print(f"O {n1} é ímpar e positivo")
    else:
        print(f"O {n1} é ímpar e negativo")


