#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'



import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "death_valley_2014.csv"

with open(filename, "r") as f:
    # csv.reader - accept itetable, return iterator
    reader = csv.reader(f)
    header_row = next(reader)  # already got header

    dates, highs, lows = [], [], []
    # for .. in ..
    # actually call iterator's next method to iterate
    for row in reader:
        # the best way to use try statement is to
        # just execute one statement (operation)

        # here, to make the x and y have same dimension
        # once there's data missing, throw the row
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except:
            print("Missing data.")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
        # another way to make x and y hava same dimension is
        # using remove() or del extracted data

    # draw chart
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c="red")
    plt.plot(dates, lows, c="blue")  # will draw on the same charwt
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
    plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()  # auto format X labels based on Date
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.ylim([0, 120])
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()
