'''
格式化
'''
my_name = 'jack'
my_age = 18
c = f'hello {my_name} do you age have {my_age} ?'
print(f'my name is {my_name} now age is {my_age}')
print(c)
# 四舍五入
print(round(1.4))
print(round(2.5))
# 格式化2
print('i love {}'.format('china'))
# 字符重复
print('-' * 10)
# 注释规范，#[空格]注释内容
def test(str):
    return str*1, str*2, str*3
strs = test('ha')
print('ni {} me?\n wo {} \n da jia {}'.format(*strs))
