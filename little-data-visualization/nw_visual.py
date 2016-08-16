#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'


from matplotlib import pyplot as plt
from random_walk import RandomWalk

while 1:
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values)
    # the program will stop at thi point
    plt.show()

    # only closing the window will ask user to make choice
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
