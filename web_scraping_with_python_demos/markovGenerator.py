#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''''

__author__ = 'Engine'



from urllib.request import urlopen
from random import randint


def wordListSum(wordList):
    '''统计以word开头的二元单词的总数'''
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum


def retrieveRandomWord(wordList):
    '''生成一个随机数, 用于从二元词组中取下一个单词
出现频率高的单词, 使randIndex减小地更快, 因此可能会更容易取到
此处的算法随机性不够高'''
    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word


def buildWordDict(text):
    '''创建一个二维字典,表示一个单词搭配另一个单词的词频
如{"I": {"like": 5, "have": 3, "sleep": 1}}'''
    # 剔除掉文章中的换行符与引号
    text = text.replace("\n", " ")
    text = text.replace("\"", "")
    text = text.replace("\'", "")

    # 用空格包裹标点, 如此才能将标点与单词分隔开, 就能保留下这些标点插入句子
    # 英文的标点一般紧更在单词之后
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, " " + symbol + " ")

    words = text.split(" ")
    # 去掉切割产生空单词, 多个连续空格引起的
    words = [word for word in words if word != ""]

    wordDict = {}
    for i in range(1, len(words)):
        # 每次都是取2个单词组合的词组构建字典
        if words[i-1] not in wordDict:
            # 一维字典中不存在词组中前一个单词的, 为其创建一个字典
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            # 词组首次出现的, 则为其创建一个二维字典项
            wordDict[words[i-1]][words[i]] = 0
        # 词组的词频+1
        wordDict[words[i-1]][words[i]] += 1
    return wordDict

text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), "utf-8")
wordDict = buildWordDict(text)

# 生成长度为1000的马尔可夫链
length = 100
chain = ""
currentWord = "I"
for i in range(0, length):
    chain += currentWord + " "  # 加入单词与作为分隔符的空格
    # 取下一个单词
    currentWord = retrieveRandomWord(wordDict[currentWord])

print(chain)
