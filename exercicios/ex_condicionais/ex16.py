meses = ['Janeiro',
         'Fevereiro',
         'Março',
         'Abril',
         'Maio',
         'Junho',
         'Julho',
         'Agosto',
         'Setembro',
         'Outubro',
         'Novembro',
         'Dezembro']

mes = int(input("Digite um número: "))
if 1 < mes > 12:
    print("Número inválido!!")
elif mes == 0:
    print("Número inválido")
else:
    print(f"O mês equivalente ao número escolhido é: {meses[mes - 1]}.")
