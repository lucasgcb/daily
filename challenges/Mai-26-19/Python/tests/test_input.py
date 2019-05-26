import context
import pytest
from context import solution


def test_input():
    query = 'de'
    wordSet = ['dog','deer','deal']
    expected = ['deer','deal']
    returned = solution.autocomplete(query,wordSet)
    assert set(returned) == set(expected)

