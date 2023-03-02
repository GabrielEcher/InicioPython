"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

idades = []
alturas = []

for i in range(1, 6):
    i = 0
    print(str(i+1) + 'ª ' + 'Pessoa')
    idade = int(input('Digite a sua idade: '))
    altura = float(input('Digite sua altura: '))
    idades.append(idade)
    alturas.append(altura)
    
    
print('ORDEM INVERSA ALTURAS')
print(alturas[::-1])
print('ORDEM INVERSA DAS IDADES')
print(idades[::-1])
