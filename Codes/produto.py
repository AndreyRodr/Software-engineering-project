class Produto:
    def __init__(self, id_produto, nome, valor, quantidade):
        self.id_produto = id_produto
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade

    def atualizar_estoque(self, quantidade):
        self.quantidade += quantidade

    def reduzir_estoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            return True
        return False

    def __str__(self):
        return f"[ID: {self.id_produto}] {self.nome} - R$ {self.valor:.2f} - Quantidade: {self.quantidade}"
