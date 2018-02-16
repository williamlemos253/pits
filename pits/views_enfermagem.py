from pits import app, db
from pits.models import User, UserRoles, Role, Afugulin
from flask import render_template, redirect, url_for, request, flash
from flask_user import login_required
from flask_login import current_user, AnonymousUserMixin
from flask_sqlalchemy import SQLAlchemy
from pits.forms import FugulinForm
from datetime import date, datetime

@app.route('/pacientesenf')
@login_required
def pacientesenf():
    usuarios = User.query.filter(User.paciente==True, User.active==True)
    return render_template('enfermagem/pacientesenf.html', usuarios=usuarios)
    
@app.route('/escaladefugulin/')
@app.route('/escaladefugulin/<int:id>', methods=('GET', 'POST'))
@login_required
def escaladefugulin(id):
    form = FugulinForm()
    nomepaciente = User.query.filter(User.id==id).first()
    nomepaciente2 = nomepaciente.first_name+" "+nomepaciente.last_name
    if form.validate_on_submit():
        soma1 = 0
        soma2 = 0
        soma3 = 0
        soma4 = 0
        somatotal = 0
        
        estadomental = int(form.estadomental.data)
        oxigenacao = int(form.oxigenacao.data)
        sinaisvitais = int(form.sinaisvitais.data)
        motibilidade = int(form.motibilidade.data)
        deambulacao = int(form.deambulacao.data)
        alimentacao = int(form.alimentacao.data)
        cuidadocorporal = int(form.cuidadocorporal.data)
        eliminacao = int(form.eliminacao.data)
        terapeutica = int(form.terapeutica.data)
        
        somatotal = estadomental + oxigenacao + sinaisvitais + motibilidade \
        + deambulacao + alimentacao + cuidadocorporal + eliminacao + terapeutica
        
        #soma1
        if int(estadomental) == 1:
            soma1 = soma1 + 1
        if int(oxigenacao) == 1:
            soma1 = soma1 + 1
        if int(sinaisvitais) == 1:
            soma1 = soma1 + 1
        if int(motibilidade) == 1:
            soma1 = soma1 + 1
        if int(deambulacao) == 1:
            soma1 = soma1 + 1
        if int(alimentacao) == 1:
            soma1 = soma1 + 1
        if int(cuidadocorporal) == 1:
            soma1 = soma1 + 1
        if int(eliminacao) == 1:
            soma1 = soma1 + 1
        if int(terapeutica) == 1:
            soma1 = soma1 + 1
        
        #soma2
        if int(estadomental) == 2:
            soma2 = soma2 + 1
        if int(oxigenacao) == 2:
            soma2 = soma2 + 1
        if int(sinaisvitais) == 2:
            soma2 = soma2 + 1
        if int(motibilidade) == 2:
            soma2 = soma2 + 1
        if int(deambulacao) == 2:
            soma2 = soma2 + 1
        if int(alimentacao) == 2:
            soma2 = soma2 + 1
        if int(cuidadocorporal) == 2:
            soma2 = soma2 + 1
        if int(eliminacao) == 2:
            soma2 = soma2 + 1
        if int(terapeutica) == 2:
            soma2 = soma2 + 1
            
        #soma3
        if int(estadomental) == 3:
            soma3 = soma3 + 1
        if int(oxigenacao) == 3:
            soma3 = soma3 + 1
        if int(sinaisvitais) == 3:
            soma3 = soma3 + 1
        if int(motibilidade) == 3:
            soma3 = soma3 + 1
        if int(deambulacao) == 3:
            soma3 = soma3 + 1
        if int(alimentacao) == 3:
            soma3 = soma3 + 1
        if int(cuidadocorporal) == 3:
            soma3 = soma3 + 1
        if int(eliminacao) == 3:
            soma3 = soma3 + 1
        if int(terapeutica) == 3:
            soma3 = soma3 + 1
            
         #soma4
        if int(estadomental) == 4:
            soma4 = soma4 + 1
        if int(oxigenacao) == 4:
            soma4 = soma4 + 1
        if int(sinaisvitais) == 4:
            soma4 = soma4 + 1
        if int(motibilidade) == 4:
            soma4 = soma4 + 1
        if int(deambulacao) == 4:
            soma4 = soma4 + 1
        if int(alimentacao) == 4:
            soma4 = soma4 + 1
        if int(cuidadocorporal) == 3:
            soma4 = soma4 + 1
        if int(eliminacao) == 4:
            soma4 = soma4 + 1
        if int(terapeutica) == 4:
            soma4 = soma4 + 1
            
        fugulin = Afugulin(idpaciente=id, paciente=nomepaciente2, idprofissional=current_user.id, username_profissional=form.username_profissional.data,
        estadomental=estadomental, oxigenacao=oxigenacao, sinaisvitais=sinaisvitais, motibilidade=motibilidade, deambulacao=deambulacao, alimentacao=alimentacao, 
        cuidadocorporal=cuidadocorporal, eliminacao=eliminacao, terapeutica=terapeutica, soma1=soma1, soma2=soma2, soma3=soma3, soma4=soma4, somatotal=somatotal)    
            
        db.session.add(fugulin)
        db.session.commit()
        flash('Dados de complixidade assistencial cadastrados com sucesso', 'success')
        
        return redirect('/fugulinresultado/'+str(id))
    return render_template('enfermagem/escaladefugulin.html', FugulinForm=form, paciente=nomepaciente2)
    

@app.route('/fugulinresultado/')
@app.route('/fugulinresultado/<int:id>')
@login_required
def fugulinresultado(id):
    fugulin = Afugulin.query.filter(Afugulin.idpaciente==id).order_by(Afugulin.datareg.desc()).first()
    usuario = User.query.filter(User.id==id).first()
    idade = (datetime.today() - usuario.datanasc) / 365
    idade = (str(idade).split()[0])
    return render_template('enfermagem/fugulinresultado.html', resultados=fugulin, idade=idade)
    
@app.route('/fugulinresultadosanteriores/')
@app.route('/fugulinresultadosanteriores/<int:id>')
@login_required
def fugulinresultadosanteriores(id):
    resultado = Afugulin.query.filter(Afugulin.idpaciente==id).order_by(Afugulin.datareg.desc()).all()
    return render_template('enfermagem/fugulinresultadosanteriores.html', resultados=resultado)    
    
@app.route('/fugulinresultado2/')
@app.route('/fugulinresultado2/<int:id>')
@login_required
def fugulinresultado2(id):
    resultado = Afugulin.query.filter(Afugulin.id==id).order_by(Afugulin.datareg.desc()).first()
    idpaciente = resultado.idpaciente
    usuario = User.query.filter(User.id==idpaciente).first()
    idade = (datetime.today() - usuario.datanasc) / 365
    idade = (str(idade).split()[0])
    return render_template('enfermagem/fugulinresultado.html', resultados=resultado, idade=idade)