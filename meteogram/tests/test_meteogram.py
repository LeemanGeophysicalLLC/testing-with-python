"""Test use of the meteogram module."""

import datetime
import os
from unittest.mock import patch

from numpy.testing import assert_almost_equal, assert_array_almost_equal
import numpy as np
import pytest

from meteogram import meteogram


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
    #`example_data_path = '/Users/johnleeman/gitrepos/testing-with-python/staticdata'
    data_path = os.path.join(example_data_path, 'AMW_example_data.csv')
    return meteogram.download_asos_data(data_path)


#
# Example starter test
#
def test_degF_to_degC_at_freezing():
    """
    Test if celsius conversion is correct at freezing.
    """
    # Setup
    freezing_degF = 32.0
    freezing_degC = 0.0

    # Exercise
    result = meteogram.degF_to_degC(freezing_degF)

    # Verify
    assert result == freezing_degC

    # Cleanup

#
# Instructor led introductory examples
#
def test_title_case():
    # Setup
    input = 'this is a test string'
    desired = 'This Is A Test String'

    # Exercise
    actual = input.title()

    # Verify
    assert actual==desired

  # Cleanup

#
# Instructor led examples of numerical comparison
#

def test_does_three_equal_three():
    assert 3==3


def test_floating_subtraction():
    # Setup
    desired = 1.5

    # Exercise
    actual = 3 - 1.5

    # Verify
    assert_almost_equal(actual, desired)

    # Cleanup - none necessary

#
# Exercise 2 - Add calculation tests here
#

def test_wind_components():
    # Setup
    speed = np.array([10, 10, 10, 0])
    direction = np.array([0, 45, 360, 45])

    # Exercise
    u, v = meteogram.wind_components(speed, direction)

    # Verify
    true_u = np.array([0, -7.0710, 0, 0])
    true_v = np.array([-10, -7.0710, -10, 0])
    assert_array_almost_equal(u, true_u, 3)
    assert_array_almost_equal(v, true_v, 3)

    # Cleanup

#
# Exercise 2 - Stop Here
#

#
# Instructor led mock example
#

@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_that_mock_works():
    """
    Test if we really know how to use a mock.
    """
    # Setup - None

    # Exercise
    result = meteogram.current_utc_time()

    # Verify
    truth = datetime.datetime(2018, 3, 26, 12)
    assert result==truth

    # Cleanup - none required

#
# Exercise 4 - Add any tests that you can to increase the library coverage.
# think of cases that may not change coverage, but should be tested for as well.
#

#
# Exercise 4 - Stop Here
#

#
# Instructor led example of image testing
#
@pytest.mark.mpl_image_compare(remove_text=True)
def test_plotting_meteogram_defaults(load_example_asos):
    """Test default meteogram plotting."""
    # Setup
    df = load_example_asos


    # Exercise
    fig, _, _, _ = meteogram.plot_meteogram(df)

    # Verify - Done by decorator when run with -mpl flag

    # Cleanup - none necessary

    return fig

#
# Exercise 5 - Modify plotting routine and add tests
#
@pytest.mark.mpl_image_compare(remove_text=True)
def test_plotting_meteogram_direction_fiducials(load_example_asos):
    """Test meteogram plotting with fiducial lines."""
    # Setup
    df = load_example_asos


    # Exercise
    fig, _, _, _ = meteogram.plot_meteogram(df, direction_markers=True)

    # Verify - Done by decorator when run with -mpl flag

    # Cleanup - none necessary

    return fig


#
# Exercise 6 - Refactor the URL builder tests that you can into a parameterized
#              test and put that here. Remove the old tests.
#
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

#
# Exercise 6 - Stop Here
#


#
# Exercise 7 - vcrpy, use it to record responses to data gathering tests.
#              modify the code already written above.
#

# Demonstration of TDD here (time permitting)
