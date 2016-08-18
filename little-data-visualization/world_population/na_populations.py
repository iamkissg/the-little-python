#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'



import pygal

wm = pygal.maps.world.World()
wm.title = "Populations of Countries in North America"
# Pygal 根据国家人口数量的多少, 自动为不同国家着深浅不一的颜色
# 人口越多, 颜色越深
wm.add("North America", {"ca": 34126000, "mx": 113423000, "us": 309349000})
wm.render_to_file("na_populations.svg")
