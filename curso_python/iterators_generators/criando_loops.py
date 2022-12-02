"""
Criando a minha própria versão de loop


"""
lista = ['a', 'b', 'c', 'd', 'e']

def my_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
    

my_for(lista)