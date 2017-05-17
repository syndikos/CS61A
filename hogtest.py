#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:25:43 2017

@author: guilin
"""

from random import randint

def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    assert isinstance(sides, int) and sides >= 1, 'Illegal value for sides'
    def dice():
        return randint(1, sides)
    return dice

def make_test_dice(*outcomes):
    """Return a die that cycles deterministically through OUTCOMES.

    >>> dice = make_test_dice(1, 2, 3)
    >>> dice()
    1
    >>> dice()
    2
    >>> dice()
    3
    >>> dice()
    1
    >>> dice()
    2
    """

    assert len(outcomes) > 0, 'you must supply outcomes to make_test_dice'
    for i in outcomes:
        assert isinstance(i, int) and i >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice  

FOUR_SIDED = make_fair_dice(4)
SIX_SIDED = make_fair_dice(6)

def roll_dice(num_rolls, dice=SIX_SIDED):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return the
    number of 1's rolled (capped at 11 - NUM_ROLLS).
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert isinstance(num_rolls, int), 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    outcomes = [] # a list contains all the outcomes of dice rolled in a
    iterator = num_rolls             # turn by a player.
    while iterator > 0:
        outcome = dice()
        outcomes.append(outcome)
        iterator -= 1

    num = 0 # num is the number in outcomes that is 1.
    for i in outcomes:
        if i == 1:
            num += 1
    if num > 0:
        print('num is:', num)
        print("11-num_rolls is:", num_rolls)
        return min(11 - num_rolls, num)
    return  sum(outcomes)





