import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Boxplot
from pyecharts.globals import ChartType, SymbolType,ThemeType
df = pd.read_excel('拉勾750条家教.xlsx')
pattern = '\d+'

df['salarys'] = df['salary'].str.findall(pattern)
avg_salary_list = []
for k in df['salarys']:
    int_list = [int(n) for n in k]
    avg_salary = int_list[0] + (int_list[1] - int_list[0]) / 4
    avg_salary_list.append(avg_salary)
df['月薪'] = avg_salary_list
#处理工作年限数据
df['workYears']=df['workYear'].replace({'应届毕业生':'1年以下','不限':'1年以下'})
groupby_workyear=df.groupby(['workYears'])['月薪']
count_groupby_workyear=groupby_workyear.count()
count_groupby_workyear=count_groupby_workyear.reindex(['1年以下','1-3年','3-5年','5-10年'])
a = count_groupby_workyear.index
dff=[]
for b in a:
    c=groupby_workyear.get_group(b).values
    dff.append(c)
c = Boxplot(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
c.add_xaxis(['1年以下','1-3年','3-5年','5-10年']).add_yaxis("薪酬k/月", c.prepare_data(dff)
    ).set_global_opts(title_opts=opts.TitleOpts(title="不同工作经验的薪酬分布"))
c.render("不同工作经验的薪酬分布.html")