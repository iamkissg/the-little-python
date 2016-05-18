#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''将任意pdf读成字符串, 再用StringIO转换成文件对象'''

__author__ = 'Engine'



from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
# from io import open


def readPDF(pdfFile):
    '''以下对象没有深究, 反正我都不认识'''
    # 创建pdf资源管理器对象
    rsrcmgr = PDFResourceManager()
    # 创建字符串IO对象
    retstr = StringIO()
    # 创建这什么什么
    laparams = LAParams()
    # 创建文本转换器对象
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    # 转换pdf
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    # 从字符串IO对象中取值
    content = retstr.getvalue()
    retstr.close()  # StringIO对象是一个类文件(file-like)对象, 用完要关闭
    return content


# 读取pdf文件, 需要是二进制类型
pdfFile = urlopen("http://www.tutorialspoint.com/python/python_tutorial.pdf")
# pdfFile = open("/home/kissg/Dropbox/Books/development/linux-101_hacks.pdf", "rb")
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()
