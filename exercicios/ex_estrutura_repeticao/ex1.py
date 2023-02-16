"""
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
nota = 10
verif = 0

while verif != nota:
    verif = float(input("Adivinhe a nota: "))
else:
    print("Acertou")