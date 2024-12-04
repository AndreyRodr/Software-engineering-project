from bancoDeDados import BancoDeDados
from venda import Venda
class Carrinho:
    def __init__(self, bancoDeDados):
        self.bancoDeDados = bancoDeDados

    def RealizarVenda(self):
        id_produto = input("ID do Produto: ")
        cliente = input("Nome do Cliente: ")
        credencial = input("Credencial do Cliente: ")
        quantidade = int(input("Quantidade: "))
        
        if not self.bancoDeDados.verificaID(id_produto):
            print("Produto não encontrado. Venda não realizada.")
            return
        
        if not self.bancoDeDados.verificaCredencial(credencial):
            print("Credencial inválida. Venda não realizada.")
            return
        
        preco = None
        for produto in self.bancoDeDados.produtos:
            if produto.IDProduto == id_produto:
                preco = produto.preco
                break
        
        if preco is None:
            print("Produto não encontrado. Venda não realizada.")
            return
        
        venda = Venda(id_produto, cliente, quantidade, preco)
        self.bancoDeDados.vendas.append(venda)
        print("Venda realizada com sucesso!")
