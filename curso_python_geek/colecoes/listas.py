"""

listas em python funcionam como vetores ou matrizes ou seja arrays, com a diferença de serem dinâmicos e também
de podermos colocar QUALQUER tipo de dado

- Dinâmico: Não possui tamanho fixo, podemos criar a lista e ir adicionando elementos
- Qualquer tipo de dado: As listas não possuem tipo de dado fixo, ou seja podemos colocar qualquer tipo de dado
- As listas em python são representadas por []

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'a', 'b', 'r', 'i', 'e', 'l']

lista3 = []

lista4 = list(range(11))

lista5 = list("Gabriel Echer")

lista1.append(42)
print(lista1)

lista1.append([8, 3, 1])  #COLOCA A LISTA COMO ELEMENTO ÚNICO (SUBLISTA)
print(lista1)

lista1.extend((12, 154, 122))  #COLOCA CADA ELEMENTO COMO VALOR ADICIONAL NALISTA
print(lista1)

#Podemos checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f"Encontrei o número {num}")
else:
    print(f"Não encontrei o número {num}")

#ORDENAÇÃO
lista1.sort()
print(lista1)

#OCORRENCIA DE VALOR
print(lista1.count(1))
print(lista5.count('e')

#PODEMOS INSERIR UM NOVO ELEMENTO NA LISTA INFORMANDO A POSIÇÃO DO INDICE
#NÃO SUBSITUI O VALOR, TROCADO, APENAS O COLOCA PARA A DIREITA
lista1.insert(2, 'Novo valor')
print(lista1)

#PODEMOS JUNTAR DUAS LISTAS (pode usar o extend, se não quiser criar outra lista)
lista6 = lista1 + lista2
print(lista6)

#PODEMOS FACILMENTE INVERTER UMA LISTA (REVERSE)
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

#OU

print(lista1[::-1])
print(lista2[::-1])

#PODEMOS COPIAR UMA LISTA

lista6 = lista2.copy()
print(lista6)

#PODEMOS CONTAR QUANTOS ELEMENTOS EXISTEM NA LISTA
print(len(lista5))

#PODEMOS REMOVER FACILMENTE O ULTIMO ELEMENTO DE UMA LISTA
#OBS: o pop não somente remove o ultimo elemento mas também o retorna

print(lista5)
lista5.pop()
print(lista5)

#podemos remover um elemento pelo indice
lista5.pop(2)
print(lista5)

#PODEMOS REMOVER TODOS OS ELEMENTOS (ZERAR A LISTA)

print(lista5)
lista5.clear()
print(lista5)

#PODEMOS REPETIR ELEMENTOS EM UMA LISTA

nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

#PODEMOS FACILMENTE CONVERTER UMA STRING PARA UMA LISTA
#OBS: Por padrão o split separa os elementos da lista pelo espaço entre elas
#EX1:
curso = "Programação Python"
print(curso)
curso = curso.split()
print(curso)

#EX2:
curso = "Programação, Python, aaa"
print(curso)
curso = curso.split(',')
print(curso)

#CONVERTENDO LISTA PARA STRING
lista6 = ['Programação', 'em', 'python']
print(lista6)

#abaixo estamos para pegar a lista 6 colocar espaço em cada elemento e transformar em uma string
curso = ' '.join(lista6)
print(curso)

#utilizamos o join para inserir qualquer elemento entre os espaços da string
curso = '_'.join(lista6)
print(curso)

#PODEMOS UTILIZAR QUALQUERR TIPO DE DADO EM UMA LISTA
lista6 = [1, 2.43, True, 'Echer', 'd', [1, 2, 3], 312321423]

#ITERANDO SOBRE LISTAS

#EX1 - UTILIZANDO FOR
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

#EX2 - UTILIZANDO O WHILE

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

#UTILIZANDO VARIAVEIS EM LISTAS

numeros = [1, 2, 3, 4, 5]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeross = [num1, num2, num3, num4, num5]
print(numeross)

#ACESSAR ELEMENTOS DE FORMA INDEXADA

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

#ACESSAR OS ELEMENTOS DE FORMA INDEXADA INVERSA (funciona como um circulo)

print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

#GERAR INDICE EM UM FOR (enumerate)

for indice, cor in enumerate(cores):
    print(indice, cor)

#LISTAS ACEITAM VALORES REPETIDOS
lista = []
lista.append(2111)
lista.append(212)
lista.append(212)
lista.append(212)
lista.append(23)
print(lista)

#METODOS NÃO TÃO IMPORTANTES MAS UTEIS

#ENCONTRAR O INDICE DE UM ELEMENTO NA LISTA

numeros = [5, 6, 7, 8, 7, 10]

print(numeros.index(6))
print(numeros.index(5))
print(numeros.index(5))  #RETORNA O INDICE DO PRIMEIRO VALOR ENCONTRADO


#PODEMOS BUSCAR DENTRO DE UM RANGE, OU SEJA, QUAL INDICE COMEÇAR BUSCAR
print(numeros.index(7, 1))
print(numeros.index(7, 2))
print(numeros.index(7, 3))
print(numeros.index(7, 4))

#BUSCAR O MAIOR ELEMENTO DE UMA LISTA E SEU INDICE
indice = lista.index(max(lista))

#PODEMOS FAZER BUSCA DE UM RANGE, INICIO/FIM

print(numeros.index(8, 0, 4))

# REVISÃO SLICING

# lista[inicio:fim:passo]

# PARAMETRO INICIO
lista = [1, 2, 3, 4]

print(lista[1:])  # INICIA NO INDICE 1 PARA FRENTE

# PARAMETRO FIM

print(lista[:2])  # COMEÇA EM 0, ATÉ O INDICE 2 - 1 (NÃO INCLUSO)
print(lista[:4])  # COMEÇA EM 0, ATÉ O INDICE 4 - 1 (NÃO INCLUSO)
print(lista[1:4])  # COMEÇA EM 1 ATÉ O INDICE 4 - 1

# PARAMETRO PASSO

print(lista[1::2])  # COMEÇA EM 1, VAI ATÉ O FINAL DE 2 EM 2

#SOMA*, VALOR MÁXIMO*, VALOR MINIMO*, TAMANHO
#SE OS VALORES FOREM TODOS INTEIROS OU REAIS

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  #SOMA
print(max(lista))  #MÁXIMO
print(min(lista))  #MINIMO
print(len(lista))  #TAMANHO DA LISTA

#TRANSFORMAR UMA LISTA EM TUPLE

lista = [1, 2, 3, 4, 5, 6]
print(lista)

tupla = tuple(lista)
print(tupla)

#DESEMPACOTAMENTO DE LISTAS

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

#obs: se tivermos mais elementos para desempacotar do que variaveis para receber teremos ValueError

#COPIANDO UMA LISTA PARA OUTRA (Shallow Copy e Deep Copy

#Forma 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(lista)
print(nova)

#Ao utilizarmos lista.copy() os dados de uma lista e da outra se tornam totalmente independentes
#Modificando uma não afeta a outra

#Forma 2 - Shallow Copy
lista = [1, 2, 3]

print(lista)

nova = lista

print(nova)

nova.append(4)
print(lista)
print(nova)

#Utilizamos a cópia via atribuição, e copiamos os dados da lista para a nova, mas modificando uma das listas
#modificação se refletiu em ambas as listas
"""
