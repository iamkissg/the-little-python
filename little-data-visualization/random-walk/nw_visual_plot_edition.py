#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'


from matplotlib import pyplot as plt
from random_walk import RandomWalk

while 1:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6), dpi=160)

    point_numers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1, color="red")

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
