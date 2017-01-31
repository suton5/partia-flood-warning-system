"""Unit test for the geo module"""

import pytest
from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list

station_list = build_station_list()


def test_rivers_with_station():
    """Test rivers_with_station()"""
    rivers = rivers_with_station(station_list)
    assert len(rivers) > 0

