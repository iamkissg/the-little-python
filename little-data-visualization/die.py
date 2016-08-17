#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'



# return random integer in range [a, b]
from random import randint

class Die():
    """"""

    def __init__(self, num_sides=6):
        """by default, a die has 6 sides"""
        self.num_sides = num_sides

    def roll(self):
        """"""
        return randint(1, self.num_sides)
