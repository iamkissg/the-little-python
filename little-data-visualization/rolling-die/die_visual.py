#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'



import pygal
from die import Die
from collections import Counter

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    # list.count(value) -> integer
    # return number of occurrences of value
    frequency = results.count(value)
    frequencies.append(frequency)

# another way to count frequencies
counter = Counter(results)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.add("yet another D6", counter.values())
hist.render_to_file("die_visual.svg")
