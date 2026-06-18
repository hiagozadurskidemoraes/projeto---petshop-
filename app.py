from flask import Flask, render_template, request, redirect
from banco import inicializar_banco, conectar
from clientes import carregar_clientes
from produtos import carregar_produtos

app = Flask(__name__)
inicializar_banco()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/clientes")
def clientes():
    lista = carregar_clientes()
    return render_template("clientes.html", clientes=lista)

@app.route("/clientes/novo", methods=["POST"])
def novo_cliente():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, cpf, telefone, endereco) VALUES (?, ?, ?, ?)",
                   (request.form["nome"], request.form["cpf"],
                    request.form["telefone"], request.form["endereco"]))
    conn.commit()
    conn.close()
    return redirect("/clientes")

@app.route("/produtos")
def produtos():
    lista = carregar_produtos()
    return render_template("produtos.html", produtos=lista)

@app.route("/produtos/novo", methods=["POST"])
def novo_produto():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, categoria, preco, estoque, tipo) VALUES (?, ?, ?, ?, ?)",
                   (request.form["nome"], request.form["categoria"],
                    request.form["preco"], request.form.get("estoque", "0"),
                    request.form["tipo"]))
    conn.commit()
    conn.close()
    return redirect("/produtos")

@app.route("/atendimentos")
def atendimentos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM atendimentos")
    lista = cursor.fetchall()
    conn.close()

    total = 0
    for a in lista:
        try:
            total += float(a[4])
        except:
            pass

    return render_template("atendimentos.html", atendimentos=lista, total=f"{total:.2f}")

if __name__ == "__main__":
    app.run(debug=True)