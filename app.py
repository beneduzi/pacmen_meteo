#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask, request

import json
import datetime
import io
import base64
import gc

import professor.json_function
import chomp.db_rendler


app = Flask(__name__)


@app.route('/models', methods=['GET'])  # , 'POST'])
def get_models():
    suc, ret = chomp.db_rendler._get_modelos()
    ret = professor.json_function._get_aux_DB(ret)
    gc.collect()
    return(app.response_class(response=json.dumps(ret, default=str),
                              status=200, mimetype='application/json'))


@app.route('/models/query', methods=['GET'])  # , 'POST'])
def query_models():
    if request.method == 'GET':
        suc, ret = chomp.db_rendler._pull_model_data(int(request.args.get('id')))
        ret = professor.json_function._ret_files(ret)
    gc.collect()
    return(app.response_class(response=json.dumps(ret, default=str),
                              status=200, mimetype='application/json'))


@app.route('/periods', methods=['GET'])  # , 'POST'])
def get_periods():
    suc, ret = chomp.db_rendler._get_periodos()
    ret = professor.json_function._get_aux_DB(ret)
    gc.collect()
    return(app.response_class(response=json.dumps(ret, default=str),
                              status=200, mimetype='application/json'))


@app.route('/periods/query', methods=['GET'])  # , 'POST'])
def query_periods():
    if request.method == 'GET':
        suc, ret = chomp.db_rendler._pull_period_data(int(request.args.get('id')))
        ret = professor.json_function._ret_files(ret)
    gc.collect()
    return(app.response_class(response=json.dumps(ret, default=str),
                              status=200, mimetype='application/json'))


@app.route('/projects', methods=['GET'])  # , 'POST'])
def get_projects():
    suc, ret = chomp.db_rendler._get_projects()
    ret = professor.json_function._get_aux_DB(ret)
    gc.collect()
    return(app.response_class(response=json.dumps(ret, default=str),
                              status=200, mimetype='application/json'))


@app.route('/projects/query', methods=['GET'])  # , 'POST'])
def query_projects():
    if request.method == 'GET':
        suc, ret = chomp.db_rendler._pull_project_data(int(request.args.get('id')))
        ret = professor.json_function._ret_files(ret)
    gc.collect()
    return(app.response_class(response=json.dumps(ret, default=str),
                              status=200, mimetype='application/json'))


@app.route('/members', methods=['GET'])  # , 'POST'])
def get_mmembers():
    suc, ret = chomp.db_rendler._get_membros()
    ret = professor.json_function._get_aux_DB(ret)
    gc.collect()
    return(app.response_class(response=json.dumps(ret, default=str),
                              status=200, mimetype='application/json'))


@app.route('/members/query', methods=['GET'])  # , 'POST'])
def query_members():
    if request.method == 'GET':
        suc, ret = chomp.db_rendler._pull_member_data(int(request.args.get('id')))
        ret = professor.json_function._ret_files(ret)
    gc.collect()
    return(app.response_class(response=json.dumps(ret, default=str),
                              status=200, mimetype='application/json'))


@app.route('/date/query', methods=['GET'])  # , 'POST'])
def query_date():
    if request.method == 'GET':
        _dateI = datetime.datetime.strptime(
            str(request.args.get('initi_date')), '%Y-%m-%d')   # iso date or NOT
        _dateF = datetime.datetime.strptime(
            str(request.args.get('final_date')), '%Y-%m-%d')
        suc, ret = chomp.db_rendler._pull_date_data(_dateI, _dateF)
        ret = professor.json_function._ret_files(ret)
    gc.collect()
    return(app.response_class(response=json.dumps(ret, default=str),
                              status=200, mimetype='application/json'))


@app.route('/coords/query', methods=['GET'])  # , 'POST'])
def query_coords():
    if request.method == 'GET':
        _lat = float((request.args.get('latitude')))
        _lon = float((request.args.get('longitude')))
        suc, ret = chomp.db_rendler._get_lat_lon(_lat, _lon)
        if ret[0]:
            suc, ret = chomp.db_rendler._pull_lat_lon_data(ret[1], ret[2])
            ret = professor.json_function._ret_files(ret)
    gc.collect()
    return(app.response_class(response=json.dumps(ret, default=str),
                              status=200, mimetype='application/json'))


@app.route('/file/preview', methods=['GET'])  # , 'POST'])
def preview():
    import professor.nc_ploter
    if request.method == 'GET':
        is_valid, suc, ret = chomp.db_rendler._pull_file(
            int(request.args.get('id')))
        if is_valid:
            nc_vars, nc_file = professor.nc_vars(ret)
            img_bufer = []
            for var in nc_vars:
                img = io.BytesIO()
                data = nc_file.variables[var]
                is_plot = professor.nc_ploter.gen_map_plot(img, data)
                if is_plot:
                    img_bufer.append(img.seek(0))
        out_str = []
        for ib in img_bufer:
            out_str.append('<img src= "data:image/png;base64,%s">' %
                           (base64.b64encode(ib.getvalue(0)).decode()))
    gc.collect()
    return(app.response_class(response=out_str,
                              status=200, mimetype='text/html'))


@app.route('/file/cut', methods=['GET'])  # , 'POST'])
def cutter():
    uniq = base64.b64encode(os.urandom(16)).decode('utf-8')
    import professor.nc_croper
    if request.method == 'GET':
        _lat0 = float((request.args.get('latitude0')))
        _lon0 = float((request.args.get('longitude0')))
        _lat1 = float((request.args.get('latitude1')))
        _lon1 = float((request.args.get('longitude1')))
        is_valid, suc, ret = chomp.db_rendler._pull_file(
            int(request.args.get('id')))
        if is_valid:
            out_path = '/path/to/opendap/' + \
                (ret.split('/')[-1]).split('.')[-2] + '_' + uniq + '_.nc'
            is_nc = professor.nc_croper.crop_nc(
                ret, out_path, lat0, lon0, lat1, lon1)
            if is_nc:
                ret = professor.json_function._ret_crop(
                    ret, out_path, lat0, lon0, lat1, lon1)
    gc.collect()
    return(app.response_class(response=json.dumps(ret, default=str),
                              status=200, mimetype='application/json'))


@app.route('/file/transfer', methods=['GET'])  # , 'POST'])
def transfer():
    from shutil import copyfile
    uniq = base64.b64encode(os.urandom(16)).decode('utf-8')
    if request.method == 'GET':
        is_valid, suc, ret = chomp.db_rendler._pull_file(
            int(request.args.get('id')))
        if is_valid:
            out_path = '/path/to/opendap/' + \
                (ret.split('/')[-1]).split('.')[-2] + '_' + uniq + '_.nc'
            copyfile(ret, out_path)
            ret = professor.json_function._ret_tramsfer(ret, out_path)
    gc.collect()
    return(app.response_class(response=json.dumps(ret, default=str),
                              status=200, mimetype='application/json'))


@app.route('/opendap')  # Need tp be validated
def opendap():
    return redirect("0.0.0.0:8080", code=302)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        processes=4,
        threaded=False,
        use_reloader=True,)
