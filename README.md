# assertive
the amazing 50-loc Python test framework

# Installing

Either git clone, download or paste the contents of `runner.py` into a new file tab of a code editr.

# Usage

Annotate tests as follows:

```py
runner import assertive
from random import randint 

@assertive
def test_twice_is_bigger():
    "Test whether 2*x is bigger than x"
    
    x = randint(1,10)
    assert 2*x > x
    
@assertive
def test_twice_is_odd():
    "Test whether twice any number is odd"
    x = randint(1,10)
    assert (2*x) % 2 == 1
    
```

And run them as follows:

```py
from runner import run_tests, print_traceback_log

if __name__ == '__main__':
    results = run_tests()
    # The following is how I like to summarize my results
    print("------------")
    count = sum(results.values())
    total = len(results)
    ok = (count / total)
    print(f"{100*ok:.1f}% OK\n\n")
    
    # I also like to inspect the traceback logs of failed tests.
    if ok < 1:
        print_traceback_log()

```

The output of this script is:

```
test_twice_is_bigger Test whether 2*x is bigger than x OK
test_twice_is_odd Test whether twice any number is odd FAILED
------------
50.0% OK


-----------------
test_twice_is_odd Test whether twice any number is odd
Traceback (most recent call last):
  File "/home/xheimlich/smuckles/tests/runner.py", line 28, in wrapper
    func(*args, **kwargs)
  File "/home/xheimlich/smuckles/tests/faux.py", line 15, in test_twice_is_odd
    assert (2*x) % 2 == 1
AssertionError
```
