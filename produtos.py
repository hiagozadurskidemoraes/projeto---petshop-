import pickle
import os

ARQUIVO = "dados/produtos.pkl"

def carregar_produtos():
    if not os.path.exists("dados"):
        os.makedirs("dados")
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "rb") as f:
        return pickle.load(f)

def salvar_produtos(produtos):
    with open(ARQUIVO, "wb") as f:
        pickle.dump(produtos, f)

def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")
    nome = input("Nome do produto: ")
    categoria = input("Categoria (ração, remédio, acessório, etc.): ")
    preco = input("Preço: R$ ")
    estoque = input("Quantidade em estoque: ")

    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque
    }

    produtos = carregar_produtos()
    produtos.append(produto)
    salvar_produtos(produtos)
    print(f"\n✔ Produto '{nome}' cadastrado com sucesso!")

def cadastrar_servico():
    print("\n--- CADASTRAR SERVIÇO ---")
    nome = input("Nome do serviço: ")
    descricao = input("Descrição: ")
    preco = input("Preço: R$ ")

    servico = {
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "tipo": "servico"
    }

    produtos = carregar_produtos()
    produtos.append(servico)
    salvar_produtos(produtos)
    print(f"\n✔ Serviço '{nome}' cadastrado com sucesso!")

def listar_produtos():
    produtos = carregar_produtos()

    if not produtos:
        print("\nNenhum produto ou serviço cadastrado ainda.")
        return

    print("\n--- LISTA DE PRODUTOS E SERVIÇOS ---")
    for i, p in enumerate(produtos):
        if p.get("tipo") == "servico":
            print(f"\n[{i+1}] SERVIÇO: {p['nome']}")
            print(f"    Descrição: {p['descricao']}")
            print(f"    Preço: R$ {p['preco']}")
        else:
            print(f"\n[{i+1}] PRODUTO: {p['nome']}")
            print(f"    Categoria: {p['categoria']}")
            print(f"    Preço: R$ {p['preco']}")
            print(f"    Estoque: {p['estoque']} unidades")

def remover_produto():
    produtos = carregar_produtos()

    if not produtos:
        print("\nNenhum produto ou serviço cadastrado.")
        return

    listar_produtos()
    try:
        escolha = int(input("\nDigite o número do item a remover: ")) - 1
        if 0 <= escolha < len(produtos):
            removido = produtos.pop(escolha)
            salvar_produtos(produtos)
            print(f"\n✔ '{removido['nome']}' removido com sucesso!")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nEntrada inválida. Digite um número.")

def menu_produtos():
    while True:
        print("\n=============================")
        print("  MÓDULO 2 - PRODUTOS        ")
        print("=============================")
        print("1. Cadastrar produto")
        print("2. Cadastrar serviço")
        print("3. Listar produtos e serviços")
        print("4. Remover produto/serviço")
        print("0. Voltar ao menu principal")
        print("-----------------------------")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            cadastrar_servico()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            remover_produto()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida. Tente novamente.")