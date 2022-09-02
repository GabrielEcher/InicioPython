"""
Faça um programa que receba 10 valores do usuário de um vetor e imprima quais elementos são os maiores e os menores
"""

lista = []
count = 1
for n in range(10):
    entrada = int(input(f"Digite os números - {count}/10\n"))
    lista.append(entrada)
    count += 1
print(f"Essa é a lista:{lista}")

print("O maior número da lista é:")
print(max(lista))

print("O menor número da lista é:")
print(min(lista))

