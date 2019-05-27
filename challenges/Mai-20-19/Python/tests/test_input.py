import context
import pytest
from context import solution


def test_cons():
    a = 3
    b = 4
    def pair(f):
        return f(a,b)
    result = solution.cons(a,b)
    assert isinstance(result,type(pair))

def test_car():
    expected = 3
    result = solution.car(solution.cons(3,4))
    assert result == expected

def test_cdr():
    expected = 4
    result = solution.cdr(solution.cons(3,4))
    assert result == expected


def test_car_alt():
    expected = 8
    result = solution.car_alt(solution.cons(8,7))
    assert result == expected

def test_cdr_alt():
    expected = 7
    result = solution.cdr_alt(solution.cons(8,7))
    assert result == expected
