"""
Leia 10 números inteiros de uma lista e imprima os números que são primos e suas posições no vetor
"""

primos = []

for n in range(1, 10001):
    cont = 0
    
    for x in range(1,n+1):
        if n % x == 0:
            cont += 1
        
    if cont <= 2:
        primos.append(n)

print(primos)

