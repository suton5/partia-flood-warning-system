#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 12:51:23 2017

@author: Sujay
"""
from datetime import datetime, date, time
from floodsystem.analysis import polyfit

def test_polyfit():
    
    d = date(2017, 2, 25)
    t1 = time(10, 30)
    t2 = time(10, 45)
    t3 = time(11, 00)
    t4 = time(11, 15)
    t5 = time(11, 30)
    x1 = datetime.combine(d, t1)
    x2 = datetime.combine(d, t2)
    x3 = datetime.combine(d, t3)
    x4 = datetime.combine(d, t4)
    x5 = datetime.combine(d, t5)
    
    dateslist = [x1, x2, x3, x4, x5]
    levelslist = [ 0., 0.00010851, 0.00043403, 0.00097656, 0.00173611]
    
    answer = polyfit(dateslist, levelslist, 2)
        
    x2coeff = round(answer[0][2], 5)
    x1coeff = round(answer[0][1], 5)
    x0coeff = round(answer[0][0], 5)
    
    assert x2coeff==1.0
    assert x1coeff==0.0
    assert x0coeff==0.0