#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:04:00 2017

@author: limyiheng
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    for i in stations_highest_rel_level(stations, 10):
        print (i[0], i[1])
    #print(stations_highest_rel_level(stations, 10))
    
if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    run()

    
    