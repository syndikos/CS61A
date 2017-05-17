#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:18:58 2017

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

    assert isinstance(x, int), "the number  is not an integer"
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
def next_prime(num):
    """Returns the first prime after num"""
    ans = num + 1
    if is_prime(ans):
        return ans
    return next_prime(num + 1)

def hogtimus(score):
        """If score is a prime, returns
        the next prime"""
        if is_prime(score):
            return next_prime(score)
        return score