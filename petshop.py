from clientes import menu_clientes
# from produtos import menu_produtos
# from atendimentos import menu_atendimentos

def menu_principal():
    while True:
        print("\n=============================")
        print("     PETSHOP - SISTEMA       ")
        print("=============================")
        print("1. Clientes e Animais")
        # print("2. Produtos e Serviços")
        # print("3. Atendimentos")
        print("0. Sair")
        print("-----------------------------")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        # elif opcao == "2":
        #     menu_produtos()
        # elif opcao == "3":
        #     menu_atendimentos()
        elif opcao == "0":
            print("\nSaindo... Até mais!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()