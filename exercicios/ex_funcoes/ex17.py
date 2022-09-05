"""
Função que receba dois números inteiros positivos como parametro e retorne
a soma dos N números inteiros existentes entre eles.

"""

a = int(input("Digite um valor inteiro e positivo: "))
b = int(input("Digite um valor inteiro e positivo: "))


def soma_numeros(a, b):
    lista = []
    for n in range(a+1, b):
        lista.append(n)
    return f'Os valores que estão entre os dois números são: {lista}' \
           f'\nA soma desses valores é {sum(lista)}'
        

print(soma_numeros(a, b))
    


