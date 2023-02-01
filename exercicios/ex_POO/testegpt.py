class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for i, produto in enumerate(self.produtos, start=1):
            print(f"{i}. {produto.nome}: R$ {produto.preco}")

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

carrinho = CarrinhoDeCompras()

produto1 = Produto("Café", 2500.0)
produto2 = Produto("Mouse", 100.0)
produto3 = Produto("Teclado", 150.0)

carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)
carrinho.adicionar_produto(produto3)

print("Produtos no carrinho:")
carrinho.listar_produtos()

total = carrinho.calcular_total()
print(f"\nTotal: R$ {total}")