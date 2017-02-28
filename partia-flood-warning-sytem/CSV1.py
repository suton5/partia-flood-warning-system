#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:17:51 2017

@author: Sujay
"""

from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.station import MonitoringStation
import csv


stations_full = build_station_list()
update_water_levels(stations_full)

stations = []
for station in stations_full:
    if MonitoringStation.typical_range_consistent(station) == False:
        pass
    else:
        stations.append(station)

#create list of (station name, coord tuple, town, river, river level)
station_coord = []
    
for station in stations:
    
    if station.town == None:
        station.town = "Missing Data"
    else:
        pass
        
    if station.river == None:
        station.river = "Missing Data"
    else:
        pass
        
    coord = (station.name, station.coord[0], station.coord[1], station.town, station.river, station.latest_level)
    station_coord.append(coord) 

#export as csv file    
with open("station_coord2.csv", "w") as station_coord_csv:
    writer = csv.writer(station_coord_csv)
    writer.writerows(station_coord)
