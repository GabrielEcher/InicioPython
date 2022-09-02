"""
Função que recebe três notas de um aluno como params e uma letra
se a letra for A, a função deverá calcular a média aritmetica das notas
e se for P calcular a média ponderada com pesos 5, 3 e 2

"""



letra_calc = str(input("Digite:\n(A) para calcular a média aritmética\n(P) para calcular a média ponderada com peso 5, 3 e 2\n"))

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

peso1 = 5
peso2 = 3
peso3 = 2

def calculo_notas(nota1, nota2, nota3):
    if letra_calc == 'a' or letra_calc == 'A':
        media_arit = (nota1 + nota2 + nota3) / 3
        return f'A média aritmética das notas é: {media_arit:.2f}'
    elif letra_calc == 'p' or letra_calc == 'P':
        media_pond = (nota1*peso1 + nota2*peso2) / (peso1+peso2)
        return f'A média ponderada das notas é: {media_pond:.2f}'
    
print(calculo_notas(nota1, nota2, nota3))