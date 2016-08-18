#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'


import random_walk
import random_walk_long_distance
import random_walk_just_turn_right
from random import choice
from matplotlib import pyplot as plt

while 1:
    RandomWalk = choice([random_walk.RandomWalk,
                         random_walk_long_distance.RandomWalk,
                         random_walk_just_turn_right.RandomWalk])
    rw = random_walk_long_distance.RandomWalk(50000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6), dpi=160)

    point_numers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numers,
                cmap=plt.cm.Reds, edgecolor="none", s=1)

    # highlight the starting point and the end point
    plt.scatter(0, 0, c="blue", edgecolor="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c="green", edgecolor="none", s=100)

    # hide axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # the program will stop at thi point
    plt.show()

    # only closing the window will ask user to make choice
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
