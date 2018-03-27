from fuzzylogic import *
profitable(10.)
def down(a, b, x):
    assert all(isinstance(val, float)
    for val in (a, b, x))
    return 1. -up(a, b, x)
