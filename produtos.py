import sqlite3
from banco import conectar, inicializar_banco

def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")
    nome = input("Nome do produto: ")
    categoria = input("Categoria (ração, remédio, acessório, etc.): ")
    preco = input("Preço: R$ ")
    estoque = input("Quantidade em estoque: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, categoria, preco, estoque, tipo) VALUES (?, ?, ?, ?, ?)",
                   (nome, categoria, preco, estoque, "produto"))
    conn.commit()
    conn.close()
    print(f"\n✔ Produto '{nome}' cadastrado com sucesso!")

def cadastrar_servico():
    print("\n--- CADASTRAR SERVIÇO ---")
    nome = input("Nome do serviço: ")
    categoria = input("Descrição: ")
    preco = input("Preço: R$ ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, categoria, preco, estoque, tipo) VALUES (?, ?, ?, ?, ?)",
                   (nome, categoria, preco, "0", "servico"))
    conn.commit()
    conn.close()
    print(f"\n✔ Serviço '{nome}' cadastrado com sucesso!")

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()

    if not produtos:
        print("\nNenhum produto ou serviço cadastrado ainda.")
        return produtos

    print("\n--- LISTA DE PRODUTOS E SERVIÇOS ---")
    for p in produtos:
        if p[5] == "servico":
            print(f"\n[{p[0]}] SERVIÇO: {p[1]}")
            print(f"    Descrição: {p[2]}")
            print(f"    Preço: R$ {p[3]}")
        else:
            print(f"\n[{p[0]}] PRODUTO: {p[1]}")
            print(f"    Categoria: {p[2]}")
            print(f"    Preço: R$ {p[3]}")
            print(f"    Estoque: {p[4]} unidades")

    return produtos

def remover_produto():
    produtos = listar_produtos()
    if not produtos:
        return

    try:
        id_produto = int(input("\nDigite o ID do item a remover: "))
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        conn.commit()
        conn.close()
        print(f"\n✔ Item removido com sucesso!")
    except ValueError:
        print("\nEntrada inválida.")

def carregar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos_raw = cursor.fetchall()
    conn.close()

    produtos = []
    for p in produtos_raw:
        produtos.append({
            "id": p[0],
            "nome": p[1],
            "categoria": p[2],
            "preco": p[3],
            "estoque": p[4],
            "tipo": p[5]
        })
    return produtos

def menu_produtos():
    inicializar_banco()
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