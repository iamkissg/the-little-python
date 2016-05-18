#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'下载http://pythonscraping.com网页上所有src属性指定的文件'

__author__ = 'Engine'


import os
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup


downloadDirectory = "/home/kissg/Tests/download"
baseUrl = "http://pythonscraping.com"


def getAbsolutionURL(baseUrl, source):
    # 根据传入source参数的格式, 构造绝对资源路径
    if source.startswith("http://www."):
        url = "http://" + source[11:]  # 去掉www?
    # 由于匹配过http://, 因此, 下述情况的url不以www开头
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = "http://" + source[4:]
    else:
        url = baseUrl + '/' + source

    if baseUrl not in url:  # 舍弃外链
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    # 在指定目录下构造出与服务器上结构相同的资源目录
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    # 目录不存在, 新建目录
    if not os.path.exists(directory):
        os.makedirs(directory)

    return path


request = "http://www.pythonscraping.com"
response = urlopen(request)
bsObj = BeautifulSoup(response)
downloadList = bsObj.findAll(src=True)  # 返回任何带src属性的标签

for download in downloadList:
    # 获取资源的绝对路径
    fileUrl = getAbsolutionURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
        # 下载文件资源
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
