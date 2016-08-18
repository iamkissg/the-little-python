#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'


import pygal
import random_walk
import random_walk_long_distance
import random_walk_just_turn_right
from random import choice
from matplotlib import pyplot as plt

RandomWalk = choice([random_walk.RandomWalk,
                        random_walk_long_distance.RandomWalk,
                        random_walk_just_turn_right.RandomWalk])
rw = random_walk_long_distance.RandomWalk(5000)
rw.fill_walk()

point_numers = list(range(rw.num_points))

xy_chart = pygal.XY()
xy_chart.add("RandomWalk", [(x, y) for x, y in zip(rw.x_values, rw.y_values)])

xy_chart.render_to_file("nw_visual_with_pygal.svg")
