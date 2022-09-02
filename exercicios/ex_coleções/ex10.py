"""
Crie um programa que lê a nota de 15 alunos, calcule a média geral e imprima-a na tela
"""

notas = []
count = 0

for n in range(15):
    ent_notas = float(input(f"Digite a nota de cada um dos 15 alunos - {count}/15\n"))
    notas.append(ent_notas)
    count += 1

print(f"As notas dos alunos são:\n{notas}")
media = sum(notas) / 15
print(f"A média geral das notas foi:\n{media.__round__(2)}")