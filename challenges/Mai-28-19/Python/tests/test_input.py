import context
import pytest
from context import solution


def test_input():
    k = 2
    s = "abcba"
    expected = "bcb"
    result = solution.find_longest(s,k)
    assert result == expected

def test_input2():
    k = 5
    s = "supercalifragilisticexpialidocious"
    expected = "gilisti"
    result = solution.find_longest(s,k)
    assert expected == result
    
    returned = False
    assert returned == False
