"""
Programa que lê 10 numeros DIFERENTES, e se caso o número informado for igual a algum digitado anteriormente
o programa pedirá novamente um número a ser digitado
"""

lista = []
count = 1

while len(lista) < 10:
    num = int(input(f"Digite os valores {count}/10:\n"))
    if num not in lista:
        lista.append(num)
        count += 1
    else:
        print("ERRO: Valor repetido, digite novamente:\n")
    
print(f"Lista formada:\n{lista}")