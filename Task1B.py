#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 22:17:50 2017

@author: limyiheng
"""
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations = build_station_list()

print (stations_by_distance(stations, (52.2053, 0.1218))[0:10])
print (stations_by_distance(stations, (52.2053, 0.1218))[-10:-1])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")


