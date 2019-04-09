<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
# Advanced PyTest

## Purpose
* Learn how to use pytest-mpl for testing plots.
* Use parameterization to clean up test smells.
* Use fixtures to aid test setup and shared data.

## Testing Plots
Often we want to ensure that our methods to plot data continue working in the
same way. This is especially useful for ensuring that we catch when other
libraries change defaults. To do this we create and store baseline images that
we will compare against.

* Create a test function that returns a figure.

* We then run the test function and store the output in a baselines directory
  in our tests directory.

#### Instructor Code

```python
@pytest.mark.mpl_image_compare(remove_text=True)
def test_plotting_meteogram_defaults():
    """Test default meteogram plotting."""
    # Setup
    url = meteogram.build_asos_request_url('AMW',
                                           start_date=datetime.datetime(2018, 3, 26),
                                           end_date=datetime.datetime(2018, 3, 27))
    df = meteogram.download_asos_data(url)


    # Exercise
    fig, _, _, _ = meteogram.plot_meteogram(df)

    # Verify - Done by decorator when run with -mpl flag

    # Cleanup - none necessary

    return fig
```

```
pytest -k test_plotting_meteogram_defaults --mpl-generate-path=tests/baseline
```

* Run the test with our nominal suite as `pytest --mpl`

<div class="alert alert-success">
<b>Exercise 5</b>
  <ul>
    <li>Modify the plotting function such that it has a keyword argument
    to plot horizontal lines (dashed) at N, S, E, W wind directions.
    This keyword argument should default to false.</li>
    <li>Create a new image test, baseline image, and make sure the test suite
    passes.</li>
  </ul>
</div>

#### Solution

```python
# Add direction lines if requested
if direction_markers:
    for value_degrees in [0, 90, 180, 270]:
        ax2b.axhline(y=value_degrees, color='k', linestyle='--', linewidth=0.25)
```

```python
@pytest.mark.mpl_image_compare(remove_text=True)
def test_plotting_meteogram_direction_fiducials():
    """Test meteogram plotting with fiducial lines."""
    # Setup
    url = meteogram.build_asos_request_url('AMW',
                                           start_date=datetime.datetime(2018, 3, 26),
                                           end_date=datetime.datetime(2018, 3, 27))
    df = meteogram.download_asos_data(url)


    # Exercise
    fig, _, _, _ = meteogram.plot_meteogram(df, direction_markers=True)

    # Verify - Done by decorator when run with -mpl flag

    # Cleanup - none necessary

    return fig
```

## Test Fixtures
Test fixtures are a good way to encapsulate data or setup needs that are used
for multiple tests. We've got plotting tests that we just wrote that are
currently making calls to the web to get plotting data. That isn't great as
we are depending on external contact. What if a server goes down, what if the
tests are run on a machine with no network connection, what if we don't want to
make API calls because they are expensive? Let's make this a fixture instead.


Make the fixture by downloading the data for a `staticdata` directory in the
top level of the repo. Data are [here](https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?station%5B%5D=AMW&tz=UTC&year1=2018&month1=03&day1=26&hour1=00&minute1=00&year2=2018&month2=03&day2=27&hour2=00&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes).

```python
from pathlib import Path

@pytest.fixture
def load_example_asos():
    """
    Fixture to load example data from a csv file for testing.
    """
    example_data_path = Path(__file__).resolve().parent / '..' / '..' / 'staticdata'
    data_path = example_data_path / 'AMW_example_data.csv'
    return meteogram.download_asos_data(data_path)
```

Modify the test functions to use our fixture.

```python
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

```


## Test Parameterization
Parameterizing tests is a good way to run the same test multiple times with
different inputs. You might be thinking that this breaks the rule about a test
only testing a single thing, but in fact the test does only test a single
thing - we are just reusing the bulk of the code as the inputs/expected outputs
are the only things that differ. This actually eliminates test smell and makes
modifying the tests if the API changes in the future much faster as we are only
modifying a single test.

<div class="alert alert-warning">
<b>Instructor Led</b>
  <ul>
    <li>Show how parameterization works.</li>
    <li>Make a single url builder parameterized test.</li>
  </ul>
</div>

#### Instructor Written Code
```python
@pytest.mark.parametrize('start, end, station, expected', [
    # Single Digit Datetimes
    (datetime.datetime(2018, 1, 5, 1), datetime.datetime(2018, 1, 9, 1),
     'FSD',
     'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
     'station%5B%5D=FSD&tz=UTC&year1=2018&month1=01&day1=05&hour1=01'
     '&minute1=00&year2=2018&month2=01&day2=09&hour2=01&minute2=00&'
     'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&'
     'sample=1min&what=view&delim=comma&gis=yes')
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

```

<div class="alert alert-success">
<b>Exercise 6</b>
  <ul>
    <li>Using parameterization, finish refactoring the url builder tests that
        make sense to reduce test smell.</li>
  </ul>
</div>

#### Solution
```python
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
```

## Recording URL Requests
We're still making url requests in a couple of tests and we would rather not
for reasons we're already discussed.

* Add to `testing.py` in the meteogram directory.

```python
import os.path

import vcr


def get_recorder(test_file_path):
    """Return an appropriate response recorder for the given path."""
    return vcr.VCR(cassette_library_dir=os.path.join(os.path.dirname(test_file_path),
                                                     'fixtures'))
```

* Add this to the top of our test file.

```python
from meteogram import meteogram
from meteogram.testing import get_recorder


recorder = get_recorder(__file__)
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

## Checking for Raised Errors
In retrospect, silently returning nothing when the user switches the start
and end dates seems like poor behavior and we should warn them that they are
making a malformed request. We would typically do that by raising an exception.

#### Instructor Code
Modify the `build_asos_request_url` function to raise an error when the dates
are switched (put right above string building):

```python
# Make sure the starting and ending dates are not reversed
if start_date > end_date:
    raise ValueError('Start date cannot be after end date.')
```

Now we need to change our test to verify that the `ValueError` is raised. Don't
forget to remove the now unused fixture.

```python
def test_download_asos_data_start_after_end():
    """Test for correct behavior when start and end times are reversed."""
    # Setup
    start = datetime.datetime(2018, 8, 1, 12)
    end = datetime.datetime(2018, 7, 1, 12)

    # Exercise/Verify
    with pytest.raises(ValueError):
        meteogram.build_asos_request_url('AMW', start, end)
    # Cleanup - none necessary

```

[Home](index.html)
