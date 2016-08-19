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

cc_populations, cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}, {}
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        # 原始数据有问题, 可能因为人口数据缺失而使用插值获得数据, 会导致出现小数
        # 因此, 先将数据转化为 float, 再将 float 装为 int
        # int() 函数会舍弃掉浮点数的小数部分
        population = int(float((pop_dict["Value"])))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 根据人口的不同量级再分组, 效果好很多
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop


wm = pygal.maps.world.World()
wm.title = "World Population in 2010, by Country"
wm.add("0-10m", cc_pops_1)
wm.add("10m-1b", cc_pops_2)
wm.add(">1b", cc_pops_3)
wm.render_to_file("world_population.svg")

