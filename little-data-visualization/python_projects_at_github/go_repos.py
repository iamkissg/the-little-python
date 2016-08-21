#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'


import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = "https://api.github.com/search/repositories?q=language:go&sort=stars"
# send get method request to url
r = requests.get(url)
print("Status code: ", r.status_code)

# response.json - returns the json-encoded content of a reponse, if any
response_dict = r.json()
print("Total repositories: ", response_dict["total_count"])

# just return part of repositories
repo_dicts = response_dict["items"]

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    name = repo_dict["name"]
    names.append(name)
    plot_dicts.append({
        "value": repo_dict["stargazers_count"],
        "label": repo_dict["description"],
        "xlink": repo_dict["html_url"],
        }
    )
my_style = LS("#336699", base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font = 18
# limit length of label
my_config.truncate_label = 15
# 隐藏水平线
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Go Projects on GitHub"
chart.x_labels = names

chart.add("", plot_dicts)
# chart.render_in_browser()
chart.render_to_file("most-starred-go-projects-on-github.svg")
