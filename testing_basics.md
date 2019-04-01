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
* Robust testing and test design

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
  * **"round trip"** testing only uses the public interface
  * **"layer crossing"** testing uses the public interface and monitors the back door
  * **"asynchronous"** testing interacts with real messaging and should be avoided at all costs
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
* Tests should not depend on external data (URLs, databases, etc)
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
* First, look at the tests file - with a single test currently implemented.
* Remind students of the Four-Phase testing we are doing.
* Open a terminal (or Anaconda Prompt).
* Run the command `pytest` and let the suite run.
* Look at and explain the test report.
* Modify the test so that it will fail and show what that report looks like.

## Checking Return Values

All tests need to use a form of the `assert` statement which will pass if the
condition inside is `True` and fail if it is `False`. This can be as simple as
`assert(a==b)` and we should be striving for simplicity!

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
  assert(actual==desired)

  # Cleanup - automatically garbage collected
```

<div class="alert alert-success">
<b>Exercise</b>
  <ul>
    <li>Fill out the tests for the url builder function using what you know
    about string comparisons. The test names are descriptive enough that you
    already know what to do!</li>
  </ul>
</div>

### Numerical Comparison
Numerical comparisons are a common place that new testers start getting into
trouble. Testing integers is straightforward:

```python
assert(3==3)
```

Trouble begins immediately when we leave the integer world though! Floating
point comparisons are fraught with peril. If you really want to get into why
there is a lot of light bedtime reading about the IEEE 754 specification and
how machine precision results in small rounding errors. For our purposes we
will simply say that this is **NOT** a safe thing to do:

```python
def test_floating_subtraction():
  # Setup
  desired = 1.5

  # Exercise
  actual = 3 - 1.5

  # Verify
  assert(actual==desired)

  # Cleanup - automatically garbage collected
```

The best way to deal with this is to add a tolerance check, something like:

```python
def test_floating_subtraction():
    # Setup
    desired = 1.5

    # Exercise
    actual = 3 - 1.5

    # Verify
    assert(abs(actual-desired) < 0.00001)

    # Cleanup - automatically garbage collected
```

That would result in too much logic and duplicated code in our tests and seems
like a solved problem right? Numpy has a testing helper for exactly this:
`np.testing.assert_almost_equal`. Instead of calling that every time, we're
going to wrap it in a testing helpers module of meteogram.

* Create `testing.py` in the `meteogram` directory.
* Add this function:

```python
import numpy as np


def assert_almost_equal(actual, desired, decimal=7):
    """Check that values are almost equal.
    Wrapper around :func:`numpy.testing.assert_almost_equal`
    """
    np.testing.assert_almost_equal(actual, desired, decimal)
```

Now our test can simplify to:
```python
from meteogram.testing import assert_almost_equal


def test_floating_subtraction():
    # Setup
    desired = 1.5

    # Exercise
    actual = 3 - 1.5

    # Verify
    assert_almost_equal(actual, desired)

    # Cleanup - automatically garbage collected
```

<div class="alert alert-success">
<b>Exercise</b>
  <ul>
    <li>Fill out the test for a simple temperature conversion. Test the value
    of 32&deg;F.</li>
  </ul>
</div>

### Array Comparison

Array comparisons are much like floating point. In this case we're going to
add functionality to compare if the arrays are almost equal to get around
the same floating point issue we just tackled.

<div class="alert alert-success">
<b>Exercise</b>
  <ul>
    <li>Write a wrapper for the numpy testing function
    numpy.testing.assert_array_almost_equal called assert_array_almost_equal.</li>
    <li>Create a new test (we didn't provide a skeleton here!) that checks the
    temperature conversion on an array of temperatures: -40, 32, and 40&deg;F</li>
  </ul>
</div>

### Mocking out functions
Let's modify the url builder again!

* Add a default of `None` to `start_date` and `end_date`.
* Add logic for what to do when they are none.

```python
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
def test_the_thing():
```

<div class="alert alert-success">
<b>Exercise</b>
  <ul>
    <li>Finish writing and modifying the tests for the URL builder.</li>
  </ul>
</div>

[Home](index.html)
