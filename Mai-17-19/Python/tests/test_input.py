import context
import pytest
from context import solution


def test_return_all_except():
    import copy
    the_input = [0,1,2,3,4,5]
    the_input_copy = copy.deepcopy(the_input)
    expected = [0,1,2,4,5]
    returned = solution.return_all_except(3,the_input)
    assert set(expected)==set(returned)
    assert set(the_input)==set(the_input_copy)

def test_input():
    the_input = [1,2,3,4,5]
    expected = [120,60,40,30,24]
    returned = solution.new_array(the_input)
    assert set(returned) == set(expected)

def test_input2():
    the_input = [3,2,1]
    expected = [2,3,6]
    returned = solution.new_array(the_input)
    assert set(returned) == set(expected)
def test_input_fail():
    the_input = [1,2,3,4,6]
    expected = [120,60,40,30,24]
    returned = solution.new_array(the_input)
    assert set(returned) != set(expected)


def test_input_extra():
    the_input = [1,2,3,4,5]
    expected = [120,60,40,30,24]
    returned = solution.new_array_no_division(the_input)
    assert set(returned) == set(expected)


def test_input2_extra():
    the_input = [3,2,1]
    expected = [2,3,6]
    returned = solution.new_array_no_division(the_input)
    assert set(returned) == set(expected)

def test_input_fail_extra():
    the_input = [1,2,3,4,6]
    expected = [120,60,40,30,24]
    returned = solution.new_array_no_division(the_input)
    assert set(returned) != set(expected)
