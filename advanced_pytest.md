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

```
pytest -k test_func_name --mpl-generate-path=tests/baseline
```

* Run the test with our nominal suite as `pytest --mpl`

<div class="alert alert-success">
<b>Exercise 5</b>
  <ul>
    <li>Modify the plotting function such that it has a keyword argument
    to plot horizontal lines (dashed) at N, S, E, W wind directions.</li>
    <li>Create a new image test, baseline image, and make sure the test suite
    passes.</li>
  </ul>
</div>

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
# TODO Write me!
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
# TODO Write me!
```

## Test Fixtures

<div class="alert alert-success">
<b>Exercise 7</b>
  <ul>
    <li>Make a fixture for testing our potential temperature calculation.
        We can assume that we'll have other tests that need "fake" temperature
        and pressure data, so this fixture will get reused.</li>
    <li>In fact, we do have another test that needs temperature data - refactor
        it to use the fixture.</li>
  </ul>
</div>

[Home](index.html)
