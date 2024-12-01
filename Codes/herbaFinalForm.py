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
        print("3. Registrar Venda") 
        print("0. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")
        return opcao

    def menuProdutos(self):
        print("\nMenu Produtos:")
        print("1. Consultar Preço")
        print("2. Editar Produto")
        print("3. Verificar ID")
        print("4. Verificar Credencial")
        print("0. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")
        return opcao

    def menuAnalise(self):
        print("\nMenu Análise:")
        print("1. Faturamento por Produto")
        print("2. Produtos Mais Vendidos")
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
    def __init__(self, IDVenda, cliente, quantidade, produto):
        self.IDVenda = IDVenda
        self.cliente = cliente
        self.quantidade = quantidade
        self.produto = produto 


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


class Carrinho:
    def __init__(self, bancoDeDados):
        self.bancoDeDados = bancoDeDados

    def RealizarVenda(self):
        id_produto = input("ID do Produto: ")
        cliente = input("Nome do Cliente: ")
        credencial = input("Credencial do Cliente: ")
        quantidade = int(input("Quantidade: "))
        
        if not self.bancoDeDados.verificaID(id_produto):
            print("Produto não encontrado. Venda não realizada.")
            return
        
        if not self.bancoDeDados.verificaCredencial(credencial):
            print("Credencial inválida. Venda não realizada.")
            return
        
        preco = None
        for produto in self.bancoDeDados.produtos:
            if produto.IDProduto == id_produto:
                preco = produto.preco
                break
        
        if preco is None:
            print("Produto não encontrado. Venda não realizada.")
            return
        
        venda = Venda(id_produto, cliente, quantidade, preco)
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
                    controladorVendas.registrarVenda()
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
                elif opcao == "3":
                    id = input("Digite o ID do produto: ")
                    bancoDeDados.verificaID(id)
                elif opcao == "4":
                    credencial = input("Digite a credencial: ")
                    bancoDeDados.verificaCredencial(credencial)
                elif opcao == "0":
                    break
                else:
                    print("Opção inválida!")
        
        elif opcao_menu_principal == "3":
            while True:
                opcao = interface.menuAnalise()
                if opcao == "1":
                    id = input("Digite o ID do produto: ")
                    controladorVendas.faturamentoPorProduto(id)
                elif opcao == "2":
                    controladorVendas.produtosMaisVendidos()
                elif opcao == "0":
                    break
                else:
                    print("Opção inválida!")

        elif opcao_menu_principal == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
