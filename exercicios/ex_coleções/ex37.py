"""
Ordenar um vetor A de 11 elementos da seguinte forma
A1 < A2 < ... < A6 > A7 > ... A11


"""

lista = [11, 22, 35, 67, 82, 21, 55, 100, 21, 3, 1]
lista1 = []
lista2 = []

for i in range(11):
    
    if i < 5:
        s = lista[i]
        lista1.append(s)
        lista1.sort()
        
    elif i >= 5:
        s = lista[i]
        lista2.append(s)
        lista2.sort()
        lista2.reverse()
    
lista = lista1 + lista2

print(lista)
print(lista1)
print(lista2)