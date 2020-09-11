#!/usr/bin/env python
# coding=utf-8
'''
Date: 2020-09-07 22:02:21
Author: JackCh3n
LastEditTime: 2020-09-08 14:13:15
LastEditors: JackCh3n
FilePath: \zero\23字符串字节串和字符编码.py
'''
import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # 移除空白
    next_lang = line.strip()
    # 编码
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # 解码
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes,'<====>',cooked_string)

language = open('languages.txt', encoding='utf-8')

main(language, encoding, error)