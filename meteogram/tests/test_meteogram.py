"""Test use of the meteogram module."""

import pytest

from meteogram import meteogram


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

#
# Exercise 1 - Fill out the following test cases
#

# def test_build_asos_request_url_single_digit_datetimes():
#     """
#     Test building URL with single digit month and day.
#     """
#     # Setup
#     # Exercise
#     # Verify
#     # Cleanup
#     pass
#
#
# def test_build_asos_request_url_double_digit_datetimes():
#     """
#     Test building URL with double digit month and day.
#     """
#     # Setup
#     # Exercise
#     # Verify
#     # Cleanup
#     pass

#
# Exercise 1 - Stop Here
#

#
# Exercise 2 - Add calculation tests here
#

#
# Exercise 2 - Stop Here
#

#
# Exercise 3 - Fill out theses tests using our mock when necessary
#

# def test_build_asos_request_url_defaults():
#     """
#     Test building URL with all defaults.
#     """
#     # Setup
#     # Exercise
#     # Verify
#     # Cleanup
#     pass
#
#
# def test_build_asos_request_url_default_start_only():
#     """
#     Test building URL with default start date.
#     """
#     # Setup
#     # Exercise
#     # Verify
#     # Cleanup
#     pass
#
#
# def test_build_asos_request_url_default_end_only():
#     """
#     Test building URL with default end date.
#     """
#     # Setup
#     # Exercise
#     # Verify
#     # Cleanup
#     pass

#
# Exercise 3 - Stop Here
#

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

#
# Exercise 5 - Modify plotting routine and add tests
#

#
# Exercise 6 - Refactor the URL builder tests that you can into a parameterized
#              test and put that here. Remove the old tests.
#

#
# Exercise 6 - Stop Here
#

#
# Exercise 7 - Make a fixture for testing calculations
#

#
# Exercise 7 - Stop Here
#

#
# Exercise 8 - vcrpy, use it to record responses to data gathering tests.
#              modify the code already written above.
#

# Demonstration of TDD here (time permitting)
