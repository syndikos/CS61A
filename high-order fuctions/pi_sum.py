#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:43:38 2017

@author: guilin
"""

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), after(k)
    return total

def after(n):
    return n + 1

def pi_term(x):
    return 8 / ((4*x - 3) * (4*x - 1))
def pi_sum(n):
    return summation(n, pi_term)