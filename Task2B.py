#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 23:21:00 2017

@author: limyiheng
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    for i in stations_level_over_threshold(stations, 0.8):
        print(i[0], i[1])
    #print(stations_level_over_threshold(stations, 0.8))

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")

    run()

    
    
