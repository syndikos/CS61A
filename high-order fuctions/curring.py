#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:22:18 2017

@author: guilin
"""

def curried_pow(x):
    """example of curring
    
    >>> curried_pow(2)(3)
    8
    """
    def h(y):
        return pow(x, y)
    return h

def map_to_range(start, end, f):
    """apply f to each number from start to end
    start: integer, the first number
    end: integer, the end number
    f: a function
    
    >>> map_to_range(0, 10, curried_pow(2))
    1
    2
    4
    8
    16
    32
    64
    128
    256
    512
    """
    
    while start < end:
        print(f(start))
        start += 1
        
def curry2(f):
    """Return a curried version of the given two-argument function.
    """
    def g(x):
        def h(y):
            return g(x)(y)
        return h
    return g

def uncurry2(g):
    """Return a two-argument version of the given curried function."""
    def f(x, y):
        return g(x)(y)
    return f


        
