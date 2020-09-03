import imageio
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from jedi.api.refactoring import inline

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# %matplotlib inline
plt.show()
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import jieba.analyse

df = pd.read_excel('Java.xls')
# 将职位需求合并成一个长字符串
needs = []
for i in df['need']:
    needs.append(i)

set_need = str(needs)
# 用jieba分词，将岗位需求切割成词语
cut = jieba.lcut(set_need)
need_cut = ' '.join(cut)
# 设置停止词，删除跟岗位需求无关的词
stopwords = ['nan', '具备', '岗位职责', '任职', '相关', '公司', '进行', '工作', '根据', '提供', '作品', '以上学历', '优先', '计算', '经验', '学历', '上学',
             '熟练', '使用', '以上',
             '熟悉', '能力', '负责', '完成', '能够', '要求', '项目', '制作', '具有', '良好', '行业', '专业', '设计', '团队', '岗位', '优秀', '我们', '关注'
    , 'n1', 'n2', 'n3', 'n4', 'n5', 'xao', 'xa0', '产品', '软件', 'n6', '视频', '创意', '游戏', '需求', '视觉', '大专', '本科', '各种',
             '以及', 'n7', '了解', '职位', '结果'
             ]

# 读取背景图片
mk = imageio.imread('timg.jfif')
wordcloud = WordCloud(background_color='white',
                      # 设置字体为中文字体！！！
                      #SIMLI.TTF：设置字体为自己电脑的字体
                      font_path="/Library/Fonts/SIMLI.TTF",
                      # 设置清晰度
                      scale=15, mask=mk, stopwords=stopwords).generate(need_cut)
image_colors = ImageColorGenerator(mk)
# 将图片颜色应用到词云中
wc_color = wordcloud.recolor(color_func=image_colors)
#设置词云图片名
wc_color.to_file('ciyun.png')
plt.imshow(wc_color)