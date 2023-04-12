valor1 = input('Digite um valor:')
valor2 = input('Digite outro valor:')

valor1_int = int(valor1)
valor2_int = int(valor2)

if valor1_int > valor2_int:
    print(f'{valor1_int} é maior que {valor2_int}')
    
elif valor1_int < valor2_int:
    print(f'{valor2_int} é maior que {valor1_int}')

else:
    print('Os dois valores são iguais')

