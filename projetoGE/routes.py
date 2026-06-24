from projetoGE import app, bcrypt, database
from flask import render_template, url_for, redirect, flash
from flask_login import login_required, login_user, logout_user, current_user
from projetoGE.forms import FormLogin, FormCriarConta, FormTarefa
from projetoGE.models import Usuario, Tarefa
from werkzeug.utils import secure_filename
import os

@app.route('/', methods=['GET', 'POST'])
def homepage():
    formlogin= FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario, remember=True)
            return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('homepage.html', form=formlogin)

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    formcriarconta = FormCriarConta()

    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data).decode('utf-8')
        usuario = Usuario(nome=formcriarconta.username.data,
                          cargo = formcriarconta.cargo.data,
                          email=formcriarconta.email.data,
                          senha=senha)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', id_usuario=usuario.id))

    return render_template('criarconta.html', form=formcriarconta)


@app.route('/perfil/<id_usuario>')
@login_required
def perfil(id_usuario):
    if int(id_usuario) == current_user.id:
        # O usuário está vendo o perfil dele
        form = FormTarefa()
        if form.validate_on_submit():
            nova_tarefa = Tarefa(
                titulo=form.titulo.data,
                descricao=form.descricao.data,
                demanda=form.demanda.data,
                prazo=form.prazo.data,
                id_Criador=current_user.id,
                id_Responsavel=form.id_responsavel.data
            )
            database.session.add(nova_tarefa)
            database.session.commit()
            flash('Tarefa criada com sucesso!', category='success')

        return render_template('perfil.html', id_usuario=id_usuario, usuario=current_user, form=form)
    else:
        # O user está vendo o perfil de outra pessoa
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('perfil.html', template_name_or_list='perfil.html', usuario=usuario, form=None)




@app.route('/logout')
@login_required
def logout():
    logout_user(current_user)
