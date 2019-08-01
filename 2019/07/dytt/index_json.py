import requests
import json
import time
from bs4 import BeautifulSoup
print(str(int(time.time())))
headers = {'user-agent': 'okhttp/3.8.0','x-header-request-key':'68134c60606fa1677e43b080aced00c8','Accept-Encoding':'gzip','x-header-request-timestamp':'1'}
movie_list = requests.get('http://m.dydytt.net:8080/adminapi/api/movieList.json?categoryId=9&page=1&searchContent=',headers=headers)
print(movie_list.text)
# print(json.loads(movie_list.text))