from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ti102.db'
app.config['SECRET_KEY'] = 'a2c2fcd11d509a802a80471c10a80fca071fb88c703f91e5a6e8069fd96bad71'

database = SQLAlchemy(app)
Bcrypt = Bcrypt(app)
Login_manager = LoginManager(app)
Login_manager.login_view ='homepage'

from projetoGE import routes, models

