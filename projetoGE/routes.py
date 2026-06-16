from projetoGE import app, Bcrypt, database
from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user
from projetoGE.forms import FormLogin, FormCriarConta
from projetoGE.models import Funcionario


@app.route('/', methods=['GET', 'POST'])
def homepage():
    formLogin = FormLogin()
    return render_template('homepage.html', form=formLogin)


@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    formcriarconta = FormCriarConta()

    if formcriarconta.validate_on_submit():
        senha = Bcrypt.generate_password_hash(formcriarconta.senha.data).decode('utf-8')
        usuario = Funcionario(username=formcriarconta.username.data,
                          email=formcriarconta.email.data,
                          senha=senha)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', usuario=usuario.username))

    return render_template('criarconta.html', form=formcriarconta)


@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)