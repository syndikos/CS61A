#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:29:31 2017

@author: guilin
"""

s = lambda x: x*x

def trace(fn):
    def wrapped(x):
        print('->', fn, '(', x, ')')
        return fn(x)
    return wrapped


def exp(b, n):
    if n == 0:
        return 1
    return b * exp(b, n - 1)

def is_even(x):
    if x % 2 == 0:
        return True
    return False
    
def square(x):
    return x*x

def fast_exp(b, n):
    if n == 0:
        return 1
    elif is_even(n):
        return square(fast_exp(b, n/2))
    return b * fast_exp(b, n-1)

def gcd(a, b):
    """Returns the greatest reminder of a and b"""
    if b == 0:
        return a
    return gcd(b, a % b)

def divides(a, b):
    return a % b == 0

def smallest_divisor(n):
    def find_divisor(n, test_divisor):
        if square(test_divisor) > n:
            return n
        elif divides(n, test_divisor):
            return test_divisor
        return find_divisor(n, test_divisor + 1)
    return find_divisor(n, 2)

def is_prime(n):
    assert isinstance(n, int), 'n must be integer'
    assert n >= 0, 'n must be positive'
    if n == 1:
        return False
    return n == smallest_divisor(n)

def next_prime(num):
    """Returns the first prime after num"""
    ans = num + 1
    if is_prime(ans):
        return ans
    return next_prime(num + 1)
################################
# Recursion
################################
def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

# Mutual Recursion

def is_even_recursive(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)
    
def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even_recursive(n-1)
    
# Printing in Recursive Functions

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)
        
def improved_cascade(n):
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)
        
def play_alice(n):
    if n == 0:
        print('Bob wins!')
    else:
        play_bob(n-1)
        
def play_bob(n):
    if n == 0:
        print('Alice wins!')
    elif is_even_recursive(n):
        play_alice(n-2)
    else:
        play_alice(n-1)
        
# Tree Recursion

def fib_recursive(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib_recursive(n-2) + fib_recursive(n-1)
    
def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)
    
# Currying
def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start += 1
        
def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    def f(x, y):
        return g(x)(y)
    return f

def test(x, y):
    return x + y

def largest_num(the_list):
    """"Returns the largest number in the_list."""
    ans = 0
    for index in range(len(the_list)-1):
        if the_list[index] <= the_list[index+1]:
            ans = the_list[index+1]
        else:
            ans = the_list[index]
    return ans

def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return (temp < 60) or (raining == True)

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    for i in range(1, n+1):
        if cond(i):
            print(i)

def outer(n):
    def inner(m):
        return n - m
    return inner

def keep_ints_high_order(n):
    """Returns a function which takes one parameter cond and
    prints out all integers 1..i..n where calling cond(i)
    returns True.
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> keep_ints_high_order(5)(is_even)
    2
    4
    """
    def h(cond):
        return keep_ints(cond, n)
    return h

def and_add(f, n):
    """Return a new function. This new function takes an
    argument x and returns f(x) + n.
    >>> def square(x):
    ... return x * x
    >>> new_square = and_add(square, 3)
    >>> new_square(4) # 4 * 4 + 3
    19
    """
    def h(x):
        return f(x) + n
    return h

def even_high_order(f):
    def odd(x):
        if x < 0:
            return f(-x)
        return f(x)
    return odd

def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie
a = cake()
x, b = a(), cake

def snake(x):
    if cake == b:
        x += 3
        return lambda y: y + x
    else:
        return y - x
    
def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)


    
    
    

        
            
    


    