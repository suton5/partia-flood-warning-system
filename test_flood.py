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
def test_stations_level_over_threshold():
    """assign relative water levels to certain stations, and make the latest levels at
    all other stations extremely high, so that the relative water level is definitely
    higher than the tolerance, but in a list. see if the function prints the list"""
    stations = build_station_list()

    for station in stations:
        
        
        if station.name == "Cam":
            station.relative_water_level = 0.5
            
        elif station.name == "Girton":
            station.relative_water_level = 1.0

        elif station.name == "Bourton Dickler":
            station.relative_water_level = 1.2

        elif station.name == "Norlands":
            station.relative_water_level = 1.4
            
        elif station.name == "Topsham":
            station.relative_water_level = 0.6
            
        elif station.name == "Pocklington":
            station.relative_water_level = None 
       
            
        x = stations_level_over_threshold(stations, 0.8)
        
        if x == [("Norlands", 1.4), ("Bourton Dickler", 1.2), ("Girton", 1.0)]:
            True
            
        else:
            False
            
        assert True
        
            
            


#test for 2C
def test_stations_highest_rel_level():
    #assign latest levels to a few stations in the list, and make all the other
    #stations have a latest level of 0, test if the function returns what it was asked to
    
    #stations = ["Cam", "Girton", "Bourton Dickler", "Norlands", "Topsham" ]
    stations = build_station_list()


    for station in stations:
        
        if station == "Cam":
            station.relative_water_level = 0.5
            
        elif station.name == "Girton":
            station.relative_water_level = 1.0

        elif station.name == "Bourton Dickler":
            station.relative_water_level = 1.2

        elif station.name == "Norlands":
            station.relative_water_level = 1.4
            
        elif station.name == "Topsham": 
            station.relative_water_level = 0.6
            
        else:
            station.latest_level = [1000,500]

    
        x = stations_highest_rel_level(stations, 3)
        
        if x == [("Norlands", 1.4), ("Dickler", 1.2), ("Girton", 1.0)]:
            
            True
        
        else:
        
            False
            
        assert True
        
        

    

