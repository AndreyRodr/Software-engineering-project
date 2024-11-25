from produto import Produto

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, id_produto, nome, valor, quantidade):
        if id_produto in self.produtos:
            print(f"Produto com ID {id_produto} já existe. Atualize o estoque.")
        else:
            self.produtos[id_produto] = Produto(id_produto, nome, valor, quantidade)
            print(f"Produto '{nome}' adicionado com sucesso!")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto no estoque.")
        else:
            print("\n--- Produtos no Estoque ---")
            for produto in self.produtos.values():
                print(produto)

    def atualizar_estoque(self, id_produto, quantidade):
        if id_produto in self.produtos:
            self.produtos[id_produto].atualizar_estoque(quantidade)
            print(f"Estoque atualizado para o produto '{self.produtos[id_produto].nome}'.")
        else:
            print("Produto não encontrado.")

    def obter_produto(self, id_produto):
        return self.produtos.get(id_produto)
