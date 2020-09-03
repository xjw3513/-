import requests
import time
import csv
from urllib.parse import urlencode
from urllib.parse import quote

# 使用面向对象的方式
class Spider:
    def __init__(self, page, cityId, search_keywords):
        '''初始化方法'''
        start = (page - 1) * 90  # 搜索结果每页90个，请求参数的start的值为0,90,180等。
        self.headers = {
            'referer': 'https://sou.zhaopin.com/?jl=' + str(cityId) + '&kw=' + quote(search_keywords) + '&kt=3',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)',
            'x-requested-with': 'XMLHttpRequest'  # ajax异步请求
            }
        self.params = {
             'start': start,
             'pageSize': '90',
             'cityId': cityId,
             'workExperience': -1,
             'education': -1,
             'companyType': -1,
             'employmentType': -1,
             'jobWelfareTag': -1,
             'kw': search_keywords,
             'kt': 3,
             '_v': '0.00882343',
             'x-zp-page-request-id': '',
             'x-zp-client-id': ''
            }
        self.url_search = 'https://fe-api.zhaopin.com/c/i/sou?' + urlencode(self.params)

    def get_one_page(self):
        '''请求网页'''
        try:
            response = requests.get(self.url_search, headers=self.headers)
            if response.status_code == 200:
                return response.json()
        except requests.ConnectionError:
            print('连接错误')
            return None

    def parse_one_page(self, response_json):
        '''解析网页'''
        if response_json:
            items = response_json.get('data').get('results')
            for item in items:
                crawlTime = str(time.ctime())  # 抓取时间
                businessArea = item.get('businessArea')  # 公司所在区域
                city = item.get('city').get('items')[0].get('name')  # 公司所在城市
                companyName = item.get('company').get('name')  # 公司名称
                companyNumber = item.get('company').get('number')  # 公司ID
                companySize = item.get('company').get('size').get('name')  # 公司人数规模
                eduLevel = item.get('eduLevel').get('name')  # 职位要求的学历
                jobName = item.get('jobName')  # 职位名称
                jobNumber = item.get('number')  # 职位ID
                jobType = item.get('jobType').get('items')[0].get('name')  # 职位类别
                positionURL = item.get('positionURL')  # 职位网址
                salary = item.get('salary')  # 薪资
                updateDate = item.get('updateDate')  # 职位更新时间
                workingExp = item.get('workingExp').get('name')  # 工作年限要求
                zhilian_results = [crawlTime, businessArea, city, companyName, companyNumber, companySize, eduLevel,
                                  jobName, jobNumber, jobType, positionURL, salary, updateDate, workingExp]
                print('zhilian_results:', zhilian_results)
                yield zhilian_results

    def save_to_csv(self, zhilian_results):
        '''保存数据到CSV文件'''
        headers = ['crawlTime', 'businessArea', 'city', 'companyName', 'companyNumber',
                   'companySize', 'eduLevel', 'jobName', 'jobNumber', 'jobType', 'positionURL',
                   'salary'  , 'updateDate', 'workingExp']
        with open('zhilian_results.csv', 'a', encoding='utf-8', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(zhilian_results)

    def run(self):
        '''启动函数'''
        response_json = self.get_one_page()
        zhilian_search_results = self.parse_one_page(response_json)
        self.save_to_csv(zhilian_search_results)

if __name__ == '__main__':
    # 抓取搜索相关性较高的前3页
    for i in range(1, 4):
        time.sleep(1)
        s = Spider(i, 763, '数据分析')
        s.run()