# coding=utf-8
import urllib.request
import random
import requests
from bs4 import BeautifulSoup
import re
import datetime

def getContent(url, headers):
    """
    此函数用于抓取返回403禁止访问的网页
    """
    random_header = random.choice(headers)

    """
    对于Request中的第二个参数headers，它是字典型参数，所以在传入时
    也可以直接将个字典传入，字典中就是下面元组的键值对应
    """
    req = urllib.request.Request(url)
    req.add_header("User-Agent", random_header)
    req.add_header("GET", url)
    req.add_header("Host", "search.51job.com")
    req.add_header("Referer", "")

    content = urllib.request.urlopen(req).read()
    html = content.decode("gbk")
    return html

# 这里面的my_headers中的内容由于是个人主机的信息，所以我就用句号省略了一些，在使用时可以将自己主机的User-Agent放进去
my_headers = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"]

data = []
for page in range(1,9):
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25AE%25B6%25E6%2595%2599,1,"+str(page)+".html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    html = getContent(url, my_headers)
    pagedata = re.findall(r'"job_title":"(.*?)".*?"providesalary_text":"(.*?)".*?"workarea_text":"(.*?)".*?"updatedate":"(.*?)"',html)
    data.append(pagedata)
for dat in data :
  print(dat)

