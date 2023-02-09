"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

print("Em qual turno você estuda")
verif_turno = str(input("MATUTINO, DIGITE M\nVESPERTINO, DIGITE V\nNOTURNO, DIGITE N\n"))

if verif_turno == "M" or verif_turno == "m":
    print("Bom dia!")

elif verif_turno == "V" or verif_turno == "v":
    print("Boa tarde!")

elif verif_turno == "N" or verif_turno == "n":
    print("Boa noite!")
    
else:
    print("Valor inválido")
