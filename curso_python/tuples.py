"""
Tuples são parecidas com listas
2 diferenças básicas

1 - São representadas por parênteses ()

2 - São imutáveis, significa que ao criar uma tuple ela não muda. Toda operação em
uma tuple gera uma nova tuple

#CUIDADO: Tupla com 1 elemento não é tupla, apenas 2 ou mais valores
ex: tupla1 = (4)
mas se:
tupla2 = (4,)

#PODEMOS GERAR UMA TUPLE DINAMICAMENTE COM RANGE
tupla = tuple(range(11))
print(tupla)

#DESEMPACOTAMENTO DE TUPLES
tupla = ('Geek University', 'Programação em Py')

escola, curso = tupla

print(escola)
print(curso)

#MÉTODOS PARA ADIÇÃO E REMOÇÃO DE ELEMENTOS NAS TUPLES NÃO EXISTEM (IMUTÁVEIS)

#SOMA*, VALOR MÁX*, VALOR MIN*, E TAMANHO
# * SE OS VALORES FOREM TODOS INTEIROS OU REAIS

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

#CONCATENAÇÃO DE TUPLES

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

#VERIFICAÇÃO SE DETERMINADO ELEMENTO ESTÁ NA TUPLE

tupla = (1, 2, 3)
print(3 in tupla)

#ITERANDO NAS TUPLES
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

#CONTANDO ELEMENTOS DENTRO DE UMA TUPLE

tupla = ('a', 'b', 'c', 'a', 'b')
print(tupla.count('a'))

nome = tuple('Gabriel')
print(nome)
print(nome.count('e'))

#DICAS NA UTILIZAÇÃO DE TUPLES

#DEVEMOS UTILIZAR TUPLES SEMPRE QUE NÃO PRECISAMOS MODIFICAR OS DADOS CONTIDOS EM UMA COLEÇÃO

#EX:
dias_da_semana = ("domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sabado")

#O ACESSO A ELEMENTOS DENTRO DAS TUPLES
print(dias_da_semana[1])

#ITERAR COM WHILE
i = 0
while i < len(dias_da_semana):
    print(dias_da_semana[i])
    i = i + 1

#VERIFICAR EM QUAL INDICE UM ELEMENTO ESTÁ NA TUPLE
print(dias_da_semana.index('terça'))

#SLICING
#TUPLE[inicio:fim:passo]
print(dias_da_semana[0:7:2])

#OBS: PQ UTILIZAR AS TUPLES?
# -  TUPLES SÃO MAIS RÁPIDAS DO QUE LISTAS
# -  TUPLAS DEIXAM SEU CÓDIGO MAIS SEGURO(IMUTÁVEL)

#COPIANDO UMA TUPLE PARA OUTRA
#NA TUPLE NÃO TEMOS SHALLOW COPY
tupla = (1, 2, 3)
print(tupla)

nova = tupla

print(tupla)
print(nova)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
"""

