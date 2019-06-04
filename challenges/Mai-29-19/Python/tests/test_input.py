import context
import pytest
from context import solution
from math import pi

###
# randomly plot points in the following frame then
# continue:
# -----------------
# |   _________   |
# |  /         \  |
# | |     ---r->| |
# |  \_________/  |
# |  <----2r--->  |
# -----------------
# areaOfSquare = (2r)^2 = 4r^2
# areaOfCircle = pi*r^2
# areaOfCircle / areaOfSquare = pi/4
# pi = 4 x ( number of dots in circle / all points )


def test_input():
    returned = True
    assert returned == True


def test_input2():
    returned = False
    assert returned == False
