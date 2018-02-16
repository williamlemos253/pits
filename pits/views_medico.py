from pits import app, db
from pits.models import User, UserRoles, Role, Acirsg
from flask import render_template, redirect, url_for, request, flash
from flask_user import login_required
from flask_login import current_user, AnonymousUserMixin
from flask_sqlalchemy import SQLAlchemy
from pits.forms import SearchForm, CirsgForm
from datetime import date, datetime


@app.route('/pacientesmedico')
@login_required
def pacientesmedico():
    form = SearchForm()
    usuarios = User.query.filter(User.paciente==True, User.active==True)
    if form.validate_on_submit():
        return redirect('/pacientesfisio2')
    return render_template('medicina/pacientesmedico.html', usuarios=usuarios, SearchForm=form)
    
@app.route('/cirsg')
@app.route('/cirsg/<int:id>', methods=('GET', 'POST'))
@login_required
def cirsg(id):
    form = CirsgForm()
    nomepaciente = User.query.filter(User.id==id).first()
    nomepaciente2 = nomepaciente.first_name+" "+nomepaciente.last_name
    
    if form.validate_on_submit():
        a1=int(form.coracao.data) 
        a2=int(form.vascular.data) 
        a3=int(form.hematopoietico.data) 
        a4=int(form.respiratorio.data) 
        a5=int(form.otorrino.data) 
        a6=int(form.gastrointestinalsup.data) 
        a7=int(form.gastrointestinalinf.data) 
        a8=int(form.figado.data) 
        a9=int(form.renal.data) 
        a10=int(form.genitourinario.data) 
        a11=int(form.musculosqueletico.data)  
        a12=int(form.neurologico.data)
        a13=int(form.endocrino.data)
        a14=int(form.psiquiatrica.data)
        somapontuacao = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a11 + a12 + a13 + a14
        contadorcatclass = 0
        contnumcatsev3 = 0
        contnumcatsev4 = 0
        if int(form.coracao.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        if int(form.vascular.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        if int(form.hematopoietico.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        if int(form.respiratorio.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        if int(form.otorrino.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        if int(form.gastrointestinalsup.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        if int(form.gastrointestinalinf.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        if int(form.figado.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        if int(form.renal.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        if int(form.genitourinario.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        if int(form.musculosqueletico.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        if int(form.neurologico.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        if int(form.endocrino.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        if int(form.psiquiatrica.data) >= 1:
            contadorcatclass = contadorcatclass + 1
        
        calculaindgravidade = somapontuacao / contadorcatclass
        
        if int(form.coracao.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
        if int(form.vascular.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
        if int(form.hematopoietico.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
        if int(form.respiratorio.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
        if int(form.otorrino.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
        if int(form.gastrointestinalsup.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
        if int(form.gastrointestinalinf.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
        if int(form.figado.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
        if int(form.renal.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
        if int(form.genitourinario.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
        if int(form.musculosqueletico.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
        if int(form.neurologico.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
        if int(form.endocrino.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
        if int(form.psiquiatrica.data) == 3:
            contnumcatsev3 = contnumcatsev3 + 1
            
        if int(form.coracao.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
        if int(form.vascular.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
        if int(form.hematopoietico.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
        if int(form.respiratorio.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
        if int(form.otorrino.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
        if int(form.gastrointestinalsup.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
        if int(form.gastrointestinalinf.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
        if int(form.figado.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
        if int(form.renal.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
        if int(form.genitourinario.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
        if int(form.musculosqueletico.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
        if int(form.neurologico.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
        if int(form.endocrino.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
        if int(form.psiquiatrica.data) == 4:
            contnumcatsev4 = contnumcatsev4 + 1
    
        dadocirsg = Acirsg(idpaciente=id, paciente=nomepaciente2, idprofissional=current_user.id, username_profissional=form.username_profissional.data, coracao=form.coracao.data,
        vascular=form.vascular.data, hematopoietico=form.hematopoietico.data, respiratorio=form.respiratorio.data, otorrino=form.otorrino.data,
        gastrointestinalsup=form.gastrointestinalsup.data, gastrointestinalinf=form.gastrointestinalinf.data,
        figado=form.figado.data, renal=form.renal.data, genitourinario=form.genitourinario.data,
        musculosqueletico=form.musculosqueletico.data, neurologico=form.neurologico.data,
        endocrino=form.endocrino.data, psiquiatrica=form.psiquiatrica.data, numcatclass=contadorcatclass,
        pontuacao=somapontuacao, indgravidade= round(calculaindgravidade,2), numcatsev3=contnumcatsev3,
        numcatsev4=contnumcatsev4)
        
        db.session.add(dadocirsg)
        db.session.commit()
        flash('Dados do CIRS-G cadastrados com sucesso', 'success')
        return redirect("/cirsgresultado/"+str(id))
        
    return render_template('medicina/cirsg.html', CirsgForm=form, paciente=nomepaciente2)

@app.route('/cirsgajuda')
@login_required
def cirsgajuda():
    return render_template('medicina/cirsgajuda.html')
    
    
@app.route('/cirsgresultado/')
@app.route('/cirsgresultado/<int:id>')
@login_required
def cirsgresultado(id):
    usuario = User.query.filter(User.id==id).first()
    idade = (datetime.today() - usuario.datanasc) / 365
    idade = (str(idade).split()[0])
    resultado = Acirsg.query.filter(Acirsg.idpaciente==id).order_by(Acirsg.datareg.desc()).first()
    return render_template('medicina/cirsgresultado.html', resultados=resultado, idade=idade)
    
    
@app.route('/cirsgresultadosanteriores/')
@app.route('/cirsgresultadosanteriores/<int:id>')
@login_required
def cirsgresultadosanteriores(id):
    resultado = Acirsg.query.filter(Acirsg.idpaciente==id).order_by(Acirsg.datareg.desc()).all()
    return render_template('medicina/cirsgresultadosanteriores.html', resultados=resultado)
    
    
@app.route('/cirsgresultado2/')
@app.route('/cirsgresultado2/<int:id>')
@login_required
def cirsgresultado2(id):
    resultado = Acirsg.query.filter(Acirsg.id==id).order_by(Acirsg.datareg.desc()).first()
    idpaciente = resultado.idpaciente
    print (idpaciente, "ta aqui o id")
    usuario = User.query.filter(User.id==idpaciente).first()
    idade = (datetime.today() - usuario.datanasc) / 365
    idade = (str(idade).split()[0])
    return render_template('medicina/cirsgresultado.html', resultados=resultado, idade=idade)