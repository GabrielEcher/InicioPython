num1 = int(input(f"Digite um número: "))
num2 = int(input(f"Digite outro número: "))

if num1 > num2:
    print(f"{num1} é maior que o {num2}!")
elif num2 > num1:
    print(f"{num2} é maior que {num1}!")
else:
    print("Os dois números têm o mesmo valor")
