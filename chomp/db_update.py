#!/usr/bin/env python3
import argparse
import os
import MySQLdb
import netCDF4
import datetime
import numpy as np
import fnmatch


class element_model(object):

    def __init__(self):
        self.file = []
        self.model = []
        self.period = []
        self.project = []
        self.member = []
        self.latitude = []
        self.longitude = []
        self.cre_date = []
        self.sim_date = []


def create_model(modelo, cursor):
    insert_query = 'INSERT INTO modelos_tb (name) VALUES ("%s")' % (modelo)
    cursor.execute(insert_query)
    cursor.fetchall()


def create_member(membro, cursor):
    insert_query = 'INSERT INTO membros_tb (name) VALUES ("%s")' % (membro)
    cursor.execute(insert_query)
    cursor.fetchall()


def create_period(periodo, cursor):
    insert_query = 'INSERT INTO periodos_tb (name) VALUES ("%s")' % (periodo)
    cursor.execute(insert_query)
    cursor.fetchall()


def create_project(projeto, cursor):
    insert_query = 'INSERT INTO projetos_tb (name) VALUES ("%s")' % (projeto)
    cursor.execute(insert_query)
    cursor.fetchall()


def create_lat(lat, cursor):
    insert_query = 'INSERT INTO latitudes_tb (max, min) VALUES ("%s", "%s")' % (lat[
        0], lat[1])
    cursor.execute(insert_query)
    cursor.fetchall()


def create_lon(lon, cursor):
    insert_query = 'INSERT INTO longitudes_tb (max, min) VALUES ("%s", "%s")' % (lon[
        0], lon[1])
    cursor.execute(insert_query)
    cursor.fetchall()


def create_create_dates(create_date, cursor):
    insert_query = 'INSERT INTO create_date_tb (name) VALUES ("%s")' % (
        create_date)
    cursor.execute(insert_query)
    cursor.fetchall()


def create_simulation_dates(simul_date, cursor):
    insert_query = 'INSERT INTO simulation_date_tb (start, steps, description) VALUES ("%s", "%s", "%s")' % (
        simul_date[0], simul_date[1], simul_date[2])
    cursor.execute(insert_query)
    cursor.fetchall()


def _push_model_data(nome, modelo, membro, periodo, projeto, lat, lon, criacao, datas):
    db = MySQLdb.connect("localhost", "root", "a", "pacmen_db")
    cursor = db.cursor()

    query_model = 'SELECT id FROM modelos_tb WHERE name="%s"' % (modelo)
    cursor.execute(query_model)
    id_model = cursor.fetchall()
    if id_model == ():
        create_model(modelo, cursor)
        query_model = 'SELECT id FROM modelos_tb  WHERE modelos_tb.name= "%s"' % (
            modelo)
        cursor.execute(query_model)
        id_model = cursor.fetchall()[0][0]

    query_member = 'SELECT id FROM membros_tb  WHERE name= "%s"' % (membro)
    cursor.execute(query_member)
    id_member = cursor.fetchall()
    if id_member == ():
        create_member(membro, cursor)
        query_member = 'SELECT id FROM membros_tb  WHERE name= "%s"' % (membro)
        cursor.execute(query_member)
        id_member = cursor.fetchall()

    query_period = 'SELECT id FROM periodos_tb WHERE name= "%s"' % (periodo)
    cursor.execute(query_period)
    id_period = cursor.fetchall()
    if id_period == ():
        create_period(periodo, cursor)
        query_period = 'SELECT id FROM periodos_tb  WHERE name= "%s"' % (
            periodo)
        cursor.execute(query_period)
        id_period = cursor.fetchall()

    query_project = 'SELECT id FROM projetos_tb WHERE name= "%s"' % (projeto)
    cursor.execute(query_project)
    id_project = cursor.fetchall()
    if id_project == ():
        create_project(projeto, cursor)
        query_project = 'SELECT id FROM projetos_tb  WHERE name= "%s"' % (
            projeto)
        cursor.execute(query_project)
        id_project = cursor.fetchall()

    query_latitude = 'SELECT id FROM latitudes_tb WHERE max="%s" and min="%s"' % (lat[
                                                                                  0], lat[1])
    cursor.execute(query_latitude)
    id_latitude = cursor.fetchall()
    if id_latitude == ():
        create_lat(lat, cursor)
        cursor.execute(query_latitude)
        id_latitude = cursor.fetchall()

    query_longitude = 'SELECT id FROM longitudes_tb WHERE max="%s" and min="%s"' % (lon[
                                                                                    0], lon[1])
    cursor.execute(query_longitude)
    id_longitude = cursor.fetchall()
    if id_longitude == ():
        create_lon(lon, cursor)
        cursor.execute(query_longitude)
        id_longitude = cursor.fetchall()

    query_creation = 'SELECT id FROM create_date_tb WHERE name="%s"' % (
        criacao)
    cursor.execute(query_creation)
    id_creation = cursor.fetchall()
    if id_creation == ():
        create_create_dates(criacao, cursor)
        cursor.execute(query_creation)
        id_creation = cursor.fetchall()

    query_simulation = 'SELECT id FROM simulation_date_tb WHERE start="%s" \
        and steps="%s" and description="%s"' % (datas[0], datas[1], datas[2])
    cursor.execute(query_simulation)
    id_simulation = cursor.fetchall()
    if id_simulation == ():
        create_simulation_dates(datas, cursor)
        cursor.execute(query_simulation)
        id_simulation = cursor.fetchall()
    db.commit()

    verify_query = 'SELECT id FROM dados_tb WHERE name="%s"' % (nome)
    cursor.execute(verify_query)
    is_in = cursor.fetchall()
    if is_in == ():
        insert_query = 'INSERT INTO dados_tb (name, periodo,  membro, modelo, projeto,\
                                              lat, lon, creation_date, simulation_date)\
                        VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' \
                        % (nome, id_period[0][0],  id_member[0][0], id_model[0][0], id_project[0][0],
                           id_latitude[0][0], id_longitude[0][0], id_creation[0][0], id_simulation[0][0])

        print(insert_query)
        cursor.execute(insert_query, cursor)
        cursor.fetchall()
        db.commit()
        db.close()
        return (True)
    else:
        db.close()
        return (False)

# Arg parser
parser = argparse.ArgumentParser(
    description="This script insert NetCDF4 files on the database")
parser.add_argument('-n', help="Imput NetCDF4 file",
                    action='store', required=True, dest='nc_path')
args = parser.parse_args()
sublist = os.listdir(args.nc_path)
files = [val for sublist in [[os.path.join(i[0], j)
                              for j in i[2]] for i in os.walk('./')] for val in sublist]
files = [f for f in files if fnmatch.fnmatch(f, '*.nc')]
out = element_model()

for file_path in files:
    file = file_path.split('/')[-1]
    model = file_path.split('/')[-2]
    period = file_path.split('/')[-3]
    member = file_path.split('/')[-4]
    project = file_path.split('/')[-5]

    out.file.append(file)
    out.model.append(model)
    out.period.append(period)
    out.member.append(member)
    out.project.append(project)
    try:
        nc_file = netCDF4.Dataset(file_path, 'r')
        valid_nc = True
    except:
        valid_nc = False
    if valid_nc == True:
        out.cre_date.append(nc_file.creation_date)
        out.latitude.append([np.amin(nc_file['lat'][:]),
                             np.amax(nc_file['lat'][:])])

        out.longitude.append([(np.amin(nc_file['lon']) if np.amin(nc_file['lon']) >= 0
                               else (360 + np.amin(nc_file['lon']))),
                              (np.amax(nc_file['lon']) if np.amax(nc_file['lon']) >= 0
                               else (360 + np.amax(nc_file['lon'])))])

        out.sim_date.append([nc_file['time'].units.split(
            ' ')[-2], nc_file['time'][-1], nc_file['time'].units])
    else:
        del out.file[-1]
        del out.model[-1]
        del out.period[-1]
        del out.member[-1]
        del out.project[-1]
num_new_files = 0
for i in range(0, len(out.file)):
    try:
        inserted = _push_model_data(out.file[i], out.model[i], out.member[i],
                                    out.period[i], out.project[
                                        i], out.latitude[i],
                                    out.longitude[i], out.cre_date[i], out.sim_date[i])
    except:
        inserted = 'Erro'
    if inserted == True:
        num_new_files += 1
    elif inserted == 'Erro':
        print("Erro ao inserir o arquivo: %s" % (out.file[i].split('/')[-1]))

print("Total de arquivos: %s" % (len(out.file)))
print("Novos: %s" % (num_new_files))
