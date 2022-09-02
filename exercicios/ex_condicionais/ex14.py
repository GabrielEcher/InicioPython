nota1 = float(input("Digite a nota 1 \n"))
nota2 = float(input("Digite a nota 2 \n"))
nota3 = float(input("Digite a nota 3 \n"))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10
if media < 3:
    print(f"Média: {media}. Você foi reprovado!")
elif 3 < media < 5:
    print(f"Média: {media}. Você terá de fazer recuperação!")
else:
    print(f"Média: {media}. Parabéns você foi aprovado")
