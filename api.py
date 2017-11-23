#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask, flash, redirect, render_template, \
     request, url_for
import os

import parse_form
import 

app = Flask(__name__)

@app.route('/')
def index():
	"""
	Renderiza o index, quando o endpoint for o diretorio raiz
	"""
	out = 
    return render_template('index.html', out)

@app.route("/lista")
def lista():
	"""
	renderiza os forms da pagina lista
	"""
	out =
    return render_template('list.html', out)

@app.route("/modglob")
def modglob():
	"""
	renderiza os forms da pagina de modelos globais
	"""
	out =
    return render_template('modglob.html', out)

@app.route("/lista/l_form" , methods=['GET', 'POST'])
def l_form():
	"""
	endpoind para o form das listas
	"""
    select = request.form.get('comp_select')  #recebe os dados do select
    out =
    return render_template('file_list.html', out)

@app.route("/modglog/m_form" , methods=['GET', 'POST'])
def m_form():
	"""
	endpoint para o form dos modelos globais 
	"""
    select = request.form.get('comp_select') #recebe os dados do select
    out =
    return render_template('file_list.html', out) 

if __name__=='__main__':
    app.run(debug=True)