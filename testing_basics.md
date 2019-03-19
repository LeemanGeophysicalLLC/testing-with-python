# Testing Basics

## Purpose
* Understand the structure of a test.
* Learn how to run tests.
* Learn how to check return values in tests.
* Write your own tests.

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

Let's look at an example of the Four-Phase Test Pattern in action. **Instructor:
write this out on the board or type in editor in no board available.**

Here's a simple function to test:
```python
def degc_to_degf(degc):
  return degc * (9 / 5) + 32
```

Here's the test for it following the Four-Phase Test Pattern:
```python
def test_degc_to_degf_scalar():
  # Setup
  deg_c_value = 22.0
  truth_value = 71.6  # From Jones et al. (1971)

  # Exercise
  res = degc_to_degf(deg_c_value)

  # Verify
  assert(res == truth_value)

  ## Cleanup - None in this case.
```

## Running Tests
PyTest will automatically look for files named `test_*.py` or `*_test.py` and
from them run functions whose names begin with `test` and/or methods that
begin with `test` contained in classes that begin with `Test` and have no
`__init__`. There are some more custom configurations you can provide and the
full test discovery process is detailed
[here](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)
in the documentation.

### Run the existing test suite
* First, look at the tests that are written and how we've broken it up.
* Remind students on the Four-Phase testing we are doing.
* Open a terminal (or Anaconda Prompt).
* Run the command `pytest` and let the suite run.
* Look at and explain the test report.
* Modify a test so that it will fail and show what that report looks like.

## Checking Return Values

### String Comparison

### Numerical Comparison

### Array Comparison

## Exercise
We've show you some tests and talked about how to structure them, now it's your
turn! Write tests for the foo, bar, and zorp functions of the meteogram library.
