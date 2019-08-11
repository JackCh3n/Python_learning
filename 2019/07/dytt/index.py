# -*-coding:gb18030-*-
import requests
import re
import os
import psutil
import time
from bs4 import BeautifulSoup
def get_page(url,movie_list):
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
        n = 0
        for i in bsObj.find_all('a',{'class':'ulink'}):
            if get_disk_free() < 3:
                push_ios('迅雷脚本:空间小于3G')
                #剩余空间小于3G就不下载,推送消息
                break
            url_mark = ''
            url_mark = i.attrs['href'].split('/')[5]#58895.html
            run_dir = set_dir()
            os.chdir(run_dir)
            if os.path.isfile(run_dir+url_mark):
                print(i.get_text()+'___已下载跳过')
                continue
            else:
                link = html_de_link('https://www.ygdy8.net'+i.attrs['href'])
                if link:
                    with open(run_dir+url_mark,'w',encoding='gb18030') as urls:
                        urls.writelines('{"name":"'+i.get_text()+'","link":'+link+'"}');
                        urls.close()
                    print(i.get_text()+'___加入下载中')
                    n += 1
                    download_movie(link)
            time.sleep(300)#5分钟,100M宽带，5m/s 60*5*5 大概1.5G左右
        push_ios('迅雷脚本:共下载【'+str(n)+'】部电影')
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

def get_disk_free():
    '''
    获取py文件所属分区可用空间
    需要 import psutil
    返回 GB/int
    '''
    disk_free_size = psutil.disk_usage('/')
    return int(disk_free_size.free/1024/1024/1024)
def download_movie(url):
    '''
    下载电影，防止硬盘塞满，定时删除
    假设每部电影2gb
    迅雷X起支持ftp链接，不用专门去转换链接
    '''
    # os.chdir("D:\\xiao\\ThunderX\\Program")
    os.system("D:\\xiao\\ThunderX\\Program\\Thunder.exe -StartType:DesktopIcon \"%s\""%url)
def url2txt(url):
    '''
    保存下载链接

    '''
    with open('urls.txt','a+') as urls:
        urls.writelines(url+'\n');
        urls.close()
def push_ios(message):
    '''
    通过OnlyTalk API来推送到IOS设备
    '''
    USER_KEY = 'a15ecdefb94597d67438676fc1f77923cbe7d2c5a15c7d1435af5c76861392d3'#日了狗，python没有常量
    requests.get('https://www.onlytalk.top/api/v1/push/'+USER_KEY+'/'+message)
def set_dir():
    '''
    设置执行文件夹
    '''
    run_dir = 'D:\\robot\\history\\';
    if not os.path.exists(run_dir):
        os.mkdir(run_dir);
    return run_dir
if __name__ == '__main__':
    disk_free_size = psutil.disk_usage('/')#获取py文件所属分区情况
    movie_list=[]
    for i in range(1,4):
        get_page('https://www.ygdy8.net/html/gndy/dyzz/list_23_'+str(i)+'.html',movie_list)#最新电影
    # download_movie('ftp://ygdy8:ygdy8@yg45.dydytt.net:4207/阳光电影www.ygdy8.com.复仇者联盟4：终局之战.HD.720p.中英双字幕.mkv')
    # print(movie_list)
    if int(time.strftime("%H", time.localtime())) < 9:
        os.system("shutdown -s -t 1800")#半小时后关机,9点后网络唤醒
    