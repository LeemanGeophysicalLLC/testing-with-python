<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

# Testing Basics

## Purpose
* Understand the structure of a test.
* Learn how to run tests.
* Learn how to check return values in tests.
* Write your own tests.
* Write a mock for out tests.

Tests in software are like rumble strips on the highway - they provide feedback
to the driver as early as possible when they depart their normal lane and gives
them time to correct the situation comfortably before they depart the road and
have an accident.

### Goals of Testing
* Improve software quality
  * Act as a specification
  * Provide defect localization
  * Bug repellant
* Understand the system under test (SUT)
  * Act as documentation
* Reduce, not introduce risk
  * Provide a safety net
  * Do no harm (no test logic in production)
* Be easy to run (and are run frequently)
  * Automated
  * Self-Checking (Hollywood Principle)
  * Repeatable
  * Independent
* Be easy to write and maintain
  * Simple
  * Expressive
  * Separation of Concerns
* Require minimal maintenance as the system evolves

> The effectiveness of the safety net is determined by how completely our tests
> verify the behavior of the system. Missing tests are like holes in the safety
> net. Incomplete assertions are like broken strands. Each gap in the safety net
> can let bugs of various sizes through. - Meszaros

Just like code can have smells, tests can have smells. If something stinks, it
should be changed and tests are no exception. Stinky test suites can become
brittle, untrusted, and expensive to maintain, defeating their purpose!

> "Writing good test code is hard, and maintaining obtuse test code is even
> harder." - Meszaros

## Testing Principles
* Write tests first (TDD)
* Design for testability
* Use the front door first
  * **"api level"** testing only uses the public interface
  * **"layer crossing"** testing uses the public interface and monitors
    the back door
  * **"asynchronous"** testing interacts with external services
    (databases, remote servers) and should be avoided at all costs
* Communicate intent
* Don't modify the SUT
* Keep tests independent
* Isolate the SUT
* Minimize test overlap
* Minimize untestable code
* Keep test logic out of production code
* Verify one condition per test
  * No alternating exercise/verify blocks
* Test concerns separately
* Ensure commensurate effort and responsibility
  * The effort to write the test shouldn't overshadow the effort to
    write the production code.

## Structure of a Test
* Tests should test one and only functionality in a way as independent of outside
  influences as possible.
* Tests should be as authentic as possible (don't test with only integers if
  most user data will be floating point).
* Tests should not depend on data external to the test framework
  (URLs, databases, etc)
* Tests should use all functionality of the testing harness to eliminate any
  "test smell" - just like code smell.

### The Four-Phase Test Pattern
The Four-Phase Test Pattern is described in Gerard Meszaros' book
["xUnit Testing Patterns"](https://amzn.to/2TjYE2O) and is a nice clear way to
structure your tests. It allows the reader to easily see what is being testing
and greatly increases the documentation value of the test.

1. **Setup** - Establish the preconditions to the test.
1. **Exercise** - Do something to the system.
1. **Verify** - Check the expected outcome.
1. **Cleanup** - Return the system under test to its initial state after the test.

## Running Tests
PyTest will automatically look for files named `test_*.py` or `*_test.py` and
from them run functions whose names begin with `test` and/or methods that
begin with `test` contained in classes that begin with `Test` and have no
`__init__`. There are some more custom configurations you can provide and the
full test discovery process is detailed
[here](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)
in the documentation.

### Run the existing test suite
* First, look at the tests file - with a single test currently.
* Remind students of the Four-Phase testing we are doing.
* Open a terminal (or Anaconda Prompt).
* Run the command `pytest` and let the suite run.
* Look at and explain the test report.
* Modify the test so that it will fail and show what that report looks like.

## Checking Return Values

All tests need to use a form of the `assert` statement which will pass if the
conditional is `True` and fail if it is `False`. This can be as simple as
`assert a==b` and we should be striving for simplicity!

### String Comparison
Comparing strings is done with a simple equality check.

```python
def test_title_case():
    # Setup
    input = 'this is a test string'
    desired = 'This Is A Test String'

    # Exercise
    actual = input.title()

    # Verify
    assert actual==desired

  # Cleanup
```

<div class="alert alert-success">
<b>Exercise 1</b>
  <ul>
    <li>Fill out the tests for the url builder function using what you know
    about string comparisons. The test names are descriptive enough that you
    already know what to do!</li>
  </ul>
</div>

#### Solution
```python
def test_build_asos_request_url_single_digit_datetimes():
    """
    Test building URL with single digit month and day.
    """
    # Setup
    start = datetime.datetime(2018, 1, 5, 1)
    end = datetime.datetime(2018, 1, 9, 1)
    station = 'FSD'

    # Exercise
    result_url = meteogram.build_asos_request_url(station, start, end)

    # Verify
    truth_url = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
                 'station%5B%5D=FSD&tz=UTC&year1=2018&month1=01&day1=05&hour1=01'
                 '&minute1=00&year2=2018&month2=01&day2=09&hour2=01&minute2=00&'
                 'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&'
                 'sample=1min&what=view&delim=comma&gis=yes')
    assert result_url == truth_url

    # Cleanup - none necessary


def test_build_asos_request_url_double_digit_datetimes():
    """
    Test building URL with double digit month and day.
    """
    # Setup
    start = datetime.datetime(2018, 10, 11, 12)
    end = datetime.datetime(2018, 10, 16, 15)
    station = 'MLI'

    # Exercise
    result_url = meteogram.build_asos_request_url(station, start, end)

    # Verify
    truth_url = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
                 'station%5B%5D=MLI&tz=UTC&year1=2018&month1=10&day1=11&hour1=12'
                 '&minute1=00&year2=2018&month2=10&day2=16&hour2=15&minute2=00&'
                 'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&'
                 'sample=1min&what=view&delim=comma&gis=yes')
    assert result_url == truth_url

    # Cleanup - none necessary
```

### Numerical Comparison
Numerical comparisons are a common place that new testers start getting into
trouble. Testing integers is straightforward:

```python
def test_does_three_equal_three():
    assert 3==3
```

Trouble begins immediately when we leave the integer world though! Floating
point comparisons are fraught with peril. If you really want to get into why
there is a lot of light bedtime reading about the IEEE 754 specification and
how machine precision results in small rounding errors. For our purposes we
will simply say that this is **NOT** a safe thing to do:

```python
def test_floating_subtraction():
  # Setup
  desired = 0.293

  # Exercise
  actual = 1 - 0.707

  # Verify
  assert actual==desired

  # Cleanup
```

The best way to deal with this is to add a tolerance check, something like:

```python
def test_floating_subtraction():
    # Setup
    desired = 0.293

    # Exercise
    actual = 1 - 0.707

    # Verify
    assert(abs(actual-desired) < 0.00001)

    # Cleanup
```

That would result in too much logic and duplicated code in our tests and seems
like a solved problem right? Numpy has a testing helper for exactly this:
`np.testing.assert_almost_equal`.

Now our test can simplify to:
```python
from np.testing import assert_almost_equal


def test_floating_subtraction():
    # Setup
    desired = 1.5

    # Exercise
    actual = 3 - 1.5

    # Verify
    assert_almost_equal(actual, desired)

    # Cleanup - none necessary
```

<div class="alert alert-success">
<b>Exercise 2</b>
  <ul>
    <li>Add a function to the library to calculate the vector components u, v
        of wind given a windspeed and direction.</li>
    <li>Write tests to verify proper behavior for directions of 0, 180, 360, and
        for a windspeed of zero.</li>
  </ul>
</div>

#### Solution
```python
def wind_components(speed, direction):
    """
    Calculate the U, V wind vector components from the speed and direction.

    Parameters
    ----------
    speed : array_like
        The wind speed (magnitude)
    wdir : array_like
        The wind direction, specified as the direction from which the wind is
        blowing (0-360 degrees), with 360 degrees being North.

    Returns
    -------
    u, v : tuple of array_like
        The wind components in the X (East-West) and Y (North-South)
        directions, respectively.

    """
    direction = np.radians(direction)
    u = -speed * np.sin(direction)
    v = -speed * np.cos(direction)
    return u, v

```

```python
def test_wind_components_north():
    # Setup
    speed = 10
    direction = 0

    # Exercise
    u, v = meteogram.wind_components(speed, direction)

    # Verify
    true_u = 0
    true_v = -10
    assert_almost_equal(u, true_u)
    assert_almost_equal(v, true_v)

def test_wind_components_northeast():
    # Setup
    speed = 10
    direction = 45

    # Exercise
    u, v = meteogram.wind_components(speed, direction)

    # Verify
    true_u = -7.0710
    true_v = -7.0710
    assert_almost_equal(u, true_u, 3)
    assert_almost_equal(v, true_v, 3)


def test_wind_components_threesixty():
    # Setup
    speed = 10
    direction = 360

    # Exercise
    u, v = meteogram.wind_components(speed, direction)

    # Verify
    true_u = 0
    true_v = -10
    assert_almost_equal(u, true_u)
    assert_almost_equal(v, true_v)


def test_wind_components_zero_wind():
    # Setup
    speed = 0
    direction = 45

    # Exercise
    u, v = meteogram.wind_components(speed, direction)

    # Verify
    true_u = 0
    true_v = 0
    assert_almost_equal(u, true_u)
    assert_almost_equal(v, true_v)

    # Cleanup
```


### Array Comparison

Array comparisons are much like integer and floating point comparisons.
In this case we're going to use `np.testing.assert_array_almost_equal` to
cleanup our tests we just wrote.

<div class="alert alert-warning">
<b>Instructor Led</b>
  <ul>
    <li>Add the needed import.</li>
    <li>Refactor the four tests just written into a single test using array
        comparison.</li>
  </ul>
</div>

#### Instructor Code
```python
from numpy.testing import assert_almost_equal, assert_array_almost_equal


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
```

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

[Home](index.html)
