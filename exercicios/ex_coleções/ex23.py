"""
Ler 2 conjuntos com 5 elementos
"""

conj_a = []
conj_b = []
produto = []

for i in range(5):
    conj_a.append(int(input(f"Digite os valores para o  1º conjunto na posição {i}:")))
    conj_b.append(int(input(f"Digite os valores para o  2º conjunto na posição {i}:")))
    
for j in range(len(conj_a)):
    produto.append(conj_a[j] * conj_b[j])
    
print(f"\n\nO primeiro conjunto é composto pelos números: {str(conj_a).strip('[]')}.\nO segundo conjunto"
      f"é composto pelos números: {str(conj_b).strip('[]')}.\nO produto escalar desses números é da seguinte "
      f"forma: {str(produto).strip('[]')}")
    