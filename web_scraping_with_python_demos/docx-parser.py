#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'



from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup


# 从.docx文件读取xml的步骤

# 1. 读取.docx文件
wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
# 2. 转换成二进制对象
wordFile = BytesIO(wordFile)
# 3. 解压(所有.docx文件为了节省空间都进行过压缩)
document = ZipFile(wordFile)
# 4. 读取解压文件, 就得到了xml内容
xml_content = document.read("word/document.xml")


# 创建BeautifulSoup对象
wordObj = BeautifulSoup(xml_content.decode("utf-8"))
# 根据xml标签再处理就很简单了
textStrings = wordObj.findAll("w:t")  # 所有正文内容都包含在<w:t>标签里
for textElem in textStrings:
    closeTag = ""
    try:
        style = textElem.parent.previousSibling.find("w:pstyle")
        if style is not None and style["w:val"] == "Title":
            print("<h1>")
            closeTag = "</h1>"
    except AttributeError:
        pass
    print(textElem.text)
    print(closeTag)
