#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:32:23 2017

@author: guilin
"""

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), after(k)
    return total

def after(x):
    return x + 1

def identity(x):
    return x

def sum_naturals(n):
    """assummes n is a integer
    returns the sum of the first n numbers
    
    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    return summation(n, identity)
