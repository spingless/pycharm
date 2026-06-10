from projetoGE import app
from flask import render_template, url_for
from flask_login import login_required
from projetoGE.forms import Formlogin, FormCriarConta


@app.route('/', methods = ['GET', 'POST'])
def homepage():
    return render_template('homepage.html', form=formlogin)

@app.route('/criarconta', methods = ['GET', 'POST'])
def criarconta():
    form = FormCriarConta()
    return render_template('criarconta.html', form=FormCriarConta)

@app.route('/perfil/<usuario>', methods = ['GET', 'POST'])
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario )