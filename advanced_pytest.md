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
<b>Exercise</b>
  <ul>
    <li>Modify the plotting function such that it has a keyword argument
    to plot horizontal lines (dashed) at N, S, E, W wind directions.</li>
    <li>Create a new image test, baseline image, and make sure the test suite
    passes.</li>
  </ul>
</div>

## Test Parameterization

## Test Fixtures

[Home](index.html)
