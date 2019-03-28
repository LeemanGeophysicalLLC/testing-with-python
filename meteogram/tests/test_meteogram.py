"""Test use of the meteogram module."""

import datetime
from unittest.mock import Mock, patch

import pandas as pd
import pytest

from meteogram import meteogram
from meteogram.testing import (assert_almost_equal, assert_dataseries_equal,
                               get_recorder)


recorder = get_recorder(__file__)


@patch('meteogram.meteogram.current_utc_time')
def test_current_utc_time(mocked_current_utc_time):
    """Test that the current_utc_time function returns current time."""
    mocked_current_utc_time.return_value = datetime.datetime(2019, 3, 26, 12, 0)

    #assert(meteogram.current_utc_time == datetime.datetime(2019, 3, 26, 12, 0))


def test_build_asos_request_url_single_digit_datetimes():
    """Test that data url building works with single digit datetimes."""
    start = datetime.datetime(2018, 1, 5, 1)
    end = datetime.datetime(2018, 1, 9, 1)
    station_id = 'FSD'

    url = meteogram.build_asos_request_url(station_id, start, end)

    truth = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
             'station%5B%5D=FSD&tz=UTC&year1=2018&month1=01&day1=05&hour1=01'
             '&minute1=00&year2=2018&month2=01&day2=09&hour2=01&minute2=00&'
             'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&'
             'sample=1min&what=view&delim=comma&gis=yes')
    assert url ==truth


def test_build_asos_request_url_double_digit_datetimes():
    """Test that data url building works with double digit datetimes."""
    start = datetime.datetime(2018, 10, 11, 12)
    end = datetime.datetime(2018, 10, 16, 15)
    station_id = 'MLI'

    url = meteogram.build_asos_request_url(station_id, start, end)

    truth = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
             'station%5B%5D=MLI&tz=UTC&year1=2018&month1=10&day1=11&hour1=12'
             '&minute1=00&year2=2018&month2=10&day2=16&hour2=15&minute2=00&'
             'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&'
             'sample=1min&what=view&delim=comma&gis=yes')
    assert url ==truth


@patch('meteogram.meteogram.current_utc_time')
def test_build_asos_request_url_all_defaults(mocked_current_utc_time):
    """Test that data url building works with all default arguments."""
    mocked_current_utc_time.return_value = datetime.datetime(2019, 3, 26, 12)

    url = meteogram.build_asos_request_url('MLI')

    truth = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
             'station%5B%5D=MLI&tz=UTC&year1=2019&month1=03&day1=25&hour1=12'
             '&minute1=00&year2=2019&month2=03&day2=26&hour2=12&minute2=00&'
             'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct'
             '&sample=1min&what=view&delim=comma&gis=yes')
    assert url ==truth


def test_build_asos_request_url_default_start_only():
    """Test that data url building works with default start argument."""
    end_date = datetime.datetime(2019, 3, 25, 12)

    url = meteogram.build_asos_request_url('MLI', end_date=end_date)

    truth = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
             'station%5B%5D=MLI&tz=UTC&year1=2019&month1=03&day1=24&hour1=12'
             '&minute1=00&year2=2019&month2=03&day2=25&hour2=12&minute2=00&'
             'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct'
             '&sample=1min&what=view&delim=comma&gis=yes')
    assert url ==truth

@patch('meteogram.meteogram.current_utc_time')
def test_build_asos_request_url_default_end_only(mocked_current_utc_time):
    """Test that data url building works with default end argument."""
    mocked_current_utc_time.return_value = datetime.datetime(2019, 3, 26, 12)
    start_date = datetime.datetime(2019, 3, 24, 12)

    url = meteogram.build_asos_request_url('MLI', start_date=start_date)

    truth = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
             'station%5B%5D=MLI&tz=UTC&year1=2019&month1=03&day1=24&hour1=12'
             '&minute1=00&year2=2019&month2=03&day2=26&hour2=12&minute2=00&'
             'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct'
             '&sample=1min&what=view&delim=comma&gis=yes')
    assert url ==truth


@recorder.use_cassette('ASOS_AMW_2018032512_2018032612')
@patch('meteogram.meteogram.current_utc_time')
def test_download_asos_data(mocked_current_utc_time):
    """Test downloading ASOS data."""
    mocked_current_utc_time.return_value = datetime.datetime(2018, 3, 26, 12)
    url = meteogram.build_asos_request_url('AMW')

    df = meteogram.download_asos_data(url)

    first_row_truth = pd.Series(
                      {'station_id': 'AMW',
                       'station_name': 'Ames',
                       'latitude_deg': 41.990439,
                       'longitude_deg': -93.618515,
                      # 'UTC': pd.Timestamp('2018-03-05 12:00:00'),
                       'temperature_degF': 29,
                       'dewpoint_degF': 24,
                       'wind_speed_knots': 8,
                       'wind_direction_degrees': 113})

    assert_dataseries_equal(df.iloc[0], first_row_truth)


@recorder.use_cassette('ASOS_AMW_Future')
def test_download_asos_data_in_future():
    """Test for correct behavior when asking for non-existant (future) data."""
    url = meteogram.build_asos_request_url('AMW',
                                           datetime.datetime(2999, 10, 10, 10),
                                           datetime.datetime(2999, 11, 10, 10))

    df = meteogram.download_asos_data(url)

    assert(len(df) == 0)


@recorder.use_cassette('ASOS_AMW_Reversed_Dates')
def test_download_asos_data_start_after_end():
    """Test for correct behavior when start and end times are reversed."""
    start = datetime.datetime(2018, 8, 1, 12)
    end = datetime.datetime(2018, 7, 1, 12)
    url = meteogram.build_asos_request_url('AMW', start, end)

    df = meteogram.download_asos_data(url)

    assert(len(df) == 0)


@pytest.mark.mpl_image_compare(remove_text=True)
@recorder.use_cassette('ASOS_AMW_2018032512_2018032612')
@patch('meteogram.meteogram.current_utc_time')
def test_plotting_meteogram_defaults(mocked_current_utc_time):
    """Test default meteogram plotting."""
    mocked_current_utc_time.return_value = datetime.datetime(2018, 3, 26, 12)
    url = meteogram.build_asos_request_url('AMW')

    df = meteogram.download_asos_data(url)

    fig, _, _ = meteogram.plot_meteogram(df)
    return fig
