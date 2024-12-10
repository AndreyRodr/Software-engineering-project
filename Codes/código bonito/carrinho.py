from vendas import Venda
from typing import List

class Carrinho:
    def __init__(self):
        self.itens: List[Venda] = []

    def realizarVenda(self, id: str, nomeCliente: str, credencial: str, quantidade: int) -> Venda:
        novaVenda:Venda = Venda(id, nomeCliente, quantidade, credencial)

        print("Produto adicionado ao carrinho!")
        self.itens.append(novaVenda)