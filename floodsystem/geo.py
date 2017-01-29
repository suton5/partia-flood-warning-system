"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.stationdata import build_station_list
from haversine import haversine
from floodsystem.utils import sorted_by_key


    
#create an empty list, and then append later on
liststations = []

#create a list of stations
stations = build_station_list()




        
#define a function
def stations_by_distance(stations, p):
    
    for station in stations:
        distance = haversine(p, station.coord)
        liststations.append((station.name, distance))
        
    return liststations
        
print(stations_by_distance(stations, (52.2053, 0.1218)))