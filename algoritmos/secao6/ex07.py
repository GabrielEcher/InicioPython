print("Abaixo digite 4 números e elevarei os quatro ao quadrado!")

n1 = int(input("Número: "))
n2 = int(input("Número: "))
n3 = int(input("Número: "))
n4 = int(input("Número: "))

q1 = n1 ** 2
q2 = n2 ** 2
q3 = n3 ** 2
q4 = n4 ** 2

if q3 >= 1000:
    print(q3)
else:
    print(q1)
    print(q2)
    print(q3)
    print(q4)
