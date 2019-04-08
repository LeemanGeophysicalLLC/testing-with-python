# Setup and Introductions

## Purpose
Ensure learner's systems are setup and that we have met.

## Meet Each Other
Ask attendees to *briefly* introduce themselves in 30 seconds on less telling us:
* Name
* Job/Function
* What they want from this course

## Introduce Sticky Note System
* **Green** - You are done with an exercise or ready to move on.
* **Red** - You need help - one of the instructors will be there shortly.
* Ask if there are any colorblind attendees that cannot differentiate the
  colors and offer to label the sticky notes.

## Setup/Startup
* Ensure that everyone has followed the setup instructions on the
  [course homepage](index.html).
* Open a terminal/Anaconda prompt
* Activate the environment: `conda activate python-testing`
* Anyone that has not followed the instructions needs to begin install ASAP so
  they do not fall behind.

## Why Testing?
* Untested code is broken code.
* Test across multiple Python versions, dev builds, operating systems, etc. with
  little to no effort.
* Make sure other dependencies are not breaking your code.
* Make changes with no fear of breakage.
* Verify to users and yourself that calculations match references (i.e. papers)
  from which they were implemented.

## Coding Philosophy
* **Code** is *what* your program does.
* **Comments** are *why* your program does what it does.
* **Tests** are *how* your program does what it does. They are documentation!

## Introduce the Example Library
We will be testing a simple library called meteogram that retrieves, performs
calculations on, and plots surface observations for meteorological stations.
Observations include parameters like temperature, pressure, dewpoint, wind speed,
wind direction, etc. Scientists often want to view all these data on a comprehensive
plot called a meteogram. See examples of meteograms
[here](http://www.mesonet.org/index.php/weather/meteogram/nrmn/).

This is a good problem to test because it provides the following test scenarios:
* URL data retrieval
* String comparison
* Numerical comparison
* Array comparison
* Image comparison

## Install Example Library
We need to install an editable instance of our meteogram library. To do so,
navigate to the top level of the repository and run the following:

```
pip install -e .
```

## Wrap Up
* What questions do you have before we get started?

[Home](index.html)
