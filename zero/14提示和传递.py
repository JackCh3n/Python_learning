#!/usr/bin/env python
# coding=utf-8
'''
Date: 2020-09-05 15:06:21
Author: JackCh3n
LastEditTime: 2020-09-05 15:44:54
LastEditors: JackCh3n
FilePath: \zero\14提示和传递.py
'''
from sys import argv
path, user_name = argv
data_error = '>'
print(f'你好 {user_name}, 我是python脚本\r {path}')
print(f'我有几个问题想问你')
print(f'你喜欢我么{user_name}')
like = input(data_error)

print(f'你生活在哪里? {user_name}')
live = input(data_error)

print('你的电脑是笔记本还是台式?')
computer = input(data_error)
print(f'''
好的,我已经大概知道了.
你看起来 {like} 喜欢我
你生活在 {live} 
{computer} 是你的主用电脑
''')
