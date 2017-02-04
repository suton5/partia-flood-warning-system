"""Unit test for the station module"""

import pytest
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    
def test_inconsistent_typical_range_stations():
    
    # Create test station 1
    s_id1 = "test-s-id1"
    m_id1 = "test-m-id1"
    label1 = "some station1"
    coord1 = (-2.0, 4.0)
    trange1 = None
    river1 = "River X1"
    town1 = "My Town1"
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
    
    # Create test station 2
    s_id2 = "test-s-id2"
    m_id2 = "test-m-id2"
    label2 = "some station2"
    coord2 = (-2.0, 4.0)
    trange2 = (5.5, 3.4445)
    river2 = "River X2"
    town2 = "My Town2"
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
    
    # Create test station 3
    s_id3 = "test-s-id3"
    m_id3 = "test-m-id3"
    label3 = "some station3"
    coord3 = (-2.0, 4.0)
    trange3 = (-2.3, 3.4445)
    river3 = "River X3"
    town3 = "My Town3"
    s3 = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)
    
    test_list = [s1, s2, s3]
    inconsistent_data = inconsistent_typical_range_stations(test_list)
    assert len(inconsistent_data) == 2