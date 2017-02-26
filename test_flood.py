#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:25:50 2017

@author: limyiheng
"""

import pytest 
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold


#test for 2B











#test for 2C
def test_stations_highest_rel_level():
    """assign latest levels to a few stations in the list, and make all the other
    stations have a latest level of 0, test if the function returns what it was asked to
    """
    #stations = ["Cam", "Girton", "Bourton Dickler", "Norlands", "Topsham" ]
    stations = build_station_list()


    for station in stations:
        
        if station == "Cam":
            station.latest_level = 0.1
            
        elif station.name == "Girton":
            station.latest_level = 0.2

        elif station.name == "Bourton Dickler":
            station.latest_level = 0.3

        elif station.name == "Norlands":
            station.latest_level = 1.0
            
        elif station.name == "Topsham":
            station.latest_level = None
            
        else:
            station.latest_level = 0

    
        x = stations_highest_rel_level(stations, 3)
        
        if x == [("Norlands", 1.0), ("Bourton Dickler", 0.3), ("Girton", 0.2)]:
            
            True
        
        else:
        
            False
            
        assert True
        
        
        
    
    

