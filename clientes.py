import pickle
import os

ARQUIVO = "dados/clientes.pkl"

def carregar_clientes():
    if not os.path.exists("dados"):
        os.makedirs("dados")
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "rb") as f:
        return pickle.load(f)

def salvar_clientes(clientes):
    with open(ARQUIVO, "wb") as f:
        pickle.dump(clientes, f)

def cadastrar_cliente():
    print("\n--- CADASTRAR CLIENTE ---")
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")

    novo_cliente = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "endereco": endereco,
        "animais": []
    }

    clientes = carregar_clientes()
    clientes.append(novo_cliente)
    salvar_clientes(clientes)
    print(f"\n✔ Cliente '{nome}' cadastrado com sucesso!")

def listar_clientes():
    clientes = carregar_clientes()

    if not clientes:
        print("\nNenhum cliente cadastrado ainda.")
        return

    print("\n--- LISTA DE CLIENTES ---")
    for i, c in enumerate(clientes):
        print(f"\n[{i+1}] {c['nome']}")
        print(f"    CPF: {c['cpf']}")
        print(f"    Telefone: {c['telefone']}")
        print(f"    Endereço: {c['endereco']}")

        if c["animais"]:
            print("    Animais:")
            for a in c["animais"]:
                print(f"      - {a['nome']} | {a['especie']} | {a['raca']} | {a['idade']} anos")
        else:
            print("    Animais: nenhum cadastrado")

def remover_cliente():
    clientes = carregar_clientes()

    if not clientes:
        print("\nNenhum cliente cadastrado.")
        return

    listar_clientes()
    try:
        escolha = int(input("\nDigite o número do cliente a remover: ")) - 1
        if 0 <= escolha < len(clientes):
            removido = clientes.pop(escolha)
            salvar_clientes(clientes)
            print(f"\n✔ Cliente '{removido['nome']}' removido com sucesso!")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nEntrada inválida. Digite um número.")

def cadastrar_animal():
    clientes = carregar_clientes()

    if not clientes:
        print("\nNenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return

    listar_clientes()
    try:
        escolha = int(input("\nDigite o número do dono do animal: ")) - 1
        if 0 <= escolha < len(clientes):
            print("\n--- CADASTRAR ANIMAL ---")
            nome = input("Nome do animal: ")
            especie = input("Espécie (cão, gato, etc.): ")
            raca = input("Raça: ")
            idade = input("Idade (anos): ")

            animal = {
                "nome": nome,
                "especie": especie,
                "raca": raca,
                "idade": idade
            }

            clientes[escolha]["animais"].append(animal)
            salvar_clientes(clientes)
            print(f"\n✔ Animal '{nome}' cadastrado para '{clientes[escolha]['nome']}'!")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nEntrada inválida. Digite um número.")

def menu_clientes():
    while True:
        print("\n=============================")
        print("   MÓDULO 1 - CLIENTES       ")
        print("=============================")
        print("1. Cadastrar cliente")
        print("2. Cadastrar animal")
        print("3. Listar clientes e animais")
        print("4. Remover cliente")
        print("0. Voltar ao menu principal")
        print("-----------------------------")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_animal()
        elif opcao == "3":
            listar_clientes()
        elif opcao == "4":
            remover_cliente()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_clientes()