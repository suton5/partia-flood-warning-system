#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:57:48 2017

@author: Sujay
"""

import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import matplotlib.pyplot as plt

def run():
    
    #build stations list and update
    stations = build_station_list()
    update_water_levels(stations)
    
    #use previous function to get names of 5 riskiest stations
    risk_stationname_levels = stations_highest_rel_level(stations, 5)
    
    #get the actual MonitoringStation object for these 5 stations
    risk_stationname = []

    for station, level in risk_stationname_levels:
        risk_stationname.append(station)
    
        risk_stations=[]

    for station in stations:
        if station.name in risk_stationname:
            risk_stations.append(station)
        else:
            pass
    
    
    station_1 = risk_stations[0]
    station_2 = risk_stations[1]
    station_3 = risk_stations[2]
    station_4 = risk_stations[3]
    station_5 = risk_stations[4]

    #retrieve station data for past 10 days
    dt=10
    dates1, levels1 = fetch_measure_levels(station_1.measure_id,
                                     dt=datetime.timedelta(days=dt))
    dates2, levels2 = fetch_measure_levels(station_2.measure_id,
                                     dt=datetime.timedelta(days=dt))
    dates3, levels3 = fetch_measure_levels(station_3.measure_id,
                                     dt=datetime.timedelta(days=dt))
    dates4, levels4 = fetch_measure_levels(station_4.measure_id,
                                     dt=datetime.timedelta(days=dt))
    dates5, levels5 = fetch_measure_levels(station_5.measure_id,
                                     dt=datetime.timedelta(days=dt))
    
    #plot graphs on multiple windows
    p1 = plot_water_levels(station_1, dates1, levels1)
    p2 = plot_water_levels(station_2, dates2, levels2)   
    p3 = plot_water_levels(station_3, dates3, levels3)
    p4 = plot_water_levels(station_4, dates4, levels4)
    p5 = plot_water_levels(station_5, dates5, levels5)
    ax1 = p1.add_subplot(111)
    ax1.plot()
    ax2 = p2.add_subplot(111)
    ax2.plot()
    ax3 = p3.add_subplot(111)
    ax3.plot()
    ax4 = p4.add_subplot(111)
    ax4.plot()
    ax5 = p5.add_subplot(111)
    ax5.plot()
    plt.show()

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    run()