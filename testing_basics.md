<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

# Testing Basics

## Purpose
* Understand the structure of a test.
* Learn how to run tests.
* Learn how to check return values in tests.
* Write your own tests.

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
  * "round trip" testing only uses the public interface
  * "layer crossing" testing uses the public interface and monitors the back door
  * "asynchronous" testing interacts with real messaging and should be avoided at all costs
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
  desired = 'This Is A Yest String'

  # Exercise
  actual = input.title()

  # Verify
  assert(actual==desired)

  # Cleanup - automatically garbage collected
```

<span style="background-color:#28a745">
<b>Exercise</b>
<ul>
<li>Fill out the tests for the url builder function.</li>
</ul>
</span>

<div class="alert alert-success">
Testing bootstrap classes
</div>
### Numerical Comparison

### Array Comparison

## Exercise
We've shown you some tests and talked about how to structure them, now it's your
turn! We've provided descriptive test names in the commented out skeletons.
Write tests to the point that says "Stop here for testing basics exercise".

[Home](index.html)
