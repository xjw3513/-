import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

'''
各个省市招聘人数条形图
'''

df = pd.read_excel('Java.xls')
dfp = pd.read_excel('province.xlsx')
df_new = pd.merge(df,dfp.loc[:,['city','province']],how='left',on = 'city')  # 两个表进行连接，相当于关系运算中的连接
result=pd.value_counts(df_new['province'])  # 计数并排序
resultp=dict(result)  # 转换成字典
province = list(resultp.keys())  # 转换成列表
values = list(resultp.values())
valuesint=[]
for i in values:
    valuesint.append(int(i))
c3 = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))#设置主题，亮色
    .add_xaxis(province)#x轴为省份
    .add_yaxis("人数",valuesint)#y轴为人数
    .set_global_opts(title_opts=opts.TitleOpts(title="各个省市招聘人数"))
    .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            #插入平均值线
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average", name="平均值"),]),
            #插入最大值最小值点
            markpoint_opts=opts.MarkPointOpts(data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ])
    )
)
c3 .render('各个省市招聘人数条形图.html')
c3 .render_notebook()