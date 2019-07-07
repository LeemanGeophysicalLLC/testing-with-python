<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
# Advanced PyTest

## Purpose
* Mock out requesting data from a web server.

## Recording URL Requests
We're still making url requests in a couple of tests and we would rather not
for reasons we're already discussed.

* Add to `testing.py` in the meteogram directory.

```python
from numpy.testing import assert_almost_equal
import vcr


def get_recorder(test_file_path):
    """Return an appropriate response recorder for the given path."""
    return vcr.VCR(cassette_library_dir=str(test_file_path / 'fixtures'))
```

* Add this to the top of our test file.

```python
from meteogram import meteogram
from meteogram.testing import get_recorder


recorder = get_recorder(Path(__file__).resolve().parent)
```

* Modify any functions calling out with the recorder.

```python
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
```

* Run the test suite and observe the creation of the fixture.

<div class="alert alert-success">
<b>Exercise 7</b>
  <ul>
    <li>Write a test using a cassette to check the behavior when we request
        data that are in the future. (Currently no error will be raised and
        we will say that we've decided that is acceptable behavior.)</li>
    <li>Write a test using a cassette to check the behavior when we request
        data, but mix up the start and end dates. (Currently no error will be
        raised and we will say that we've decided that is acceptable behavior.)
    </li>
  </ul>
</div>

#### Solution

```python
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
    assert df.empty

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
    assert df.empty

    # Cleanup - none necessary
```

[Home](index.html)
