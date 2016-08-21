#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'


import requests
import pygal
from operator import itemgetter

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
# it seems there is no ca for *.firebaseio.com
r = requests.get(url, verify=False)
print("Status code: ", r.status_code)

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    url_ = "https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + ".json"
    # to get more details instead of just a id
    submission_r = requests.get(url_, verify=False)
    response_dict = submission_r.json()

    submission_dict = {
        # value - used as data
        # label - description
        # xlink - link
        "label": response_dict["title"],
        "xlink": "https://news.ycombinator.com/item?id=" + str(submission_id),
        "value": response_dict.get("descendants", 0),
    }
    submission_dicts.append(submission_dict)

chart = pygal.Bar()
# add title
chart.title = "Real time Top 10 news of Hacker News"
# add x labels
chart.x_labels = range(1, len(submission_dicts) + 1)
# add data
chart.add("", submission_dicts)
chart.render_in_browser()
