#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:50:18 2017

@author: guilin
"""

def f():
    global a
    a = 2
    def g(a):
        
        a += 1
        print('a in sub_function is:', a)
    g(a)
    print('a in main_function is:', a)