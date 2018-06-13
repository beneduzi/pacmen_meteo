#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb

#######################################
# Buscas na tabela final


def _pull_model_data(tipo='*', nome='*', membro='*'):
    '''
    Each function recoveries entries with especifc characteristics or Null
    '''
    try:
        db = MySQLdb.connect("localhost", "root", "&i1hm", "pacmen_db")
        cursor = db.cursor()
        query = 'SELECT f_id, f_path FROM dados_tb WHERE tipo=%s AND nome=%s AND membro=%s' % (
            tipo, nome, membro)
        cursor.execute(query)
        output = cursor.fetchall()
        # db.commit()
        db.close()
        return (True, output)
    except:
        return (False, "Null")


def _pull_date_data(_start='*', _end='*'):
    try:
        db = MySQLdb.connect("localhost", "root", "&i1hm", "pacmen_db")
        cursor = db.cursor()
        query = 'SELECT f_id, f_path FROM dados_tb WHERE s_date=%s AND e_date=%s ' % (
            _start, _end)
        cursor.execute(query)
        output = cursor.fetchall()
        # db.commit()
        db.close()
        return (True, output)
    except:
        return (False, "Null")

#######################################
# Buscas nas tabelas primarias


def _get_modelos():
    '''
    Each function returns every element in the respective table or Null(control flow)
    '''
   try:
        db = MySQLdb.connect("localhost", "root", "&i1hm", "pacmen_db")
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

def _get_projetos():
    try:
        db = MySQLdb.connect("localhost","root","&i1hm","pacmen_db" )
        cursor = db.cursor()
        query = 'SELECT name, pt_desc FROM projetos_tb'
        cursor.execute(query)
        output = cursor.fetchall()
        # db.commit()
        db.close()
        return (True, output)
    except:
        return (False, "Null")

def _get_lat_lon():
    try:
        db = MySQLdb.connect("localhost","root","&i1hm","pacmen_db" )
        cursor = db.cursor()
        query = 'SELECT min, max FROM latitudes_tb'
        cursor.execute(query)
        output1 = cursor.fetchall()
        # db.commit()
        query = 'SELECT min, max FROM longitudes_tb'
        cursor.execute(query)
        output2 = cursor.fetchall()
        db.close()
        return (True, [output1, output2])
    except:
        return (False, "Null")

#######################################
