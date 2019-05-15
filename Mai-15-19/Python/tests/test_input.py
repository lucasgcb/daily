import context
import pytest
from context import solution

def test_sums():
    the_list = [10, 15, 3, 7]
    expected_sums = [25,13,17,18,22,10]
    sums = solution.possible_sums(the_list)
    assert set(expected_sums) == set(sums)


def test_input():
    k = 17
    the_list = [10, 15, 3, 7]
    returned = solution.adds_up(the_list, k)
    assert returned == True


def test_input2():
    k = 16
    the_list = [10, 15, 3, 7]
    returned = solution.adds_up(the_list, k)
    assert returned == False

def test_input3():
    k = 20
    the_list = [10, 15, 3, 7, 10]
    returned = solution.adds_up(the_list, k)
    assert returned == True
