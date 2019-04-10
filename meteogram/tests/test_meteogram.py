"""Test use of the meteogram module."""

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

    # Cleanup - none necessary

#
# Instructor led introductory examples
#

#
# Instructor led examples of numerical comparison
#

#
# Exercise 1
#
def test_build_asos_request_url_single_digit_datetimes():
    """
    Test building URL with single digit month and day.
    """
    pass


def test_build_asos_request_url_double_digit_datetimes():
    """
    Test building URL with double digit month and day.
    """
    pass

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
# Instructor led mock example
#

#
# Exercise 3
#

#
# Exercise 3 - Stop Here
#

#
# Exercise 4 - Add any tests that you can to increase the library coverage.
# think of cases that may not change coverage, but should be tested
# for as well.
#

#
# Exercise 4 - Stop Here
#

#
# Instructor led example of image testing
#

#
# Exercise 5
#

#
# Exercise 5 - Stop Here
#

#
# Exercise 6
#

#
# Exercise 6 - Stop Here
#

#
# Exercise 7
#

#
# Exercise 7 - Stop Here
#

# Demonstration of TDD here (time permitting)
