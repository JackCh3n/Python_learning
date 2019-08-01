# -*-coding:gb18030-*-
import requests
import re
from bs4 import BeautifulSoup
#获取电影列表
def get_page(url,movie_list):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    html = requests.get(url,headers=headers)
    try:
        html.encoding = 'gb18030'
        bsObj = BeautifulSoup(html.text,'lxml')
        for i in bsObj.find_all('a',{'class':'ulink'}):
            print(i.get_text())
            link = html_de_link('https://www.ygdy8.net'+i.attrs['href'])
            # print('https://www.ygdy8.net'+i.attrs['href'])
            if link:
                movie_list.append([i.get_text(),link])
    except ArithmeticError as e:
        return None
#获取电影下载链接
def html_de_link(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    html = requests.get(url,headers=headers)
    try:
        html.encoding = 'gb18030'
        bsObj = BeautifulSoup(html.text,'lxml')
        if bsObj.title:
            return bsObj.find('td',{'style':'WORD-WRAP: break-word'}).a.attrs['href']
        else:
            return None
    except ArithmeticError as e:
        print(e)

def html_de_link_regex(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    html = requests.get(url,headers=headers)
    try:
        html.encoding = 'gb18030'
        pattern = re.compile(r'ftp+://[^s]*(avi|rmvb|mp4|mov|flv|wmv|mkv)')
        # url = pattern.search(html.text).group(0)
        print(pattern.search(html.text).group())
    except ArithmeticError as e:
        print(e)
# get_page('https://www.ygdy8.net/html/gndy/dyzz/list_23_1.html')
# pattern = re.compile(r'ftp+://[^s]*(avi|mpeg|rmvb|mp4|mov|flv|wmv|mkv)')
# str = ''
# print(pattern.search(str))
# html_de_link('https://www.ygdy8.net/html/gndy/dyzz/20190702/58768.html')
# html_de_link_regex('https://www.ygdy8.net/html/gndy/dyzz/20190702/58768.html')
if __name__ == '__main__':
    movie_list=[]
    for i in range(1,2):
        get_page('https://www.ygdy8.net/html/gndy/dyzz/list_23_'+str(i)+'.html',movie_list)
    print(movie_list)