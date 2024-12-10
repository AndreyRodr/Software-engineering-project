from produto import Produto
from carrinho import Carrinho
from funcionarios import Funcionario
from typing import List

class BancoDeDados:
    def __init__(self):
        self.__vendas:List[Carrinho] = []
        self.__produtos:List[Produto] = []
        self.__funcionarios:List[Funcionario] = []
        # self.contador_vendas = 1
        # Adicionando funcionário Marcos com a credencial
        # self.funcionarios.append(Funcionario(codigo=1, nome="Marcos", senha="123456"))

    def getProdutos(self) -> List[Produto]:
        return self.__produtos
    
    def getVendas(self) -> List[Carrinho]:
        return self.__vendas

    def adicionarProduto(self, nome:str, preco:float, descricao:str, quantidade:int, idProduto: str) -> None:
        if not self.verificaID(self.__produtos, idProduto):
            novoProduto = Produto(nome, preco, descricao, quantidade, idProduto)
            self.__produtos.append(novoProduto)
            print("Produto adicionado com sucesso!")
        else:
            print("ID do produto já existe.")

    def consultaPreco(self, id):
        for produto in self.produtos:
            if produto.IDProduto == id:
                print(f"O preço do produto {produto.nome} é {produto.preco}")
                return produto.preco
        print("Produto não encontrado")
        return None

    def editaProduto(self, idProduto) -> None:
        produto = self.verificaID(idProduto)
        if produto:
            produto.setName(input("Novo nome do produto: "))
            produto.setPreco(float(input("Novo preço do produto: ")))
            produto.setDescricao(input("Nova descrição do produto: "))
            produto.setQuantidade(int(input("Nova quantidade do produto: ")))
            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado")

    def deletaProduto(self, idProduto) -> None:
        produto = self.verificaID(self.__produtos, idProduto)
        if produto:
            if input("Você tem certeza que quer deletar este item? [s/n]").lower() == "s":
                self.__produtos.remove(produto)
                print("Produto removido")
        else:
            print("Produto não encontrado")

    def mostraProdutos(self):
        for produto in self.__produtos:
            print(f"{produto.getIDProduto()} - {produto.getNome()} ({produto.getQuantidade()} no estoque)")

    def cadastrarFuncionario(self):
        novoFuncionario = Funcionario("1111", "Marcos", "123")
        self.__funcionarios.append(novoFuncionario)

    def adicionaVenda(self, id: str, nomeCliente: str, credencial: str, quantidade: int) -> bool:
        novoCarrinho: Carrinho = Carrinho()
        
        if id == "":
            self.__vendas.append(novoCarrinho)
            # del novoCarrinho
            return False

        produto:Produto = self.verificaID(self.__produtos, id)

        if produto.getQuantidade() - quantidade >= 0:
            novoCarrinho.realizarVenda(id, nomeCliente, credencial, quantidade)
            self.__vendas.append(novoCarrinho)
            produto.setQuantidade(produto.getQuantidade() - quantidade)
        else:
            print("Quantidade insuficiente no estoque")

        return True

    @staticmethod
    def verificaID(produtos: List[Produto], idProduto: str) -> Produto:
        for produto in produtos:
            if produto.getIDProduto() == idProduto:
                return produto
        return None

    def verificaCredencial(self, credencial):
        for funcionario in self.__funcionarios:
            if funcionario.codigo == credencial:
                return True
        print("Credencial não encontrada")
        return False