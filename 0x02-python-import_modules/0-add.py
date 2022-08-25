#!/usr/bin/python3
from add_0 import add

if _name_ == "_main_":
    """
    Prints the result of the addition between two numbers
    """
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
