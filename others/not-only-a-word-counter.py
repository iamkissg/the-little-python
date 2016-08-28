#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Yet another wheel for words-counting.
Everything goes fines, while its word-counting function just works fine with English text.
The only hard thing is to create a proper regex!
'''

__author__ = 'Engine'

import re
import argparse


# '.*?' - lazy match
RE_SENTENCE = re.compile(r"(\S+?.*?[\.\?\!\~]+)")
# In the default mode, dot matches any character except a newline.
RE_PARAGRAPH = re.compile(r"(\S+?.*)")
RE_WORD = re.compile(r"(\S+?)[\,\;\:\?\!\~\，\。\；\：\？\！\s]")


def count_word(s):
    return len(re.findall(RE_WORD, s))


def count_sentence(s):
    return len(re.findall(RE_SENTENCE, s))


def count_paragraph(s):
    return len(re.findall(RE_PARAGRAPH, s))


def count_char(s):
    '''count char'''
    return len(s)


def count_space(s):
    '''count space'''
    return s.count(" ")


def count_nonspace(s):
    '''count nonspace char'''
    return count_char(s) - count_space(s)


def count_byte(s):
    '''count byte'''
    return len(s.encode("utf-8"))


def count_line(s):
    '''count line'''
    return s.count("\n")


if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser("kiss's word counter.")

    app_group = arg_parser.add_mutually_exclusive_group()

    app_group.add_argument("-a", "--all", action="store_true", help="Count all, including words, characters, bytes, spaces, nonspaces, sentences, lines, paragraphs.")
    app_group.add_argument("-w", "--word", action="store_true",
                           help="Count words.")
    app_group.add_argument("-c", "--char", action="store_true",
                           help="Count characters.")
    app_group.add_argument("-b", "--byte", action="store_true",
                           help="Count bytes.")
    app_group.add_argument("-s", "--space", action="store_true",
                           help="Count spaces.")
    app_group.add_argument("-S", "--sentence", action="store_true",
                           help="Count sentences.")
    app_group.add_argument("-l", "--line", action="store_true",
                           help="Count lines.")
    app_group.add_argument("-p", "--paragraph", action="store_true",
                           help="Count paragraphs.")
    arg_parser.add_argument("file", help="The input file.")

    args = arg_parser.parse_args()

    statistics = {}

    with open(args.file) as f:
        text = f.read()

    if args.word:
        statistics["words"] = count_word(text)
    elif args.char:
        statistics["characters"] = count_char(text)
    elif args.byte:
        statistics["bytes"] = count_byte(text)
    elif args.space:
        statistics["spaces"] = count_space(text)
    elif args.sentence:
        statistics["sentences"] = count_sentence(text)
    elif args.paragraph:
        statistics["paragraphs"] = count_paragraph(text)
    elif args.line:
        statistics["lines"] = count_line(text)
    else:
        statistics["words"] = count_word(text)
        statistics["characters"] = count_char(text)
        statistics["bytes"] = count_byte(text)
        statistics["spaces"] = count_space(text)
        statistics["sentences"] = count_sentence(text)
        statistics["paragraphs"] = count_paragraph(text)
        statistics["lines"] = count_line(text)
    for k, v in statistics.items():
        print("The number of " + k + " is:" + str(v))
