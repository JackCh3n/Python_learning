# coding=utf-8
# 参数,解包和变量
'''
接收命令行运行的参数,string
可以无限个参数
argv[]
'''
from sys import argv
print('len----',len(argv))
if len(argv)  == 5:
    script, first, secound, third, a = argv
    # 路径
    print(script)
    # 第一个参数
    print(first)
    # 第二个参数
    print(secound)
    # 第三个参数
    print(third)
    # 第三个参数
    print(a)
else:
    print(argv)