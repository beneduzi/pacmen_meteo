#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb

#######################################
# Buscas na tabela final


def _pull_model_data(_model):
    '''
    Each function recoveries entries with especifc characteristics or Null
    '''
    try:
        db = MySQLdb.connect("localhost", "root", "&i1hm", "pacmen_db")
        cursor = db.cursor()
        query = 'SELECT f_id, f_path FROM dados_tb WHERE modelo=%s' % (_model)
        cursor.execute(query)
        output = cursor.fetchall()
        # db.commit()
        db.close()
        return (True, output)
    except:
        return (False, "Null")


def _pull_period_data(_period):
    try:
        db = MySQLdb.connect("localhost", "root", "&i1hm", "pacmen_db")
        cursor = db.cursor()
        query = 'SELECT f_id, f_path FROM dados_tb WHERE periodo=%s' % (
            _period)
        cursor.execute(query)
        output = cursor.fetchall()
        # db.commit()
        db.close()
        return (True, output)
    except:
        return (False, "Null")


def _pull_member_data(_member):
    try:
        db = MySQLdb.connect("localhost", "root", "&i1hm", "pacmen_db")
        cursor = db.cursor()
        query = 'SELECT f_id, f_path FROM dados_tb WHERE membro=%s' % (_member)
        cursor.execute(query)
        output = cursor.fetchall()
        # db.commit()
        db.close()
        return (True, output)
    except:
        return (False, "Null")


def _pull_project_data(_project):
    try:
        db = MySQLdb.connect("localhost", "root", "&i1hm", "pacmen_db")
        cursor = db.cursor()
        query = 'SELECT f_id, f_path FROM dados_tb WHERE projeto=%s' % (
            _project)
        cursor.execute(query)
        output = cursor.fetchall()
        # db.commit()
        db.close()
        return (True, output)
    except:
        return (False, "Null")


def _pull_lat_lon_data(_lat, _lon):
    try:
        db = MySQLdb.connect("localhost", "root", "&i1hm", "pacmen_db")
        cursor = db.cursor()
        query = 'SELECT f_id, f_path FROM dados_tb WHERE latitude=%s AND longitude=%s' % (
            _lat, _lon)
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


def _pull_file(_f_id):
    try:
        db = MySQLdb.connect("localhost", "root", "&i1hm", "pacmen_db")
        cursor = db.cursor()
        query = 'SELECT f_path FROM dados_tb WHERE f_id=%i' % (_f_id)
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
        query = 'SELECT id, name, pt_desc FROM modelos_tb'
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
        query = 'SELECT id, name, pt_desc FROM periodos_tb'
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
        query = 'SELECT id, name, pt_desc FROM membros_tb'
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
        query = 'SELECT id, name, pt_desc FROM projetos_tb'
        cursor.execute(query)
        output = cursor.fetchall()
        # db.commit()
        db.close()
        return (True, output)
    except:
        return (False, "Null")

def _get_lat_lon(_lat, _lon):
    try:
        db = MySQLdb.connect("localhost","root","&i1hm","pacmen_db" )
        cursor = db.cursor()
        query = 'SELECT id FROM latitudes_tb WHERE max < %f AND min > %f' %(_lat, _lat)
        cursor.execute(query)
        output1 = cursor.fetchall()
        # db.commit()
        query = 'SELECT id FROM longitudes_tb WHERE max < %f AND min > %f' %(_lon, _lon)
        cursor.execute(query)
        output2 = cursor.fetchall()
        db.close()
        return (True, [output1, output2])
    except:
        return (False, "Null")

#######################################
def _push_file(_file_path, _temp_path):
    try:
        db = MySQLdb.connect("localhost","root","&i1hm","pacmen_db" )
        cursor = db.cursor()
        query = '' #Query to insert into a new table date of creation, shelf life, file path
        cursor.execute(query)
        output = cursor.fetchall()
        db.close()
        return (True, output)
    except:
        return (False, "Null")
    