from bs4 import BeautifulSoup
import requests
def parseHtml(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}

    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    #使用css选择器获取class="article"的节点下面的所有li节点
    for index,li in enumerate(soup.select(".xing_vb ul")):
    	# print(index)
        if (index>0 and index<51):
            # movie_name=li.find(class_="xing_vb4").a.text

            print(li.find(class_="xing_vb5").previous_siblings.text)
            # movie_updata=movie_name.find("更新",0)
            # print(movie_updata)
            
            # print("电影名称："+movie_name)
            # if (movie_updata==-1):
            #     movie_update=li.find(class_="xing_vb6").text
            # else:
            #     movie_update=li.find("span[4]").text

            # movie_type=li.find(class_="xing_vb5").text
            # print("电影类型："+movie_name)
            # print("更新时间："+movie_update)
            print('--------')
    		# pass
	    	# print('歌曲名：' + li.find(class_="xing_vb4").a.text)#使用方法选择器
	        # print('歌曲排名：' + li.span.text)
	        # print('歌曲链接：' + li.a['href'])
	        # print('歌曲名：' + li.find(class_="icon-play").a.text)#使用方法选择器
	        # print('演唱者/播放次数：' + li.find(class_="intro").p.text.strip())
	        # print('上榜时间：'+li.find(class_="days").text.strip())
def main():
    url = "http://www.okzyw.com/?m=vod-index-pg-1.html"
    parseHtml(url)

if __name__ == '__main__':
    main()