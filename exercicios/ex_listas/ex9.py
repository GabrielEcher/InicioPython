"""
Faça um Programa que leia um vetor A com 10 números inteiros, 
calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

lista = []
lista_quadrado = []


while len(lista) < 10:
    entrada = input("Digite um número inteiro, ou qualquer outro digito para sair: ")
    if entrada.isdigit():
        lista.append(int(entrada))
    else:
        break

print(lista)

for i in lista:
    lista_quadrado.append(i**2)
    
print(lista_quadrado)