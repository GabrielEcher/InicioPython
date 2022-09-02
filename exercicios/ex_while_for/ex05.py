contagem = 0
soma = 0
qtd = 10

while contagem <= qtd:

    res = int(input(f"Você tem: {contagem}/{qtd}\n Digite 10 números:  "))
    soma = res + soma
    contagem = contagem + 1

print(f"A soma dos números é:{soma}")
