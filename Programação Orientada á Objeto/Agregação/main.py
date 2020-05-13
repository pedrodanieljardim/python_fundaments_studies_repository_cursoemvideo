from classes import CarrinhoDeCompras, Produto


carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
p3 = Produto('Caneca', 15)
p4 = Produto('Livro',89.90)


carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p4)


carrinho.lista_produto()
print("PREÇO FINAL DOS PRODUTOS = R$ {:.2f}".format(carrinho.soma_total()))