print("Vamos começar a sua inscrição para natação:\n")

idade = (int(input("Informe qual a sua idade: ")))

if 5 <= idade <= 7:
    print(f"Com a sua idade ({idade}) você está na categoria INFANTIL A")
elif 8 <= idade <= 10:
    print(f"Com a sua idade ({idade}) você está na categoria INFANTIL B")
elif 11 <= idade <= 13:
    print(f"Com a sua idade ({idade}) você está na categoria JUVENIL A")
elif 14 <= idade <= 17:
    print(f"Com a sua idade ({idade}) você está na categoria JUVENIL B")
elif idade > 18:
    print(f"Com a sua idade ({idade}) você está na categoria SÊNIOR")
else:
    print("Você não tem idade suficiente para entra para a natação")
