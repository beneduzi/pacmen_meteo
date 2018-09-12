#!/usr/bin/env python3


def _get_aux_DB(_obj):
    DIC = []
    for _ in _obj:
        entry = {
            "id": _[0],
            "Name": _[1],
            "Description": _[2],
        }
        DIC.append(entry)
    return DIC


def _ret_files(_obj):
    DIC = []
    for _ in _obj:
        entry = {
            "id": _[0],
            "File path": _[-1],
        }
        DIC.append(entry)
    return DIC


def _ret_crop(_obj, _path, _la0, _lo0, _la1, _lo1):
    return({
        "id": _obj[0],
        "Original path": _obj[-1],
        "OpenDAP path": _path,
        "latitude 0": _la0,
        "longitude 0": _lo0,
        "latitude 0": _la1,
        "longitude 0": _lo1,
    })


def _ret_crop(_obj, _path):
    return({
        "id": _obj[0],
        "Original path": _obj[-1],
        "OpenDAP path": _path,
    })
