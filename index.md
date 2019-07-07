<img src="assets/img/unit_testing.gif" alt="Testing Representation" align="left">

Every developer has heard the saying that “untested software is broken
software.” In this tutorial we will show you the best practices for software
testing in Python using the pytest framework. Learners will write tests for
several existing functions in a provided library, including testing strings,
integers, floats, lists, and arrays. We will also use the pytest-mpl library to
test matplotlib plotting functions with image comparison. Topics such as test
fixtures, parameterization, and test coverage will also be demonstrated.
Finally, students will implement new functionality in the example library and
employ test-driven-development practices.

This course is targeted at anyone writing code for their own scientific use or
for a scientific library and wants to learn effective ways to test that code.
Learners are expected to have a grasp on the Python language features, be able
to write functions, be able to create and run python scripts, and be comfortable
with the command line. Learners are also encouraged to have a GitHub account and
be comfortable with git, though it is not necessary for the core testing
materials that will be taught.

By the end of this tutorial, learners will be able to write tests for numerical
and string returning functions, write image tests for plotting functions, and
check the coverage of their existing codebase. This knowledge will equip them to
be able to implement a test suite on their new or legacy code bases.

**If you are planning on attending the course, please follow the "Before the
  Course" instructions below before you arrive and contact us with any questions
  or issues.**

## Prerequisite Skills
This is an **intermediate** skill level course. We assume that participants:
- Can create, edit, and run simple Python scripts unassisted.
- Understand basic Python language principles (dictionaries, functions, lists, etc.)
- Have a GitHub account.

## Course Outline
- [Setup and Introductions](setup.html)
  - Meet each other.
  - Ensure that all learner's machines are setup properly with course content
    downloaded and the environment created and activated.
  - Introduce the example library we will be testing during the course.
- Introduction to Testing
  - [Testing Basics](testing_basics.html)
  - [Testing Philosophy](testing_philosophy.html)
  - [Mocking](mocking.html)
  - [Test Helpers](test_helpers.html)
- Coverage
  - [Determining coverage](coverage.html)
- Advanced PyTest
  - [Image Testing](pytest-mpl.html)
  - [Fixtures](fixtures.html)
  - [Parameterization](parameterization.html)
  - [Mocking Web Requests](mocking_web_requests.html)
  - [Testing for Exceptions](error_testing.md)
- Test Driven Development
  - [Test Driven Development Introduction](TDD_intro.html)
- [Conclusion](conclusion.html)
  - Questions
  - Resources
  - Survey

## Before the Course
Planning on attending the workshop or going through this material on your own?
We recommend getting setup ahead of time to avoid any bandwidth issues at the
venue. In this short guide, we'll get your environment setup and running.

### Miniconda
We'll be using the conda package manager. So if you don't already have
Anaconda or Miniconda installed, that's the first step.

1. Head over to [https://conda.io/miniconda.html](https://conda.io/miniconda.html)
   and download the Python 3 installation for your operating system.
1. On Windows, run and follow the graphical installer. On Max/Linux, open a
   command prompt and run the command line installer:
   `bash Miniconda3-latest-MacOSX-x86_64.sh` (or whatever the filename of the
    script you downloaded is).
1. Restart your terminal on Mac/Linux.
1. Open a terminal on Mac/Linux or open the Anaconda Prompt on Windows.
1. Run `conda --version` and make sure that you are running at least conda
   4.5.X

If you're having issues, checkout the video tutorial below on installing conda.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-fOfyHYpKck"
 frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

### Environment
We've created and environment that has the dependencies we'll use during this
tutorial. It's in the repository for the tutorial, so we'll need to clone that
repository, then setup the environment. You'll be setting up your own repository
during the tutorial, so no need to fork this one, we just need some of the
content.

1. Clone the repository or download the ZIP file. Use the links on the left side
   of the page. If you opt for the zip option, unzip the folder.
1. Open a terminal (or Anaconda Prompt) and `cd` into the repository.
1. Create the environment with `conda env create` in the terminal/Anaconda
   prompt.
1. The instructions following installation completion tell you how to activate
   and deactivate the environment.

To learn more about conda environments, checkout the following video.
<iframe width="560" height="315" src="https://www.youtube.com/embed/15DNH25UCi0"
 frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

### Other Requirements
There are a just a couple of other things you'll want to do:
1. If you don't already have a GitHub account, sign up for one (free).
1. Make sure you are familiar with the git workflow. Checkout some of
   [these](https://try.github.io/) free resources.

## After the Course
After the course is complete, we encourage you to implement testing and basic
test driven practices in your software development cycle. You can always
contact us with questions!
