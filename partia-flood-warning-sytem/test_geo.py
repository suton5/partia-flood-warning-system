"""Unit test for the geo module"""

import pytest
from floodsystem.geo import rivers_with_station
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.geo import dict_fordemo


station_list = build_station_list()


def test_rivers_with_station():
    """Test rivers_with_station()"""
    rivers = rivers_with_station(station_list)
    assert len(rivers) > 0

def test_rivers_by_station_number():
    """Test rivers_by_station_number()"""
    N=9
    first_N = rivers_by_station_number(dict_fordemo, N)
    assert len(first_N) > 0
    for i in range (0, N):
        if first_N[i][1] <= first_N[i+1][1]:
            sort_checker = True
        else:
            sort_checker = False
            
    assert sort_checker == True