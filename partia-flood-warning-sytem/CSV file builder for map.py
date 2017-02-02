from floodsystem.stationdata import build_station_list
import csv


stations_full = build_station_list()
stations = []
for station in stations_full:
    if MonitoringStation.typical_range_consistent(station) == False:
        pass
    else:
        stations.append(station)
#create list of (station name, coord tuple, town, river, high river level)
station_coord = []
    
for station in stations:
    color = ''
    
    if station.town == None:
        station.town = "Missing Data"
    else:
        pass
        
    if station.river == None:
        station.river = "Missing Data"
    else:
        pass
        
    if station.typical_range[1] >= 0.8:
        color = 'rgba(255, 0, 0)'
    elif station.typical_range[1] < 0.8 and station.typical_range[1] >= 0.5:
        color = 'rgba(255, 194, 0)'
    else:
        color = 'rgba(0, 204, 0)'
        
    coord = (station.name, station.coord, station.town, station.river, station.typical_range[1], color)
    station_coord.append(coord) 
   
#break up old list into (station name, lat, long, town, river, high river level ) 
station_coord1=[]

for i in station_coord:
    coord1 = (i[0], i[1][0], i[1][1], i[2], i[3], i[4], i[5])
    station_coord1.append(coord1)

#export as csv file    
with open("station_coord.csv", "w") as station_coord_csv:
    writer = csv.writer(station_coord_csv)
    writer.writerows(station_coord1)
