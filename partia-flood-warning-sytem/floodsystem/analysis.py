#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:59:14 2017

@author: Sujay
"""
import matplotlib
import numpy as np


def polyfit(dates, levels, p):
    
    #if length of dates or levels == 0, do nothing
    if len(dates) == 0 or len(levels) == 0:
            pass
    else:
        dates_float = matplotlib.dates.date2num(dates)
        dT=dates_float[0]
        p_coeff = np.polyfit(dates_float-dT, levels, p)
    
        #convert into usable polynomial function
        poly = np.poly1d(p_coeff)
    
    #to accommodate for poly not being referenced before attempted assignment
    #this would happen if the if statement above were fulfilled
    try:
        return poly, dT
    except:
        pass