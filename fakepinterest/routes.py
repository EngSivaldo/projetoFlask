#cria as rotas
from flask import render_template, url_for, request, redirect
from fakepinterest import app #importa o app do __init__.py



# simulação de banco de dados simples 
usuarios = {} #dicionario {username: password}

@app.route("/")
def homepage():
  return render_template("index.html")

@app.route("/perfil/<usuario>")
def perfil(usuario):
  return render_template("perfil.html", usuario=usuario)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Verifica se o usuário existe e a senha está correta
        if username in usuarios and usuarios[username] == password:
            # Redireciona para a dashboard passando o username
            return redirect(url_for("dashboard", username=username))
        else:
            # Se não existe, redireciona para cadastro
            return redirect(url_for("cadastro"))
    # Se for GET, apenas mostra o formulário de login
    return render_template("login.html")



@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    usuarios[username] = password
    return redirect(url_for("login")) # depois do cadastro, redireciona para login
  return render_template("cadastro.html")


@app.route("/dashboard/<username>")
def dashboard(username):
    # Exemplo de dados que aparecem na dashboard
    pins = [
        {"img": "https://via.placeholder.com/250", "title": "Pin 1", "description": "Descrição do pin 1"},
        {"img": "https://via.placeholder.com/250", "title": "Pin 2", "description": "Descrição do pin 2"},
        {"img": "https://via.placeholder.com/250", "title": "Pin 3", "description": "Descrição do pin 3"},
        {"img": "https://via.placeholder.com/250", "title": "Pin 4", "description": "Descrição do pin 4"}
    ]
    return render_template("dashboard.html", pins=pins)