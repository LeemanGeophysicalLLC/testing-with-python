<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

# Mocking

## Purpose
* Determine when mocks are useful
* Learn how to write a mock

### Mocking out functions
Let's modify the url builder again!

* Add a default of `None` to `start_date` and `end_date`.
* Add logic for what to do when they are none.

```python
def build_asos_request_url(station, start_date=None, end_date=None):
    # If there is no ending date specified, use the current date and time
    if end_date is None:
        end_date = current_utc_time()

    # If there is no starting date specified, use 24 hours before the ending date and time
    if start_date is None:
        start_date = end_date - datetime.timedelta(hours=24)
```

* What problems will we run into when trying to test this?
* Let's create a mock function to override our library `current_utc_time`.

```python
def mocked_current_utc_time():
    """
    Mock our utc time function for testing with defaults.
    """
    return datetime.datetime(2018, 3, 26, 12)
```

* Now let's use it on a test.

```python
from unittest.mock import patch

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
```

<div class="alert alert-success">
<b>Exercise 3</b>
  <ul>
    <li>Fill out the tests for the URL builder to test our new defaults.
        Use the mock as necessary.</li>
  </ul>
</div>

#### Solution
```python
@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_build_asos_request_url_defaults():
    """
    Test building URL with all defaults.
    """
    # Setup - none required

    # Exercise
    url = meteogram.build_asos_request_url('MLI')

    # Verify
    truth = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
             'station%5B%5D=MLI&tz=UTC&year1=2018&month1=03&day1=25&hour1=12'
             '&minute1=00&year2=2018&month2=03&day2=26&hour2=12&minute2=00&'
             'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct'
             '&sample=1min&what=view&delim=comma&gis=yes')
    assert url==truth

    # Cleanup - none required


@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_build_asos_request_url_default_start_only():
    """
    Test building URL with default start date.
    """
    # Setup
    end_date = datetime.datetime(2019, 3, 25, 12)

    # Exercise
    url = meteogram.build_asos_request_url('MLI', end_date=end_date)

    # Verify
    truth = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
             'station%5B%5D=MLI&tz=UTC&year1=2019&month1=03&day1=24&hour1=12'
             '&minute1=00&year2=2019&month2=03&day2=25&hour2=12&minute2=00&'
             'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct'
             '&sample=1min&what=view&delim=comma&gis=yes')
    assert url==truth

    # Cleanup - none required


@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_build_asos_request_url_default_end_only():
    """
    Test building URL with default end date.
    """
    # Setup
    start_date = datetime.datetime(2018, 3, 24, 12)

    # Exercise
    url = meteogram.build_asos_request_url('MLI', start_date=start_date)

    # Verify
    truth = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
             'station%5B%5D=MLI&tz=UTC&year1=2018&month1=03&day1=24&hour1=12'
             '&minute1=00&year2=2018&month2=03&day2=26&hour2=12&minute2=00&'
             'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct'
             '&sample=1min&what=view&delim=comma&gis=yes')
    assert url==truth

    # Cleanup - none required
```
