#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''每天给Ta讲一个笑话~
受python开发者的一篇推送文章影响,也写了一个类似的脚本
使用2个api,一个是易源笑话大全api,一个是阿里大鱼的短信api
有机会可以再加上其他的内容,比如发送天气消息等'''

__author__ = 'Engine'

import urllib.request
import json
# 阿里的module太老旧了,还没来得及修改,以下使用github上另一位同学的module
# github address: https://github.com/raptorz/alidayu/blob/master/alidayu.py
from random import randint
from alidayu_sms import AlibabaAliqinFcSmsNumSendRequest
from datetime import datetime

# 调用易源笑话大全的api获取笑话
def get_jokes(joke_url, joke_appkey):
    req = urllib.request.Request(joke_url) # 创建url请求
    req.add_header("apikey", joke_appkey)  # 添加appkey进request header
    resp = urllib.request.urlopen(req)
    raw_content = resp.read().decode("utf8") # resp是字节流,将其转换成utf8格式
    if(raw_content):
        json_result = json.loads(raw_content) # 将内容转为dict格式
        content = json_result["showapi_res_body"]["contentlist"] # 取得笑话部分
        return (content[0]["text"]) # 取得笑话部分的第一则笑话
    else:
        print("error")


# 使用阿里大鱼的sms接口发送短信,此处使用系统的模板,其使用code和product两个变量
def send_sms(sms_appkey, sms_secret, sms_url, sms_name, sms_title, sms_content, sms_end):
    req = AlibabaAliqinFcSmsNumSendRequest(key=sms_appkey, secret=sms_secret, url=sms_url) # 通过指定url,appkey,secret创建url请求
    req.sms_type = "normal" # 必选字段, 短信的类型
    req.sms_free_sign_name = "kissg私语" # 必选字段, 签名
    req.sms_param = '{"name":"' + sms_name + '", "title": "' + sms_title + '", "content": "' + sms_content + '", "end": "' + sms_end + '"}' # 可选字段, 套用模板,并指定变量内容, json格式
    req.rec_num = "" # 必选字段, 指定接收的号码,多个号码之间用','隔开,中间不能带空格
    req.sms_template_code = "SMS_7791287"   # 必选字段, 指定短信模板
    try:
        resp = req.getResponse()
        print(resp)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    n = randint(1, 100)
    joke_url = "http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text?page=" + str(n)
    joke_appkey = "your key"
    sms_url = "https://eco.taobao.com/router/rest"
    sms_appkey = "your key"
    sms_secret = "your secret"
    sms_name = "your name"
    sms_title = "your title"
    sms_content = get_jokes(joke_url, joke_appkey)
    sms_end = datetime.today().strftime("%Y-%M-%d, %a")
    send_sms(sms_appkey, sms_secret, sms_url, sms_name, sms_title, sms_content, sms_end)
