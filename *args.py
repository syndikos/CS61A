#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:26:28 2017

@author: guilin
"""

def printed(fn):
    def print_and_return(*args):
        result = fn(*args)
        print('Result:', result)
        return result
    return print_and_return



