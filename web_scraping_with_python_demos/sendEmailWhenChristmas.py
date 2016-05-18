#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'



import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time


def sendMail(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "cwf773810@163.com"
    msg["To"] = "747524153@qq.com"
    s = smtplib.SMTP("smtp.163.com")
    s.ehlo()
    s.login("cwf773810@163.com", "JwpuDj6h2z")
    s.send_message(msg)
    s.quit()


# bsObj = BeautifulSoup(urlopen("http://isitchristmas.com/"))
# while(bsObj.find("a", {"id": "answer"}).attrs["title"] == "NO"):
    # print("It is not Christmas yet.")
    # time.sleep(3600)
# bsObj.find("a", {"id": "answer"})
sendMail("It's Christmas!", "Merry Christmas!")
