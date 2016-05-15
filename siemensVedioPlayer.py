#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''西门子视频学习中心, 视频自动播放器
好吧, 这是我计算控制系统老师(杨曦)布置的任务的变种实现方式
主要利用了自动化测试工具Selenium来模拟鼠标键盘事件来实现'''

__author__ = 'Engine'


from selenium import webdriver
import selenium.webdriver.common.action_chains as sac
import argparse
import time


class siemensAutoPlayer(object):

    def __init__(self, url="/service/elearning/cn/Course.aspx?CourseID=81"):
        '''初始化, 设置视频url, 选择浏览器, 并取得浏览器大小'''
        self.baseUrl = "http://www.ad.siemens.com.cn"
        if url.startswith("http://") or url.startswith("www"):
            self.url = url
        else:
            self.url = self.baseUrl + url
        driver = "/home/kissg/Tools/chromedriver/chromedriver"
        self.browser = webdriver.Chrome(executable_path=driver)  # chrome
        self.browser.get(self.url)
        self.win_size = self.browser.get_window_size()  # get window size

    def maxBrowser(self):
        '''最大化窗口, 并重新获取窗口大小'''
        self.browser.maximize_window()
        self.win_size = self.browser.get_window_size()

    def autoPlay(self):
        '''查找到页面上的视频位置, 单击开始播放'''
        self.vedio = self.browser.find_element_by_id("divCourseVideo")
        act_play = sac.ActionChains(self.browser)
        act_play.move_to_element(self.vedio).click()
        act_play.perform()

    def setScreen(self):
        '''设置显示屏幕, 西门子视频学习中心有2类视频, 一类除了视频还带有ppt
对于只有视频的, 全屏播放即可,
对于有ppt的, 选择显示ppt'''
        # 其实就是一个if判断, 但selenium搜索不到元素会报错, 因此改用try语句
        try:
            self.pic = self.browser.find_element_by_id("picture")
        except:
            # 异常, 说明页面上无ppt, 全屏显示
            # 直接使用selenium定义的 double_click似乎点击过快, 触发全屏有问题
            # 故使用click.click的形式
            act_fullScreen = sac.ActionChains(self.browser).move_to_element(self.vedio).click().click()
            act_fullScreen.perform()
        else:
            # JavaScript 脚本, 清楚掉ppt的右侧栏目, 使显示更整洁
            self.browser.execute_script('''
                var element = document.querySelector(".right-content-spec");
                if (element)
                element.parentNode.removeChild(element);''')
            self.playWithPic()

    def playWithPic(self):
        '''缩放, 并调整页面位置'''
        self.pic = self.browser.find_element_by_id("picture")  # 找到ppt
        # 利用屏幕大小和图片大小计算放大倍率
        magnification = min(self.win_size["width"] / self.pic.size["width"],
                            self.win_size["height"] / self.pic.size["height"])
        self.zoomOut(magnification)  # 放大
        # 定位到ppt, 几种方式
        # self.browser.execute_script("return arguments[0].scrollintoview();", self.pic)
        # 以图片的左上角坐标为准, 使图片显示在屏幕正中
        scroll_script = "window.scrollTo(" + str(self.pic.location["x"] * magnification) + ",\
                 " + str(self.pic.location["y"] * magnification) + ");"
        # 滚动脚本
        self.browser.execute_script(scroll_script)

    def zoomOut(self, magnification):
        '''运行放大脚本'''
        mag_script = "document.body.style.zoom='" + str(magnification * 100) + "%'"
        self.browser.execute_script(mag_script)

if __name__ == '__main__':
    # 设置脚本参数
    arg_parser = argparse.ArgumentParser(description="For Yang's task.")
    arg_parser.add_argument("id",
                            help="CourseID is needed.")
    args = arg_parser.parse_args()
    autoPlayer = siemensAutoPlayer("http://www.ad.siemens.com.cn/service/elearning/cn/Course.aspx?CourseID=" + args.id)
    autoPlayer.maxBrowser()
    time.sleep(2)  # 过快点击会有问题, 加点时延等页面完全加载
    autoPlayer.autoPlay()
    time.sleep(1)
    autoPlayer.setScreen()
