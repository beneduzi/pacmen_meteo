#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Flask
from pydap.wsgi.app import DapServer

application = DapServer('/root/moonshot_api/')

app = Flask(__name__)
opendap = DapServer('/path/to/opendap')
app.wsgi_app = opendap
app.run(host='0.0.0.0',
        port=80,
        debug=False,
        processes=4,
        threaded=False,
        use_reloader=True,)



