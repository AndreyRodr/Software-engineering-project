from produto import Produto
from bancoDeDados import BancoDeDados

class ControladorVendas:
    def __init__(self, bancoDeDados):
        self.__bancoDeDados:BancoDeDados = bancoDeDados

    def cadastrarProduto(self):
        nome:str = input("Nome do produto: ")
        preco:float = float(input("Preço do produto: "))
        descricao:str = input("Descrição do produto: ")
        quantidade:int = int(input("Quantidade do produto: "))
        IDProduto:str = input("ID do produto: ")
        
        self.__bancoDeDados.adicionarProduto(nome, preco, descricao, quantidade, IDProduto)

    
    def cadastraVenda(self):
        nomeCliente:str = input("Insira o nome do cliente: ")
        credencial:str = input("Insira sua credêncial: ")

        if self.__bancoDeDados.verificaCredencial(credencial):

            print("Pressione Enter no campo do ID para finalizar a operação")
            while True:
                try:
                    IDProduto:str = input("ID do produto: ")
                    quantidade:int = int(input("Quantidade: "))
        
                    if self.__bancoDeDados.verificaID(self.__bancoDeDados.getProdutos(), IDProduto) or IDProduto == "":
                        retornoVenda = self.__bancoDeDados.adicionaVenda(IDProduto, nomeCliente, credencial, quantidade)
                        if retornoVenda == False:
                            break
                    else:
                        print("Não existe nenhum produto com esse ID")
                except ValueError:
                    print("Coloque qualquer valor no campo de quantidade")

    def faturamentoPorProduto(self, id: str):
        produto:Produto = self.__bancoDeDados.verificaID(self.__bancoDeDados.getProdutos(), id)
        preco = 0 
        for i in self.__bancoDeDados.getVendas():
            for j in i.itens:
                if j.IDVenda == id:
                    preco += produto.preco * j.quantidade
        print(f"O produto {produto.getNome()} faturou: R${preco:.2f}")

    def listarVendas(self):
        if not self.__bancoDeDados.getVendas():
            print("Não houveram vendas")
        
        total = 0

        for i in self.__bancoDeDados.getVendas():
            for j in i.itens:
                produto = self.__bancoDeDados.verificaID(self.__bancoDeDados.getProdutos(), j.IDVenda)
                preco = produto.getPreco() * j.quantidade
                total += preco
                print(f"Cliente: {j.cliente} -> R${preco:.2f}")
        print("-"*60)
        print(f"Faturamento total: R$ {total:.2f}")

    def produtosMaisVendidos(self):
        venda_contagem = {}
        for venda in self.__bancoDeDados.getVendas():
            for j in venda.itens:
                if j.IDVenda in venda_contagem:
                    produto = self.__bancoDeDados.verificaID(self.__bancoDeDados.getProdutos(), j.IDVenda)
                    venda_contagem[produto.IDProduto] += j.quantidade * produto.getPreco()
                else:
                    produto = self.__bancoDeDados.verificaID(self.__bancoDeDados.getProdutos(), j.IDVenda)
                    venda_contagem[produto.IDProduto] = j.quantidade

        produtos_ordenados = sorted(venda_contagem.items(), key=lambda x: x[1], reverse=True)
        
        print("\nProdutos Mais Vendidos:")
        for id_produto, quantidade in produtos_ordenados:
            for produto in self.__bancoDeDados.getProdutos():
                if produto.getIDProduto() == id_produto:
                    print(f"Produto: {produto.nome}, Quantidade Vendida: {quantidade}")
