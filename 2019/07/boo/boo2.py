from bs4 import BeautifulSoup
import requests
def get_url(dwz):
    url = 'http://b00.tw/'+dwz+'?l=zh-CN'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Referer':'http://boo.tw/'+dwz,'Cookie':'__cfduid=dbe7f283940f0ab449fc82dc848d020871561471287'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    url = soup.find(id='shorturl-go')
    # print(url)
    if url:
        urls = url.get('x')
        return urls
        # urls = url.get('x')
        # print('1---')
        # return urls
    # else:
        # print('---')
    # print(urls)
a=['VJx-A',
'BJ5Y_',
'1O8hZ',
'y4GUV',
'7UpEB',
'R-coH',
'gf410',
'bUv23',
'Ojkzu',
'QbWra',
'gqh5-',
'b67hJ',
'1bp3A',
'J9Fh_',
'3pElI',
'GfQkP',
'ZEo8M',
'8VKGt',
't8in0',
'gBv9x',
'oLAUy',
'e80rK',
'xvuqI',
'nDQEF',
'k9-gf',
'Y9o63',
'x9zUo',
'pvOXO',
'BIOSr',
'Tl_mA',
'ikRwP',
'lOfh3',
'JaGbR',
'FaSBO',
'JyLV7',
'u7DQS',
'HwnL6',
'q1kbo',
'AgkVh',
'YlBKU',
'EqQ7P',
'kUAJP',
'D6WTx',
'kiWE7',
'hkcBD',
'Fpp4b',
'kQYm_',
'd3i8-',
'paynI',
'vv4Bu']
for x in a:
    print(get_url(x))