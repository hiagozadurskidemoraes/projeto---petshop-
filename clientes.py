import sqlite3
from banco import conectar, inicializar_banco

def cadastrar_cliente():
    print("\n--- CADASTRAR CLIENTE ---")
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, cpf, telefone, endereco) VALUES (?, ?, ?, ?)",
                   (nome, cpf, telefone, endereco))
    conn.commit()
    conn.close()
    print(f"\n✔ Cliente '{nome}' cadastrado com sucesso!")

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()

    if not clientes:
        print("\nNenhum cliente cadastrado ainda.")
        return clientes

    print("\n--- LISTA DE CLIENTES ---")
    for c in clientes:
        print(f"\n[{c[0]}] {c[1]}")
        print(f"    CPF: {c[2]}")
        print(f"    Telefone: {c[3]}")
        print(f"    Endereço: {c[4]}")

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM animais WHERE cliente_id = ?", (c[0],))
        animais = cursor.fetchall()
        conn.close()

        if animais:
            print("    Animais:")
            for a in animais:
                print(f"      - {a[1]} | {a[2]} | {a[3]} | {a[4]} anos")
        else:
            print("    Animais: nenhum cadastrado")

    return clientes

def remover_cliente():
    clientes = listar_clientes()
    if not clientes:
        return

    try:
        id_cliente = int(input("\nDigite o ID do cliente a remover: "))
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM animais WHERE cliente_id = ?", (id_cliente,))
        cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
        conn.commit()
        conn.close()
        print(f"\n✔ Cliente removido com sucesso!")
    except ValueError:
        print("\nEntrada inválida.")

def cadastrar_animal():
    clientes = listar_clientes()
    if not clientes:
        print("\nNenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return

    try:
        id_cliente = int(input("\nDigite o ID do dono do animal: "))
        print("\n--- CADASTRAR ANIMAL ---")
        nome = input("Nome do animal: ")
        especie = input("Espécie (cão, gato, etc.): ")
        raca = input("Raça: ")
        idade = input("Idade (anos): ")

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO animais (nome, especie, raca, idade, cliente_id) VALUES (?, ?, ?, ?, ?)",
                       (nome, especie, raca, idade, id_cliente))
        conn.commit()
        conn.close()
        print(f"\n✔ Animal '{nome}' cadastrado com sucesso!")
    except ValueError:
        print("\nEntrada inválida.")

def carregar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes_raw = cursor.fetchall()
    conn.close()

    clientes = []
    for c in clientes_raw:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM animais WHERE cliente_id = ?", (c[0],))
        animais_raw = cursor.fetchall()
        conn.close()

        animais = [{"nome": a[1], "especie": a[2], "raca": a[3], "idade": a[4]} for a in animais_raw]
        clientes.append({
            "id": c[0],
            "nome": c[1],
            "cpf": c[2],
            "telefone": c[3],
            "endereco": c[4],
            "animais": animais
        })
    return clientes

def menu_clientes():
    inicializar_banco()
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