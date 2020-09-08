import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Boxplot
from pyecharts.globals import ChartType, SymbolType,ThemeType

'''
箱线图
'''

df = pd.read_excel('alljob.xlsx')
#处理薪酬数据
pattern = '\d+'
# 将字符串转化为列表,薪资取最低值加上区间值得25%，比较贴近现实
df['salarys'] = df['salary'].str.findall(pattern)  # 一维字符串列表变为二维数字字符串列表
avg_salary_list = []
i = 0
for k in df['salarys']:
    int_list = [int(n) for n in k]
    if len(int_list) == 2:
        avg_salary = int_list[0] + (int_list[1] - int_list[0]) / 4
        avg_salary_list.append(avg_salary)
    else :
        print(i)
        print(df['salary'][i])
    i += 1