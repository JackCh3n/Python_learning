#!/usr/bin/env python
# coding=utf-8
'''
Date: 2020-09-05 21:14:16
Author: JackCh3n
LastEditTime: 2020-09-05 21:24:07
LastEditors: JackCh3n
FilePath: \zero\19函数和变量.py
'''
def fun_two(a,b):
    print('这是一个简单的函数')
    print(f'可以打印a 的值\t{a}')
    print(f'可以打印b 的值\t{b}')
    print(f'也可以打印a+b=\t{a+b}\n\n')

fun_two(1,2)

fun_two(20,12)
num_a = 100
num_b = 189
fun_two(num_b+2,num_a+3)