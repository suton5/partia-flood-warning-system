#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 16:54:10 2017

@author: Sujay
"""
import matplotlib.pyplot as plt
import matplotlib
from floodsystem.analysis import polyfit


def plot_water_levels(station, dates, levels):
 
    low = station.typical_range[0]
    high = station.typical_range[1]
    low_list = [low]*len(dates)
    high_list = [high]*len(dates)
    
# Plot
    plt.plot(dates, levels, label="Water Levels")
    plt.plot(dates, low_list, label="Typical Low")
    plt.plot(dates, high_list, label="Typical High")

# Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.legend()
    plt.xticks(rotation=45);
    plt.title(station.name)

    # This makes sure plot does not cut off date labels
    plt.tight_layout()  
    
    return plt.figure()
    
def plot_water_level_with_fit(station, dates, levels, p):
    
    if len(dates) == 0 or len(levels) == 0:
        print("not enough data available for {}".format(station.name))
    
    else:    
        dates_float = matplotlib.dates.date2num(dates)
        poly = polyfit(dates, levels, p) [0]
        dT = polyfit(dates, levels, p) [1]
        
        low = station.typical_range[0]
        high = station.typical_range[1]
        low_list = [low]*len(dates)
        high_list = [high]*len(dates)
        
        #plot original data points
        plt.plot(dates_float, levels, label="Original")
    
        #plot best-fit polynomial
        plt.plot(dates_float, poly(dates_float-dT), label="Polynomial")
        
        plt.plot(dates_float, low_list, label="Low")
        plt.plot(dates_float, high_list, label="High")
    
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.legend()
        plt.xticks(rotation=45);
        plt.title(station.name)
        
        #Display plot
        plt.tight_layout
        
        return plt.figure()