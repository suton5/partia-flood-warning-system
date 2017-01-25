"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.stationdata import build_station_list
#from floodsystem.utils import sorted_by_key
from operator import itemgetter

stations = build_station_list()

def rivers_with_station(stations):
    """Builds a set of rivers with monitoring stations"""
    
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
    """Builds a dictionary with river names as keys that map to all the 
    stations on the river"""
    
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

def rivers_by_station_number(stations, N):
    """Determines the N rivers with the greatest number of stations. 
    If there are more rivers with same number of stations as Nth, then
    they are included as well"""
    
    #create the empty list
    river_stationnumbers = []
    
    #iterate over all entries in the dictionary from Task 1D
    for river, stations in stations.items():
        river_tuple = (river, len(stations)) #make tuples
        river_stationnumbers.append(river_tuple) #add tuples into list
        
    #sort the list in decreasing order by the value of the second tuple entry (station number)
    sorted_river_stationnumbers = sorted(river_stationnumbers, key=lambda tup: tup[1], reverse=True)
    
    #slice N first values
    first_N = sorted_river_stationnumbers[:N]
    
    #from remainder of list, add in any extra rivers that have same station number
    for i in sorted_river_stationnumbers:
        if i in first_N:
            pass
        elif i[1] == first_N[-1][1]:
            first_N.append(i)
            

    return first_N
    
    


    

