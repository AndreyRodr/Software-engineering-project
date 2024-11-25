from estoque import Estoque

class SistemaVendas:
    def __init__(self):
        self.estoque = Estoque()

    def registrar_venda(self, id_produto, quantidade):
        produto = self.estoque.obter_produto(id_produto)
        if produto:
            if produto.reduzir_estoque(quantidade):
                total = produto.valor * quantidade
                print(f"Venda registrada: {quantidade}x {produto.nome} - Total: R$ {total:.2f}")
            else:
                print("Estoque insuficiente para realizar a venda.")
        else:
            print("Produto não encontrado.")

    def menu_principal(self):
            print("\n--- Sistema de Vendas ---")
            print("1. Adicionar Produto")
            print("2. Atualizar Estoque")
            print("3. Listar Produtos")
            print("4. Registrar Venda")
            print("0. Sair")
            opcao = input("Opção: ")

            return opcao

    def adicionar_produto(self):
        try:
            print("\n--- Adicionar Produto ---")
            id_produto = input("ID do Produto: ")
            nome = input("Nome do Produto: ")
            valor = float(input("Valor (R$): "))
            quantidade = int(input("Quantidade Inicial: "))
            self.estoque.adicionar_produto(id_produto, nome, valor, quantidade)
        except(ValueError):
            print("Valor inválido.")
    def atualizar_estoque(self):
        try:
            print("\n--- Atualizar Estoque ---")
            id_produto = input("ID do Produto: ")
            quantidade = int(input("Quantidade a Adicionar: "))
            self.estoque.atualizar_estoque(id_produto, quantidade)
        except(ValueError):
            print("Quantidade inválida.")
    def listar_produtos(self):
        self.estoque.listar_produtos()

    def realizar_venda(self):
        total_venda = 0  # Initialize total sale amount
        while True:
            try:
                print("\n--- Registrar Venda ---")
                id_produto = input("ID do Produto: ")
                quantidade = int(input("Quantidade Vendida: "))
                # Register the sale and get the price for the current product
                preco_produto = self.registrar_venda(id_produto, quantidade)
                total_venda += preco_produto  # Add the price of the current sale to the total
            except ValueError:
                print("Quantidade inválida.")

            continuar = input("Deseja registrar outro produto? (s/n): ").strip().lower()
            if continuar != 's':
                break
        print(f"Total da venda: R$ {total_venda:.2f}")  # Print the total sale amount
