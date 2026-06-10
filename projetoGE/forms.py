from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from projetoGE.models import Usuario

class Formlogin(FlaskForm):
    email = StringField("Email", validators= [DataRequired(), Email()])
    senha = PasswordField("Senha", validators = [DataRequired()])
    botaoSub = SubmitField("Entrar")

class FormCriarConta(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email()])
    user = StringField("Usuario", validators = [DataRequired()])
    senha = PasswordField("senha", validators = [DataRequired(), Length(min= 6)])
    confirma_senha = PasswordField("Confirme a Senha", validators = [DataRequired(), EqualTo("senha")])
    submit = SubmitField("Entrar")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email = email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado. Faça login para continuar.")
