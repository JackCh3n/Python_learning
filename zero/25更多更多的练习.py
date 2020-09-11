#!/usr/bin/env python
# coding=utf-8
'''
Date: 2020-09-08 14:51:00
Author: JackCh3n
LastEditTime: 2020-09-08 16:16:59
LastEditors: JackCh3n
FilePath: \zero\25更多更多的练习.py
'''
# 字符转数组
def break_words(stuff):
    return stuff.split(' ')

# 数组排序
def sort_words(words):
    return sorted(words)

# 返回数组第一个
def print_first_word(words):
    return words.pop(0)

# 返回数组最后一个
def print_last_word(words):
    return words.pop(-1)

