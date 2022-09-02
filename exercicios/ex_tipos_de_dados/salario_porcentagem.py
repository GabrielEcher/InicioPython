print("Saiba qual seria seu salário de acordo com a porcentagem de aumento desejada!")

porcentagem = int(input("Digite a porcentagem: "))
salario = float(input("Qual é o seu salário? R$"))

novo = salario + (salario * porcentagem / 100)
print("Seu salário passará a ser:R$", novo)
