class InterfaceUsuario:
    def escolherMenu(self):
        print("1. Menu Vendas")
        print("2. Menu Produtos")
        print("3. Menu Análise")
        print("0. Sair.")
        opcao = input("Escolha o Menu desejado: ")
        return opcao

    def menuVendas(self):
        print("\nMenu Vendas:")
        print("1. Listar Vendas")
        print("2. Registrar Venda") 
        print("0. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")
        return opcao

    def menuProdutos(self):
        print("\nMenu Produtos:")
        print("1. Cadastrar Produto")
        print("2. Consultar Preço")
        print("3. Editar Produto")
        print("4. Verificar ID")
        print("5. Verificar Credencial")
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