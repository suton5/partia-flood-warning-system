#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:00:18 2017

@author: Sujay
"""
import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit
import matplotlib
import csv

def run():

    stations = build_station_list()
    update_water_levels(stations)
    #make list of 20 riskiest stations
    biglist = stations_highest_rel_level(stations, 30)
    #top 10 risky
    highlist0 = biglist[:15]
    #bottom 10 risky
    lowlist0 = biglist[-15:]
    

    #get the actual MonitoringStation class data for these stations
    highlist1=[]
    lowlist1=[]
    for name, level in highlist0:
        highlist1.append(name)
    for name, level in lowlist0:
        lowlist1.append(name)
    
        
    highlist_station=[]
    lowlist_station=[]
    for station in stations:
            if station.name in highlist1:
                highlist_station.append(station)
            elif station.name in lowlist1:
                lowlist_station.append(station)
            else:
                pass
            
    highlist_dates_levels=[]
    lowlist_dates_levels=[]
    
    #get water level data for these stations
    for station in highlist_station:
        dt=2
        
        dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))
        if len(dates)==0:
            pass
        elif len(levels)==0:
            pass
        else:
            station_tuple = (station, dates, levels)
            highlist_dates_levels.append(station_tuple)
            
    for station in lowlist_station:
        dt=2
        
        dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))
        if len(dates)==0:
            pass
        elif len(levels)==0:
            pass
        else:
            station_tuple = (station, dates, levels)
            lowlist_dates_levels.append(station_tuple)
    
    #get polynomial function for these stations
    high_poly=[]
    low_poly=[]
    

    for station, dates, levels in highlist_dates_levels:
        poly = polyfit(dates, levels, 4) [0]
        station_tuple = (station, poly)
        high_poly.append(station_tuple)
        
    for station, dates, levels in lowlist_dates_levels:
        poly = polyfit(dates, levels, 4) [0]
        station_tuple = (station, poly)
        low_poly.append(station_tuple)
    
    now = datetime.datetime.utcnow()
    now_float = matplotlib.dates.date2num(now)
    
    #plot derivatives for these stations
    high_dy=[]
    low_dy=[]
    
    for station, poly in high_poly:
        dy = poly.deriv()
        station_tuple = (station, dy(now_float))
        high_dy.append(station_tuple)
    
    for station, poly in low_poly:
        dy = poly.deriv()
        station_tuple = (station, dy(now_float))
        low_dy.append(station_tuple)
        
    severe=[]
    high=[]
    moderate=[]
    low=[]
    
    for station, dy in high_dy:
        if dy > 0:
            severe.append(station)
            
        else:
            high.append(station)
            
    for station, dy in low_dy:
        if dy > 0:
            moderate.append(station)
            
        else:
            low.append(station)
            
    severe_name=[]
    high_name=[]
    moderate_name=[]
    low_name=[]

    for station in severe:
        severe_name.append(station.name)
    for station in high:
        high_name.append(station.name)
    for station in moderate:
        moderate_name.append(station.name)
    for station in low:
        low_name.append(station.name)
        
            
    print("Stations with severe risk: {}".format(severe_name))
    print("Stations with high risk: {}".format(high_name))
    print("Stations with moderate risk: {}".format(moderate_name))
    print("Stations with low risk: {}".format(low_name))
    
    station_coord = []
    
    for station in severe:
        risk = 'severe'
        
        if station.town == None:
            station.town = "Missing Data"
        else:
            pass
            
        if station.river == None:
            station.river = "Missing Data"
        else:
            pass
            
            
        coord = (station.name, station.coord[0],station.coord[1], station.town, station.river, risk)
        station_coord.append(coord) 
        
    for station in high:
        risk = 'high'
        
        if station.town == None:
            station.town = "Missing Data"
        else:
            pass
            
        if station.river == None:
            station.river = "Missing Data"
        else:
            pass
            
            
        coord = (station.name, station.coord[0],station.coord[1], station.town, station.river, risk)
        station_coord.append(coord) 
        
    for station in moderate:
        risk = 'moderate'
        
        if station.town == None:
            station.town = "Missing Data"
        else:
            pass
            
        if station.river == None:
            station.river = "Missing Data"
        else:
            pass
            
            
        coord = (station.name, station.coord[0],station.coord[1], station.town, station.river, risk)
        station_coord.append(coord) 
        
    for station in low:
        risk = 'low'
        
        if station.town == None:
            station.town = "Missing Data"
        else:
            pass
            
        if station.river == None:
            station.river = "Missing Data"
        else:
            pass
            
            
        coord = (station.name, station.coord[0],station.coord[1], station.town, station.river, risk)
        station_coord.append(coord) 
       
    
    
    #export as csv file    
    with open("station_coord1.csv", "w") as station_coord_csv:
        writer = csv.writer(station_coord_csv)
        writer.writerows(station_coord)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")

    run()