import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time
from datetime import datetime


# 从职位详情页面内获取职位要求
def getjobneeds(positionId):
    '''

    :param positionId:
    :return:
    '''
    url = 'https://www.lagou.com/jobs/{}.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E8%AE%BE%E8%AE%A1/p-city_0?px=default',
        'Upgrade-Insecure-Requests': '1'
    }

    s = requests.Session()
    s.get(url.format(positionId), headers=headers, timeout=10)  # 请求首页获取cookies
    cookie = s.cookies  # 为此次获取的cookies
    response = s.get(url.format(positionId), headers=headers, cookies=cookie, timeout=10)  # 获取此次文本
    time.sleep(3)  # 休息 休息一下

    soup = BeautifulSoup(response.text, 'html.parser')
    need = ' '.join([p.text.strip() for p in soup.select('.job_bt div')])
    return need


# 获取职位具体信息#获取职位具体
def getjobdetails(jd):
    '''

    :param jd:
    :return:返回结果集
    '''
    results = {}
    results['createTime'] = jd['createTime']
    results['companyShortName'] = jd['companyShortName']
    results['positionName'] = jd['positionName']  # 职位
    results['salary'] = jd['salary']
    results['salaryMonth'] = jd['salaryMonth']
    results['city'] = jd['city']
    results['workYear'] = jd['workYear']
    results['education'] = jd['education']
    results['jobNature'] = jd['jobNature']
    results['positionAdvantage'] = jd['positionAdvantage']
    results['firstType'] = jd['firstType']
    results['secondType'] = jd['secondType']
    results['thirdType'] = jd['thirdType']
    positionId = jd['positionId']
    results['need'] = getjobneeds(positionId)
    results['companyFullName'] = jd['companyFullName']  # 公司名
    results['industryField'] = jd['industryField'] # 公司领域
    results['companyLabelList'] = jd['companyLabelList']  # 公司标签
    results['financeStage'] = jd['financeStage'] # 发展阶段
    results['companySize'] = jd['companySize']  # 公司人数
    results['city'] = jd['city']
    results['district'] = jd['district']
    results['businessZones'] = jd['businessZones']

    print(jd, 'get')
    return results


# 获取整个页面上的职位信息
def parseListLinks(url_start, url_parse):
    '''

    :param url_start:
    :param url_parse:
    :return:
    '''

    jobs = []
    from_data = {'first': 'true',
                'pn': '1',
                'kd': 'java'}#设置爬取岗位

    headers = {
        'Host': 'www.lagou.com',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_%E8%AE%BE%E8%AE%A1/p-city_0?px=default',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
    }

    res = []
    for n in range(1130):#访问页数
        from_data['pn'] = n + 1
        s = requests.Session()
        s.get(url_start, headers=headers, timeout=10)  # 请求首页获取cookies
        cookie = s.cookies  # 为此次获取的cookies
        response = s.post(url_parse, data=from_data, headers=headers, cookies=cookie, timeout=10)  # 获取此次文本
        time.sleep(3)#设置睡眠时间
        res.append(response)

    jd = []
    for m in range(len(res)):
        jd.append(json.loads(res[m].text)['content']['positionResult']['result'])
    for j in range(len(jd)):
        for i in range(len(jd[j])):
            jobs.append(getjobdetails(jd[j][i]))

    return jobs


def main():
    '''
    :return:
    '''
    url_start = "https://www.lagou.com/jobs/list_Java?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput="
    url_parse = "https://www.lagou.com/jobs/positionAjax.json?city=&needAddtionalResult=false"
    jobs_total = parseListLinks(url_start, url_parse)
    now = datetime.now().strftime('%m%d_%H%M%S')
    newsname = 'lagou_sj' + now + '.xlsx'  # 按时间命名文件
    #df = pd.DataFrame(jobs_total)
    #df.to_excel(newsname,engine='xlsxwriter')
    pd.DataFrame(jobs_total).to_excel(newsname,engine='xlsxwriter')
    print('文件已保存')


if __name__ == '__main__':
    main()