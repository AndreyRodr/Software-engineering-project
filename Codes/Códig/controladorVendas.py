from produto import Produto
from bancoDeDados import BancoDeDados
from venda import Venda
class ControladorVendas:
    def __init__(self, bancoDeDados):
        self.bancoDeDados = bancoDeDados

    def cadastrarProduto(self):
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        descricao = input("Descrição do produto: ")
        quantidade = int(input("Quantidade do produto: "))
        IDProduto = input("ID do produto: ")
        produto = Produto(nome, preco, descricao, quantidade, IDProduto)
        self.bancoDeDados.produtos.append(produto)
        print("Produto cadastrado com sucesso!")

    def registrarVenda(self):
        id_produto = input("Digite o ID do produto para a venda: ")
        cliente = input("Nome do Cliente: ")
        quantidade = int(input("Quantidade do produto: "))

        produto_encontrado = None
        for produto in self.bancoDeDados.produtos:
            if produto.IDProduto == id_produto and produto.quantidade >= quantidade:
                produto_encontrado = produto
                break

        if produto_encontrado:
            IDVenda = self.bancoDeDados.contador_vendas
            venda = Venda(IDVenda, cliente, quantidade, produto_encontrado)
            self.bancoDeDados.vendas.append(venda)
            produto_encontrado.quantidade -= quantidade
            self.bancoDeDados.contador_vendas += 1
            print(f"Venda registrada com sucesso! ID da venda: {IDVenda}")
        else:
            print("Produto não encontrado ou quantidade insuficiente.")

    def listarVendas(self):
        if not self.bancoDeDados.vendas:
            print("Não há vendas registradas.")
            return
        
        for venda in self.bancoDeDados.vendas:
            produto = venda.produto
            total = venda.quantidade * produto.preco
            print(f"ID Venda: {venda.IDVenda}, Produto: {produto.nome}, Cliente: {venda.cliente}, "
                  f"Quantidade: {venda.quantidade}, Preço Unitário: {produto.preco}, "
                  f"Valor Total: {total:.2f}")

    def faturamentoPorProduto(self, id_produto):
        faturamento = 0
        for venda in self.bancoDeDados.vendas:
            if venda.produto.IDProduto == id_produto:
                faturamento += venda.quantidade * venda.produto.preco
        print(f"Faturamento do produto com ID {id_produto}: {faturamento:.2f}")

    def produtosMaisVendidos(self):
        venda_contagem = {}
        for venda in self.bancoDeDados.vendas:
            produto = venda.produto
            if produto.IDProduto in venda_contagem:
                venda_contagem[produto.IDProduto] += venda.quantidade
            else:
                venda_contagem[produto.IDProduto] = venda.quantidade

        produtos_ordenados = sorted(venda_contagem.items(), key=lambda x: x[1], reverse=True)
        
        print("\nProdutos Mais Vendidos:")
        for id_produto, quantidade in produtos_ordenados:
            for produto in self.bancoDeDados.produtos:
                if produto.IDProduto == id_produto:
                    print(f"Produto: {produto.nome}, Quantidade Vendida: {quantidade}")
