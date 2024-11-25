from sistemaVendas import SistemaVendas

if __name__ == "__main__":
    sistema = SistemaVendas()
    while True:
        if input("Aperte ENTER para ir ao menu") == '':
            opcao = sistema.menu_principal()
            
            if opcao == "1":
                sistema.adicionar_produto()
            elif opcao == "2":
                sistema.atualizar_estoque()
            elif opcao == "3":
                sistema.listar_produtos()
            elif opcao == "4":
                sistema.realizar_venda()
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")            
