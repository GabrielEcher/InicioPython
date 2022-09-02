num = int(input("Digite um número: "))
num1 = str(num)

if num > 0:
    soma = int(num1[0]) + int(num1[1]) + int(num1[2])
    print(f"A soma dos digitos do número é:{soma}")
else:
    print("Número inválido!")

