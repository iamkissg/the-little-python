#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''python网络数据采集一书的一个示例, 有点像社交网络.
爬取一个维基百科词条五条范围内的所有词条信息
并存储到数据库中'''

__author__ = 'Engine'


from bs4 import BeautifulSoup
import re
import pymysql
from urllib.request import urlopen


conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",  passwd="Engine,618251", db="wikipedia", charset="utf8")
cur = conn.cursor()
cur.execute("use wikipedia")


def pageScraped(url):
    '''查询词条是否已经被爬取过了, 即其是否作为源词条'''
    # 查询抓取的词条是否已经存入数据库
    cur.execute("select * from pages where url = %s", (url))
    if cur.rowcount == 0:
        return False
    page = cur.fetchone()  # 获取该词条的数据库信息
    # 查询该词条是否作为过源词条
    cur.execute("select * from links where fromPageId = %s", (int(page[0])))
    if cur.rowcount == 0:
        return False
    return True


def insertPageIfNotExists(url):
    '''在数据库中插入没有记录的url'''
    # 先在数据库中查询url是否已经存在
    cur.execute("select * from pages where url = %s", (url))
    if cur.rowcount == 0:  # 查无此url, 则将其插入数据库
        cur.execute("insert into pages (url) values (%s)", (url))
        conn.commit()  # mysql需要提交事务
        return cur.lastrowid  # 返回新插入记录的id
    else:  # 数据库中已存在url, 直接返回url的id(第一个字段)
        return cur.fetchone()[0]


def insertLink(fromPageId, toPageId):
    '''建立词条间的跳转关系'''
    # 同样,在插入之前先查询此关系是否已存在
    cur.execute("select * from links where fromPageId = %s and toPageId = %s", (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("insert into links (fromPageId, toPageId) values (%s, %s)", (int(fromPageId), int(toPageId)))
        conn.commit()


def getLinks(pageUrl, recursionLevel):
    ''''''
    global pages
    # 当递归层数大于等于5层, 停止搜索
    if recursionLevel > 4:
        return
    # 将待搜索的url存入数据库, 并返回一个pageId
    pageId = insertPageIfNotExists(pageUrl)
    request = "http://en.wikipedia.org" + pageUrl
    response = urlopen(request)
    bsObj = BeautifulSoup(response)
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        # 建立词条与新获取的词条跳转关系
        insertLink(pageId, insertPageIfNotExists(link.attrs["href"]))
        # 如果词条是否已经记录过,是则跳过, 否则深挖该词条的跳转
        if not pageScraped(link.attrs["href"]):
            newPage = link.attrs["href"]
            print(newPage)
            getLinks(newPage, recursionLevel + 1)
        else:
            print("Skipping: " + str(link.attrs["href"]) + " found on " + pageUrl)

getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()
