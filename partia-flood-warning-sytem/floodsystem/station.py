"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None
        
    #using property decorators to prevent accidental
    #changes from occuring to the attributes
    @property
    def station_id(self):
        return self.station_id
    @property
    def measure_id(self):
        return self.measure_id
    @property
    def label(self):
        return self.name
    @property
    def coord(self):
        return self.coord
    @property
    def typical_range(self):
        return self.typical_range
    @property
    def river(self):
        return self.river
    @property
    def town(self):
        return self.town

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += " measure id: {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    #note that typical_range is represented as a tuple (low, high)
    def typical_range_consistent(self):
        
        #missing data
        if self.typical_range == None:
            return False
        
        #swapped high/low
        elif self.typical_range[1] < self.typical_range[0]:
            return False
            
        else:
            return True
            
def inconsistent_typical_range_stations(stations):
    """Given a list of station objects, this returns a sorted list
    of stations with inconsistent data on typical ranges"""
    
    #create empty list
    inconsistent_data = []

    #iterate over each station
    for station in stations:
        
        #if data inconsistent, add name to list
        if MonitoringStation.typical_range_consistent(station) == False:
            inconsistent_data.append(station.name) 
        else:
            pass
    
        #sort list alphabetically
    return sorted(inconsistent_data)