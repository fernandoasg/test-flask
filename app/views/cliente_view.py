from flask import render_template
from app.forms import cliente_form

from app import app

# @app.route("/ola", defaults={'nome':None}, methods={"POST", "GET"})
# @app.route("/ola/<string:nome>")
# def teste(nome):
#     return render_template("clientes/teste.html", nome_usuario=nome)
#
# @app.route("/oi")
# def oi():
#     return "Oi, mundo!"
@app.route("/cadastrar_cliente")
def cadastrar_cliente():
    form = cliente_form.ClienteForm()

    return render_template("clientes/form.html", form=form)