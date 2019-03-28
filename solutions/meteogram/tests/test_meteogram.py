"""Test use of the meteogram module."""

import datetime
from meteogram import meteogram

def test_current_utc_time():
    """Test that the current_utc_time function returns current time."""
    pass


def test_build_asos_request_url_single_digit_datetimes():
    """Test that data url building works with single digit datetimes."""
    start = datetime.datetime(2018, 1, 5, 1)
    end = datetime.datetime(2018, 1, 9, 1)
    station_id = 'FSD'

    url = meteogram.build_asos_request_url(station_id, start, end)

    truth = 'http'
    assert url ==truth


def test_build_asos_request_url_double_digit_datetimes():
    """Test that data url building works with double digit datetimes."""
    pass


def test_build_asos_request_url_all_defaults():
    """Test that data url building works with all default arguments."""
    pass


def test_build_asos_request_url_default_start_only():
    """Test that data url building works with default start argument."""
    pass


def test_build_asos_request_url_default_end_only():
    """Test that data url building works with default end argument."""
    pass


def test_download_asos_data():
    """Test downloading ASOS data."""
    pass


def test_download_asos_data_in_future():
    """Test for correct behavior when asking for non-existant (future) data."""
    pass


def test_download_asos_data_start_after_end():
    """Test for correct behavior when start and end times are reversed."""
    pass


def test_plotting_meteogram_defaults():
    """Test default meteofram plotting."""
    pass
