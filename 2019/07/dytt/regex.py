
import requests
import re
import os
import psutil
import time
from bs4 import BeautifulSoup
def get_page(url):
    '''
    获取电影列表
    最新电影：https://www.ygdy8.net/html/gndy/dyzz/list_23_2.html
    一页25部电影，5分钟*25 1小时差不多，+30分钟缓冲时间
    '''
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    html = requests.get(url,headers=headers)
    try:
        html.encoding = 'gb18030'
        bsObj = BeautifulSoup(html.text,'lxml')
        url_list = bsObj.find_all('div > ul >a',{'class':'co_content2'})
        # url_list[1].pop(0)
        # url_list[1].pop(1)
        # print(len(url_list[1]))
        print(url_list)
        # for i in url_list[1].select('div > ul'):
            # print(i)
    except ArithmeticError as e:
        return None
get_page('https://www.dytt8.net/index.htm')