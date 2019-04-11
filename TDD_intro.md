# Test Driven Development Introduction

## Purpose
* Demonstrate how to implement a new feature with a TDD methodology.

With Test Driven Development (TDD), the tests serve as a sort of specification
for the software. This means we can separate our approach to coding into two
phases : what the code should do (writing the test from the specification) and
how the code should do it (writing the actual production code).

## Advantages
* Fewer bugs
* Less debug time
* Fewer side effect defects
* Documentation does not lie
* Peace of mind
* Production code tends to be more minimalist (YAGNI principle)
* Progress monitor
* According to James Grenning "Fun and rewarding"

## Red-Green-Refactor
When writing your tests and code you should follow the red-green-refactor
pattern.

* Red - you wrote the test first and it should fail!
* Green - write the least amount of code that makes the test pass.
* Refactor - you likely added code and the functionality might be ready for a
  refactor. If it is, do it now and keep the tests green. That way you know you
  didn't break things and caught bugs ahead of time!

## Workflow
* You have functionality to implement and pull your ticket off the job board.
  It's helpful to write a test list first to anticipate some of the corner cases
  you might encounter and get an idea of the interface.
* Write the first test.
* Make it pass. Don't let the code get ahead of the tests!
* Repeat

## Bob Martin's Three Laws of TDD
1. You are not allowed to write any production code unless it is to make a
   failing unit test pass.
1. You are not allowed to write any more of a unit test than is sufficient to
   fail; and compilation failures are failures.
1. You are not allowed to write any more production code than is sufficient to
   pass the one failing unit test.
You can read more of Uncle Bob's explanation
[here](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd).

## Let's try it
Now it's our turn to implement new functionality using TDD! In our case we want
to implement a running average class that we can use to keep track of the best
estimate of current temperature from a noisy station.

Yes, this is a bit of a contrived example, but without needing to build up hours
of other functionality, it will do!

### Requirements
* Must compute the average of `n` datapoints with our most recent observation as
  the last point. (i.e. a 10 point average would use the most recent observation
  and the previous 9.)
* Have a method to provide a new data point one point at a time.
* Have a method to calculate the average
* When starting from a fresh start with no prior data, return the average of all
  data until we have at least `n` points.

### Make a test list
* Is initialized to an empty list
* Number of points attribute is zero on initialization
* Test adding a datapoint when empty
* Test adding a datapoint when partially full
* Test removing the oldest datapoint
* Test adding a datapoint when full
* Returns correct average for 1 data point
* Returns correct average for n-1 data points
* Returns correct average for n data points
* Returns correct average for n+1 data points
* Returns correct average after 2n data points

### Start going through the list

#### test_is_list_initialized_to_empty
```python
def test_is_list_initialized_to_empty():
    """Test if the data list is empty after initialization."""
    avg = averager()

    assert avg.data == []
```

```python
class averager(object):
    def __init__(self):
        self.data = []
```

#### test_number_of_points_is_zero_on_initialization
```python
def test_number_of_points_is_zero_on_initialization():
    """Test that the number of data points is zero on initialization."""
    avg = averager()

    assert avg.number_of_data_points == 0
```

```python
class averager(object):
    def __init__(self):
        self.data = []
        self.number_of_data_points = 0
```

#### test_adding_datapoint_to_empty
```python
def test_adding_datapoint_to_empty():
    """Test adding a datapoint to an empty instance."""
    avg = averager()

    avg.add_data(1)

    assert avg.data == [1]
    assert avg.number_of_data_points == 1
```

```python
class averager(object):
    def __init__(self):
        self.data = []
        self.number_of_data_points = 0

    def add_data(self, datapoint):
        self.data.append(datapoint)
        self.number_of_data_points = 1
```

#### test_adding_datapoint_to_partially_full
```python
def test_adding_datapoint_to_partially_full():
    """Test adding a datapoint to a partially full instance."""
    avg = averager()

    avg.add_data(1)
    avg.add_data(2)
    avg.add_data(3)

    assert avg.data == [1, 2, 3]
    assert avg.number_of_data_points == 3
```

```python
class averager(object):
    def __init__(self):
        self.data = []
        self.number_of_data_points = 0

    def add_data(self, datapoint):
        self.data.append(datapoint)
        self.number_of_data_points += 1
```

#### test_remove_first_point
```python
def test_remove_first_point():
    """Test removing the first point from the list."""
    avg = averager(3)
    avg.add_data(1)
    avg.add_data(2)
    avg.add_data(3)

    avg.remove_first_point()

    assert avg.data == [2, 3]
    assert avg.number_of_data_points == 2
```

```python
class averager(object):
    def __init__(self):
        self.data = []
        self.number_of_data_points = 0

    def add_data(self, datapoint):
        self.data.append(datapoint)
        self.number_of_data_points += 1

    def remove_first_point(self):
        self.data.pop(0)
        self.number_of_data_points -= 1
```

#### test_adding_datapoint_to_full
```python
def test_adding_datapoint_to_full():
    avg = averager(3)

    for i in range(1, 5):
        avg.add_data(i)

    assert avg.data == [2, 3, 4]
    assert avg.number_of_data_points == 3
```

```python
class averager(object):
    def __init__(self, npts_average):
        self.data = []
        self.number_of_data_points = 0
        self.npts_average = npts_average

    def add_data(self, datapoint):
        self.data.append(datapoint)
        self.number_of_data_points += 1

        if self.number_of_data_points > self.npts_average:
            self.remove_first_point()

    def remove_first_point(self):
        self.data.pop(0)
        self.number_of_data_points -= 1
```

#### test_average_for_one_data_point
```python
def test_average_for_one_data_point():
    avg = averager(3)
    avg.add_data(5)

    average = avg.running_mean()

    assert average == 5
```

```python
class averager(object):
    def __init__(self, npts_average):
        self.data = []
        self.number_of_data_points = 0
        self.npts_average = npts_average

    def add_data(self, datapoint):
        self.data.append(datapoint)
        self.number_of_data_points += 1

        if self.number_of_data_points > self.npts_average:
            self.remove_first_point()

    def remove_first_point(self):
        self.data.pop(0)
        self.number_of_data_points -= 1

    def running_mean(self):
        return 5
```

#### test_average_for_n_minus_one_data_points
```python
def test_average_for_n_minus_one_data_points():
    avg = averager(3)
    avg.add_data(5)
    avg.add_data(7)

    average = avg.running_mean()

    assert average == 6
```

```python
class averager(object):
    def __init__(self, npts_average):
        self.data = []
        self.number_of_data_points = 0
        self.npts_average = npts_average

    def add_data(self, datapoint):
        self.data.append(datapoint)
        self.number_of_data_points += 1

        if self.number_of_data_points > self.npts_average:
            self.remove_first_point()

    def remove_first_point(self):
        self.data.pop(0)
        self.number_of_data_points -= 1

    def running_mean(self):
        return sum(self.data) / self.number_of_data_points
```

#### test_average_for_n_data_points
```python
def test_average_for_n_data_points():
    avg = averager(3)
    avg.add_data(5)
    avg.add_data(7)
    avg.add_data(9)

    average = avg.running_mean()

    assert average == 7
```

```python
# No change to production code - be very careful here!
```

#### test_average_for_n_plus_one_data_points
```python
def test_average_for_n_plus_one_data_points():
        avg = averager(3)
        avg.add_data(5)
        avg.add_data(7)
        avg.add_data(9)
        avg.add_data(11)

        average = avg.running_mean()

        assert average == 9
```

```python
# No change again, but the expected result if this failed would be 8
```

#### test_average_for_2n_data_points
```python
def test_average_for_2n_data_points():
    avg = averager(3)
    for i in range(1, 7):
        avg.add_data(i)

    average = avg.running_mean()

    assert average == 5
```

```python
# No change!
```

### What did we miss?
Can you think of cases we missed? What about removing data from a zero length
dataset? What about a zero length average?

[Home](index.html)
