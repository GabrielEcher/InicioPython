"""
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos 
possuem altura inferior à média de altura desses alunos.
"""

import random

n = 30  # número de elementos na lista
min_altura = 1.35  # menor valor possível na lista
max_altura = 2.00  # maior valor possível na lista
min_idade = 12
max_idade = 18
aluno_13 = []
media_13 = []

lista_alturas = [round(random.uniform(min_altura, max_altura), 2) for _ in range(n)] # uniform cria uma lista de um valor até outro
print(lista_alturas)

lista_idades = [random.randint(min_idade, max_idade) for _ in range(n)] # randint criando uma lista aleatória, do minimo de idade até o maximo de idade
print(lista_idades)

for i in range(30):
    if lista_idades[i] > 13:
        aluno_13.append(lista_alturas[i])

media = sum(aluno_13) / len(aluno_13)

for i in range(len(aluno_13)):
    if aluno_13[i] < media:
        media_13.append(aluno_13[i])
        
print('\nA idade dos alunos são:\n',lista_idades,'\nA altura dos alunos em cm são:\n',lista_alturas)
print('\nForam ',len(aluno_13),' alunos com idade acima de 13 anos que são:\n',aluno_13)
print('\nA média de altura desses ',len(aluno_13),' alunos é:', media,'cm')
print('\nForam ',len(media_13),' alunos com mais de 13 anos possuem altura inferior à média de altura:\n',media_13)