#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask, flash, redirect, render_template, request, url_for
import json
import os

import parse_form
import professor.json_objects as j_obj

app = Flask(__name__)


@app.route('/')
def index():
	"""
	Renderiza o index, quando o endpoint for o diretorio raiz
	"""
	out =
    return render_template('index.html', out)

@app.route("/lista/latlon/")
def list_lat_lon():
	"""
	return a list of all know domains limits
	"""
	if request.method == 'GET':
		out = db_rendler._get_lat_lon
		obj = []
		for o in out:
		    obj.append(j_obj._latlon(o).toJSON())
    RESPONSE = j_obj._response(obj)
    response = app.response_class(response=json.dumps(
        RESPONSE, default=str), status=200, mimetype='application/json')
    return response  


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
    app.run(host='0.0.0.0', port=8085, debug=False, threaded=False, processes=2, use_reloader=True)

