import context
import pytest
import time
from context import solution

## This is actually very VERY bad for implementing in pure Python 
## Because of the overhead. Find another language or make a C-extension :)

## The following is a sorry excuse for a scheduler, but I went for the bare minimum
## of what the requirements specified.
def test_input():
    def f():
        return 1

    milisec = 5
    expectedTime = 5 * 10**-3

    start = time.time()
    returned = solution.scheduler(f, milisec)
    end = time.time()
    length = (end - start)
    assert round(length,3) == expectedTime
    assert returned == 1


def test_input2():
    returned = False
    assert returned == False
