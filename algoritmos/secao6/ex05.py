e = 0
m = 0

peso = float(input("Quantos kg de peixe há: "))

if peso > 50:
    e = peso - 50
    m = e * 4
    print("Você deverá pagar R${0:.2f}".format(m))
else:
    e = 0
    m = 0
    print("Multas: R$:0.00")
    print("Excesso de peso: 0 kg")
