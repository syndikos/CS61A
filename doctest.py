#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:35:59 2017

@author: guilin
"""

def sum_naturals(n):
    """Return the sum of the first n natural numbers.
    
    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total
    