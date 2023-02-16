"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
"""

nota1 = float(input("Informe a primeira nota do semestre: "))
nota2 = float(input("Informe a segunda nota do semestre: "))

def calculo_conceito(nota1, nota2):
    media = (nota1 + nota2) / 2
    
    if media >= 9:
        print(f'Média de aproveitamento: {media}')
        print('Conceito final: A')

    elif media >= 7.5:
        print(f'Média de aproveitamento: {media}')
        print('Conceito final: B')
    
    elif media >= 6:
        print(f'Média de aproveitamento: {media}')
        print('Conceito final: C')
    
    elif media >= 4:
        print(f'Média de aproveitamento: {media}')
        print('Conceito final: D')
    
    elif media >= 0:
        print(f'Média de aproveitamento: {media}')
        print('Conceito final: E')
        
calculo_conceito(nota1, nota2)