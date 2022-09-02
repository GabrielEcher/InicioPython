"""
Faça uma função para verificar se o número é positivo ou negativo
sendo que o valor de retorno será 1 se for positivo, -1 se for negativo, e 0 se for 0
"""

num = int(input("Digite um número: "))

def verif_num():
    if num == 0:
        return 0
    elif num > 0:
        return 1
    else:
        return -1

print(verif_num())