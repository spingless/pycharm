from sqlalchemy.engine import default
from projetoGE import database
from datetime import datetime

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100), nullable=False)
    email = database.Column(database.String(120), nullable=False, unique=True)
    senha = database.Column(database.String(100), nullable=False)
    cargo = database.Column(database.String(20), nullable=False, default='funcionario')

class Tarefa(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String(100), nullable=False)
    descricao = database.Column(database.String(200), nullable=False)
    status = database.Column(database.String(30),nullable=False, default='pendente')
    demanda = database.Column(database.String(20), nullable=False, default='baixa')
    data_Criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    prazo = database.Column(database.DateTime, nullable=False)
    id_Criador = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    id_Responsavel = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)


