#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
This script is only place holding prototype endpoint functions
"""

@app.route('/')
def render_index():
    """
    Renderiza o index, quando o endpoint for o diretorio raiz
    """
    out = datetime.datetime.now()
    return render_template('template/index.html', out=out)


@app.route("/historia")
def render_historia():
    """
    renderiza a pagina de historia do projeto
    """
    return render_template('template/historia.html')


@app.route("/descricao")
def render_descricao():
    """
    renderiza a descricao dos elementos
    """
    return render_template('template/descricao.html')


@app.route("/contato")
def render_contato():
    """
    renderiza o form de contato
    """
    return render_template('template/contato.html')


@app.route("/header")
def render_header():
    """
    renderiza o header
    """
    return render_template('template/header.html')


@app.route("/footer")
def render_header():
    """
    renderiza o footer
    """
    return render_template('template/footer.html')
