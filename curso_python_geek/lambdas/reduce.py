"""
Reduce

OBS: A partir do Python3 a função reduce() não pe uma função built-in
precisamos importar e utilizar a função a partir do módulo 'functools'
Entendendo o reduce

# Imagine que você tem uma coleção de dados:
dados = [a1, a2, a3.... an]

# E tu tem uma função que recebe dois parâmetros
def funcao(x, y):
    return x * y

Assim como o map() e filter(), ela recebe dois parâmetros, a função e o iterável
reduce(funcao, dados)

A função reduce() funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois parametros elementos da coleção e guarda o resultado
    Passo 2: res2 = f(a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res
    
    Isso é repetido até o final
    Passo 3: res3 = f(res2, a4)
    
    Passo n: resn = f(resm, an)
    
"""

# COMO FUNCIONA NA PRÁTICA

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29] #PRIMEIRO VALOR VEZES O SEGUNDO, O RESULTADO VEZES O PROXIMO VALOR

multi = lambda x, y: x * y

res = reduce(multi, dados) # ARMAZENA OS VALORES
print(res)