<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
# Checking for Raised Errors

## Purpose
* Learn how to test if errors are raised.

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
