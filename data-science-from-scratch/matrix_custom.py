#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Demo code for the book "Data Science from Scratch"
Cumtom matrix operation based on list'''

__author__ = 'Engine'


def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A, i):
    return A[i]


def get_column(A, j):
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    '''return a num_rows * num_cols make_matrix,
    whose (i, j)th entry is entry_fn(i, j)'''
    return [[entry_fn(i, j)            # 嵌套的列表生成式
             for j in range(num_cols)] # 生成多维(2)列表
           for i in range(num_rows)]   # 即表示矩阵


# 用于创建单位矩阵的简单函数
def is_diagonal(i, j):
    return 1 if i == j else 0
