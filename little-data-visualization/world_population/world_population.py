#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'



import json
import pygal
from country_codes import get_country_code

filename = "population_data.json"

with open(filename, "r") as f:
    # json.load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    # deserialize fp (a file-like obeject containing a json document) to a Python object
    pop_data = json.load(f)
    # json.loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    # deserialize s (a str instance containing a json document) to a Python object

for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        # 原始数据有问题, 可能因为人口数据缺失而使用插值获得数据, 会导致出现小数
        # 因此, 先将数据转化为 float, 再将 float 装为 int
        # int() 函数会舍弃掉浮点数的小数部分
        population = int(float((pop_dict["Value"])))
        code = get_country_code(country_name)
        if code:
            print(code + ": " + str(population))
        else:
            print("Error - " + country_name)

