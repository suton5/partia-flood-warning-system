"""Unit test for the geo module"""

import pytest
from floodsystem.geo import stations_by_distance 
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from floodsystem.station import MonitoringStation
from haversine import haversine


station_list = build_station_list()

def test_stations_by_distance():
    
    """ to test if the function sorts the list by distance"""
    stations = build_station_list()

    newlist = stations_by_distance(stations, (52.2053, 0.1218))
    for i in range(len(newlist)-1):
        if newlist[i][1] <= newlist[i+1][1]:
            check = True
            
        else:
            check = False
            
        assert check == True
        
        
    """to test if the elements in the list are tuples"""
    
    for i in newlist:
        assert type(i) == tuple


def test_stations_within_radius():
    stations = build_station_list()
    testlist = stations_within_radius(stations, (52.2053, 0.1218), 10)
    #the first 2 coordinates are around cambridge centre, last 2 coordinates
    #are in Germany
    samples = [(52.176734, 0.120083), (52.183625, 0.09323), (51.463206, 7.363607), (51.892385, 13.329183)]
    for i in testlist:
        assert type(i) == str


    if haversine((52.2053, 0.1218), samples[0]) <= 10:
        check = True
    else:
        check = False

    assert check == True

    if haversine((52.183625, 0.09323), samples[0]) <= 10:
        check = True
    else:
        check = False

    assert check == True

    if haversine((51.463206, 7.363607), samples[0]) <= 10:
        check = True
    else:
        check = False

    assert check == False

    if haversine((51.892385, 13.329183), samples[0]) <= 10:
        check = True
    else:
        check = False

    assert check == False

def test_rivers_with_station():
    """Test rivers_with_station()"""
    rivers = rivers_with_station(station_list)
    assert len(rivers) > 0

    # Create test station 1 (correct data)
    s_id1 = "test-s-id1"
    m_id1 = "test-m-id1"
    label1 = "some station1"
    coord1 = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    river1 = "River X1"
    town1 = "My Town1"
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
    
    # Create test station 2 (missing river data)
    s_id2 = "test-s-id2"
    m_id2 = "test-m-id2"
    label2 = "some station2"
    coord2 = (-2.0, 4.0)
    trange2 = (-2.3, 3.4445)
    river2 = None
    town2 = "My Town2"
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
    
    test_list = [s1, s2]
    rivers_test = rivers_with_station(test_list)
    assert len(rivers_test) == 1
    
def test_stations_by_river():
    """Test stations_by_river()"""
    river_dict = stations_by_river(station_list)
    assert len(river_dict) > 0

    # Create test station 1 (same river)
    s_id1 = "test-s-id1"
    m_id1 = "test-m-id1"
    label1 = "some station1"
    coord1 = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    river1 = "River X1"
    town1 = "My Town1"
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
    
    # Create test station 2 (same river)
    s_id2 = "test-s-id2"
    m_id2 = "test-m-id2"
    label2 = "some station2"
    coord2 = (-2.0, 4.0)
    trange2 = (-2.3, 3.4445)
    river2 = "River X1"
    town2 = "My Town2"
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
    
    # Create test station 3 (different river)
    s_id3 = "test-s-id3"
    m_id3 = "test-m-id3"
    label3 = "some station3"
    coord3 = (-2.0, 4.0)
    trange3 = (-2.3, 3.4445)
    river3 = "River X3"
    town3 = "My Town3"
    s3 = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)
    
    
    test_list = [s1, s2, s3]
    river_dict_test = stations_by_river(test_list)
    assert len(river_dict_test) == 2

def test_rivers_by_station_number():
    """Test rivers_by_station_number()"""
    first_N = rivers_by_station_number(station_list, 9)
    assert len(first_N) > 0

    # Set up the stations such that 3 have the same rivers, 2 have the same 
    # rivers and the last two have  different rivers
    
    # Create test station 1 
    s_id1 = "test-s-id1"
    m_id1 = "test-m-id1"
    label1 = "some station1"
    coord1 = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    river1 = "River X1"
    town1 = "My Town1"
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
    
    # Create test station 2
    s_id2 = "test-s-id2"
    m_id2 = "test-m-id2"
    label2 = "some station2"
    coord2 = (-2.0, 4.0)
    trange2 = (-2.3, 3.4445)
    river2 = "River X1"
    town2 = "My Town2"
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
    
    # Create test station 3
    s_id3 = "test-s-id3"
    m_id3 = "test-m-id3"
    label3 = "some station3"
    coord3 = (-2.0, 4.0)
    trange3 = (-2.3, 3.4445)
    river3 = "River X1"
    town3 = "My Town3"
    s3 = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)
    
    # Create test station 4
    s_id4 = "test-s-id4"
    m_id4 = "test-m-id4"
    label4 = "some station4"
    coord4 = (-2.0, 4.0)
    trange4 = (-2.3, 3.4445)
    river4 = "River X2"
    town4 = "My Town4"
    s4 = MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)
    
    # Create test station 5
    s_id5 = "test-s-id5"
    m_id5 = "test-m-id5"
    label5 = "some station5"
    coord5 = (-2.0, 4.0)
    trange5 = (-2.3, 3.4445)
    river5 = "River X2"
    town5 = "My Town5"
    s5 = MonitoringStation(s_id5, m_id5, label5, coord5, trange5, river5, town5)
    
    # Create test station 6
    s_id6 = "test-s-id6"
    m_id6 = "test-m-id6"
    label6 = "some station6"
    coord6 = (-2.0, 4.0)
    trange6 = (-2.3, 3.4445)
    river6 = "River X4"
    town6 = "My Town6"
    s6 = MonitoringStation(s_id6, m_id6, label6, coord6, trange6, river6, town6)
    
    # Create test station 7
    s_id7 = "test-s-id7"
    m_id7 = "test-m-id7"
    label7 = "some station7"
    coord7 = (-2.0, 4.0)
    trange7 = (-2.3, 3.4445)
    river7 = "River X5"
    town7 = "My Town7"
    s7 = MonitoringStation(s_id7, m_id7, label7, coord7, trange7, river7, town7)
    
    test_list = [s1, s2, s3, s4, s5, s6, s7]

    # Should return 1 , since only 1 river has 3 stations
    first_N_test_1 = rivers_by_station_number(test_list, 1)
    # Should return 2 , since the 2 highest rivers have 3 and 2 stations, respectively
    first_N_test_2 = rivers_by_station_number(test_list, 2)
    # Should return 4 , since the last 2 rivers both have only 1 station
    first_N_test_3 = rivers_by_station_number(test_list, 3)
    
    assert len(first_N_test_1) == 1
    assert len(first_N_test_2) == 2
    assert len(first_N_test_3) == 4


