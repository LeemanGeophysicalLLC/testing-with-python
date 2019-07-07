# Testing Philosophy

## Purpose
* Discuss some of the principles for best practices when testing code.

## Structure of a Test
* Tests should test one and only functionality in a way as independent of outside
  influences as possible.
* Tests should be as authentic as possible (don't test with only integers if
  most user data will be floating point).
* Tests should not depend on data external to the test framework
  (URLs, databases, etc)
* Tests should use all functionality of the testing harness to eliminate any
  "test smell" - just like code smell.}

### Goals of Testing
* Improve software quality
  * Act as a specification
  * Provide defect localization
  * Bug repellant
* Understand the system under test (SUT)
  * Act as documentation
* Reduce, not introduce, risk
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
  * **"api level"** testing only uses the public interface
  * **"layer crossing"** testing uses the public interface and monitors
    the back door
  * **"asynchronous"** testing interacts with external services
    (databases, remote servers) and should be avoided at all costs
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
