#!/usr/bin/env python
# coding=utf-8
'''
Date: 2020-09-05 16:59:01
Author: JackCh3n
LastEditTime: 2020-09-05 17:06:04
LastEditors: JackCh3n
FilePath: \zero\18命名变量代码和函数.py
'''
def print_one():
    print('hello world')

# 可以拥有无限个参数
def print_two(*args):
    val1 ,val2 = args
    print(f'传入的参数为{val1}\t{val2}')

def print_three(val):
    print(f'只有个参数的函数\t{val}')

print_one()
print_two('ni','hao')
print_three('three')