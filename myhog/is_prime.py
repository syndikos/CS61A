#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:09:29 2017

@author: guilin
"""



def is_prime(num):
    """assumes num is a integer,
    if num is a prime number,returns True, else
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
    assert isinstance(num, int), "the number  is not an integer"
    assert num >= 0, "the number is negative"
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if remainder(num, i) == 0:
            return False
    return True

def remainder(dividend, divisor):
    """assumes dividend, divisor are integers,
    return the remainder of dividend divided bdivisor divisor
    >>> remainder(2, 3)
    2
    >>> remainder(4, 2)
    0
    """
    assert isinstance(dividend, int), "divisorour input must be an noninteger"
    assert divisor != 0, "divisor cannot be 0"
    while dividend > 0:
        dividend -= divisor
    if dividend == 0:
        return 0
    return dividend + divisor

def next_prime(num):
    """Returns the next prime number after num"""
    assert isinstance(num, int) and num >= 2, 'It has to be a positive integer\
    to find a next prime number'
    result = num + 1
    while not is_prime(result):
        result += 1
    return result

