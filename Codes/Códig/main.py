from bancoDeDados import BancoDeDados
from controladorVendas import ControladorVendas
from carrinho import Carrinho
from interface import InterfaceUsuario
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
                    controladorVendas.listarVendas()
                elif opcao == "2":
                    controladorVendas.registrarVenda()
                elif opcao == "0":
                    break
                else:
                    print("Opção inválida!")
        
        elif opcao_menu_principal == "2":
            while True:
                opcao = interface.menuProdutos()
                if opcao == "1":
                    controladorVendas.cadastrarProduto()
                elif opcao == "2":
                    id = input("Digite o ID do produto: ")
                    bancoDeDados.consultaPreco(id)
                elif opcao == "3":
                    id = input("Digite o ID do produto: ")
                    bancoDeDados.EditaProduto(id)
                elif opcao == "4":
                    id = input("Digite o ID do produto: ")
                    bancoDeDados.verificaID(id)
                elif opcao == "5":
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