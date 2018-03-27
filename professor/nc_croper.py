#!/usr/bin/env python3

from netCDF4 import Dataset
import os
import numpy as np
import datetime
import argparse


def cut_nc(nc_file, var, x0, x1, y0, y1):
    try:
        data = nc_file['var'][:, x0 - 1:x1 + 1, y0 - 1:y1 + 1]
    except:
        data = nc_file['var'][x0 - 1:x1 + 1, y0 - 1:y1 + 1]
    return(data)


def locate_lat_lon(nc_file, lat0, lat1, lon0, lon1):
    latvals = np.array(nc_file['lat'][:])
    lonvals = np.array(nc_file['lon'][:])
    rad_factor = np.pi / 180.0
    latvals = latvals[:] * rad_factor
    lonvals = lonvals[:] * rad_factor

    if lon0 < 0:
        lon0 = (360 + lon0)
    lat0_rad = lat0 * rad_factor
    lon0_rad = lon0 * rad_factor
    x0 = np.abs(latvals[:] - lat0_rad).argmin()
    y0 = np.abs(lonvals[:] - lon0_rad).argmin()

    if lon1 < 0:
        lon1 = (360 + lon1)
    lat1_rad = lat1 * rad_factor
    lon1_rad = lon1 * rad_factor
    x1 = np.abs(latvals[:] - lat1_rad).argmin()
    y1 = np.abs(lonvals[:] - lon1_rad).argmin()

    return(x0, x1, y0, y1)


def list_vars_dimensions(nc_file):
    nc_var = list(nc_file.variables.keys())
    nc_dim = list(nc_file.dimensions.keys())

    return(nc_var, nc_dim)


def create_nc(nc_path, nc_dim, var, data):
    nc_file = netCDF4.Dataset(nc_path, 'w')

    shape = data.shape
    if len(shape) == 4:
        # for i in range(0, len(nc_dim)):
        #     nc_file.createDimension(nc_dim[i], shape[i])
        nc_file.createDimension(nc_dim[0], shape[0])
        nc_file.createDimension(nc_dim[1], shape[1])
        nc_file.createDimension(nc_dim[2], shape[2])
        nc_file.createDimension(nc_dim[3], shape[3])

        nc_file.createVariable(var, 'f8', (nc_dim[0], nc_dim[1], nc_dim[2], nc_dim[
                               3]), zlib=True, least_significant_digit=5)
        nc_file['var'][:, :, :, :] = data[:, :, :, :]

    elif len(shape) == 3:
        nc_file.createDimension(nc_dim[0], shape[0])
        nc_file.createDimension(nc_dim[1], 0)
        nc_file.createDimension(nc_dim[2], shape[1])
        nc_file.createDimension(nc_dim[3], shape[2])

        nc_file.createVariable(var, 'f8', (nc_dim[0], nc_dim[1], nc_dim[
                               2]), zlib=True, least_significant_digit=5)
        nc_file['var'][:, :, :] = data[:, :, :]

    elif len(shape) == 2:
        nc_file.createDimension(nc_dim[0], 0)
        nc_file.createDimension(nc_dim[1], 0)
        nc_file.createDimension(nc_dim[2], shape[1])
        nc_file.createDimension(nc_dim[3], shape[2])

        nc_file.createVariable(
            var, 'f8', (nc_dim[1], nc_dim[2]), zlib=True, least_significant_digit=5)
        nc_file['var'][:, :] = data[:, :]

    return(nc_file)


def append_nc(nc_file, var, data):
    nc_var, nc_dim = list_vars_dimensions(nc_file)
    if ~var in nc_var:
        shape = data.shape
        if len(shape) == 4:
            nc_file.createVariable(var, (nc_dim[0], nc_dim[1], nc_dim[2], nc_dim[
                                   3]), zlib=True, least_significant_digit=5)
            nc_file['var'][:, :, :, :] = data[:, :, :, :]
        elif len(shape) == 3:
            nc_file.createVariable(var, (nc_dim[0], nc_dim[1], nc_dim[
                                   2]), zlib=True, least_significant_digit=5)
            nc_file['var'][:, :, :] = data[:, :, :]
        elif len(shape) == 2:
            nc_file.createVariable(
                var, (nc_dim[1], nc_dim[2]), zlib=True, least_significant_digit=5)
            nc_file['var'][:, :] = data[:, :]
        else:
            nc_file.createVariable(var, 'S3', (nc_dim[0]))
            nc_file['var'][:] = data[:]
    return(nc_file)


def run(files, lat0, lat1, lon0, lon1):
    for file in files:
        out_path = file.split('.')[-2] + '__CROP__.nc'
        in_file = netCDF4.Dataset(file, 'r')
        x0, x1, y0, y1 = locate_lat_lon(in_file, lat0, lat1, lon0, lon1)
        in_var, in_dim = list_vars_dimensions(in_file)
        for i, var in enumarate(in_var, 0):
            data = cut_nc(in_file, var, x0, x1, y0, y1)
            if i == 0:
                out_file = create_nc(out_path, in_dim, var, data)
            else:
                out_file = append_nc(out_file, var, data)
        in_file.close()
        out_file.close()
