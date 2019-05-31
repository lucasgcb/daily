import context
import pytest
from context import solution


def test_Log_init():
    entries = {1:"2312", 2:"312321"}
    my_log = solution.Log(entries)
    assert set(entries) == set(my_log.entries)


def test_Log_record():
    entries = {1:"2312", 2:"312321"}
    new_entry = "36112"
    my_log = solution.Log(entries)
    my_log.record(new_entry)
    last = my_log.get_last(2) # Return 2nd last
    assert entries[2] == last

def test_Log_record2():
    entries = {1:"2312", 2:"312321"}
    new_entry = "36112"
    my_log = solution.Log(entries)
    my_log.record(new_entry)
    last = my_log.get_last() ## Empty returns the very last
    assert new_entry == last

def test_input2():
    returned = False
    assert returned == False
