"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

nome = str(input("Digite seu nome: "))
while len(nome) < 3:
    print("O nome deve conter 3 ou mais carácteres ")
    nome = str(input("Digite seu nome: "))
else:
    print("SUCESSO, Nome aceito")


idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Idade deve ser maior que 0 ou menor que 150!")
    idade = int(input("Digite sua idade: "))
else:
    print("SUCESSO, Idade válida")


salario = float(input("Digite seu salário: "))
while salario < 0.0:
    print("Salário deve ser maior que 0")
    salario = float(input("Digite seu salário: "))
else:
    print("SUCESSO, Salário válido!")


sexo = str(input("Digite F para feminino ou M para masculino: "))

while sexo != 'F' and sexo != 'M':
    print("Valor inválido, por favor digite novamente")
    sexo = str(input("Digite F para feminino ou M para masculino: "))
else: 
    print("SUCESSO, Valor válido!")



civil = str(input("ESTADO CIVIL === S - Solteiro, C - Casado, V - Viúvo(a), D - Divorciado(a): "))  

while civil != "S" and civil != "C" and civil != "V" and civil != "D":
    print("Valor para estado civil inválido! Por favor digite novamente")
    civil = str(input("ESTADO CIVIL === S - Solteiro, C - Casado, V - Viúvo(a), D - Divorciado(a): "))
else:
    print("SUCESSO, Valor para estado civil válido!")
    