"""
Faça um programa que leia um vetor de 5 valores para números reais, e depois, um código inteiro. Se o código for zero o programa finaliza,
se for 1 mostra o vetor na ordem direta, e se for 2 mostra o vetor na ordem inversa, se caso o código for diferente de 1 e 2, escreva uma mensagem que o 
código é inválido
"""


lista = [21, 20.5, 32, 44, 50]
cod = int(input("Digite:\n0 para sair do programa\n1 para visualizar o vetor em ordem direta\n2 para visualizar o vetor em ordem inversa\nCÓDIGO:"))

if cod == 0:
    print("Saindo do programa...")
    quit()

elif cod == 1:
    print("Aqui está a lista na ordem normal")
    print(lista)

elif cod == 2:
    print("Aqui está a lista na ordem inversa")
    lista.reverse()
    print(lista)

else:
    print("ERROR: Código inválido")
    