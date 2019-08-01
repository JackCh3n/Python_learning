# -*-coding:utf-8-*-
import requests
import re
from bs4 import BeautifulSoup
def diff(listA,listB):
    #求差集，在A中但不在B中；把A中的B去除
    return list(set(listA).difference(set(listB)))

a = '''影片名称：【初撮り】ネットでAV応募→AV体験撮影 1016 彼氏とハメ撮りすらしたことがない娘が緊張の撮影初体験！身長170cmの美脚美女が見せるちょっとぎこちない仕草にギャップ萌え！
影片容量:1.22GB
出演：        りさ 20歳 コンビニアルバイト
メーカー：        シロウトTV
収録時間：        57min
配信開始日：        2019/07/16
シリーズ：        【初撮り】ネットでAV応募→AV体験撮影
レーベル：        
ジャンル：        独占配信 ハイビジョン(HD) 配信専用 素人 初撮り 長身 美脚 パイパン 顔射
品番：        SIRO-3886

  
磁力链接
magnet:?xt=urn:btih:10F423579914DA97A2C4D22202C805185BB0E6D3
复制代码'''
# print(a)
#获取电影列表
def get_page(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    html = requests.get(url,headers=headers)
    html.encoding = 'utf-8'
    bsObj = BeautifulSoup(html.text,'lxml')
    b = bsObj.find('td',{'class':'t_f'})
    print(b.get_text())
get_page('http://localhost:8080/page.html')