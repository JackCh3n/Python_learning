# -*-coding:utf-8-*-
import requests
import re
from bs4 import BeautifulSoup
#求差集，在A中但不在B中；把A中的B去除
def diff(listA,listB):
    return list(set(listA).difference(set(listB)))
#获取电影列表
def get_page(url,movie_list):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    proxies = {"http": "http://127.0.0.1:1080", "https": "127.0.0.1:1080"}
    html = requests.get(url,headers=headers, proxies=proxies)
    # html = requests.get(url,headers=headers)
    try:
        html.encoding = 'utf-8'
        bsObj = BeautifulSoup(html.text,'lxml')
        url_list = bsObj.find_all('a',{'class':'s xst'})#获取全部链接
        print(str(type(url_list)))
        print(len(url_list))
        # print(url_list)
        url_list_b = ['thread-141587-1-1.html','thread-141585-1-1.html','thread-126525-1-1.html','thread-101886-1-1.html']
        #发布器，app，改革，招聘
        for item in url_list:
            temp_url = item.attrs['href']
            if temp_url not in url_list_b:
                print(item.get_text()+'----正在获取中')#标题
                # print(temp_url)#链接
                movie_list.append(html_de_link('https://www.sehuatang.net/'+temp_url))
                print('----成功捕获一只小姐姐----')
                break
    except ArithmeticError as e:
        return None
#获取电影下载链接
def html_de_link(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    proxies = {"http": "http://127.0.0.1:1080", "https": "127.0.0.1:1080"}
    html = requests.get(url,headers=headers, proxies=proxies)
    try:
        html.encoding = 'utf-8'
        bsObj = BeautifulSoup(html.text,'lxml')
        if bsObj.title:
            b = bsObj.find('td',{'class':'t_f'})
            # print(len(b))
            c = b.get_text().replace('：',':').replace('：',':').replace('\r','').split("\n")
            # print(c)
            #种子
            torrent = b.select('a[target="_blank"]')
            if torrent:
                torrent = torrent[0].attrs['href']
            # print(torrent)
            
            #图片
            image = b.find_all('img')
            images = []
            for item in image:
                images.append(item.attrs['file'])
            # print(images)
            
            #影片信息
            movie_info = {}
            for item in c:
                if item.startswith('影片名称:'):
                    # print(item.replace('影片名称:',""))
                    movie_info['name'] = item.replace('影片名称:',"")

                if item.startswith('影片容量:'):
                    movie_info['size'] = (item.replace('影片容量:',""))

                if item.startswith('出演:'):
                    movie_info['star'] = (item.replace('出演:        ',""))

                if item.startswith('収録時間:'):
                    movie_info['Rtime'] = (item.replace('収録時間:        ',""))

                if item.startswith('シリーズ:'):
                    movie_info['series'] = (item.replace('シリーズ:        ',""))

                if item.startswith('レーベル:'):
                    movie_info['lable'] = (item.replace('レーベル:        ',""))

                if item.startswith('ジャンル:'):
                    movie_info['schools'] = (item.replace('ジャンル:        ',""))

                if item.startswith('品番:'):
                    movie_info['code'] = (item.replace('品番:        ',""))

                if item.startswith('magnet:'):
                    movie_info['magnet'] = (item.replace('复制代码',""))
                if item.startswith('磁力链接 '):
                    movie_info['magnet'] = (item.replace('复制代码',"").replace('磁力链接 ',''))
            movie_info['torrent'] = 'https://www.sehuatang.net/'+torrent
            movie_info['images'] = images
            return movie_info
            # print(movie_info)
            # return bsObj.find('td',{'style':'WORD-WRAP: break-word'}).a.attrs['href']
        # else:
            # return None
    except ArithmeticError as e:
        print(e)


if __name__ == '__main__':
    movie_list=[]
    for i in range(1,2):
        get_page('https://www.sehuatang.net/forum-37-'+str(i)+'.html',movie_list)
    print(movie_list)
    # get_page('http://localhost:8080/list.html',movie_list)
    # html_de_link('http://localhost:8080/page.html')