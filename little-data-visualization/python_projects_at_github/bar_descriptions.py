#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'


import pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS


my_style = LS("#336699", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)


chart._title = "Python Projects"
chart.x_labels = ["httpie", "django", "flask"]

plot_dicts = [
    {"value": 16101, "label": "Description of httpie"},
    {"value": 12344, "label": "Description of django"},
    {"value": 15213, "label": "Description of flas"},
]

chart.add("", plot_dicts)
chart.render_in_browser()
