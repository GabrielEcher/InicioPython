num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num1 == num2:
    print("Os dois números têm o mesmo valor!")
else:
    print(f"{num2} é maior que {num1}")
