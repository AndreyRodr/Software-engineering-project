class Produto:
    def __init__(self, nome, preco, descricao, quantidade, IDProduto):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.quantidade = quantidade
        self.IDProduto = IDProduto

    def getNome(self):
        return self.nome

    def setNome(self, value):
        self.nome = value

    def getPreco(self):
        return self.preco

    def setPreco(self, value):
        self.preco = value

    def getDescricao(self):
        return self.descricao

    def setDescricao(self, value):
        self.descricao = value

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, value):
        self.quantidade = value

    def getIDProduto(self):
        return self.IDProduto

    def setIDProduto(self, value):
        self.IDProduto = value