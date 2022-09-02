sex = int((input("Qual o seu sexo?\n Digite 1 para Masculino \n Digite 2 para feminino \n")))
h = float(input("Qual a sua altura? "))

if sex == 1:
    pi = (72.7 * h) - 58
    print(f"Seu peso ideal é {pi}kg")
elif sex == 2:
    pi = (62.1 * h) - 44.7
    print(f"Seu peso ideal é {pi}kg")
else:
    print("Dados inválidos para o calculo de peso")
