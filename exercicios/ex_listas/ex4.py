"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

lista_char = []
consoantes = 0

print("Informe os carácteres: ")

for i in range(10):
    lista_char.append(input('Carácter ' + str(i+1) + ': '))
    char = lista_char[i]
    
    if(char not in ('a', 'e', 'i', 'o', 'u')):
        consoantes += 1

print(f'Lista dos carácteres: {lista_char}')    
print(f'Consoantes digitadas: {consoantes}')
