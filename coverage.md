<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
# Coverage

Coverage tells us how much of our code is tested by the test suite. It is easy
to forget to test a branch, code path, or function/method when following the
"write it then test it" model (called "debug later" by James Grenning). There
is an alternative method of "Test Driven Development" or TDD for short, but
development strategies are really beyond the scope of what we're trying to do
here. Even when following the TDD methodology, a coverage check helps keep you
honest!

To check coverage we'll be using `pytest-cov`. It's simple to run from the
command line.

* Open a terminal (or Anaconda Prompt)
* Navigate to the root directory of the repository.
* Run `pytest --cov-report term-missing --cov=meteogram tests/` from
  the meteogram directory.

<div class="alert alert-success">
<b>Exercise 4</b>
  <ul>
    <li>Run a coverage check on our library. What holes do we have? Are there
        any you can repair with what we've learned so far? Try writing some
        tests to increase the coverage. You haven't learned techniques to test
        everything yet, but increase coverage where you can.</li>
  </ul>
</div>

#### Solution
```python
def test_current_utc_time():
    """Verify operation of utctime fetching (ignoring milliseconds)."""
    # Setup - none necessary

    # Exercise
    result = meteogram.current_utc_time()

    # Verify
    truth = datetime.datetime.utcnow()
    assert result.replace(microsecond=0) == truth.replace(microsecond=0)

    # Cleanup - none necessary


def test_potential_temperature():
    """Test potential temperature calculation with known result."""
    # Setup - none necessary

    # Exercise
    result = meteogram.potential_temperature(800, 273)

    # Verify
    truth = 290.96
    assert_almost_equal(result, truth, 2)

    # Cleanup - none necessary


def test_exner_function():
    """Test exner function calculation."""
    # Setup - none necessary

    # Exercise
    result = meteogram.exner_function(500)

    # Verify
    truth = 0.8203833
    assert_almost_equal(result, truth, 4)

    # Cleanup - none necessary
```

## Bonus
Add the `--flake8` flag and cleanup any errors seen there.

[Home](index.html)
