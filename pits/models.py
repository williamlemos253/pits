#coding: UTF-8
import datetime, re
from pits import app, db
from flask_login import current_user, login_manager, AnonymousUserMixin
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
from flask_user.forms import RegisterForm
from wtforms import StringField



# Define User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='' )
    
    # User email information
    email = db.Column(db.String(100), nullable=True, unique=True)
    confirmed_at = db.Column(db.DateTime())

    
    # User information
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')
    first_name = db.Column(db.String(50), nullable=False, server_default='')
    last_name = db.Column(db.String(50), nullable=False, server_default='')
    
    #campos extras dos usuarios
    datanasc = db.Column(db.DateTime, nullable=False)
    paciente = db.Column(db.Boolean(), nullable=False, server_default='0')
    cpf = db.Column(db.String(12), nullable=True, unique=True)

   
    # Relationships
    roles = db.relationship('Role', secondary='user_roles',
                backref=db.backref('users', lazy='dynamic'))
    
    def is_active(self):
        return self.active
        
    def __repr__(self):
        return '<Usuário: %r>' % self.first_name +  self.last_name
        

    
# Define Role model
class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), unique=True)
    
    def __repr__(self):
        return '<Role %r>' % self.name
        


# Define UserRoles model
class UserRoles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

    def __repr__(self):
        return '<UserRoles %r>' % self.id
        
    def __init__(self, user_id, role_id):
        self.user_id = user_id
        self.role_id = role_id

#define as funcoes de cadastro do fisioterapeuta modelo de katz
class Afisioterapeutas(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    paciente = db.Column(db.String(100), nullable=False)
    idpaciente = db.Column(db.Integer(), db.ForeignKey('user.id'))
    idprofissional = db.Column(db.Integer(), db.ForeignKey('user.id'))
    username_profissional = db.Column(db.String(100), nullable=False)
    datareg = db.Column(db.DateTime, default=datetime.datetime.now)
    banho = db.Column(db.Boolean())
    vestir = db.Column(db.Boolean())
    higiene = db.Column(db.Boolean())
    transferencia = db.Column(db.Boolean())
    continencia = db.Column(db.Boolean())
    alimentacao = db.Column(db.Boolean())
    niveldor = db.Column(db.Integer(), nullable=False)
    
#define as funcoes de cadastro do medico para o cirs-g
class Acirsg(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    idpaciente = db.Column(db.Integer(), db.ForeignKey('user.id'))
    paciente = db.Column(db.String(100), nullable=False)
    idprofissional = db.Column(db.Integer(), db.ForeignKey('user.id'))
    username_profissional = db.Column(db.String(100), nullable=False)
    datareg = db.Column(db.DateTime, default=datetime.datetime.now)
    coracao = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    vascular = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    hematopoietico = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    respiratorio = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    otorrino = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    gastrointestinalsup = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    gastrointestinalinf = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    figado = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    renal = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    genitourinario = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    musculosqueletico = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    neurologico = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    endocrino = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    psiquiatrica = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    numcatclass = db.Column(db.SmallInteger(), nullable=False)
    pontuacao = db.Column(db.SmallInteger(), nullable=False)
    indgravidade = db.Column(db.Float(), nullable=False)
    numcatsev3 = db.Column(db.SmallInteger(), nullable=False)
    numcatsev4 = db.Column(db.SmallInteger(), nullable=False)

#define as funcoes de cadastro do enfermeiro para o indice de complexidade de fugulin    
class Afugulin(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    idpaciente = db.Column(db.Integer(), db.ForeignKey('user.id'))
    paciente = db.Column(db.String(100), nullable=False)
    idprofissional = db.Column(db.Integer(), db.ForeignKey('user.id'))
    username_profissional = db.Column(db.String(100), nullable=False)
    datareg = db.Column(db.DateTime, default=datetime.datetime.now)
    estadomental = db.Column(db.SmallInteger(), nullable=False, server_default='1')
    oxigenacao = db.Column(db.SmallInteger(), nullable=False, server_default='1')
    sinaisvitais = db.Column(db.SmallInteger(), nullable=False, server_default='1')
    motibilidade = db.Column(db.SmallInteger(), nullable=False, server_default='1')
    deambulacao = db.Column(db.SmallInteger(), nullable=False, server_default='1')
    alimentacao = db.Column(db.SmallInteger(), nullable=False, server_default='1')
    cuidadocorporal	 = db.Column(db.SmallInteger(), nullable=False, server_default='1')
    eliminacao = db.Column(db.SmallInteger(), nullable=False, server_default='1')
    terapeutica = db.Column(db.SmallInteger(), nullable=False, server_default='1')
    soma1 = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    soma2 = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    soma3 = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    soma4 = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    somatotal = db.Column(db.SmallInteger(), nullable=False, server_default='0')
    
    
    
db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)