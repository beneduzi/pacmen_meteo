#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask, request
import json

import professor.login
import professor.models
import professor.views
import chomp.db_rendler


app = Flask(__name__)


@app.route('/models', methods=['GET', 'POST'])
def get_models():
    if request.method == 'POST':
        data = request.json
        lat = [float(l['latitude']) for l in data['points']]
        lon = [float(l['longitude']) for l in data['points']]
        var = data['variables']

    elif request.method == 'GET':
        lat = [float(request.args.get('latitude'))]
        lon = [float(request.args.get('longitude'))]
        var = [request.args.get('variables')]
    DIC = chomp.db_rendler.clima(lat, lon, var)
    OUT = professor.models(DIC)
    RESPONSE = professor.views(OUT)
    response = professor.app.response_class(response=json.dumps(
        RESPONSE, default=str), status=200, mimetype='application/json')
    return response
