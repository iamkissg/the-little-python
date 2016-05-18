#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'



from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict


def cleanInput(input):
    input = re.sub("\n+", " ", input)  # 将多个换行符转为一个空格
    input = re.sub("\[[0-9]*\]", "", input)  # 剔除维基百科的引用标记,如[1]
    input = re.sub(" +", " ", input)  # 将多个空格合并为1个空格, 确保单词间只有一个空格
    # 以utf8编码,再以ascii解码, 剔除unicode字符
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')  # 以空格分割单词, 获得单词的list
    for item in input:
        # 剔除单词两边的标点符号,有点矫枉过正
        item = item.strip(string.punctuation)
        # 剔除单字符, 除非是i或a
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def getNgrams(input, n):
    input = cleanInput(input)  # 数据清洗
    output = dict()  # 创建字典, 用于保存n元 组
    for i in range(len(input) - n + 1):
        newNGram = ' '.join(input[i:i+n])  # 相邻的单词构成一个n元组
        if newNGram in output:  # 统计n元组的词频
            output[newNGram] += 1
        else:
            output[newNGram] = 1
    return output


request = "http://en.wikipedia.org/wiki/Python_(programming_language)"
response = urlopen(request)
bsObj = BeautifulSoup(response)
# 获取词条的主体部分内容
input = bsObj.find("div", {"id": "mw-content-text"}).get_text()  # str
ngrams = getNgrams(input, 2)  # 获取2元 组
# 对n元组按词频排序
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams)
