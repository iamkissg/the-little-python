#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'


import pygal
from die import Die
from collections import Counter

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# another way to count frequencies
frequencies = Counter(results)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 and one D10 50000 times"
hist.x_labels = frequencies.keys()
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D10", frequencies)
hist.render_to_file("different_dice_visual.svg")
