"""
Função para verificar se um número é um quadrado perfeito
"""
import math

num = int(input("Digite um número: "))
 
def quadrado_perfeito():
    raiz = math.sqrt(num) 
    if raiz ** 2 == num:
        print(f"O {num} é um quadrado perfeito")
    else:
        print(f"O {num} não é um quadrado perfeito")
    
quadrado_perfeito()