#-*- coding:utf-8 -*-
#!/usr/bin/env python2.7

# from pyv8 import PyV8
import time
import json
import hashlib
import requests

url1 = 'http://captcha.su.baidu.com/session_cb/?pub=377e4907e1a3b419708dbd00df9e8f79&callback=callback'
rsp = requests.get(url1)
dt = json.loads(rsp.text.lstrip('callback(').rstrip(')'))
session=dt['sessionstr']
#请求验证码
yzm_url='https://captcha.su.baidu.com/image/?session='+session+'&pub=377e4907e1a3b419708dbd00df9e8f79'
yzm = requests.get(yzm_url)
with open('code.jpg','wb') as file:
    file.write(yzm.content)
print(yzm_url)