import requests

from lxml import html
'''
    get_movie_url(String url):void
'''
def get_movie_url(url):
    # url='https://www.okzyw.com/?m=vod-index-pg-1.html' #需要爬数据的网址
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
    page=requests.get(url,headers=headers) 
    tree=html.fromstring(page.text) 
    # movie_name=tree.xpath("//div[@class='xing_vb']//ul/li/span/a/text()") #获取需要的数据
    movie_link=tree.xpath("//div[@class='xing_vb']//ul/li/span/a/@href") #获取需要的数据
    movie_type=tree.xpath("//div[@class='xing_vb']//ul/li/span[3]/text()") #获取需要的数据
    movie_type.pop(0)
    for url in movie_link:
        page_url='https://www.okzyw.com'+str(url)
        print(get_movie_info(page_url))
        print("--------------------")
        # exit()
def info_to_str(info):
    if(type(info)==list and len(info)>0):
        return str(info[0])
    elif(type(info)==list and len(info)==0):
        return ''
    else:
        return str(info)
def info_to_int(info):
    if(type(info)==list and len(info)>0):
        return int(info[0])
    elif(type(info)==list and len(info)==0):
        return ''
    else:
        return int(info)
def info_to_float(info):
    if(type(info)==list and len(info)>0):
        return float(info[0])
    elif(type(info)==list and len(info)==0):
        return ''
    else:
        return float(info)
'''
    get_movie_info(String url):字典Dictionary
'''
def get_movie_info(url):
    # print(url)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
    page=requests.get(url,headers=headers) 
    tree=html.fromstring(page.text) 
    #电影名称
    movie_name=info_to_str(tree.xpath("//h2/text()"))

    # 清晰度
    movie_qingxi=info_to_str(tree.xpath("//div[@class='vodh']/span/text()"))

    # 评分
    movie_pingfen=info_to_float(tree.xpath("//div[@class='vodh']/label/text()"))

    # 别名
    movie_bieming=info_to_str(tree.xpath("//div[@class='vodinfobox']/ul/li[1]/span/text()"))

    # 导演
    movie_daoyan=info_to_str(tree.xpath("//div[@class='vodinfobox']/ul/li[2]/span/text()"))

    # 主演
    movie_zhuyan=info_to_str(tree.xpath("//div[@class='vodinfobox']/ul/li[3]/span/text()"))

    # 类型
    movie_type=info_to_str(tree.xpath("//div[@class='vodinfobox']/ul/li[4]/span/text()"))

    # 地区
    movie_diqu=info_to_str(tree.xpath("//div[@class='vodinfobox']/ul/li[5]/span/text()"))

    # 语言
    movie_language=info_to_str(tree.xpath("//div[@class='vodinfobox']/ul/li[6]/span/text()"))

    # 上映
    movie_shangying=info_to_str(tree.xpath("//div[@class='vodinfobox']/ul/li[7]/span/text()"))

    # 片长
    movie_lenght=info_to_str(tree.xpath("//div[@class='vodinfobox']/ul/li[8]/span/text()"))

    # 更新
    movie_update=info_to_str(tree.xpath("//div[@class='vodinfobox']/ul/li[9]/span/text()"))

    # 总播放量
    movie_playSum=info_to_str(tree.xpath("//div[@class='vodinfobox']/ul/li[10]/span/text()"))

    # 今日播放量
    movie_todayPlay=info_to_int(tree.xpath("//div[@class='vodinfobox']/ul/li[11]/span/text()"))

    # 总评分数
    movie_pingfenSum=info_to_int(tree.xpath("//div[@class='vodinfobox']/ul/li[12]/span/text()"))

    # 评分次数
    movie_pingfenN=info_to_int(tree.xpath("//div[@class='vodinfobox']/ul/li[13]/span/text()"))

    # 剧情介绍
    movie_jianjie=info_to_str(tree.xpath("//div[@class='jjText']/comment()"))
    movie_jianjie=movie_jianjie.strip('<!-- span class="more" txt="')
    movie_jianjie=movie_jianjie.strip('</span>  -->')

    # kuyun
    movie_kuyun=info_to_str(tree.xpath("//*[@id='1']/ul/li/input/@value"))

    # m3u8
    movie_m3u8=info_to_str(tree.xpath("//*[@id='2']/ul/li/input/@value"))

    # 迅雷
    movie_xunlei=info_to_str(tree.xpath("//*[@id='down_1']/ul/li/input/@value"))

    # 图片
    movie_image=info_to_str(tree.xpath("//img[@class='lazy']/@src"))
    #key
    array_key=['movie_name','movie_qingxi','movie_pingfen','movie_bieming','movie_daoyan',
                'movie_zhuyan','movie_type','movie_diqu','movie_language','movie_shangying',
                'movie_lenght','movie_update','movie_playSum','movie_todayPlay','movie_pingfenSum',
                'movie_pingfenN','movie_jianjie','movie_kuyun','movie_m3u8','movie_xunlei','movie_image']
    array_value=[movie_name,movie_qingxi,movie_pingfen,movie_bieming,movie_daoyan,
                movie_zhuyan,movie_type,movie_diqu,movie_language,movie_shangying,
                movie_lenght,movie_update,movie_playSum,movie_todayPlay,movie_pingfenSum,
                movie_pingfenN,movie_jianjie,movie_kuyun,movie_m3u8,movie_xunlei,movie_image]
    #合并成字典
    return dict(zip(array_key,array_value))
def main():
    url = "http://www.okzyw.com/?m=vod-index-pg-1.html"
    get_movie_url(url)

if __name__ == '__main__':
    main()
    # movie_update=tree.xpath("//div[@class='xing_vb']//ul/li/span[4]/text()") #获取需要的数据
