'''
模式
    a 追加 apped
        因为是追加，所以不存在便创建，如同写一般 
    w 写入 write
        因为是写，所以不存在便创建
    r 读取 read
'''
a = open('test.txt','r')
print(a.read())
a.close()