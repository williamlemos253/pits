#coding: UTF-8
"""
The flask application package.
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_babel import Babel
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)

app.config.from_object('pits.config')

Bootstrap(app)

babel = Babel(app)

bcrypt = Bcrypt(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

#conf do csrf do wtforms
csrf = CSRFProtect(app)
csrf.init_app(app)



from pits import models
from pits import views
from pits import views_medico
from pits import views_enfermagem
from pits import admin