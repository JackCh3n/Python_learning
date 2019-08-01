from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def get_ranking_list(url):
    try:
        html =  urlopen(url)
    except HTTPError as e:
        print(e)
    try:
        bsObj=BeautifulSoup(html.read(),'lxml')
        movie_list=[]
        for x in bsObj('dd'):
            ranking = x.find('i').get_text()#排名
            board_img = x.find('img',{'class':'board-img'}).attrs['data-src'].replace('@160w_220h_1e_1c','')#图片
            name = x.find('p').get_text()#电影名称
            star = x.find('p',{'class':'star'}).get_text().strip()#主演
            release_time = x.find('p',{'class':'releasetime'}).get_text().strip()#上映时间
            score = x.find('p',{'class':'score'}).get_text().strip()#评分
            movie_list.append({'ranking' : ranking,'board_img' : board_img,'name' : name,'star' : star,'release_time' : release_time,'score' : score})
        return movie_list
    except AttributeError as e:
        print(e)
if __name__ == '__main__':
    ranking_lists = get_ranking_list('https://maoyan.com/board/4?offset=0')
    for i in range(10,100,10):#范围10-90
        ranking_lists.append(get_ranking_list('https://maoyan.com/board/4?offset='+str(i)))
    print(ranking_lists)