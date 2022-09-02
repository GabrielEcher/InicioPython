
linguagens = (float(input("Qual foi sua nota de linguagens? ")))
exatas = (float(input("Qual foi sua nota de exatas? ")))

if linguagens < 0 or linguagens > 10:
    print("Nota invalida")
    exit(),
elif exatas < 0 or exatas > 10:
    print("Nota invalida")
    exit(),
else:
    media = (linguagens + exatas) / 2
    print(f"A média é {media}")
