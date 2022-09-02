print("Responda às seguintes questões para saber se você poderá se aposentar!\n")

idade = (int(input("Digite sua idade: ")))
servico = (int(input("Quantos anos de carteira assinada você tem? ")))

if 60 > idade and servico < 25:
    print("Infelizmente você não pode se aposentar ainda :(")
elif idade >= 60 and servico >= 25:
    print("Você pode se aposentar")
elif idade >= 60 and servico < 25:
    print("Infelizmente você não pode se aposentar ainda :(")
elif idade > 65 and servico > 30:
    print("Você pode se aposentar")