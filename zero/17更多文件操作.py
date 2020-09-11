#!/usr/bin/env python
# coding=utf-8
'''
Date: 2020-09-05 16:10:21
Author: JackCh3n
LastEditTime: 2020-09-05 16:50:32
LastEditors: JackCh3n
FilePath: \zero\17更多文件操作.py
'''
import sys,os
script, file_a, file_b = sys.argv

file_a  = open(file_a)
text_a = file_a.read()
print(f'file a is {len(text_a)} bytes long')

print(f'file b is {os.path.exists(file_b)}')