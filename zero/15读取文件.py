#!/usr/bin/env python
# coding=utf-8
'''
Date: 2020-09-05 15:46:23
Author: JackCh3n
LastEditTime: 2020-09-05 15:55:34
LastEditors: JackCh3n
FilePath: \zero\15读取文件.py
'''
from sys import argv
script, file_name = argv
text = open(file_name)
# open 返回的的是文件对象
print(f'要读取的文件是\t{file_name}')
print(text.read())

print('请输入要读取的文件名称:')
file_again = input('>')
text_again = open(file_again)

print(text_again.read())