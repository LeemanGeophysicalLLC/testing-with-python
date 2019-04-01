"""Test use of the meteogram module."""

import datetime
import os
from unittest.mock import Mock, patch

import pandas as pd
import pytest

from meteogram import meteogram
from meteogram.testing import (assert_almost_equal, assert_dataseries_equal,
                               get_recorder)


recorder = get_recorder(__file__)


def mocked_current_utc_time():
    """
    Mock our utc time function for testing with defaults.
    """
    return datetime.datetime(2018, 3, 26, 12)


@pytest.fixture
def load_example_asos():
    """
    Fixture to load example data from a csv file for testing.
    """
    example_data_path = os.path.abspath(os.path.join('..', 'staticdata'))
    data_path = os.path.join(example_data_path, 'AMW_example_data.csv')
    return meteogram.download_asos_data(data_path)


@pytest.mark.parametrize('start, end, station, expected', [
    # Single Digit Datetimes
    (datetime.datetime(2018, 1, 5, 1), datetime.datetime(2018, 1, 9, 1),
     'FSD',
     'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
     'station%5B%5D=FSD&tz=UTC&year1=2018&month1=01&day1=05&hour1=01'
     '&minute1=00&year2=2018&month2=01&day2=09&hour2=01&minute2=00&'
     'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&'
     'sample=1min&what=view&delim=comma&gis=yes'),

    # Double Digit Datetimes
    (datetime.datetime(2018, 10, 11, 12), datetime.datetime(2018, 10, 16, 15),
     'MLI',
     'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
     'station%5B%5D=MLI&tz=UTC&year1=2018&month1=10&day1=11&hour1=12'
     '&minute1=00&year2=2018&month2=10&day2=16&hour2=15&minute2=00&'
     'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&'
     'sample=1min&what=view&delim=comma&gis=yes'),

    # Defaults
    (None, None,
     'MLI',
     'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
     'station%5B%5D=MLI&tz=UTC&year1=2018&month1=03&day1=25&hour1=12'
     '&minute1=00&year2=2018&month2=03&day2=26&hour2=12&minute2=00&'
     'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct'
     '&sample=1min&what=view&delim=comma&gis=yes'),

    # Default Start Only
    (None, datetime.datetime(2019, 3, 25, 12),
     'MLI',
     'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
     'station%5B%5D=MLI&tz=UTC&year1=2019&month1=03&day1=24&hour1=12'
     '&minute1=00&year2=2019&month2=03&day2=25&hour2=12&minute2=00&'
     'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct'
     '&sample=1min&what=view&delim=comma&gis=yes'),

    # Default End Only
    (datetime.datetime(2018, 3, 24, 12), None,
     'MLI',
     'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
     'station%5B%5D=MLI&tz=UTC&year1=2018&month1=03&day1=24&hour1=12'
     '&minute1=00&year2=2018&month2=03&day2=26&hour2=12&minute2=00&'
     'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct'
     '&sample=1min&what=view&delim=comma&gis=yes')
])
@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_build_asos_request_url(start, end, station, expected):
    """
    Test URL building for requests.
    """
    # Setup - Done by parameterized fixture

    # Exercise
    url = meteogram.build_asos_request_url(station, start, end)

    # Verify
    assert url == expected

    # Cleanup - none necessary

@recorder.use_cassette('ASOS_AMW_2018032512_2018032612')
@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_download_asos_data():
    """Test downloading ASOS data."""
    # Setup
    url = meteogram.build_asos_request_url('AMW')

    # Exercise
    df = meteogram.download_asos_data(url)

    # Verify
    first_row_truth = pd.Series(
                      {'station_id': 'AMW',
                       'station_name': 'Ames',
                       'latitude_deg': 41.990439,
                       'longitude_deg': -93.618515,
                       'UTC': pd.Timestamp('2018-03-25 12:00:00'),
                       'temperature_degF': 29,
                       'dewpoint_degF': 24,
                       'wind_speed_knots': 8,
                       'wind_direction_degrees': 113})

    assert_dataseries_equal(df.iloc[0], first_row_truth)

    # Cleanup - none necessary


@recorder.use_cassette('ASOS_AMW_Future')
def test_download_asos_data_in_future():
    """Test for correct behavior when asking for non-existant (future) data."""
    # Setup
    url = meteogram.build_asos_request_url('AMW',
                                           datetime.datetime(2999, 10, 10, 10),
                                           datetime.datetime(2999, 11, 10, 10))

    # Exercise
    df = meteogram.download_asos_data(url)

    # Verify
    assert(len(df) == 0)

    # Cleanup - none necessary


@recorder.use_cassette('ASOS_AMW_Reversed_Dates')
def test_download_asos_data_start_after_end():
    """Test for correct behavior when start and end times are reversed."""
    # Setup
    start = datetime.datetime(2018, 8, 1, 12)
    end = datetime.datetime(2018, 7, 1, 12)
    url = meteogram.build_asos_request_url('AMW', start, end)

    # Exercise
    df = meteogram.download_asos_data(url)

    # Verify
    assert(len(df) == 0)

    # Cleanup - none necessary


@pytest.mark.mpl_image_compare(remove_text=True)
def test_plotting_meteogram_defaults(load_example_asos):
    """Test default meteogram plotting."""
    # Setup
    df = load_example_asos

    # Exercise
    fig, _, _ = meteogram.plot_meteogram(df)

    # Verify - Done by decorator when run with -mpl flag

    # Cleanup - none necessary

    return fig
