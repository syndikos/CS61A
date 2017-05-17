#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 15:01:58 2017

@author: guilin
"""

def curry2(f):
    """Return a curried version of the given two-argument function.
    """
    def g(x):
        def h(y):
            return g(x)(y)
        return h
    return g

