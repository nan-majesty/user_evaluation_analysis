# -*- coding:utf-8 -*-
#爬虫：爬去京东评论150页

import requests
import urllib3
import json
import urllib
import urllib.request
from bs4 import BeautifulSoup
for i in range(1, 150):
    url1 = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4403&productId=3487485&score=3&sortType=5&page='
    url2 = str(i)
    uel3 = '&pageSize=10&isShadowSku=0&rid=0&fold=1'
    finalurl = url1+url2+uel3
    xba = requests.get(finalurl)
    data=json.loads(xba.text[26:-2])
    for i in data['comments']:
        content = i['content']
        print("评论内容".format(content))
        file=open("E:\\reptile\\comm.txt", 'a')
        file.writelines(format(content))
print("finished")