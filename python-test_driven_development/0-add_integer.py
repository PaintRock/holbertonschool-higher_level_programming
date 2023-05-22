#!/usr/bin/python3
def add_integer(a, b=98)
"""a function that adds 2 integers"""


"""raises TypeError if either input is not an integer"""

if ((not isinstance(a, int) and not isinstance(a, float))):
    raise TypeError("a must be an integer")
if ((not isinstance (b, int) and not isinstance(a, float))):
    raise TypeError("b must be an integer")
return (a + b)
