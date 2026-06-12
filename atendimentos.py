import pickle
import os
from clientes import carregar_clientes
from produtos import carregar_produtos

ARQUIVO = "dados/atendimentos.pkl"

def carregar_atendimentos():
    if not os.path.exists("dados"):
        os.makedirs("dados")
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "rb") as f:
        return pickle.load(f)

def salvar_atendimentos(atendimentos):
    with open(ARQUIVO, "wb") as f:
        pickle.dump(atendimentos, f)

def registrar_atendimento():
    clientes = carregar_clientes()
    produtos = carregar_produtos()

    if not clientes:
        print("\nNenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return
    if not produtos:
        print("\nNenhum produto ou serviço cadastrado. Cadastre um primeiro.")
        return

    print("\n--- REGISTRAR ATENDIMENTO ---")

    print("\nClientes:")
    for i, c in enumerate(clientes):
        print(f"  [{i+1}] {c['nome']}")
    try:
        ic = int(input("\nEscolha o cliente: ")) - 1
        if not (0 <= ic < len(clientes)):
            print("\nNúmero inválido.")
            return
    except ValueError:
        print("\nEntrada inválida.")
        return

    cliente = clientes[ic]

    if not cliente["animais"]:
        print("\nEsse cliente não tem animais cadastrados.")
        return

    print("\nAnimais:")
    for i, a in enumerate(cliente["animais"]):
        print(f"  [{i+1}] {a['nome']} ({a['especie']})")
    try:
        ia = int(input("\nEscolha o animal: ")) - 1
        if not (0 <= ia < len(cliente["animais"])):
            print("\nNúmero inválido.")
            return
    except ValueError:
        print("\nEntrada inválida.")
        return

    animal = cliente["animais"][ia]

    print("\nProdutos e Serviços:")
    for i, p in enumerate(produtos):
        print(f"  [{i+1}] {p['nome']} - R$ {p['preco']}")
    try:
        ip = int(input("\nEscolha o produto ou serviço: ")) - 1
        if not (0 <= ip < len(produtos)):
            print("\nNúmero inválido.")
            return
    except ValueError:
        print("\nEntrada inválida.")
        return

    produto = produtos[ip]
    data = input("\nData do atendimento (ex: 12/06/2026): ")
    obs = input("Observações (ou Enter para pular): ")

    atendimento = {
        "cliente": cliente["nome"],
        "animal": animal["nome"],
        "produto_servico": produto["nome"],
        "valor": produto["preco"],
        "data": data,
        "obs": obs
    }

    atendimentos = carregar_atendimentos()
    atendimentos.append(atendimento)
    salvar_atendimentos(atendimentos)
    print(f"\n✔ Atendimento registrado com sucesso!")

def listar_atendimentos():
    atendimentos = carregar_atendimentos()

    if not atendimentos:
        print("\nNenhum atendimento registrado ainda.")
        return

    print("\n--- LISTA DE ATENDIMENTOS ---")
    for i, a in enumerate(atendimentos):
        print(f"\n[{i+1}] Cliente: {a['cliente']}")
        print(f"    Animal: {a['animal']}")
        print(f"    Serviço/Produto: {a['produto_servico']}")
        print(f"    Valor: R$ {a['valor']}")
        print(f"    Data: {a['data']}")
        if a['obs']:
            print(f"    Obs: {a['obs']}")

def menu_atendimentos():
    while True:
        print("\n=============================")
        print("  MÓDULO INTEGRADOR          ")
        print("  ATENDIMENTOS               ")
        print("=============================")
        print("1. Registrar atendimento")
        print("2. Listar atendimentos")
        print("0. Voltar ao menu principal")
        print("-----------------------------")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_atendimento()
        elif opcao == "2":
            listar_atendimentos()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida. Tente novamente.")