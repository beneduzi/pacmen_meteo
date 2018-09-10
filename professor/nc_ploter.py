#!/usr/bin/env python3

import netCDF4 as nc
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def gen_map_plot(file_name, data, right_c=[-90, 90], left_c=[-180, 180]):
    parallels = np.arange(left_c[0], right_c[0], (right_c[0] - left_c[0]) // 4)
    meridians = np.arange(left_c[1], right_c[1], (right_c[1] - left_c[1]) // 4)
    try:
        fig1 = plt.figure(file_name, figsize=(16, 9))
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
            map1.pcolormesh(x, y, data[0, :, :])
        except:
            map1.pcolormesh(x, y, data[:, :])
        map1.colorbar(location='right', size='5%', pad='2%')
        map1.drawparallels(
            parallels,
            labels=[
                True,
                False,
                False,
                False],
            linewidth=1,
            color="k")  # labels = [left,right,top,bottom]
        map1.drawmeridians(
            meridians,
            labels=[
                False,
                False,
                False,
                True],
            linewidth=1,
            color="k")
        plt.savefig(file_name, dpi=300, pad_inches=0)

        return True
    except:
        return False
