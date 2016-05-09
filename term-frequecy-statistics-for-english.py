#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''python网络数据采集第八章的例子
英文文章高频词汇统计
略作修改完善'''

__author__ = 'Engine'



from urllib.request import urlopen
import re
import string
import operator


def isCommon(ngram):
    '''用于判断是否常用词汇'''
    commonWords = {"the", "be", "and", "of", "a", "in", "to", "have", "it",
                   "i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
                   "they", "is", "an", "at", "but","we", "his", "from", "that", "not",
                   "by", "she", "or", "as", "what", "go", "their","can", "who", "get",
                   "if", "would", "her", "all", "my", "make", "about", "know", "will",
                   "as", "up", "one", "time", "has", "been", "there", "year", "so",
                   "think", "when", "which", "them", "some", "me", "people", "take",
                   "out", "into", "just", "see", "him", "your", "come", "could", "now",
                   "than", "like", "other", "how", "then", "its", "our", "two", "more",
                   "these", "want", "way", "look", "first", "also", "new", "because",
                   "day", "more", "use", "no", "man", "find", "here", "thing", "give",
                   "many", "well"}
    for word in ngram:
        if word in commonWords:
            return True
    return False


def cleanText(input):
    input = re.sub("\n+", " ", input)  # 将多个换行符转为一个空格
    input = re.sub("\[[0-9]*\]", "", input)  # 剔除维基百科的引用标记,如[1]
    input = re.sub(" +", " ", input)  # 将多个空格合并为1个空格, 确保单词间只有一个空格
    # 以utf8编码,再以ascii解码, 剔除unicode字符
    input = re.sub("u\.s\.", "us", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    return input


def cleanInput(input):
    input = cleanText(input)
    cleanInput = []
    input = input.split(' ')  # 以空格分割单词, 获得单词的list
    for item in input:
        # 剔除单词两边的标点符号,有点矫枉过正
        item = item.strip(string.punctuation)
        # 剔除单字符, 除非是i或a
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def getNgrams(input, n):
    input = cleanInput(input)  # 数据清洗
    output = dict()  # 创建字典, 用于保存n元 组
    # 可以通过filter函数过滤掉常用词汇
    # noCommonWord = filter(lambda t: not isCommon(t), input)
    for i in range(len(input) - n + 1):
        if isCommon(input[i:i+n]):  # 过滤常用词汇
            continue
        ngramTemp = ' '.join(input[i:i+n])  # 相邻的单词构成一个n元组
        if ngramTemp not in output:  # 统计n元组的词频
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output


def getFirtSentenceContaining(ngram, content):
    '''打印词汇第一次出现的句子'''
    sentences = content.split(".")  # 以.分割句子也不太对
    # s = []  #  用list按先后顺序存储单词出现的所有句子
    for sentence in sentences:
        if ngram in sentence:
            return sentence
            # s.append(sentence)
    return ""


request = "http://pythonscraping.com/files/inaugurationSpeech.txt"
response = urlopen(request)
content = response.read().decode("utf-8").lower()  # 为了统计方便, 将文本全部转为小写形式
# 获取词条的主体部分内容
ngrams = getNgrams(content, 2)  # 获取2元 组
# 对n元组按词频排序
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
# 对n元组进行过滤, 只取高频词汇
filteredNGrams = filter(lambda t: t[1] >= 3, sortedNGrams)
for ngram in filteredNGrams:  # 打印统计信息
    print('"' +  ngram[0] + '" appears ' +
          str(ngram[1]) + ' times, and is first appears in sentence:')
    print(getFirtSentenceContaining(ngram[0], content))
    print('=' * 80)
