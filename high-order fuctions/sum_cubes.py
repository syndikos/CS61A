#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:26:49 2017

@author: guilin
"""

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def cube(x):
    return pow(x, 3)

def sum_cubes(n):
    return summation(n, cube)
