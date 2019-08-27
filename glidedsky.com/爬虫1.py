import requests
from bs4 import BeautifulSoup
import lxml
from bs4 import BeautifulSoup

import re
if __name__ == "__main__":
     headers = {
    'Host':'glidedsky.com',
    'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64;rv:67.0)Gecko/20100101Firefox/67.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip,deflate',
    'Referer':'http://glidedsky.com/level/crawler-basic-1',
    'Connection':'keep-alive',
    'cookie': '_ga=GA1.2.1345585421.1566567811; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1566567810,1566660967,1566818793; _gid=GA1.2.1602433473.1566818793; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1566822957; _gat_gtag_UA_75859356_3=1; XSRF-TOKEN=eyJpdiI6IkRGaXVuRGdxVWw5Tm0zNDZVOWZxVUE9PSIsInZhbHVlIjoiNGJwMFZpVkw5dkd6UEk5XC9NT3VPbFdcL2c3Mm1PNXR5TGFpcmUyQ21BYzVwOFwvZDhrMjlUa3ozaDRSQlR1aWdWayIsIm1hYyI6IjgyZDRlZGNlNTAyMmUyMGFmNTJhNDYwYTU3Mjc5ZDliNDI3ZWQ5YzMxOWZhOWE3Yjc4YmMxNDlmYTA2ZTg5NDMifQ%3D%3D; glidedsky_session=eyJpdiI6InNLaUlWZUdEaHNybFhYR0RkNUxjRUE9PSIsInZhbHVlIjoia09yakZVanJPSWxkUG5xbEYyb0dHSll0Y3EzSmkrUklWVUpQd2ZLU3pIN1JBRWs5MVBGVG9Ca1ZGcjAwY1c3bCIsIm1hYyI6IjQ3ZjAwYTIzZGRjOWZmZTM0NTExYWNkMTQ0ZDNjNTQ4ODM5MTRiODNhMmU4NmQ2MjI4NTk3NGNlYzMyZmI4YmQifQ%3D%3D',
#cookie为网站提供，每次都不一样
    'Upgrade-Insecure-Requests':'1',
    'Cache-Control':'max-age=0',
    }

     target='http://glidedsky.com/level/web/crawler-basic-1'
     req = requests.get(url = target,headers=headers)
     print(req)
     req.encoding='utf-8'
     html = req.text
     bf = BeautifulSoup(html,'lxml')
     texts = bf.find('div', class_ = 'card-body')
     a=texts.get_text("|", strip=True)
#find返回的为一个元素的列表，元素为字符串
     b=a.split("|")
#将texts列表中的一个元素以’|‘切片，返回的为包含所有数字的列表
     c=0
     for i in range(len(b)):
          
          c+=int(b[i])
#将字符串转为整形并求和
     print(c)

'''
爬虫的目标很简单，就是拿到想要的数据。

这里有一个网站，里面有一些数字。把这些数字的总和，输入到答案框里面，即可通过本关。

提交之前要验证邮箱哦~

待爬取网站为http://glidedsky.com/level/web/crawler-basic-1

'''
