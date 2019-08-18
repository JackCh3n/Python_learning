# -*- coding: utf8 -*-
import requests
import time
import onethingpcs
# from onethingpcs.turnsession import test_turnsession
from bs4 import BeautifulSoup


def get_page(url, movie_list):
    '''
    获取电影列表
    最新电影：https://www.ygdy8.net/html/gndy/dyzz/list_23_2.html
    一页25部电影.
    '''
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    html = requests.get(url, headers=headers)
    try:
        html.encoding = 'gb18030'
        bsObj = BeautifulSoup(html.text, 'html.parser')
        # 设置缓存目录
        for i in bsObj.find_all('a', {'class': 'ulink'}):
            url_mark = ''
            url_mark = i.attrs['href'].split('/')[5]
            # 58895.html
            temp_id = int(url_mark.replace('.html', ''))
            if file_exists_id(temp_id):
                print(i.get_text()+'___已下载跳过')
                continue
            else:
                link = html_de_link('https://www.ygdy8.net'+i.attrs['href'])
                if link:
                    print(i.get_text()+'___加入下载列表')
                    # download_movie(link)
                    movie_list.append(link)
    except ArithmeticError as e:
        print(e)
        return None


def html_de_link(url):
    '''获取电影下载链接'''
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    html = requests.get(url, headers=headers)
    try:
        html.encoding = 'gb18030'
        bsObj = BeautifulSoup(html.text, 'html.parser')
        if bsObj.title:
            return bsObj.find('td', {'style': 'WORD-WRAP: break-word'}).a.attrs['href']
        else:
            return None
    except ArithmeticError as e:
        print(e)


def file_exists_id(t_id):
    params = {'user': 'passwd', 'id': t_id}
    ids = requests.get('https://api.tiiao.cn/dytt.php', params=params)
    return True if ids.text == '1' else False


def push_ios(message):
    '''
    通过OnlyTalk API来推送到IOS设备
    '''
    USER_KEY = 'qweasdzxc'
    # 日了狗，python没有常量
    requests.get('https://www.onlytalk.top/api/v1/push/'+USER_KEY+'/'+message)


def main_handler(event, context):
    # print("Received event: " + json.dumps(event, indent = 2)) 
    # print("Received context: " + str(context))
    # 下载列表
    movie_list = []
    # 计数
    n = 0
    # 今天的时间
    ymd = time.strftime("%Y_%m_%d_", time.localtime())
    for i in range(1, 2):
        get_page('https://www.ygdy8.net/html/gndy/dyzz/list_23_'+str(i)+'.html', movie_list)
        # 最新电影

    otc = onethingpcs.otc_api()
    login_status = otc.login(user="number", passwd="passwd")
    if login_status:
        print("登陆成功")
    else:
        print("登陆失败")

    # 获取远端信息
    peer_status = otc.list_peer_info()
    if peer_status:
        print("获取成功")
        # print(otc.get_peer_info())
        # print(otc.get_peer_id())
    else:
        print("获取失败")
    for temp_link in movie_list:
        # 分割字符串获取文件名
        temp_name_sp = temp_link.split('/')
        temp_name = temp_name_sp[(len(temp_name_sp)-1)]
        # 文件名过滤
        temp_name = temp_name.replace('：', ':').replace('阳光电影www.ygdy8.com.', '')
        # 推送到玩客云
        otc.create_remote_download_task(url=temp_link, file_name=ymd+temp_name)
        n += 1
    # 推送到手机
    push_ios('迅雷脚本:即将下载【'+str(n)+'】部电影')