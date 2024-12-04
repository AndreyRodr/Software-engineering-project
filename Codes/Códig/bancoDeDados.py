class BancoDeDados:
    def __init__(self):
        self.vendas = []
        self.produtos = []
        self.funcionarios = []
        self.contador_vendas = 1  
    def consultaPreco(self, id):
        for produto in self.produtos:
            if produto.IDProduto == id:
                print(f"O preço do produto {produto.nome} é {produto.preco}")
                return produto.preco
        print("Produto não encontrado")
        return None

    def EditaProduto(self, id):
        for produto in self.produtos:
            if produto.IDProduto == id:
                produto.nome = input("Novo nome do produto: ")
                produto.preco = float(input("Novo preço do produto: "))
                produto.descricao = input("Nova descrição do produto: ")
                produto.quantidade = int(input("Nova quantidade do produto: "))
                print("Produto atualizado com sucesso!")
                return
        print("Produto não encontrado")

    def verificaID(self, id):
        for produto in self.produtos:
            if produto.IDProduto == id:
                print(f"Produto encontrado: {produto.nome}")
                print(f"Estoque: {produto.quantidade}")
                return True
        print("Produto não encontrado")
        return False

    def verificaCredencial(self, credencial):
        for funcionario in self.funcionarios:
            if funcionario.senha == credencial:
                print(f"Funcionario encontrado: {funcionario.nome}")
                return True
        print("Credencial não encontrada")
        return False

