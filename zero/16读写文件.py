#!/usr/bin/env python
# coding=utf-8
'''
Date: 2020-08-31 14:29:24
Author: JackCh3n
LastEditTime: 2020-09-05 16:08:29
LastEditors: JackCh3n
FilePath: \zero\16读写文件.py
模式
    a 追加 apped
        因为是追加，所以不存在,便创建，如同写一般 
    w 写入 write
        因为是写，所以不存在,便创建
    r 读取 read
'''
# 读取
text_object = open('text.txt','r+')
text_txt = text_object.read()
print(f'读取的内容是:\n{text_txt}')


# 写入
text_object.write('苹果')
text_object.write('橘子')

# 关闭
text_object.close()
