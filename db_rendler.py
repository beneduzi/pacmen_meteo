#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb

#######################################
##Buscas na tabela final
def _pull_model_data(tipo='*', nome='*', membro='*', lat, lon):
	try:
		db = MySQLdb.connect("localhost","root","&i1hm","pacmen_db" )
		cursor = db.cursor()
		query = 'SELECT f_id, f_path FROM dados_tb WHERE tipo=%s AND nome=%s AND membro=%s' %(tipo, nome, membro)
		cursor.execute(query)
		output = cursor.fetchall()
		# db.commit()
		db.close()
		return (True, output)
	except:
		return (False, "Null")

def _pull_date_data(_start='*', _end='*', lat, lon):
	try:
		db = MySQLdb.connect("localhost","root","&i1hm","pacmen_db" )
		cursor = db.cursor()
		query = 'SELECT f_id, f_path FROM dados_tb WHERE s_date=%s AND e_date=%s '%(_start, _end)
		cursor.execute(query)
		output = cursor.fetchall()
		# db.commit()
		db.close()
		return (True, output)
	except:
		return (False, "Null")

#######################################
##Buscas nas tabelas primarias
def _get_modelos():
	try:
		db = MySQLdb.connect("localhost","root","&i1hm","pacmen_db" )
		cursor = db.cursor()
		query = 'SELECT name, pt_desc FROM modelos_tb'
		cursor.execute(query)
		output = cursor.fetchall()
		# db.commit()
		db.close()
		return (True, output)
	except:
		return (False, "Null")

def _get_periodos():
	try:
		db = MySQLdb.connect("localhost","root","&i1hm","pacmen_db" )
		cursor = db.cursor()
		query = 'SELECT name, pt_desc FROM periodos_tb'
		cursor.execute(query)
		output = cursor.fetchall()
		# db.commit()
		db.close()
		return (True, output)
	except:
		return (False, "Null")

def _get_membros():
	try:
		db = MySQLdb.connect("localhost","root","&i1hm","pacmen_db" )
		cursor = db.cursor()
		query = 'SELECT name, pt_desc FROM membros_tb'
		cursor.execute(query)
		output = cursor.fetchall()
		# db.commit()
		db.close()
		return (True, output)
	except:
		return (False, "Null")

def _get_cenarios():
	try:
		db = MySQLdb.connect("localhost","root","&i1hm","pacmen_db" )
		cursor = db.cursor()
		query = 'SELECT name, pt_desc FROM cenarios_tb'
		cursor.execute(query)
		output = cursor.fetchall()
		# db.commit()
		db.close()
		return (True, output)
	except:
		return (False, "Null")

#######################################
