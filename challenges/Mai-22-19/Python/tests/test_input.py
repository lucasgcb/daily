import context
import pytest
from context import solution


def test_decodes():
    input = "111"
    returned = solution.decoder(input)
    expected = ['aaa','ak','ka']
    assert set(returned) == set(expected)


def test_input2():
    returned = False
    assert returned == False
