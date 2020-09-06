import numpy as np
import pandas as pd
import os
import xlsxwriter


path="C:/Users/YYF/PycharmProjects/机器学习/venv/数据采集实验/数据采集课设/lagouclean2/"

pathdir=os.listdir(path)
df=pd.DataFrame(columns=['companyFullName', 'financeStage', 'skillLables', 'companySize', 'city',
       'salary', 'secondType', 'workYear', 'education', 'firstType',
       'positionLables', 'positionAdvantage', 'maxsalary', 'minsalary',
       'avesalary', 'name', 'belong'])
# path=path+"黑盒测试.xlsx"
# df=pd.read_excel(path)
# print(df.columns)
for path2 in pathdir:
    print(path2)
    path2=path+path2
    df1=pd.read_excel(path2)
    df=df.append(df1)
df.sort_values(["secondType"], inplace=True)