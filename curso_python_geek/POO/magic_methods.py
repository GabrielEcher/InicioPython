"""
POO - Métodos Mágicos

Métodos Mágicos são todos os métodos que utilizam dunder.

dunder repr -> representação do objeto

def __repr__(self):
        return f'{self.titulo}, escrito por {self.autor}, com {self.paginas} páginas'

def __str__(self):
    return self.titulo

def __del__(self):
        print('Objeto do tipo livro foi deletado da memória')
"""

class Livro:
    
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        return self.titulo
    
    def __repr__(self):
        return f'{self.titulo}, escrito por {self.autor}, com {self.paginas} páginas'
    
    def __len__(self):
        return self.paginas
    
    def __add__(self, outro):
        return f'{self} e {outro}'
    
    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'
    
    
livro1 = Livro('Meditações', 'Marco Aurélio', 150)
livro2 = Livro('O chamado de Ctulhu', 'H.P Lovecraft', 2000)


print(livro1)
print(livro2)

print(len(livro1))

print(livro1 + livro2)

print(livro1 * 5)