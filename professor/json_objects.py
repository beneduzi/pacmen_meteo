#!/usr/bin/env python3
import json


def _try(self):
    try:
        return self.__dict__
    except:
        return str(self)


class _latlon:
    '''
    SImple object to store lat lon data before json serialising
    '''

    def __init__(self, out):
        self.lat = out[0]
        self.lon = out[1]
        self.min = [self.lat[0], self.lon[0]]
        self.max = [self.lat[1], self.lon[1]]

    def _max(self):
        self.max = [self.lat[1], self.lon[1]]
        return(self.lat[1], self.lon[1])

    def _min(self):
        self.max = [self.lat[0], self.lon[0]]
        return(self.lat[0], self.lon[0])

    def toJSON(self):
        return json.dumps(self, default=lambda _: _try(_),
                          sort_keys=True, indent=4,
                          separators=(',', ':')).replace('\n', '')


class _list:
    '''
    SImple object to store file lists data for json serialising
    '''

    def __init__(self, out):
        self.name = out[0]
        self.model = out[1]



    def toJSON(self):
        return json.dumps(self, default=lambda _: _try(_),
                          sort_keys=True, indent=4,
                          separators=(',', ':')).replace('\n', '')
