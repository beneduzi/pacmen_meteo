#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask_wtf import Form
from flask_mail import message
from app import app, mail
from config import admins
from threading import Thread
from app import app

# from wtforms import StringField, BooleanField
# from wtforms.validators import DataRequired

"""
Funçoes preparam o objeto de retorno especifico para cada pagina

"""
#######################################
# Buscas principais


def modelo(model, lat='full', lon='full'):
    success, _out = db_rendler._pull_model_data(
        model.type, model.name, model.member, lat, lon)
    if success == True:
        f_id = []
        f_path = []
        f_name = []
        for val in _out:
            f_id.append(val[0])
            f_path.append(val[1])
            f_name.append(val[2])
        out.nome = f_name
        out.id = f_id
        out.path = f_path
# outras funcoes ou acoes devem ocorrer aqui, como validacao de dominio
        return(success, out)
    elif success == False:
        return(success, f_path='Null', f_id)
    else:
        return(False, f_path='Null', f_id)


def data(_start, _end, lat='full', lon='full'):
    success, _out = db_rendler._pull_date_data(date, lat, lon)
    if success == True:
        f_id = []
        f_path = []
        f_name = []
        for val in _out:
            f_id.append(val[0])
            f_path.append(val[1])
            f_name.append(val[2])
        out.nome = f_name
        out.id = f_id
        out.path = f_path
    elif success == False:
        return(success, out='Null')
    else:
        return(False, out='Null')

#######################################
# Email e contato


def async_email(app, msg):
    """
        Funçao auvxiliar para possibilitar o envio em threads, para agilizar o retorno
    """
    with app.app_context():
        mail.send(msg)


def contato(subject, sender, recipients, text_body, html_body):
    """
        Envia email's para o destinatario, atraves do serviço configurado em config.py
    """
    try:
        msg = Message(subject, sender=sender, recipients=recipients)
        msg.body = text_body
        msg.html = html_body
        thr = Thread(target=async_email, args=[app, msg])
        thr.start()
        return(True)
    except:
        return(False)
#######################################
# Descricoes


def descricao(element='all'):
    if element == "modelo":
        success, out.modelo = db_rendler._get_modelos()
    elif element == "periodo":
        success, out.preriodo = db_rendler._get_periodos()
    elif element == "membros":
        success, out.membro = db_rendler._get_membros()
    elif element == "projetos":
        success, out.projeto = db_rendler._get_projetos()
    elif element == "all":
        success1, out1 = db_rendler._get_modelos()
        success2, out2 = db_rendler._get_periodos()
        success3, out3 = db_rendler._get_membros()
        success4, out4 = db_rendler._get_cenarios()
        if success1 == False or success2 == False or success3 == False or success4 == False:
            success = False
            out = 'Null'
        else:
            success = True
            out.modelo = out1
            out.periodo = out2
            out.membro = out3
            out.projeto = out4
    out.element = element
    return(success, out)
