def f_test(*str):
    '''
    可变参数
    '''
    for x in str:
        print(x)
f_test('123','qwe','asd','zxc')

'''
神奇的返回方式
'''
def return_more(int_value):
    return int_value*1.01, int_value+1024, int_value-223
a, b, c = return_more(100)
print('-' * 20)
print(a)
print(b)
print(c)
