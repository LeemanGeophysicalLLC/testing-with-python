<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
# Test Fixtures

## Purpose
* Use fixtures to aid test setup and shared data.

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

[Home](index.html)
