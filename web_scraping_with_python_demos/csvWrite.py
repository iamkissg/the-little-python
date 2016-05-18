#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''

__author__ = 'Engine'


import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


request = "http://en.wikipedia.org/wiki/Comparison_of_text_editors"
response = urlopen(request)
bsObj = BeautifulSoup(response)
# 获取第一张table标签, findAll返回值为list
table = bsObj.findAll("table", {"class": "wikitable"})[0]
# 在table下,获取所有tr标签
rows = table.findAll("tr")
# 新建csv文件, 若已存在, 将覆盖文件内容
csvFile = open("editors.csv", "wt", newline='', encoding="utf-8")
# 创建csv记录器
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(["td", "th"]):
            # 在tr下查找td, th标签, 并获取内容
            csvRow.append(cell.get_text())
        # 记录值
        writer.writerow(csvRow)
finally:
    csvFile.close()
