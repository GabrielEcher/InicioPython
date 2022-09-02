"""
Função que recebe a altura e o raio de um cilindro circular
e retorne o volume do cilindro.
Fórmula: V = 3.14 * raio2 * altura
"""

raio = (int(input("Digite o raio do cilindro: ")))
altura = int(input("Digite a altura do cilindro: "))

def volume_cilindro():
    V = 3.14 * raio**2 * altura
    return f'O volume do cilindro é: {V}'

print(volume_cilindro())
