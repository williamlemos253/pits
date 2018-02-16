from pits import app
from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, BooleanField, IntegerField, SubmitField, PasswordField, SelectField, HiddenField, RadioField, DateField
from wtforms.fields.html5 import IntegerRangeField, EmailField
from wtforms.validators import DataRequired, Required, NumberRange, EqualTo, Length, Regexp
from flask_user import current_user


class Formfisio(FlaskForm):
    paciente = StringField('Nome do Paciente')
    username_profissional = StringField('Relatado Por')
    banho = BooleanField('Banho')
    vestir = BooleanField('Vestir-se')
    higiene = BooleanField('Higiene')
    transferencia = BooleanField('Transferência')
    banho = BooleanField('Banho')
    continencia = BooleanField('Continência')
    alimentacao = BooleanField('Alimentação')
    niveldor = IntegerRangeField('Nível de dor', validators=[Required(), NumberRange(1,10)])
    salvar = SubmitField('Salvar')
    
    
class Formcadastropaciente(FlaskForm):
    username = StringField('Nome de Usário', validators=[Required(), Length(min=6, max=18, message='O nome de Usuário deve ter no mínimo 6 dígitos e no máximo 18'),
    Regexp('^[a-z0-9_-]{6,18}$', message="O nome de usuário não pode conter caracteres especiais, espaços e letras maiúsculas")])
    password = PasswordField('Senha', validators=[Required(), EqualTo('confirm', message='As senhas precisam ser iguais')])
    confirm = PasswordField('Repetir senha', validators=[Required(), EqualTo('password', message='As senhas precisam ser iguais')])
    email = EmailField('E-mail', validators=[Required(), Length(min=2, max=50)])
    datanasc = DateField('Data de nascimento', format='%d/%m/%Y')
    active = BooleanField('Ativo', default=True)
    first_name =  StringField('Nome', validators=[Required(), Length(min=2, max=50)])
    last_name = StringField('Sobrenome', validators=[Required(), Length(min=2, max=60)])
    cpf = StringField('CPF', validators = [Length(min=6, max=16)])
    salvar = SubmitField('Salvar')
    
class Formcadastrofuncionario(FlaskForm):
    username = StringField('Nome de Usário', validators=[Required(), Length(min=6, max=18, message='O nome de Usuário deve ter no mínimo 6 dígitos e no máximo 18'),
    Regexp('^[a-z0-9_-]{6,18}$', message="O nome de usuário não pode conter caracteres especiais, espaços e deve ter no mínimo 6 digítos")])
    password = PasswordField('Senha', validators=[Required(), EqualTo('confirm', message='As senhas precisam ser iguais')])
    confirm = PasswordField('Repetir senha', validators=[Required(), EqualTo('password', message='As senhas precisam ser iguais')])
    email = EmailField('E-mail', validators=[Required(), Length(min=2, max=50)])
    datanasc = DateField('Data de nascimento', format='%d/%m/%Y')
    active = BooleanField('Ativo', default=True)
    first_name =  StringField('Nome', validators=[Required(), Length(min=2, max=50)])
    last_name = StringField('Sobrenome', validators=[Required(), Length(min=2, max=60)])
    cpf = StringField('CPF', validators = [Length(min=6, max=12)])
    roles = SelectField('Função', choices=[('medico', 'Médico'), ('fisioterapeuta', 'Fisioterapeuta'), ('enfermeira', 'Enfermeira'), ('gestor', 'Gestor')])
    salvar = SubmitField('Salvar')
    
    
class SearchForm(FlaskForm):
  search = StringField('Pesquisar', [DataRequired()], render_kw={'class': 'pesquisa'})
  submit = SubmitField('Pesquisar', render_kw={'class': 'btn btn-success btn-block'})
  
  
class CirsgForm(FlaskForm):
    paciente = StringField('Nome do Paciente')
    username_profissional = StringField('Relatado Por')
    coracao = RadioField('Coração', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    vascular = RadioField('Vascular', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    hematopoietico = RadioField('Hematopoiético', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    respiratorio = RadioField('Respiratório', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    otorrino = RadioField('Otorrino', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    gastrointestinalsup = RadioField('Gastroinstestinal Superior', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    gastrointestinalinf = RadioField('Gastroinstestinal Inferior', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    figado = RadioField('Fígado', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    renal = RadioField('Renal', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    genitourinario = RadioField('Genitourinário', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    musculosqueletico = RadioField('Musculosquelético', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    neurologico = RadioField('Neurológico', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    endocrino = RadioField('Endócrino', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    psiquiatrica = RadioField('Psiquiátrica', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default=0)
    salvar = SubmitField('Salvar', render_kw={'class': 'btn btn-info btn-lg'})
    
class FugulinForm(FlaskForm):
    paciente = StringField('Nome do Paciente')
    username_profissional = StringField('Relatado Por')
    estadomental = RadioField('Estado Mental', choices=[('1','1'),('2','2'),('3','3'),('4','4')], default=1)
    oxigenacao = RadioField('Oxigenção', choices=[('1','1'),('2','2'),('3','3'),('4','4')], default=1)
    sinaisvitais = RadioField('Sinais Vitais', choices=[('1','1'),('2','2'),('3','3'),('4','4')], default=1)
    motibilidade = RadioField('Motibilidade', choices=[('1','1'),('2','2'),('3','3'),('4','4')], default=1)
    deambulacao = RadioField('Deambulação', choices=[('1','1'),('2','2'),('3','3'),('4','4')], default=1)
    alimentacao = RadioField('Alimentação', choices=[('1','1'),('2','2'),('3','3'),('4','4')], default=1)
    cuidadocorporal = RadioField('Cuidado Corporal', choices=[('1','1'),('2','2'),('3','3'),('4','4')], default=1)
    eliminacao = RadioField('Eliminação', choices=[('1','1'),('2','2'),('3','3'),('4','4')], default=1)
    terapeutica = RadioField('Terapêutica', choices=[('1','1'),('2','2'),('3','3'),('4','4')], default=1)
    salvar = SubmitField('Salvar', render_kw={'class': 'btn btn-info btn-lg'})