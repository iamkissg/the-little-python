#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Demo code for the book "Data Science from Scratch"
Cumtom vector operation based on list'''

__author__ = 'Engine'


import math
from functools import reduce

def vector_add(v, w):
    '''adds corresponding elements'''
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    '''subtracts corresponding elements'''
    return [v_i - w_i for v_i, w_i in zip(v, w)]


# the old way to sum all vectors
# def vector_sum(vectors):
    # ''''''
    # result = vectors[0]
    # for vector in vectors[1:]:
        # result = vector_add(result, vector)
    # return result


def vector_sum(*vectors):
    '''add all vectors by calling reduce function'''
    return reduce(vector_add, vectors)


# the 3rd amazing way to add all vectors
# vector_sum = partial(reduce, vector_add)


def scalar_multiply(c, v):
    '''c is a number, v is a vector'''
    return [c * v_i for v_i in v]

def vector_mean(*vectors):
    '''compute the vector whose ith element is the mean
    of the ith elements of the input vectors'''
    n = len(vectors)
    # yet another amazing code(function programming?)
    # it's essential to add * before vectors,
    # for unpacking the vectors tuple
    return scalar_multiply(1/n, vector_sum(*vectors))


# 向量的点乘运算是将所有的相应元素相乘, 再做和
def dot(v, w):
    '''v_1 * w_1 + v_2 * w_2 + v_3 * w_3 ...'''
    # yet another amazing code 2.
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


# 向量的平方和
def sum_of_squares(v):
    '''v_1^2 + v_2^2 + v_3^2 ...'''
    return dot(v, v)


# 向量的大小(模)
def magnitude(v):
    '''sqrt(v_1^2 + v_2^2 + v_3^2 ...)'''
    return math.sqrt(sum_of_squares(v))


# 向量距离的平方
def squared_distance(v, w):
    '''(v_1-w_1)^2 + (v_2-w_2)^2 + (v_2-w_2)^2 ...'''
    return sum_of_squares(vector_subtract(v, w))


# the old way to compute distance of 2 vectors
# def distance(v, w):
    # return math.sqrt(squared_distance(v, w))


def distance(v, w):
    return magnitude(vector_subtract(v, w))
