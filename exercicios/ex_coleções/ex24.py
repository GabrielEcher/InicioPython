"""
Programa que lê 10 conjuntos de 2 valores, um valor com o numero do aluno e outro com a idade, encontrar o aluno mais baixo e o mais alto
mostrar o número do aluno mais baixo e do mais alto
"""

aluno = []
altura = []

for n in range(10):
    aluno.append(int(input(f"Digite o número do aluno {n + 1}: ")))
    altura.append(float(input(f"Digite o altura do aluno {n + 1}: ")))

print(f"O num do aluno com maior altura é: {(altura.index(max(altura)))}\nCom {(max(altura))}m")
print(f"O num do aluno com menor altura é: {(altura.index(min(altura)))}\nCom {(min(altura))}m")

