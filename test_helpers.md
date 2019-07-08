<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

# Test Helpers

## Purpose
* Write a test helper to reduce repeated code
* Implement this helper in our tests

## Writing a custom test helper
Sometimes we need to create a special test function to help us solve a specific
issue over and over. In this case, we're going to make a special test helper
that checks if the first row of a pandas dataframe is equal to one we specify
with the caveat that the row we are comparing to can have more columns or the
columns in a different order than our truth values. This is helpful when the
returned data may have more columns (i.e. a certain station may have a radiation
sensor and another may not).

* Create a place to put these - `testing.py` in the meteogram directory.

#### Instructor code

```python
from numpy.testing import assert_almost_equal
import pandas as pd


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
```

Now, let's write a test using that helper.

```python
from meteogram.testing import assert_dataseries_equal

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

```
