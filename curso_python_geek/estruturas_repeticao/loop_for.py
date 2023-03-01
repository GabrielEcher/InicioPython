"""
Loop for

Loop -> estrutura de repetição
For -> Uma dessas estruturas

python -
for item in interavel
//execução do loop//

Utilizamos loops para iterar sobre sequências ou sobre valores iteraveis. EX:

Strings
nome = 'Gabriel'

Lista
lista = [1, 2, 3, 4, 5,]

Range
numeros = range(1, 10)

# Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

OBS: Quando não precisamos de um valor, podemos descarta-lo usando um underline

for valor in enumerate(nome):
    print(valor)

qtd = int(input("Quantas vezes esse loop dever rodar? "))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f"Informe o {n}/{qtd} valor: "))
    soma = soma + num
print(f"A soma é {soma}")

nome = "Gabriel Echer"

for letra in nome:
    print(letra, end="")

Tabela emojis unicode:
Original U+2705
Modificado: U0002705

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F63B' * num)
"""

