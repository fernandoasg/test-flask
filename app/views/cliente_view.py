from flask import render_template
from app.forms import cliente_form
from app import db

from app import app

# @app.route("/ola", defaults={'nome':None}, methods={"POST", "GET"})
# @app.route("/ola/<string:nome>")
# def teste(nome):
#     return render_template("clientes/teste.html", nome_usuario=nome)
#
# @app.route("/oi")
# def oi():
#     return "Oi, mundo!"
from app.models import cliente_model


@app.route("/cadastrar_cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    form = cliente_form.ClienteForm()

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        sexo = form.sexo.data

        cliente = cliente_model.Cliente(nome=nome, email = email, data_nascimento=data_nascimento, profissao=profissao, sexo=sexo)

        try:
            db.session.add(cliente)
            db.session.commit()
        except:
            print("Cliente não cadastrado")

    return render_template("clientes/form.html", form=form)