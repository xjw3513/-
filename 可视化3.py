import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo,Map
from pyecharts.globals import ChartType, SymbolType,ThemeType

'''
各个省市招聘人数地图
'''

df = pd.read_excel('alljob.xlsx')
result=pd.value_counts(df['city'])
# print(result)

dfp = pd.read_excel('province.xlsx')
df_new = pd.merge(df,dfp.loc[:,['city','province']],how='left',on = 'city')
result=pd.value_counts(df_new['province'])
resultp=dict(result)
province = list(resultp.keys())
values = list(resultp.values())
valuesint=[]
for i in values:

    valuesint.append(int(i))
#第一种地图
c1 = (
    Geo()
    .add_schema(maptype="china")
    .add("各个省市招聘人数", #标题
         [list(z) for z in zip(province, valuesint)],#省份数据列表，地名不能带“省”字
         type_=ChartType.EFFECT_SCATTER)#选择显示类型
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))#不显示标签
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=30000,is_piecewise = False),
        title_opts=opts.TitleOpts(title="全国各省数据分布"),
    )
)
c1.render('可视化/各个省市招聘人数点地图one.html')#保存为HTML
c1.render_notebook()#在notebook上显示


#第二种地图
c2 = (
    Map(init_opts=opts.InitOpts(bg_color="#fff", theme=ThemeType.ROMANTIC))#设置主题
    .add("各个省市招聘人数", [list(z) for z in zip(province, valuesint)], "china",is_map_symbol_show=False)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="各个省市招聘人数"),
    visualmap_opts=opts.VisualMapOpts(max_=30000,is_piecewise = True,#图例分段显示
                                      pieces=[
                {"min": 30001, "label": '>30000人', "color": "#e55039"},  # 不指定 max，表示 max 为无限大（Infinity），指定颜色。
                {"min": 15001, "max": 30000, "label": '15001-30000人', "color": "#FF4500"},
                {"min": 5001, "max": 15000, "label": '5001-15000人', "color": "#FF7F50"},
                {"min": 2001, "max": 5000, "label": '2001-5000人', "color": "#FFA500"},
                {"min": 501, "max": 2000, "label": '501-2000人', "color": "#FFDEAD"},
                {"min": 1, "max": 500, "label": '1-500人', "color": "#ffffcc"},
            ]
                                     ))
)
c2.render('可视化/各个省市招聘人数块地图tow.html')
c2.render_notebook()