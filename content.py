#!/usr/bin/python
# -*- coding:utf-8 -*-
from zhihu_oauth import ZhihuClient
from aip import AipNlp,AipImageCensor
import re
import sys
import requests
headers ={
    'Content-Type':'application/x-www-form-urlencoded'
}

APP_ID = '11156578'
API_KEY = '3K73kH6H4aGoZbUrE1N0oTO5'
SECRET_KEY = 'YoL5g6BCnWG4mQvEo0TjyDPozlySdDRp'

def answer_review(content):
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s&" % (
    API_KEY, SECRET_KEY)
    req = requests.post(url)
    access_token = req.json()["access_token"]
    url = "https://aip.baidubce.com/rest/2.0/antispam/v2/spam?access_token=%s" % (access_token)
    data = {'content': content}
    req = requests.post(url, headers=headers, data=data)
    res = req.json()["result"]
    print ("文字通过:%d") % len(res["pass"])
    print ("文字待审核:%d") % len(res["review"])
    print ("文字违规:%d") % len(res["reject"])

def picture_review(content):
    pic = re.findall(r"<img src=(.*?)data", content)
    h = 0
    l = len(pic)
    client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)
    if l > 0:
        for i in range(l):
            url = pic[0][1:-2]
            result = client.imageCensorUserDefined(url)
            print (result)
            if len(result['conclusion']) == 2:
                h += 1
        print ("图片通过:%d") % h
        print ("图片违规:%d") % (l - h)
    else:
        print ("没有图片")

if __name__ == '__main__':
    client = ZhihuClient()
    client.load_token('token.pkl')
    id = "376064029"
    content = client.answer(id).content
    answer_review(content)
    picture_review(content)
