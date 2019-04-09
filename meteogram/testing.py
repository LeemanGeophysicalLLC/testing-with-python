import os.path

from numpy.testing import assert_almost_equal
import vcr


def assert_dataseries_equal(actual, desired):
    """
    Intelligently compare dataseries (i.e. dictionary) for testing.
    Only compares the keys that are in desired, i.e. there can be extra keys
    in actual and the test will pass. Handles comparison of floating points
    in a more intelligent way and does not require fields to be lined up in
    the same order.
    """
    for key in desired.keys():
        # If this is a float, then check accordingly
        if 'float' in str(type(desired.get(key))):
            assert_almost_equal(actual.get(key), desired.get(key))
        else:
            assert actual.get(key) == desired.get(key)


def get_recorder(test_file_path):
    """Return an appropriate response recorder for the given path."""
    return vcr.VCR(cassette_library_dir=os.path.join(os.path.dirname(
                                                     test_file_path),
                                                     'fixtures'))
