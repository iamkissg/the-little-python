#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'



import csv
from matplotlib import pyplot as plt
from datetime import datetime

csv_1 = "sitka_weather_2014.csv"
csv_2 = "death_valley_2014.csv"


f_1 = open(csv_1, "r")
# csv.reader - accept itetable, return iterator
reader_1 = csv.reader(f_1)

f_2 = open(csv_2, "r")
reader_2 = csv.reader(f_2)

next(reader_1)
next(reader_2)

dates, highs_1, lows_1, highs_2, lows_2 = [], [], [], [], []
# for .. in ..
# actually call iterator's next method to iterate
for row_1, row_2 in zip(reader_1, reader_2):
    try:
        high_1 = int(row_1[1])
        high_2 = int(row_2[1])
        low_1 = int(row_1[3])
        low_2 = int(row_2[3])
    except:
        print("Missing data")
    # when execption, will use data of yesterday
    highs_1.append(high_1)
    highs_2.append(high_2)
    lows_1.append(low_1)
    lows_2.append(low_2)
    dates.append(datetime.strptime(row_1[0], "%Y-%m-%d"))

# draw chart
fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates, highs_1, c="red", alpha=0.5)
plt.plot(dates, lows_1, c="red", alpha=0.5)  # will draw on the same charwt
plt.fill_between(dates, highs_1, lows_1, facecolor="red", alpha=0.1)

plt.plot(dates, highs_2, c="blue", alpha=0.5)
plt.plot(dates, lows_2, c="blue", alpha=0.5)  # will draw on the same charwt
plt.fill_between(dates, highs_2, lows_2, facecolor="blue", alpha=0.1)

plt.title("Comparasion daily high and low temperatures\nbetween Sitka and Death Valley - 2014", fontsize=18)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()  # auto format X labels based on Date
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()

f_1.close()
f_2.close()
