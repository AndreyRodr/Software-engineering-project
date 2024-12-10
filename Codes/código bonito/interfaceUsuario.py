from controladorVendas import ControladorVendas
from bancoDeDados import BancoDeDados

class InterfaceUsuario:
    def __init__(self):
        self.__bancoDeDados:BancoDeDados = BancoDeDados()
        self.__controladorVendas:ControladorVendas = ControladorVendas(self.__bancoDeDados)
        
        self.__bancoDeDados.cadastrarFuncionario()

    def menuInicial(self) -> None:
        print("1. Menu Vendas")
        print("2. Menu Produtos")
        print("3. Menu Análise")
        opcao = input("Escolha o Menu desejado: ")
        
        if opcao == "1":
            self.registraVenda()
        elif opcao == "2":
            self.menuProdutos()
        elif opcao == "3":
            self.menuAnalise()
        else:
            print("Opção inválida")
    
    def registraVenda(self) -> None:
        self.__controladorVendas.cadastraVenda()
        
    def menuProdutos(self) -> None:
        print("1. Registrar Produto")
        print("2. Editar Produto")
        print("3. Deletar Produto")
        print("4. Mostrar Produtos")
        print("0. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            self.__controladorVendas.cadastrarProduto()
        elif opcao == "2":
            idProduto = input("Digite o ID do produto: ")
            self.__bancoDeDados.editaProduto(idProduto)
        elif opcao == "3":
            idProduto = input("Digite o ID do produto: ")
            self.__bancoDeDados.deletaProduto(idProduto)
        elif opcao == "4":
            self.__bancoDeDados.mostraProdutos()

    
    def menuAnalise(self) -> None:
        print("\nMenu Análise:")
        print("1. Faturamento por Produto")
        print("2. Produtos Mais Vendidos")
        print("3. Listar Vendas")
        print("0. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            IDProduto:str = input(f"Entre com o ID do produto: ")
            self.__controladorVendas.faturamentoPorProduto(IDProduto)
        elif opcao == "2":
            self.__controladorVendas.produtosMaisVendidos()
        elif opcao == "3":
            self.__controladorVendas.listarVendas()
