#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 21:12:01 2017

@author: limyiheng
"""

#from floodsystem.stationdata import build_station_list

#stations = build_station_list()

#Task 2B
def stations_level_over_threshold(stations, tol):
  
    station_relative_water_level = []

    #work up to 698, error at 698
    #slice out 698th element as that is a list
    for station in stations:#[:698] + stations[699:]:
        """if the data is inconsistent or unavailable, pass it, otherwise, only if station
        has relative water level higher than tolerance we append it"""
        if type(station.latest_level) == list:
            
            pass
      
        elif station.relative_water_level() == None:
            
            pass
        
        else:
            #if type(station.relative_water_level) == float:
            if station.relative_water_level() > tol:
          
                station_relative_water_level.append((station.name, station.relative_water_level()))
            
            else:
            
                pass
           
                
        sorted_station_relative_water_level = sorted(station_relative_water_level,key=lambda x:(-x[1],x[0]))
    #return sorted_station_relative_water_level(station_relative_water_level, 1, reverse=True)
    return sorted_station_relative_water_level
    

#Task 2C
def stations_highest_rel_level(stations, N):
    """noting that a list exists in the latest_level'S', insert the if statement to take
    that into account. Other than that, if there is any inconsistency we pass it, otherwise 
    we append it to the empty list"""
    
   
    station_relative_water_level = []

    for station in stations:
         
        if type(station.latest_level) == list:
            
            pass
        
        elif station.relative_water_level() == None:
            
            pass
       
        elif station.latest_level == None:
            pass
        
        else:
        
            station_relative_water_level.append((station.name, station.relative_water_level()))

    sorted_station_relative_water_level = sorted(station_relative_water_level,key=lambda x:(-x[1],x[0]))
    
    
    N_highest_stations = sorted_station_relative_water_level[:N]

    return N_highest_stations
        
        

    
# sorted_station_relative_water_level = sorted(station_relative_water_level,key=lambda x:(-x[1],x[0]))
    
#return sorted_station_relative_water_level

    