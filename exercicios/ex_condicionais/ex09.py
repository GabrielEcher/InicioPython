sal = float(input("Qual o seu salário?"))
empr = float(input("Digita o valor da prestação do empréstimo:"))

if empr <= (sal * 0.20):
    print("Empréstimo concedido!")
else:
    print("Empréstimo não concedido!")
