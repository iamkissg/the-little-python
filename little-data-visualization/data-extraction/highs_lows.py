#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'



import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "sitka_weather_07-2014.csv"

with open(filename, "r") as f:
    # csv.reader - accept itetable, return iterator
    reader = csv.reader(f)
    header_row = next(reader)  # already got header

    dates, highs = [], []
    # for .. in ..
    # actually call iterator's next method to iterate
    for row in reader:
        highs.append(int(row[1]))
        dates.append(datetime.strptime(row[0], "%Y-%m-%d"))

    # draw chart
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c="red")
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()  # auto format X labels based on Date
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()
