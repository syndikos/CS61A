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
def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]
def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def divisors_of(n):
    divides_n = lambda x: n% x == 0
    return [1] + keep_if(divides_n, range(2, n))

from operator import add
def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)
def perfect(n):
    return sum_of_divisors(n) == n

from functools import reduce
from operator import mul
def product(s):
    return reduce(mul, s)

def right_binarize(tree):
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n -2), fib_tree(n-1)
        fib_n = root(left) + root(right)
        return tree(fib_n, [left, right])

def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])

def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if root(tree):
            print(' + '.join(partition))
        else:
            left, right = branches(tree)
            m = str(root(tree))
            print_parts(left, partition + [m])
            print_parts(right, partition)
            
def make_adder(n):
    return lambda k: n + k

# @trace1
# def triple(x):
#     return 3 * x

#########
# memoization
#########
def memoize(f):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return helper

#########
# improved fib
#########
def fib(n):
    if n in (0, 1):
        return n    # if you have to write code like if n == 1 return pass elif n == 3 \
                    # return pass, you can use if n in (1, 3) return pass.
                    # when iterate, use turple insteed of list is more effecient.
    else:
        return fib(n - 1) + fib(n - 2)

########
# fib with memoization
########
fib = memoize(fib)

#############
# decoration
#############

# decorated fib
@memoize
def fib_decorated(n):
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)

# chained decorators
def trace(f):
    def helper(x):
        call_str = "{0}({1})".format(f.__name__, x)
        print("Calling {0} ...".format(call_str))
        result = f(x)
        print("... returning from {0} = {1}".format(
              call_str, result))
        return result
    return helper

@memoize
@trace
def fib_chained_decorators(n):
    if n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)

empty = 'empty'
def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]

def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

def len_link_recursive(s):
    """Return the length of a linked list s."""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    """Return the element at index i of linked list s."""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)

def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))
    
def apply_to_all_link(f, s):
    """Apply f to each element of s."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))
def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept
        
chinese = ['coin', 'string', 'myriad']
suits = chinese
suits.pop()
suits.remove('string')
suits.append('cup')
suits.extend(['sword', 'club'])
suits[2] = 'spade'
suits[0:2] = ['heart', 'diamond']

nest = list(suits)
nest[0] = suits
suits.insert(2, 'Joker')
suits.insert(2, 'Joker')
joke = nest[0].pop(2)

nest = (10, 20, [30, 40])

####################
# Local State
####################
def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance -= amount
        return balance
    return withdraw
withdraw = make_withdraw(100)

#################
# Implementing Lists and Dictionaries
#################
def mutable_link():
    """Return a functional implementation of a mutable linked list."""
    contents = empty
    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_link(contents)
        elif message == 'getitem':
            return getitem_link(contents, value)
        elif message == 'push_first':
            contents = link(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return join_link(contents, ', ')
    return dispatch

def join_link(contents, symbol=', '):
    """ contents: linked list"""
    if contents == empty:
        return ''
    else:
        return str(first(contents)) + symbol + join_link(rest(contents), symbol)

def to_mutable_link(source):
    """Return a functional list with the same contents as source."""
    s = mutable_link()
    for element in reversed(source):
        s('push_first', element)
    return s

chinese = ['coin', 'string', 'myriad']
suits = chinese
suits.pop()
suits.remove('string')
suits
suits.append('cup')
suits
suits.extend(['sword', 'club'])
suits
suits[2] = 'spade'
suits
suits[0:2] = ['heart', 'diamond']
suits
chinese
nest = list(suits)
nest
nest[0] = suits
nest
suits
list(suits)
a = [1, 2]
a
list(a)
suits.insert(2, 'Joker')
nest
nest[0].pop(2)
suits
suits.insert(2, 'Joker')
joke = nest[0].pop(2)
joke
suits is nest[0]
suits is ['heart', 'diamond', 'spade', 'club']
suits is ['heart', 'diamond', 'spade', 'club']  

#####################
# list comprehensions
#####################
from unicodedata import lookup
[lookup('WHITE ' + s.upper() + ' SUIT') for s in suits]

s = to_mutable_link(suits)
type(s)

def dictionary():
    """Return a functional implementation of a dictionary."""
    records = []
    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value
    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = non_matches + [[key, value]]
    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            return setitem(key, value)
    return dispatch

def account(initial_balance):
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']
    dispatch = {'deposit': deposit,
                'withdraw': withdraw,
                'balance': initial_balance}
    return dispatch


def withdraw(account, amount):
    return account['withdraw'](amount)
def deposit(account, amount):
    return account['deposit'](amount)
def check_balance(account):
    return account['balance']

# celsius = connector('Celsius')
# fahrenheit = connector('Fahrenheit')

# def convert(c, f):
#     """Connect c to f with constraints to convert from Celsius to Fahrenheit."""
#     u, v, w, x, y = [connector() for _ in range(5)]
#     multiplier(c, w, u)
#     multiplier(v, x, u)
#     adder(v, y, f)
#     constant(w, 9)
#     constant(x, 5)
#     constant(y, 32)
# from operator import add, sub
# def adder(a, b, c):
#     """The constraint that a + b = c."""
#     return make_ternary_constraint(a, b, c, add, sub, sub)
# def make_ternary_constraint(a, b, c, ab, ca, cb):
#     """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b) = a."""
#     def new_value():
#         av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
#         if av and bv:
#             c['set_val'](constraint, ab(a['val'], b['val']))
#         elif av and cv:
#             b['set_val'](constraint, ca(c['val'], a['val']))
#         elif bv and cv:
#             a['set_val'](constrait, cb(c['val'], b['val']))
#     def forget_value():
#         for connector in (a, b, c):
#             connector['forget'](constraint)
#     constraint = {'new_val': new_value, 'forget': forget_value}
#     for connector in (a, b, c):
#         connector['connect'](constraint)
#     return constraint



def converter(c, f):
    """Connect c to f with constraints to convert from Celsius to Fahrenheit."""
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u) # c indicates celsius
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)
from operator import add, sub

def adder(a, b, c):
    """The constraint that a + b = c."""
    return make_ternary_constraint(a, b, c, add, sub, sub)

def make_ternary_constraint(a, b, c, ab, ca, cb):
    """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b) = a."""
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))
    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint

from operator import mul, truediv
def multiplier(a, b, c):
    """The constraint that a * b = c."""
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)

def constant(connector, value):
    """The constraint that connector = value."""
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint

def connector(name=None):
    """A connector between constraints."""
    informant = None
    constraints = []
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)
    connector = {'val': None,\
    'set-val': set_value, \
    'forget': forget_value,\
    'has_val': lambda: connector['val'] is not None, \
    'connect': lambda source: constraints.append(source)}
    return connector

def inform_all_except(source, message, constraints):
    """Inform all constraints of the message, except source."""
    for c in constraints:
        if c != source:
            c[message]()
            
celsius = connector('Celsius')
fahrenheit = connector('Fahrenheit')

#############
# discussion 3: tree
#############

def tree(label, branches=[]):
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def set_label(val):
    tree[0] = val

t = tree(1,
[tree(3,\
[tree(4),\
tree(5),\
tree(6)]),\
tree(2)])

def square_tree(t):
    """ Return a tree with the square of every element in t"""
    new_tree = t[:]
    def square_tree_helper(new_tree):
        # nonlocal new_tree
        # new_tree[0] = new_tree[0] ** 2
        if is_leaf(new_tree):
            return new_tree
        else:
            for the_tree in branches(new_tree):
                return tree(label(new_tree) ** 2, square_tree(the_tree))
    # square_tree_helper(t)
    return square_tree_helper(new_tree)





