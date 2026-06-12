import sqlite3
import os

def conectar():
    if not os.path.exists("dados"):
        os.makedirs("dados")
    return sqlite3.connect("dados/petshop.db")

def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT NOT NULL,
            endereco TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS animais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especie TEXT NOT NULL,
            raca TEXT NOT NULL,
            idade TEXT NOT NULL,
            cliente_id INTEGER,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT,
            preco TEXT NOT NULL,
            estoque TEXT,
            tipo TEXT DEFAULT 'produto'
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS atendimentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_nome TEXT NOT NULL,
            animal_nome TEXT NOT NULL,
            produto_servico TEXT NOT NULL,
            valor TEXT NOT NULL,
            data TEXT NOT NULL,
            obs TEXT
        )
    ''')

    conn.commit()
    conn.close()