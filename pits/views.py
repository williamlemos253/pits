#coding: UTF-8
from pits import app, db
from pits.models import Afisioterapeutas, User, UserRoles, Role
from flask import render_template, redirect, url_for, request, flash
from flask_user import login_required
from flask_login import current_user, AnonymousUserMixin
from flask_sqlalchemy import SQLAlchemy
from pits.forms import Formfisio, Formcadastropaciente, Formcadastrofuncionario, SearchForm
import bcrypt
import re

validausernameregex = re.compile("^[a-z0-9_-]{6,20}$")

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/pacientesbusca')
@login_required
def pacientesbusca():
    usuarios = User.query.filter(User.paciente==True)
    return render_template('pacientesbusca.html', usuarios=usuarios)
    
@app.route('/pacientesfisio')
@login_required
def pacientesfisio():
    form = SearchForm()
    usuarios = User.query.filter(User.paciente==True, User.active==True)
    if form.validate_on_submit():
        return redirect('/pacientesfisio2')
    return render_template('fisioterapia/pacientesfisio.html', usuarios=usuarios, SearchForm=form)
    
@app.route('/pacientesfisio2', methods=('GET', 'POST'))
@login_required
def pacientesfisio2():
    form = SearchForm()
    filtro = form.search.data
    if not form.validate_on_submit():
        return redirect(url_for('pacientesfisio'))
    #separa o primeiro nome do resto
    usuarios = User.query.filter(User.paciente==True, User.active==True)
    return render_template('fisioterapia/pacientesfisio.html', usuarios=usuarios, SearchForm=form)


@app.route('/resumofisio')
@login_required
def homefisio():
    form = SearchForm()
    fisioterapias = Afisioterapeutas.query.order_by(Afisioterapeutas.datareg.desc())
    return render_template('fisioterapia/resumofisio.html', fisioterapias=fisioterapias, SearchForm=form)


@app.route('/cadastrafisio/')
@app.route('/cadastrafisio/<int:id>', methods=('GET', 'POST'))
@login_required
def cadastrafisio(id):
    nomepaciente = User.query.filter(User.id==id).first()
    nomepaciente2 = nomepaciente.first_name+" "+nomepaciente.last_name
    form = Formfisio()
    if form.validate_on_submit():
        cadastrofisio = Afisioterapeutas(paciente=nomepaciente2, idpaciente=id, idprofissional=current_user.id,
        username_profissional=form.username_profissional.data, banho=form.banho.data, vestir=form.vestir.data,
        higiene=form.higiene.data, transferencia=form.transferencia.data, continencia=form.continencia.data,
        alimentacao=form.alimentacao.data, niveldor=form.niveldor.data)
        db.session.add(cadastrofisio)
        db.session.commit()
        flash('Dados inseridos com sucesso', 'success')
        return redirect('/dadospacientefisio/'+str(id))
    return render_template('fisioterapia/cadastrafisio.html', Formfisio=form, paciente=nomepaciente2)
    
@app.route('/dadospacientefisio/')
@app.route('/dadospacientefisio/<int:id>', methods=('GET', 'POST'))
@login_required
def dadospacientefisio(id):
    form = SearchForm()
    a = 0
    dadosfisio = Afisioterapeutas.query.filter(Afisioterapeutas.idpaciente==id).order_by(Afisioterapeutas.datareg.desc())
    nomepaciente = Afisioterapeutas.query.filter(Afisioterapeutas.idpaciente==id).first()
    return render_template('fisioterapia/dadospacientefisio.html', fisioterapias=dadosfisio, nome=nomepaciente, SearchForm=form, a=a )


@app.route('/cadastropaciente', methods=('GET', 'POST'))
@login_required
def cadastropaciente():
    form = Formcadastropaciente()
    
    formusuario = form.username.data
    formemail = form.email.data
    formcpf = form.cpf.data
    validausername = User.query.filter(User.username==formusuario).first()
    validaemail = User.query.filter(User.email==formemail).first()
    validacpf = User.query.filter(User.cpf==formcpf).first()
    
    if not form.username.data is None:
        if not form.email.data is None:
            if not form.cpf.data is None:
                if not validausername is None:
                   if validausername.username == form.username.data:
                        flash('Esse nome de usuário já está em uso', 'danger')
                        return render_template('cadastrousuario.html', Formcadastropaciente=form)
                elif not validaemail is None:
                    if validaemail.email == form.email.data:
                        flash('Esse endereço de e-mail já está em uso', 'danger')
                        return render_template('cadastrousuario.html', Formcadastropaciente=form)
                elif not validausernameregex.match(str(formusuario)):
                    flash('O nome de usuário não pode conter caracteres especiais e espaços', 'danger')
                    return render_template('cadastrousuario.html', Formcadastropaciente=form)
                elif not form.password.data == form.confirm.data:
                    flash('As senhas não são iguais')
                    return render_template('cadastrousuario.html', Formcadastropaciente=form)
                elif not validacpf is None:
                    if validacpf.cpf == form.cpf.data:
                        flash('Esse CPF já foi cadastrado', 'danger')
                        return render_template('cadastropaciente.html', Formcadastrofuncionario=form)
                else:    
                    if form.validate_on_submit():
                        password2 = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
                        cadastro = User(username=form.username.data, password=password2, email=form.email.data, active=form.active.data,
                        first_name=form.first_name.data, last_name=form.last_name.data, datanasc=form.datanasc.data, cpf=form.cpf.data)
                        db.session.add(cadastro)
                        db.session.commit()
                        flash('Paciente cadastrado com sucesso', 'success')
                        return redirect("/")
    return render_template('cadastropaciente.html', Formcadastropaciente=form)


@app.route('/cadastrofuncionario', methods=('GET', 'POST'))
@login_required
def cadastrofuncionario():
    form = Formcadastrofuncionario()
    
    formusuario = form.username.data
    formemail = form.email.data
    formcpf = form.cpf.data
    formroles = form.roles.data
    validausername = User.query.filter(User.username==formusuario).first()
    validaemail = User.query.filter(User.email==formemail).first()
    validacpf = User.query.filter(User.cpf==formcpf).first()
    
    if not form.username.data is None:
        if not form.email.data is None:
            if not form.cpf.data is None:
                if not validausername is None:
                    if validausername.username == form.username.data:
                        flash('Esse nome de usuário já está em uso', 'danger')
                        return render_template('cadastrofuncionario.html', Formcadastrofuncionario=form)
                elif not validaemail is None:
                    if validaemail.email == form.email.data:
                        flash('Esse endereço de e-mail já está em uso', 'danger')
                        return render_template('cadastrofuncionario.html', Formcadastrofuncionario=form)
                elif not validausernameregex.match(str(formusuario)):
                    flash('O nome de usuário não pode conter caracteres especiais e espaços', 'danger')
                    return render_template('cadastrofuncionariohtml', Formcadastrofuncionario=form)
                elif not form.password.data == form.confirm.data:
                    flash('As senhas não são iguais', 'danger')
                    return render_template('cadastrofuncionario.html', Formcadastrofuncionario=form)
                elif not validacpf is None:
                    if validacpf.cpf == form.cpf.data:
                        flash('Esse CPF já foi cadastrado', 'danger')
                        return render_template('cadastrofuncionario.html', Formcadastrofuncionario=form)
                else:    
                    if form.validate_on_submit():
                        password2 = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
                        cadastro = User(username=form.username.data, password=password2, email=form.email.data, active=form.active.data,
                        first_name=form.first_name.data, last_name=form.last_name.data, paciente=False, cpf=form.cpf.data)
                        
                        db.session.add(cadastro)
                        db.session.commit()
                        userobj = User.query.filter(User.username==formusuario).first()
                        roleobj = Role.query.filter(Role.name==formroles).first()
                        print (userobj.id, "userobj")
                        print (roleobj.id, "roleobj")
                        if not roleobj is None:
                            funcao = UserRoles(userobj.id, roleobj.id)
                            db.session.add(funcao)
                            db.session.commit()
                            flash('Funcionário cadastrado com sucesso', 'success')
                            return redirect("/")
    return render_template('cadastrofuncionario.html', Formcadastrofuncionario=form)

@app.route('/escoredekatz/')
@login_required
def escoredekatz():
    return render_template('fisioterapia/escoredekatz.html')
    

#formata datas
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)