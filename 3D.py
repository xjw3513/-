import json
import requests
import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType, ChartType

reponse = requests.get('https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5').json()
data = json.loads(reponse['data'])
province = []
confirm = []
for item in data['areaTree'][0]['children']:
    province.append(item['name'])
    confirm.append(item['total']['confirm'])
china_data = pd.DataFrame({"province": province, "confirm": confirm})

dicts_all = {'黑龙江': [127.9688, 45.368], '上海': [121.4648, 31.2891],
             '内蒙古': [110.3467, 41.4899], '吉林': [125.8154, 44.2584],
             '辽宁': [123.1238, 42.1216], '河北': [114.4995, 38.1006],
             '天津': [117.4219, 39.4189], '山西': [112.3352, 37.9413],
             '陕西': [109.1162, 34.2004], '甘肃': [103.5901, 36.3043],
             '宁夏': [106.3586, 38.1775], '青海': [101.4038, 36.8207],
             '新疆': [87.9236, 43.5883], '西藏': [91.11, 29.97],
             '四川': [103.9526, 30.7617], '重庆': [108.384366, 30.439702],
             '山东': [117.1582, 36.8701], '河南': [113.4668, 34.6234],
             '江苏': [118.8062, 31.9208], '安徽': [117.29, 32.0581],
             '湖北': [114.3896, 30.6628], '浙江': [119.5313, 29.8773],
             '福建': [119.4543, 25.9222], '江西': [116.0046, 28.6633],
             '湖南': [113.0823, 28.2568], '贵州': [106.6992, 26.7682],
             '广西': [108.479, 23.1152], '海南': [110.3893, 19.8516],
             '广东': [113.28064, 23.125177], '北京': [116.405289, 39.904987],
             '云南': [102.71225, 25.040609], '香港': [114.165460, 22.275340],
             '澳门': [113.549130, 22.198750], '台湾': [121.5200760, 25.0307240]}
for item in [list(z) for z in zip(china_data['province'], china_data['confirm'])]:
    dicts_all[item[0]].append(item[1])

(Map3D()
 .add_schema(
    itemstyle_opts=opts.ItemStyleOpts(
        color="rgb(5,101,123)",
        opacity=1,
        border_width=0.8,
        border_color="rgb(62,215,213)"),
    map3d_label=opts.Map3DLabelOpts(
        is_show=False,
        formatter=JsCode(
            "function(data){return data.name + " " + data.value[2];}")),
    emphasis_label_opts=opts.LabelOpts(
        is_show=False,
        color="#fff",
        font_size=10,
        background_color="rgba(0,23,11,0)"),
    light_opts=opts.Map3DLightOpts(
        main_color="#fff",
        main_intensity=1.2,
        main_shadow_quality="high",
        is_main_shadow=False,
        main_beta=10,
        ambient_intensity=0.3))
 .add(
    series_name="bar3D",
    data_pair=list(zip(list(dicts_all.keys()), list(dicts_all.values()))),
    type_=ChartType.BAR3D,
    bar_size=1,
    shading="lambert",
    label_opts=opts.LabelOpts(
        is_show=True,
        formatter=JsCode(
            "function(data){return data.name + ' ' + data.value[2];}")))
 .set_global_opts(title_opts=opts.TitleOpts(title="COVID-19全国疫情分布图"))).render("render.html")