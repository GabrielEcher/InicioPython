"""
Ler 2 vetores x e y com 5 valores(usuario não coloca elementos repetidos)
Calcular o seguinte:
- Soma entre x e y: Soma de cada elemento de x com o elemento na mesma posição
- Produto de x e y: multiplicação de cada elemento em x com o elemento em y na mesmo pos
- Diferença entre x e y: todos os elementos de x que não existem em y
- Intersecção entre x e y: apenas elementos que aparecem nos dois vetores
- União entre x e y: todos os elementos de x e y que não estão em x
"""

x = []
y = []
soma = []
produto = []
count_x = 1
count_y = 1

for n in range(1, 6):
    ent_x = int(input(f"Digite os valores para a primeira lista {count_x}/5:\n"))
    x.append(ent_x)
    count_x += 1
    
for n in range(1, 6):
    ent_y = int(input(f"Digite os valores para a segunda lista {count_y}/5:\n"))
    y.append(ent_y)
    count_y += 1
    
for indice in range(5):
   soma.append(x[indice] + y[indice]) 
   produto.append(x[indice] * y[indice])

x1 = set(x)
y1 = set(y)

dif_x = x1.difference(y1) #Todos elementos de x que não existam em y
dif_y = y1.difference(x1) #Todos elementos de y que não existam em x
interseccao = x1.intersection(y1) #Apenas elementos que aprecem nos dois 
uniao = x1.union(y1) #Todos os elementos de x e y sem repetições  

print(f"A soma de cada elemento da lista é:\n{soma}\n")
print(f"A multiplicação dos indices duas listas é:\n{produto}\n")
print(f"A diferença de x para y é:\n{dif_x}\n")
print(f"A diferença de y para x é:\n{dif_y}\n")
print(f"A interesecção das duas listas é:\n{interseccao}\n")
print(f"A união das duas listas é:\n{uniao}\n")