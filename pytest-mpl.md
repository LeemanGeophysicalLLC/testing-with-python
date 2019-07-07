<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
# PyTest-MPL

## Purpose
* Learn how to use pytest-mpl for testing plots.

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

[Home](index.html)
