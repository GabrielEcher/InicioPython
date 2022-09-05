"""
Programa que recebe três valores (obs: maiores que zero)
representando as medidas dos tres lados de um triangulo
Função:
- Determinar se os lados formam um triangulo sabendo que:
o comprimento de cada lado de um triangulo é menor que a soma dos outros
dois lados
- Determinar e mostrar o tipo de triangulo sendo que:
*Chama-se equilatero o triangulo que tem três lados iguais
*Denominam-se isóceles o triangulo que tem o comprimento de dois 
lados iguais
*Recebe o nome de escaleno o triangulo que tem os tres lados diferentes
"""

print("\nDigite as medidas dos lados do triângulo, para descobrir o seu tipo\n")


def verif_tipo_triangulo(lado_a, lado_b, lado_c):  
    
    if lado_a > lado_b + lado_c or lado_b > lado_a + lado_c or lado_c > lado_b + lado_a:
        return quit('As medidas passadas não formam um triângulo')
    
    elif lado_a == lado_b == lado_c:
        return 'Temos um triângulo equilátero!'
    
    elif (lado_a == lado_b) or (lado_a == lado_c) or (lado_c == lado_b):
        return 'Temos um triângulo isóceles!'
    
    else:
        return 'Temos um triângulo escaleno'

while True:
    lado_a = int(input("Valor do lado A: "))
    lado_b = int(input("Valor do lado B: "))
    lado_c = int(input("Valor do lado C: "))
    
    if lado_a > 0 and lado_b > 0 and lado_c > 0:
        break
    else:
        print("Digite valores maiores que 0")

print(verif_tipo_triangulo(lado_a, lado_b, lado_c))