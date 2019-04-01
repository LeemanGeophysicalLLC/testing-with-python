"""Test use of the meteogram module."""

import pytest

from meteogram import meteogram


def test_build_asos_request_url_single_digit_datetimes():
    """
    Test building URL with single digit month and day.
    """
    # Setup
    # Exercise
    # Verify
    # Cleanup
    pass


def test_build_asos_request_url_double_digit_datetimes():
    """
    Test building URL with double digit month and day.
    """
    # Setup
    # Exercise
    # Verify
    # Cleanup
    pass

#
# Exercise 1 Stop Here
#

def test_build_asos_request_url_defaults():
    """
    Test building URL with all defaults.
    """
    # Setup
    # Exercise
    # Verify
    # Cleanup
    pass


def test_build_asos_request_url_default_start_only():
    """
    Test building URL with default start date.
    """
    # Setup
    # Exercise
    # Verify
    # Cleanup
    pass


def test_build_asos_request_url_default_end_only():
    """
    Test building URL with default end date.
    """
    # Setup
    # Exercise
    # Verify
    # Cleanup
    pass

#
# Exercise 2 Stop Here
#

def test_download_asos_data():
    """Test downloading ASOS data for station AMW with defaults."""
    # Setup
    # Exercise
    # Verify
    # Cleanup
    pass


def test_download_asos_data_in_future():
    """Test for correct behavior when asking for non-existant (future) data."""
    # Setup
    # Exercise
    # Verify
    # Cleanup
    pass


def test_download_asos_data_start_after_end():
    """Test for correct behavior when start and end times are reversed."""
    # Setup
    # Exercise
    # Verify
    # Cleanup
    pass

#
# Exercise 3 Stop Here
#

def test_plotting_meteogram_defaults(load_example_asos):
    """Test default meteogram plotting."""
    # Setup
    # Exercise
    # Verify
    # Cleanup
    pass

#
# Exercise 4 Stop Here
#
