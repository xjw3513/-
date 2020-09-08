import pandas as pd
import numpy as np
import glob,os
path1 = "data"
file=glob.glob(os.path.join(path1,"*.xlsx"))
#  *.xlsx  查找文件名为.xlsx的文件 *前面可以加文字立即为通配符
#获取文件夹里面xlsx文件的名称及路径
# print(file)
#查看获取的路径和文件名

list1=[ ]
#创建一个新的空列表 以存放读取的数据
for value in file:
    list1.append(pd.read_excel(value,index_col=None))
#循环读取xlsx文件并添加到list1列表中 pd.read_excle(可以自定义读取的方式 )
df=pd.concat(list1,axis=0)
#将list1 进行纵向合并  且转换为DataFrame类型
df.to_excel("alljob.xlsx")
#输出合并和的excel文件