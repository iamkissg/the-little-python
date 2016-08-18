#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'


# randomly select a element from a sequence
from random import choice


class RandomWalk():
    """class for generating data for random walk"""

    def __init__(self, num_points=5000):
        """"""
        # used to control the walk times
        self.num_points = num_points

        # begin with (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """"""

        while len(self.x_values) < self.num_points:

            x_step = get_step()
            y_step = get_step()
            # must move
            if x_step == 0 and y_step == 0:
                continue

            # calculate the next coordinate
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

def get_step():
    direction = choice([1, -1])
    distance = choice([0, 1, 2, 3, 4])
    return direction * distance

