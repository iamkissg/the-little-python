#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'


from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """"""
    # dict COUNTRIES contains 2-letter country code (key)
    # and country name (value)
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
