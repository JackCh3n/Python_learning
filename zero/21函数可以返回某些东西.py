#!/usr/bin/env python
# coding=utf-8
'''
Date: 2020-09-07 21:23:14
Author: JackCh3n
LastEditTime: 2020-09-07 22:00:15
LastEditors: JackCh3n
FilePath: \zero\21函数可以返回某些东西.py
'''
def add(a, b):
    print(f'加法 {a} + {b}')
    return a + b

def subtract(a, b):
    print(f'减法 {a} - {b}')
    return a - b

def multiply(a, b):
    print(f'乘法 {a} * {b}')
    return a * b

def divide(a, b):
    print(f'除法 {a} / {b}')
    return a / b

print('================')
age = add(2,16)
height = subtract(190,5)
weight = multiply(10,9)
iq = divide(360,2)

print(f'age: {age}, weight: {weight},height: {height},iq: {iq}')