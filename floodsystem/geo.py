"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.stationdata import build_station_list
#from .utils import sorted_by_key

def rivers_with_station(stations):
    """Builds a set of names of rivers with monitoring stations"""
    rivers=set()
    
    for station in stations:
        if station.river == None:
            pass
        else:
            rivers.add(station.river)
            
    print("Number of rivers with at least one monitoring station: {}".format(len(rivers)))
    
    rivers_list = list(rivers)
    rivers_sorted = sorted(rivers_list)

    first_ten_rivers = rivers_sorted[:10]
    print(first_ten_rivers)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")    

stations = build_station_list()
print(rivers_with_station(stations))