#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import flash, redirect, render_template, request, url_for
# from .forms import LoginForm
from app import app

import os
import datetime

#######################################
import parse_form
import model
# import login
#######################################
# Paginas estaticas


@app.route('/')
def render_index():
    """
    Renderiza o index, quando o endpoint for o diretorio raiz
    """
    out = datetime.datetime.now()
    return render_template('index.html', out=out)


@app.route("/hist")
def render_historia():
    """
    renderiza a pagina de historia do projeto
    """
    return render_template('historia.html')


@app.route("/desc")
def render_descricao():
    """
    renderiza a descricao dos elementos
    """
    return render_template('descricao.html')


@app.route("/cont")
def render_contato():
    """
    renderiza o form de contato
    """
    return render_template('contato.html')


@app.route("/busca/model")
def search_model():
    """
    renderiza os forms de busca por modelo
    """
    return render_template('busca_modelo.html')


@app.route("/busca/data")
def search_data():
    """
    renderiza os forms de busca por data
    """
    return render_template('busca_data.html')

#######################################
# Forms


@app.route("/form/cont", methods=['GET', 'POST'])
def recv_contato
    """
    endpoint para o form de contato 
    """
    select = request.form.get_dict(
        'FORM___NAME____')  # recebe os dados do form, precisa de nome e valor no html
    out = parse_form.contato(select)
    success = model.contato(out[])
    if success == True:
        return render_template('email_sended.html')
    else:
        return render_template('email_fail.html')


@app.route("/form/model", methods=['GET', 'POST'])
def recv_modelo():
    """
    endpoint para o form de busca por modelo
    """
    select = request.form.get_dict('comp_select')  # recebe os dados do select
    out = parse_form.modelo(select)
    success, out = model.modelo(out[])
    if success == True:
        return render_template('file_list.html', _path_=out.path, _id_=out.id, _nome_=out.nome)
    else:
        return render_template('file_fail.html')


@app.route("/form/data", methods=['GET', 'POST']):
def recv_data():
    """
    endpoint para o form de busca por data
    """
    select = request.form.get_dict('comp_select')  # recebe os dados do select
    out = parse_form.data(select)
    success, out = model.data(out[])
    if success == True:
        return render_template('file_list.html', _path_=out.path, _id_=out.id, _nome_=out.nome)
    else:
        return render_template('file_fail.html')
#######################################
# Descricoes dos elementos


@app.route("/desc/model")
def des_modelos():
    success, out = model.descricao("modelo")
    if success == True:
        return render_template('desc_element.html', out=out)
    else:
        return render_template('desc_fail.html')


@app.route("/desc/projetos")
def des_projetos():
    success, out = model.descricao("projetos")
    if success == True:
        return render_template('desc_element.html', out=out)
    else:
        return render_template('desc_fail.html')


@app.route("/desc/membros")
def desc_membros():
    success, out = model.descricao("membros")
    if success == True:
        return render_template('desc_element.html', out=out)
    else:
        return render_template('desc_fail.html')


@app.route("/desc/periodos")
def desc_periodos():
    success, out = model.descricao("periodo")
    if success == True:
        return render_template('desc_element.html', out=out)
    else:
        return render_template('desc_fail.html')


@app.route("/desc/all")
def desc_all():
    success, out = model.descricao()
    if success == True:
        return render_template('desc_element.html', out=out)
    else:
        return render_template('desc_fail.html')


# @app.route('/form/login', methods=['GET', 'POST'])
# def login():
#     out = login.LoginForm()
#     if form.validate_on_submit():
#         # flash('Login requested for OpenID="%s", remember_me=%s' %
#         #       (form.openid.data, str(form.remember_me.data)))
#         return redirect('/index')
#     return render_template('login.html', form=out)

# #######################################
# ## Execucao
# if __name__=='__main__':
#   app.run(debug=True)
