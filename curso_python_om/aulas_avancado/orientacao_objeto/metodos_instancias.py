# Métodos em instancias de classes python
# Hard coded - algo que foi escrito diretamente no código
class Carro:
    def __init__(self, nome, ):
        self.nome = nome
        
        
    def acelerar(self):
        print(f'{self.nome} está acelerando...')
        
fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()   
