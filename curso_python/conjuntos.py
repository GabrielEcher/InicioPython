"""
Conjuntos

- Referência à Teoria de Conjuntos da matemática

- Em Python são chamados de Sets

Sets - conjuntos não possuem valores duplicados;
Sets - conjuntos não possuem valores ordenados;
Sets - elementos não são acesssados via index;

Conjuntos são bons para quando precisamos armazenar elementos, mas não nos
importamos com a ordenação deles. Quando não precisamos se preocupar com chaves,
valores e itens duplicados.

Conjuntos são referenciados com {}

Diferença entre Sets e Dicts
 - Um dict tem chave/valor
 - Um Sets tem apenas valor

 #DEFININDO UM CONJUNTO:

# Forma 1 - Não convencional

s = set({1, 2, 3, 4, 5, 6, 7, 8, 9})

#Ao criar um conjunto, caso seja adicionado um valor já existente
#o mesmo será ignorado sem gerar erro e não fará parte do conjunto

# Forma 2
s1 = ({1, 2, 3, 4, 5, 6, 7, 8, 9})
print(type(s))

if 3 in s1:
    print('Tem o 3')
else:
    print("Não tem o 3")

#IMPORTANTE LEMBRAR: ALÉM DE NÃO TERMOS VALORES DUPLICADOS, NÃO TEMOS ORDEM

dados = "99, 2, 22, 23, 15, 1, 55, 55"

#Listas aceitam valores duplicados então temos 8 elementos
lista = [99, 2, 22, 23, 15, 1, 55, 55]
print(f'Lista: {lista} com {len(lista)} elementos')

#Tuples aceitam valores duplicados então temos 8 elementos
tuplee = 99, 2, 22, 23, 15, 1, 55, 55
print(f'Tuple: {tuplee} com {len(tuplee)} elementos')

#Dicionários não aceitam valores duplicados então temos 7 elementos
dicionario = {}.fromkeys([99, 2, 22, 23, 15, 1, 55, 55], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

#Conjuntos não aceitam valores duplicados então temos 7 elementos
conjunto = {99, 2, 22, 23, 15, 1, 55, 55}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

#ASSIM COM TODO OUTRO CONJUNTO EM PYTHON PODEMOS COLOCAR TIPOS DE DADOS MISTURADOS EM SETS

s = {1, 'b', True, 34,22, 44}

print(s)
print(type(s))

#Podemos iterar em um set normalmente
for valor in s:
    print(valor)


#USOS INTERESSANTES COM SETS

#Imagine que faremos um formulário de cadastro de visitantes em uma feira ou um museu
#e os visitantes informam manualmente de onde vieram

#Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos
#adicionar novos elementos e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

#Agora preicsamos saber quantas cidades distintas, ou seja, unicas temos

print(len(set(cidades)))

#ADICIONANDO ELEMENTOS EM UM CONJUNTO
s = {1, 2, 3}
s.add(4)
s.add(4)  # Duplicidade é ignorada nos conjuntos, não gera erro
print(s)

#REMOVENDO ELEMENTOS DE UM CONJUNTO
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3)  #Não é indice, é o valor a ser removido
print(s)

# Forma 2

s. discard(2)  #Com o discard nenhum KeyError é gerado caso o valor não seja encontrado
print(s)

#COPIANDO UM CONJUNTO PARA OUTRO

# Forma 1 - Deep Copy

novo = s.copy()

print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy
novo = s

novo.add(4)
print(novo)
print(s)


#PODEMOS REMOVER TODOS OS ITENS DE UM CONJUNTO

s.clear()
print(s)

#METODOS MATEMÁTICOS DE CONJUNTO

# temos 2 conjuntos um de estudantes de python e outro de estudantes de java

estudantes_python = {'Marcos', 'Gabriel', 'Luis', 'Joao', 'Miguel'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Joao'}

#alguns estudantes estão nos dois conjuntos

#PRECISAMOS GERAR UM CONJUNTO COM NOMES DE ESTUDANTES UNICOS
# Forma 1 - Utilizando o Union (RECOMENDADO)

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o pipe |

unicos2 = estudantes_python | estudantes_java
print(unicos2)

#GERAR UM CONJUNTO DE ESTUDANTES QUE ESTÃO EM AMBOS OS CURSOS

# Forma 1 - Utilizando intersection
ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

#GERAR UM CONJUNTO DE UM CURSO QUE NÃO ESTÃO NO OUTRO

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

#SOMA*, VALOR MÁX*, VALOR MÍN*, TAMANHO

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
"""










