#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''这是<Python网络数据采集>一书中的一个代码示例.
查看维基百科对词条做了修改的所有用户中未登录的用户的ip地址对应的国家.
首先以一个词条作为入口,获取其页面上的所有内链(词条),
然后逐个访问这些词条的编辑页面, 获得历史编辑信息,
再获得未登录用户的ip地址, 通过freegeoip.net的api查询ip地址对应的国家代码'''

__author__ = 'Engine'


import re
import random
import datetime
import json
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup


random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    request = "https://en.wikipedia.org" + articleUrl
    response = urlopen(request)
    bsObj = BeautifulSoup(response.read())
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


def getHistoryIPs(pageUrl):
    # 取得词条关键字, 如Python_(programming_language)
    pageUrl = pageUrl.replace("/wiki/", "")
    # 构造词条的历史编辑页面url
    historyUrl = "https://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    print("history url is:" + historyUrl)
    response = urlopen(historyUrl)
    bsObj = BeautifulSoup(response.read())
    # 获取所有未登录编辑词条的用户的ip地址
    # 登录用户对词条编辑后, 在编辑历史中将显示其用户名, html文档中用mw-userlink标明
    # 未登录用户进行编辑之后, 其ip地址会显示在编辑历史中, 在html文档中将以mw-anonuserlink表示
    ipAddresses = bsObj.findAll("a", {"class": "mw-anonuserlink"})
    addressList = set()
    # 过滤重复地址
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList


def getCountry(ipAddress):
    request = "http://freegeoip.net/json/" + ipAddress
    try:
        # 调用freegeoip.net网的api查询ip地址对应的信息
        response = urlopen(request).read().decode("utf-8")
    except HTTPError:
        return None
    # 以json格式读取信息
    responseJson = json.loads(response)
    # 返回国家代码
    return responseJson.get("country_code")


# 获取维基百科Python词条页面内的所有内链, links储存的是a标签对象
links = getLinks("/wiki/Python_(programming_language)")


while len(links) > 0:
    for link in links:
        print("=" * 80)
        # 获取未登录且对词条进行了编辑的用户的ip地址
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            # 获取ip地址对应的国家编码
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP + " is from " + country)

    # 与for迭代同级, 在while下
    # 从当前词条的所有内链中随机获取一条, 重复以上过程
    newLink = links[random.randint(0, len(links) - 1)].attrs["href"]
    links = getLinks(newLink)
