#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'



import pygal

wm = pygal.maps.world.World()
wm.title = "North, Central, and South America"
# 每次调用 add() 都为指定的国家选择一种新的颜色
# 并在图表左侧显示颜色与指定的标签
wm.add("North America", ["ca", "mx", "us"])
wm.add("Central America", ["bz", "cr", "gt", "hn", "ni", "pa", "sv"])
wm.add("South America", ["ar", "bo", "br", "cl", "co", "ec", "gf", "gy", "pe", "py", "sr", "uy", "ve"])
wm.render_to_file("americas.svg")
