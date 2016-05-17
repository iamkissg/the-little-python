#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''自动下载西门子带ppt的页面的ppt, 并通过浏览器的方式自动浏览
'''

__author__ = 'Engine'


import re
import os
import time
import argparse
import subprocess
from PIL import Image
from glob import glob
from selenium import webdriver
from urllib.request import urlretrieve


# regex, matching urls of pic and start time of it
PIC_RESOURCES = re.compile(r'urls\[(\d+)\]=\"(\S+)\"\nsts.*\"(\d+)\"')


def comma_handler(str_with_comma):
    return tuple(str_with_comma.split(","))


def get_resources(CourseID):
    '''根据资源的url, 获取ppt图片'''
    baseUrl = "http://www.ad.siemens.com.cn"
    url = baseUrl + "/service/elearning/cn/Course.aspx?CourseID=" + CourseID

    # 动态网页, 用urllib.request.urlopen获取到的html会有问题
    # 此处用selenium来获取html文档
    driver = webdriver.PhantomJS(executable_path="/home/kissg/Tools/phantomjs/bin/phantomjs")
    driver.get(url)

    page_source = driver.page_source
    try:   # 查看页面上是否有ppt资源, 不能用if语句, 因为find_element_by_id失败会抛出异常
        driver.find_element_by_id("picture")
    except Exception:
        print("Sorry, the page doesn't contain PPT resource.")
        raise Exception

    pic_resources = re.findall(PIC_RESOURCES, page_source)  # 匹配图片资源的urls与start times
    with open(CourseID + ".csv", "w") as f:
        for elm in pic_resources:  # download the pic
            urlretrieve(baseUrl + elm[1], elm[2] + ".jpg")
            # 1. 序号, 路径, 时间
            f.write(elm[0] + ',' + elm[1] + ',' + elm[2] + '\n')


def autoplay(CourseID):
    # preparation for play, set time
    with open(CourseID + ".csv", 'r') as f:
        pic_info = list(map(comma_handler, f.read().strip().split('\n')))
    # pic_st = [int(n[2]) - int(p[2]) for n, p in zip(pic_info[1:], pic_info[:-1])]
    pic_st = [(int(n[2]) - int(p[2]))/10 for n, p in zip(pic_info[1:], pic_info[:-1])]
    pic_st.reverse()

    # play the vedio
    cmds = ["vlc", glob("*.flv")[0]]
    subprocess.Popen(cmds)

    # Use browser for presentation
    browser = webdriver.Chrome(
        executable_path="/home/kissg/Tools/chromedriver/chromedriver")
    browser.maximize_window()  # maxmize the browser window
    win_size = browser.get_window_size()  # get window size for magnification
    prefix = "file://"  # the prefix for display local file

    for elm in pic_info:
        img_path = os.path.abspath(elm[2] + ".jpg")
        img = Image.open(img_path)  # open pic to get size for magnification
        browser.get(prefix + img_path)
        mag = min(win_size["width"] / img.size[0],  # cal magnification
                  win_size["height"] / img.size[1]) * 100
        mag_script = "document.body.style.zoom='" + str(mag) + "%'"
        browser.execute_script(mag_script)
        time.sleep(pic_st.pop())

if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(description="For Yang's task.")
    arg_parser.add_argument("id",
                            help="CourseID is needed.")
    args = arg_parser.parse_args()
    if not os.path.exists(args.id + ".csv"):
        get_resources(args.id)
    autoplay(args.id)
