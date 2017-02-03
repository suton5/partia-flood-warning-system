#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 22:57:18 2017

@author: limyiheng
"""
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

stations = build_station_list()

print(stations_within_radius(stations, (52.2053, 0.1218), 10))