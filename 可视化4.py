import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

'''
融资情况饼图
'''

df = pd.read_excel('alljob.xlsx')
result=pd.value_counts(df['financeStage'])
resultst=dict(result)
st= list(resultst.keys())
stvalues = list(resultst.values())
stvaluesint=[]
for i in stvalues:
    stvaluesint.append(int(i))

from pyecharts import options as opts
from pyecharts.charts import Pie

pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add(
            "",
            [
                list(z)
                for z in zip(
                    st ,
                    stvaluesint ,
                )
            ],
            #设置圆心坐标
            center=["40%", "57%"],
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="融资情况"),
            legend_opts=opts.LegendOpts(
                type_="scroll",
                #'scroll'：可滚动翻页的图例。当图例数量较多时可以使用。
                pos_left="80%",
                orient="vertical",
                 # 图例列表的布局朝向。垂直/水平
                pos_top="15%"
                # 图例组件离容器上侧的距离。
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
pie.render('可视化/融资情况饼图.html')
pie.render_notebook()