#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'



import pygal
from matplotlib import pyplot as plt
from die import Die
from collections import Counter


die = Die()
roll_num = 1000

results = []
for _ in range(roll_num):
    result = die.roll()
    results.append(result)

counter = Counter(results)

# change counter.keys() to list for indexing
plt.bar(list(counter.keys()), counter.values(), align="center")
plt.title("Results of rolling one D6 %d times" % roll_num)
plt.show()


