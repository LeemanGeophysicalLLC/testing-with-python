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
* Run `pytest --cov=myproj tests/`

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
# TODO Write me!
```

[Home](index.html)
