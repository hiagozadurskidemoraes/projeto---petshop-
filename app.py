from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from banco import inicializar_banco, conectar
from clientes import carregar_clientes
from produtos import carregar_produtos
from functools import wraps

app = Flask(__name__)
app.secret_key = "petcare_chave_secreta_2026"
inicializar_banco()

def login_obrigatorio(f):
    @wraps(f)
    def decorada(*args, **kwargs):
        if not session.get("logado"):
            return redirect("/admin/login")
        return f(*args, **kwargs)
    return decorada

# ---------------- PÚBLICO ----------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/produtos")
def produtos():
    lista = carregar_produtos()
    return render_template("produtos.html", produtos=lista)

# ---------------- CADASTRO E LOGIN ----------------

@app.route("/admin/cadastro", methods=["GET", "POST"])
def cadastro():
    erro = None
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        existe = cursor.fetchone()

        if existe:
            erro = "Esse email já está cadastrado."
            conn.close()
        else:
            senha_hash = generate_password_hash(senha)
            cursor.execute("INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?)",
                           (nome, email, senha_hash))
            conn.commit()
            conn.close()
            return redirect("/admin/login")

    return render_template("cadastro.html", erro=erro)

@app.route("/admin/login", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        usuario = cursor.fetchone()
        conn.close()

        if usuario and check_password_hash(usuario[3], senha):
            session["logado"] = True
            session["nome_usuario"] = usuario[1]
            return redirect("/admin")
        else:
            erro = "Email ou senha incorretos."

    return render_template("login.html", erro=erro)

@app.route("/admin/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------------- ADMIN ----------------

@app.route("/admin")
@login_obrigatorio
def admin_dashboard():
    return render_template("admin.html")

@app.route("/admin/clientes")
@login_obrigatorio
def admin_clientes():
    lista = carregar_clientes()
    return render_template("admin_clientes.html", clientes=lista)

@app.route("/admin/clientes/novo", methods=["POST"])
@login_obrigatorio
def novo_cliente():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, cpf, telefone, endereco) VALUES (?, ?, ?, ?)",
                   (request.form["nome"], request.form["cpf"],
                    request.form["telefone"], request.form["endereco"]))
    conn.commit()
    conn.close()
    return redirect("/admin/clientes")

@app.route("/admin/produtos")
@login_obrigatorio
def admin_produtos():
    lista = carregar_produtos()
    return render_template("admin_produtos.html", produtos=lista)

@app.route("/admin/produtos/novo", methods=["POST"])
@login_obrigatorio
def novo_produto():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, categoria, preco, estoque, tipo) VALUES (?, ?, ?, ?, ?)",
                   (request.form["nome"], request.form["categoria"],
                    request.form["preco"], request.form.get("estoque", "0"),
                    request.form["tipo"]))
    conn.commit()
    conn.close()
    return redirect("/admin/produtos")

@app.route("/admin/atendimentos")
@login_obrigatorio
def admin_atendimentos():
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

    return render_template("admin_atendimentos.html", atendimentos=lista, total=f"{total:.2f}")

if __name__ == "__main__":
    app.run(debug=True)