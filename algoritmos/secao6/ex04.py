altura = float(input("Digite sua altura: "))
sexo = input("Informe o sexo m/f: ")

if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    print("Sexo não reconhecido")

print(f"Seu peso ideal é: {peso_ideal} ")  ##posso usar o {0:.2f}.format(peso_ideal) ele vai deixar apenas 2 zeros dps .
