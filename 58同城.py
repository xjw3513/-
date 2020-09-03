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
    req.add_header("Host", "nc.58.com")
    req.add_header("Referer", "https://nc.58.com/job.shtml?PGTID=0d100000-0029-dc2a-9a53-dd069a767e65&ClickID=2")

    content = urllib.request.urlopen(req).read()
    html = content.decode("utf-8")
    return html


url = "https://nc.58.com/job/?key=%E5%AE%B6%E6%95%99&final=1&jump=1"
# 这里面的my_headers中的内容由于是个人主机的信息，所以我就用句号省略了一些，在使用时可以将自己主机的User-Agent放进去
my_headers = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"]
html = getContent(url, my_headers)
soup = BeautifulSoup(html,"html.parser")

data = []
i = 0
for name in soup.select('span.name'):
    data.append(name.string)
print(data)