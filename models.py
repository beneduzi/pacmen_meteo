#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask_wtf import Form
from flask_mail import message
from app import app, mail
from config import admins
# from wtforms import StringField, BooleanField
# from wtforms.validators import DataRequired

"""
Funçoes preparam o objeto de retorno especifico para cada pagina

"""
def modelo():

def data():

def contato():
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.body = text_body
	msg.html = html_body
	mail.send(msg)