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
for k in df['salarys']:
    int_list = [int(n) for n in k]
    avg_salary = int_list[0] + (int_list[1] - int_list[0]) / 4
    avg_salary_list.append(avg_salary)
df['月薪'] = avg_salary_list
#处理工作年限数据
# df['workYears']=df['workYear'].replace({'应届毕业生':'1年以下'})
groupby_workyear=df.groupby(['workYear'])['月薪']
count_groupby_workyear=groupby_workyear.count()
count_groupby_workyear=count_groupby_workyear.reindex(['应届毕业生','1年以下','1-3年','3-5年','5-10年','10年以上','不限'])
a = count_groupby_workyear.index
dff=[]
for b in a:
    c=groupby_workyear.get_group(b).values
    dff.append(c)
c = Boxplot(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
c.add_xaxis(['应届毕业生','1年以下','1-3年','3-5年','5-10年','10年以上','不限']).add_yaxis("薪酬k/月", c.prepare_data(dff)).set_global_opts(title_opts=opts.TitleOpts(title="不同工作经验的薪酬分布"))
c.render("可视化/不同工作经验的薪酬分布.html")