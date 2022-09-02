"""dia = int(input("Digite um número de 1 a 7: "))
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sabádo")
else:
    print("ERRO: Digite um número válido")
"""

#É possível usar a seguinte lógica também
diasemana = ['domingo',
             'segunda',
             'terça',
             'quarta',
             'quinta',
             'sexta',
             'sábado']

dia = int(input('Digite o dia da semana \n'))

if 1 < dia > 7:
    print('Esse dia não existe')
else:
    print(f'O dia selecionado é: {diasemana[dia - 1]}.')

