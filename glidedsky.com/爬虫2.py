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
    'cookie':'_ga=GA1.2.1345585421.1566567811; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1566567810,1566660967,1566818793; _gid=GA1.2.1602433473.1566818793; _gat_gtag_UA_75859356_3=1; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1566825627; XSRF-TOKEN=eyJpdiI6Iks0MjZyUUVEbkFzVFZoSExTZGVnb1E9PSIsInZhbHVlIjoidUd4M0lXMzdsNVhGcFRLcFphdXI0TFh1MHJPTUY0UU1jblpTQ2tmK3MrYlRqR09hamtuczVMc2ZhdGUyMTJCUCIsIm1hYyI6IjJjYTNhOTNmZjc4YTBkMTI5MGUxNDFmNTUwNDA1YjkwMjI4NzI0MTU4N2U0ZTcwY2I4ZTQzZjMzNmY4MWU4MjQifQ%3D%3D; glidedsky_session=eyJpdiI6Ik1uU2VzSGUwWlNoeVdVWGhiSWRcL1VRPT0iLCJ2YWx1ZSI6ImxyVThBZDE5bzZBRjBVM0FuR0NOQ1JVVHNEVjl2bWhLdmVURUxQTDJGTUNEXC9lUnhwTlBiZDZEcjJWcmk3a0pRIiwibWFjIjoiMzViZTdmMzY2MWVjODM0YmUzNmJhMWViMjU1NjhiMTZjMDMzZTM3ZDRhMGRlNzUxMGE2OGNlNTAwMTkwYWZkNiJ9',

#cookie为网站提供，每次都不一样
    'Upgrade-Insecure-Requests':'1',
    'Cache-Control':'max-age=0',
    }
     sum=0
     for i in range(1,1001) :
          c=0
          target='http://glidedsky.com/level/web/crawler-basic-2?page='+str(i)
#多个有规律网站的进入方式
          if i==1000:
               print('哈哈哈哈哈哈哈哈哈哈‘')
          elif i == 1001:
               print('hehe')
'''
这两个奇怪的if是为了测试，range函数是否执行stop，结果不执行
'''
          req = requests.get(url = target,headers=headers)
          req.encoding='utf-8'
          html = req.text
          bf = BeautifulSoup(html,'lxml')
          texts = bf.find('div', class_ = 'card-body')
          a=texts.get_text("|", strip=True)
     #find返回的为一个元素的列表，元素为字符串
          b=a.split("|")
     #将texts列表中的一个元素以’|‘切片，返回的为包含所有数字的列表
          for i in range(len(b)):
               c=c+int(b[i])
     #将字符串转为整形并求和
          sum+=c
     print(sum)

'''
爬虫往往不能在一个页面里面获取全部想要的数据，需要访问大量的网页才能够完成任务。

这里有一个网站，还是求所有数字的和，只是这次分了1000页。
请求文件为glidedsky.com


'''
