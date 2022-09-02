valor_hora = 10.00
valor_hora_excedente = 20.00
e = 0

c = int(input("Informe o código do funcionário: "))
n = float(input("Informe a quantidade de horas trabalhadas: "))

if n > 50:
    e = (n - 50) * valor_hora_excedente
    salario = (50 * valor_hora) + e
    print("Salário Total R$:{0:.2f}".format(salario))
    print("Salário excedente R$:{0:.2f}".format(e))
else:
    salario = (n * valor_hora)
    print("Salário Total R$:{0:.2f}".format(salario))
    print("Salário excedente R$:{0:.2f}".format(e))
