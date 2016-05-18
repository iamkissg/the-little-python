#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'


import re
import unittest
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import unquote


class TestWikipedia(unittest.TestCase):
    bsObj = None
    url = None

    def test_PageProperties(self):
        global bsObj
        global url

        url = "http://en.wikipedia.org/wiki/Monty_Python"
        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url), "lxml")
            titles = self.titleMatchesURL()
            try:
                self.assertEqual(titles[0], titles[1])
            except Exception:
                print("Titles don't match.")
            try:
                self.assertTrue(self.contentExists())
            except Exception:
                print("Content doesn't exist.")
            url = self.getNextLink()
        print("Done")

    def titleMatchesURL(self):
        global bsObj
        global url
        pageTitle = bsObj.find("h1").get_text()
        urlTitle = url[(url.index("/wiki/") + 6):]
        urlTitle = urlTitle.replace("_", ' ')
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global bsObj
        content = bsObj.find("div", {"id": "mw-content-text"})
        if content is not None:
            return True
        return False

    def getNextLink(self):
        global bsObj
        links = bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
        link = links[random.randint(0, len(links)-1)].attrs["href"]
        print("New link is: " + link)
        return "http://en.wikipedia.org" + link

if __name__ == '__main__':
    unittest.main()
