#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:09:29 2017

@author: guilin
"""
def square(x):
    return x*x


def is_prime(x):
    """assumes x is a integer, 
    if x is a prime number,returns True, else
    returns False
    
    >>> is_prime(47)
    True
    
    >>> is_prime(2)
    True
    
    >>> is_prime(1)
    False
    
    >>> is_prime(0)
    False
    """
    
    assert type(x) == int, "the number  is not an integer"
    assert x >= 0, "the number is negative"
    
    if x < 2:
        return False
    if x == 2:
        return True
    
    for i in range(2, x):
        if square(i) > x:
            return True
        elif x % i == 0:
            return False

def remainder(x, y):
    """assumes x, y are integers,
    return the remainder of x divided by y
    
    >>> remainder(2, 3)
    2
    >>> remainder(4, 2)
    0
    """
    assert type(x) == type(y) == int, "your input has at least an noninteger"
    assert y != 0, "divisor cannot be 0"
    while x > 0:
        x =- y
    if x == 0:
        return 0
    return x + y

    
    
    
    
    