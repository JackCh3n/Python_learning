from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
def get_movie_list(url):
    try:
        html =  urlopen(url)
    except HTTPError as e:
        print(e)
    try:
        bsObj=BeautifulSoup(html.read(),'lxml')
        movie_list=[]
        # b = bsObj.select('div.detail > div > div.list > ul > li')
        # print(b)
        for x in bsObj.select('div.detail > div > div.list > ul > li'):
            # print(x.a.previous_sibling.string[1:3])#类型
            m_link = x.a.attrs['href']#简介链接
            # m_name = x.a.get_text()#电影名称
            # m_update = x.span.string.replace('[','').replace(']','')#时间
            movie_list.append(get_movie_info(m_link))
        return movie_list
    except AttributeError as e:
        print(e)
        
'''
    获取具体的电影信息
'''
def get_movie_info(url):
    try:
        html =  urlopen(url)
    except HTTPError as e:
        print(e)
    try:
        bsObj=BeautifulSoup(html.read(),'lxml')
        board_img = bsObj.find('div',{'class':'cover'}).find('img').attrs['src']#图片

        info = bsObj.find('div',{'class':'duction'}).get_text()#名称,导演，编剧，主演，类型，国家，语言，上映时间，片长，又名，imdb，评分
        info = info.replace('\r','').replace('\t','').split('\n')
        del info[0]
        info[1] = info[1].strip()
        
        plot = bsObj.select('div.info_detail > p')[0].get_text().strip()#剧情

        previews = bsObj.find_all('div',{'class':'swiper-slide'})
        preview=[]#预览图片
        for v in previews:
            preview.append(v.img.attrs['src'])

        down_hrefs = bsObj.find_all('a',{'class':'btn btn-default btndy'})#下载链接
        down_href=[]#下载地址,只获取磁力链接
        for i in down_hrefs:
            temp_href=i.attrs['href']
            if 'magnet:?xt=urn:btih:' in temp_href:
                down_href.append(temp_href)
        return {'board_img':board_img,'info':info,'plot':plot,'preview':preview,'down_hrefs':down_hrefs}
    except AttributeError as e:
        print(e)
if __name__ == '__main__':
    ranking_lists = get_movie_list('http://www.mp4ba.com/dianying/list_1.html')
    # get_movie_info('http://www.mp4ba.com/juqingpian/1366.html')
    # for i in range(2,3):#范围10-90
        # ranking_lists.append(get_ranking_list('http://www.mp4ba.com/dianying/list_1.html'+str(i)))
    print(ranking_lists)
