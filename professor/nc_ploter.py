#!/usr/bin/env python3

from netCDF4 import Dataset
import argparse
# import numpy as np
import yaml

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def gen_map_plot(right_c, left_c, file_name, data):
        """
    Efectivile creates the plot,
    lat [-90, 90]
    lon [-180, 180] or [0, 360]
    """
    parallels = np.arange(left_c[0], right_c[0], (right_c[0]-left_c[0])//4)
    meridians = np.arange(left_c[1], right_c[1], (right_c[1]-left_c[1])//4)
    try:
        fig1 = plt.figure(file_name,figsize=(16, 9))
        map1 = Basemap(llcrnrlat=float(left_c[0]), urcrnrlat=float(right_c[0]),
                       llcrnrlon=float(left_c[1]), urcrnrlon=float(right_c[1]),
                                                    resolution='h', epsg=4326)
        map1.drawcoastlines()
        map1.drawcountries(linewidth=0.5, linestyle='solid', color='k',
                                          antialiased=1, ax=None, zorder=None)
        map1.fillcontinents(color='lightgray', zorder=0)
        try:
                ny = data.shape[1]
                nx = data.shape[2]
        except:
                ny = data.shape[0]
                nx = data.shape[1]
        lons, lats = map1.makegrid(nx, ny)
        x, y = map1(lons, lats)
        try:
                map1.pcolormesh(x, y, data[0,:,:])
        except:
                map1.pcolormesh(x, y, data[:,:])
        map1.colorbar(location='right', size='5%', pad='2%')
        map1.drawparallels(parallels,labels=[True, False, False, False], linewidth=1, color="k") # labels = [left,right,top,bottom]
        map1.drawmeridians(meridians,labels=[False, False, False, True], linewidth=1, color="k")
        plt.savefig(file_name, dpi=300, pad_inches=0)

        return True
    except:
        return False


parser = argparse.ArgumentParser(description="This script genarete plots from NetCDF4")
parser.add_argument('-i', help="Imput NetCDF4 file", action='store',required=True, dest='nc_path')
parser.add_argument('-o', help="Output destination", action='store',required=False, dest='out_path')
parser.add_argument('-v', help="Variables list", action='store',required=False, dest='nc_vars')
parser.add_argument('-l', help="Lat0, Lon0, Lat1, Lon2", action='store',required=False, dest='lat_lon', type=str)

args=parser.parse_args()

nc_path = args.nc_path
nc_vars = [args.nc_vars] or ['T2','RAINNC', 'Q2', 'PSFC'] 
out_path = args.out_path or './'

try:
        lat_lon =[float(item) for item in args.lat_lon.split(',')]
        left_c  = [lat_lon[0], lat_lon[1]]
        right_c = [lat_lon[2], lat_lon[3]]
except:
        left_c  = [-89.9, -179.9]
        right_c = [89.9, 179.9]

nc_file =  Dataset(nc_path, 'r')

for var in nc_vars:
    data = nc_file.variables[var]
    for i in range(0, len(data)):
        file_name = out_path + var + str(i) + '.png'
        try:
                suc = gen_map_plot(right_c, left_c, file_name, data[i,:,:])
                brkr = False
        except:
                suc = gen_map_plot(right_c, left_c, file_name, data[:,:])
                brkr = True
        if suc == True:
            brkr == False
            s = 'plot %s, timestep %s done!' %(var, i)
            print(s)
        else:
            s = 'Fail to plot %s, timestep %s' %(var, i)
            print(s)
        if brkr == True:
            break

nc_file.close()
