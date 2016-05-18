#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''demo code from <Web Scraping with Python>
Use JavaScript to make redirection'''

__author__ = 'Engine'


from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement


def waitForload(driver):
    elem = driver.find_element_by_tag_name("div")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10s and returning")
            return
        time.sleep(0.5)
        try:
            elem == driver.find_element_by_tag_name("div")
            print(driver.page_source)
        except Exception:
            return


driver = webdriver.PhantomJS(executable_path="/home/kissg/Tools/phantomjs/bin/phantomjs")
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForload(driver)
print(driver.page_source)
