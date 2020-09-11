#!/usr/bin/env python
# coding=utf-8
'''
Date: 2020-09-07 21:09:12
Author: JackCh3n
LastEditTime: 2020-09-07 21:21:26
LastEditors: JackCh3n
FilePath: \zero\20函数和文件.py
'''
from sys import argv
script, file_name = argv

# 读取第一字节
def print_one(f):
    print(f.seek(1))

# 打印全部内容
def print_all(f):
    print(f.read())

# 打印一行
def print_line(line_count, f):
    print(line_count, f.readline())

text = open(file_name)

print_one(text)
print('----')
print_all(text)
print('----')
print_line('1',text)