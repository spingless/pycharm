from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, data_required
from projetoGE.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("Email", validators= [DataRequired(), Email()])
    senha = PasswordField("Senha", validators = [DataRequired()])
    botaoSub = SubmitField("Entrar")


def validate_email(email):
    usuario = Usuario.query.filter_by(email = email.data).first()
    if usuario:
        raise ValidationError("Email já cadastrado. Faça login para continuar.")

class FormCriarConta(FlaskForm):
    email = StringField("Email:", validators = [DataRequired(), Email()])
    username = StringField("Usuário:", validators = [DataRequired()])

    cargo = SelectField("Cargo:", choices=[
        ('gerente', 'Gerente'),
        ('funcionario', 'Funcionario'),
    ], validators = [DataRequired()])

    senha = PasswordField("senha:", validators = [DataRequired(), Length(min= 6)])
    confirma_senha = PasswordField("Confirme a Senha:", validators = [DataRequired(), EqualTo("senha")])
    submit = SubmitField("Entrar")


class FormTarefa(FlaskForm):
    documento = FileField("Mandar Documento", validators= [DataRequired()])
    criador_tarefa = StringField("Criador da Tarefa", validators= [DataRequired()])
    responsavel = StringField("Responsavel", validators= [DataRequired()])
    botaoSub = SubmitField("Enviar")


class Formlogin:
    @classmethod
    def validate_on_submit(cls):
        pass