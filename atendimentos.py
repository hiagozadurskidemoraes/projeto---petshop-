import sqlite3
from banco import conectar, inicializar_banco
from clientes import carregar_clientes
from produtos import carregar_produtos

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
    for c in clientes:
        print(f"  [{c['id']}] {c['nome']}")
    try:
        id_cliente = int(input("\nDigite o ID do cliente: "))
        cliente = next((c for c in clientes if c['id'] == id_cliente), None)
        if not cliente:
            print("\nCliente não encontrado.")
            return
    except ValueError:
        print("\nEntrada inválida.")
        return

    if not cliente["animais"]:
        print("\nEsse cliente não tem animais cadastrados.")
        return

    print("\nAnimais:")
    for i, a in enumerate(cliente["animais"]):
        print(f"  [{i+1}] {a['nome']} ({a['especie']})")
    try:
        ia = int(input("\nEscolha o número do animal: ")) - 1
        if not (0 <= ia < len(cliente["animais"])):
            print("\nNúmero inválido.")
            return
    except ValueError:
        print("\nEntrada inválida.")
        return

    animal = cliente["animais"][ia]

    print("\nProdutos e Serviços:")
    for p in produtos:
        print(f"  [{p['id']}] {p['nome']} - R$ {p['preco']}")
    try:
        id_produto = int(input("\nDigite o ID do produto ou serviço: "))
        produto = next((p for p in produtos if p['id'] == id_produto), None)
        if not produto:
            print("\nProduto não encontrado.")
            return
    except ValueError:
        print("\nEntrada inválida.")
        return

    data = input("\nData do atendimento (ex: 12/06/2026): ")
    obs = input("Observações (ou Enter para pular): ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO atendimentos (cliente_nome, animal_nome, produto_servico, valor, data, obs) VALUES (?, ?, ?, ?, ?, ?)",
                   (cliente["nome"], animal["nome"], produto["nome"], produto["preco"], data, obs))
    conn.commit()
    conn.close()
    print(f"\n✔ Atendimento registrado com sucesso!")

def listar_atendimentos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM atendimentos")
    atendimentos = cursor.fetchall()
    conn.close()

    if not atendimentos:
        print("\nNenhum atendimento registrado ainda.")
        return

    print("\n--- LISTA DE ATENDIMENTOS ---")
    for a in atendimentos:
        print(f"\n[{a[0]}] Cliente: {a[1]}")
        print(f"    Animal: {a[2]}")
        print(f"    Serviço/Produto: {a[3]}")
        print(f"    Valor: R$ {a[4]}")
        print(f"    Data: {a[5]}")
        if a[6]:
            print(f"    Obs: {a[6]}")

def menu_atendimentos():
    inicializar_banco()
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