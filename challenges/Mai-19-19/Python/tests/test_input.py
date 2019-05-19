import context
import pytest
from context import solution


def test_input():
    input_list = [3, 4, -1, 1]
    expected = 2
    result = solution.number_finder(input_list)
    assert result == expected

def test_inputRepeated2():
    input_list = [1,1,1,1,1,2]
    expected = 3
    result = solution.number_finder(input_list)
    assert result == expected
def test_inputRepeated():
    input_list = [1,1,1,1,1,1]
    expected = 2
    result = solution.number_finder(input_list)
    assert result == expected
def test_inputNeg():
    input_list = [-3,-2,-4]
    expected = 0
    result = solution.number_finder(input_list)
    assert result == expected
    
def test_input2():
    input_list = [1, 2, 0]
    expected = 3
    result = solution.number_finder(input_list)
    assert result == expected
