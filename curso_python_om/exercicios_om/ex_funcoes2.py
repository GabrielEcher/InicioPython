# Exercicios
# Crie funcoes que duplicam, triplicam e quadriplicam
# o numero recebido como parâmetro


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(24))
print(triplicar(24))
print(quadruplicar(24))

