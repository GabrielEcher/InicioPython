"""
Ler um conjunto de números reais, armazenando-os em um vetor
e calcular o quadrado dos componentes deste vetor, armazenando o resultado
em outro vetor, os conjuntos devem ter 10 elementos cada. Imprimir todos os conjuntos
"""


vet = []
count = 1

for n in range(0, 10):
    entrada = int(input(f"Digite 10 números - {count}/10: "))
    vet.append(entrada)
    count += 1
print(vet)

n1 = vet[0] ** 2
n2 = vet[1] ** 2
n3 = vet[2] ** 2
n4 = vet[3] ** 2
n5 = vet[4] ** 2
n6 = vet[5] ** 2
n7 = vet[6] ** 2
n8 = vet[7] ** 2
n9 = vet[8] ** 2
n10 = vet[9] ** 2

print("O quadrado de cada valor da lista acima é:")
lista_qd = n1, n2, n3, n4, n5, n6, n7, n8, n9, n10
print(lista_qd)
