"""
Programa que recebe um vetor e contém funções que façam o seguinte:
- Impressão normal do vetor
- Impressão inversa
- Média aritmetica
"""
import random

vetor = []
tamanho = int(input("Digite quantos números a lista deverá ter: "))

for n in range(tamanho):
    ent_user = int(input("Informe os números: "))
    vetor.append(ent_user)

def impressao_vetor(vetor):
    print(vetor)

def impressao_inversa(vetor):
    vetor.reverse()
    print(vetor)

def media_aritmetica(vetor):
    soma = sum(vetor)
    leng = len(vetor)
    media = soma / leng
    print(media)

print("VETOR FORMADO:")
impressao_vetor(vetor)

print("VETOR NA ORDEM INVERSA:")
impressao_inversa(vetor)

print("MEDIA ARITMETICA DO VETOR:")
media_aritmetica(vetor)  