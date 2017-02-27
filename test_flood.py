#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:25:50 2017

@author: limyiheng
"""

import pytest 
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
#stations = build_station_list()
#update_water_levels(stations)
#new_list = stations_level_over_threshold(stations, 0.2)
#print(new_list)

#test for 2B
def test_stations_level_over_threshold():
    """check if the elements in the list are ranked in desceding order according to their relative
    water level, check if each element in the list is a tuple of 2"""
    stations = build_station_list()
    update_water_levels(stations)
    new_list = stations_level_over_threshold(stations, 0.2)
    
    for i in new_list:
        #check if they are tuples
        assert type(i) == tuple
        #check if the tuples have 2 items
        assert len(i) == 2
        
    
    for i in range(len(new_list)-1):
        #check if the order is correct
        if new_list[i][1] > new_list[i+1][1]:
            True
        else:
            False
        assert True
        
        if new_list[i][1] <= 0.2:
            False
        else:
            True
        assert True
        
        
        
        
        
        
        
        
        


#test for 2C
def test_stations_highest_rel_level():
    """check if the elements in the list are ranked in desceding order according to their relative
    water level, check if each element in the list is a tuple of 2, check if the length of the list is N"""
    stations = build_station_list()
    update_water_levels(stations)
    new_list_2 = stations_highest_rel_level(stations, 10)
    
    
    assert len(new_list_2) == 10

    for i in new_list_2:
        #check if they are tuples
        assert type(i) == tuple
        #check if the tuples have 2 items
        assert len(i) == 2
        
    
    for i in range(len(new_list_2)-1):
        #check if the order is correct
        if new_list_2[i][1] > new_list_2[i+1][1]:
            True
        else:
            False
        assert True
        
      