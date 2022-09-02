"""
Programa que lê 6 valores pares, armazena-os na lista e printa o inverso da lista
"""

vetor = [0, 0, 0, 0, 0, 0,]
i = 0


while i < len(vetor):
    numero = float(input(f'Digite um numero par ({i + 1}/6): '))
    if numero % 2 == 0:
        vetor[i] = numero
        i += 1

print(vetor[::-1])