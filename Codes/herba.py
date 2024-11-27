class InterfaceUsuario:
    def escolherMenu(self):
        print("1. Menu Vendas")
        print("2. Menu Produtos")
        print("3. Menu Análise")
        opcao = input("Escolha o Menu desejado: ")
        return opcao

    def menuVendas(self):
        print("\nMenu Vendas:")
        print("1. Cadastrar Produto")
        print("2. Listar Vendas")
        print("3. Faturamento por Produto")
        print("4. Produtos Mais Vendidos")
        print("0. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")
        return opcao

    def menuProdutos(self):
        print("\nMenu Produtos:")
        print("1. Consultar Preço")
        print("2. Editar Produto")
        print("0. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")
        return opcao

    def menuAnalise(self):
        print("\nMenu Análise:")
        print("1. Verificar ID")
        print("2. Verificar Credencial")
        print("0. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")
        return opcao


class Produto:
    def __init__(self, nome, preco, descricao, quantidade, IDProduto):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.quantidade = quantidade
        self.IDProduto = IDProduto


class Venda:
    def __init__(self, IDVenda, cliente, credencial, quantidade):
        self.IDVenda = IDVenda
        self.cliente = cliente
        self.credencial = credencial
        self.quantidade = quantidade


class Funcionario:
    def __init__(self, codigo, nome, senha):
        self.codigo = codigo
        self.nome = nome
        self.senha = senha


class BancoDeDados:
    def __init__(self):
        self.vendas = []
        self.produtos = []
        self.funcionarios = []

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

    def listarVendas(self):
        for venda in self.bancoDeDados.vendas:
            print(f"ID Venda: {venda.IDVenda}, Cliente: {venda.cliente}, Quantidade: {venda.quantidade}")

    def faturamentoPorProduto(self, id):
        faturamento = 0
        for venda in self.bancoDeDados.vendas:
            if venda.IDVenda == id:
                faturamento += venda.quantidade * venda.preco
        print(f"Faturamento do produto ID {id}: {faturamento}")

    def produtosMaisVendidos(self):
        vendas_por_produto = {}
        for venda in self.bancoDeDados.vendas:
            if venda.IDVenda in vendas_por_produto:
                vendas_por_produto[venda.IDVenda] += venda.quantidade
            else:
                vendas_por_produto[venda.IDVenda] = venda.quantidade
        mais_vendidos = sorted(vendas_por_produto.items(), key=lambda x: x[1], reverse=True)
        for id, quantidade in mais_vendidos:
            print(f"Produto ID {id}: {quantidade} unidades vendidas")


class Carrinho:
    def __init__(self, bancoDeDados):
        self.bancoDeDados = bancoDeDados

    def RealizarVenda(self):
        id = input("ID do Produto: ")
        cliente = input("Nome do Cliente: ")
        credencial = input("Credencial do Cliente: ")
        quantidade = int(input("Quantidade: "))
        if not self.bancoDeDados.verificaID(id):
            print("Produto não encontrado. Venda não realizada.")
            return
        if not self.bancoDeDados.verificaCredencial(credencial):
            print("Credencial inválida. Venda não realizada.")
            return
        venda = Venda(id, cliente, credencial, quantidade)
        self.bancoDeDados.vendas.append(venda)
        print("Venda realizada com sucesso!")


def main():
    bancoDeDados = BancoDeDados()
    controladorVendas = ControladorVendas(bancoDeDados)
    carrinho = Carrinho(bancoDeDados)
    interface = InterfaceUsuario()
    
    while True:
        opcao_menu_principal = interface.escolherMenu()
        
        if opcao_menu_principal == "1":
            while True:
                opcao = interface.menuVendas()
                if opcao == "1":
                    controladorVendas.cadastrarProduto()
                elif opcao == "2":
                    controladorVendas.listarVendas()
                elif opcao == "3":
                    id = input("Digite o ID do produto: ")
                    controladorVendas.faturamentoPorProduto(id)
                elif opcao == "4":
                    controladorVendas.produtosMaisVendidos()
                elif opcao == "0":
                    break
                else:
                    print("Opção inválida!")
        
        elif opcao_menu_principal == "2":
            while True:
                opcao = interface.menuProdutos()
                if opcao == "1":
                    id = input("Digite o ID do produto: ")
                    bancoDeDados.consultaPreco(id)
                elif opcao == "2":
                    id = input("Digite o ID do produto: ")
                    bancoDeDados.EditaProduto(id)
                elif opcao == "0":
                    break
                else:
                    print("Opção inválida!")
        
        elif opcao_menu_principal == "3":
            while True:
                opcao = interface.menuAnalise()
                if opcao == "1":
                    id = input("Digite o ID do produto: ")
                    bancoDeDados.verificaID(id)
                elif opcao == "2":
                    credencial = input("Digite a credencial: ")
                    bancoDeDados.verificaCredencial(credencial)
                elif opcao == "0":
                    break
                else:
                    print("Opção inválida!")
        
        else:
            print("Opção inválida!")

        opcao = input("Deseja voltar ao Menu Principal? (s/n): ")
        if opcao.lower() != 's':
            print("encerrando programa!")
            break

if __name__ == "__main__":
    main()
