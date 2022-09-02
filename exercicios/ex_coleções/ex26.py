"""
Calcular o desvio padrão de uma lista

"""

import math
 
a=[23,12,45,32,31,14,15,33,44,8]
soma =0
media = sum(a)/10
for i in range(10):
    soma = soma + (a[i]-media)**2
    
dp =  math.sqrt(soma/9)
print(a)
print(f' media dos valores = {media}, o desvio padrão = {dp}')