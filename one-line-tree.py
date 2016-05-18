#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Build a tree data structrue by using python's defaultdict
Copied from https://gist.github.com/hrldcpr/2012250'''

__author__ = 'Engine'

from collections import defaultdict


def tree():
    '''It's simply says that a tree is a dict whose default values are trees.
    '''

    return defaultdict(tree)




