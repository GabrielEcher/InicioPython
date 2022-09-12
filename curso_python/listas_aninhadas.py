"""
Exemplos:

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3

# Como acessar os dados:

print(listas[0][1])
print(listas[2][1])

# Iterando com loops nas matrizes
for lista in listas:
    for num in lista:
        print(num)

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3
print(listas)
      
# Utilizando Comprehension
[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos:

#Gerando uma matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])
"""



# Formando uma matriz no formato de matriz

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



for lista in matriz:

    print(" ") # Separa cada sublista dentro da matriz para a linha debaixo

    for num in lista:

        print(num, end="  ") # Adiciona espaço entre cada valor printado