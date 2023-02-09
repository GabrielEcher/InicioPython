"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""


def calculo_media():
    nota1 = float(input('Qual foi a sua primeira nota? '))
    nota2 = float(input('Qual foi a sua segunda nota? '))
    
    media = (nota1 + nota2) / 2
    print(f'A sua média foi de: {media}')
    
    if media >= 7:
        print("APROVADO")
    elif media < 7:
        print("REPROVADO")
    elif media == 10:
        print("APROVADO COM DISTINÇÃO")
        


calculo_media()  
