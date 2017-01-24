"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from operator import itemgetter
from collections import OrderedDict

stations = build_station_list()

def rivers_with_station(stations):
    """Builds a set of names of rivers with monitoring stations"""
    
    #create an empty set (since river names are repeated)
    rivers=set()
    
    #create the if bypass in case certain names are missing
    for station in stations:
        if station.river == None:
            pass
        else:
            rivers.add(station.river)
            
    return rivers
            
#running the demo program
rivers_fordemo = rivers_with_station(stations)
print("Number of rivers with at least one monitoring station: {}".format(len(rivers_fordemo)))
    
#change the set to list to allow for slicing
rivers_fordemo_list = list(rivers_fordemo)
#sort the list alphabetically
rivers_fordemo_sorted = sorted(rivers_fordemo_list)

#get the first 10 alphabetically
first_ten_rivers = rivers_fordemo_sorted[:10]
print(first_ten_rivers)


def stations_by_river(stations):
    """Builds a dictionary with river names as keys that map to all the stations on the river"""
    
    #create empty dictionary
    river_dict={}
    
    #if river key exists, add station name. otherwise, make new river key.
    for station in stations:
        if station.river in river_dict:
            river_dict[station.river].append(station.name)
        else:
            river_dict[station.river] = [station.name]
    return river_dict

#running the demo program
dict_fordemo = stations_by_river(stations)
print(sorted(dict_fordemo["River Aire"]))
print(sorted(dict_fordemo["River Cam"]))
print(sorted(dict_fordemo["Thames"]))


    

