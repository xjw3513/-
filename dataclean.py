import numpy as np
import pandas as pd
import os
import xlsxwriter


def salary(x):
    list1=str(x["salary"]).split("-")
    if(len(list1)==1):
        x["maxsalary"] = list1[0]
        x["minsalary"] = list1[0]
        x["avesalary"]= list1[0]
    else:
        x["maxsalary"]=list1[1]
        x["minsalary"]=list1[0]
#     print(list1[1].split("k")[0].split("K")[0])
#     print(list1[0].split("k")[0].split("K")[0])
        x["avesalary"]=(int(list1[0].replace("k","").replace("K",""))+int(list1[1].replace("k","").replace("K","")))/2.0
    return x

path="C:/Users/YYF/PycharmProjects/机器学习/venv/数据采集实验/数据采集课设/lagoujob/"
path1="C:/Users/YYF/PycharmProjects/机器学习/venv/数据采集实验/数据采集课设/lagoujobclean/"
pathdir=os.listdir(path)
# i=0
for path2 in pathdir:
    # i=i+1
    # if (i<200):
    #     continue
    df=pd.read_excel(path+path2)
    print(path2)
    df.drop(columns=["Unnamed: 0","businessZones",'latitude', 'longitude','district',"thirdType","firstType"],inplace=True)
# list1=df[[df.skillLables=="[]"][df.positionLables=="[]"]].index.tolist()
# df.loc[df.skillLables=="[]"]["positionLables"]=="[]"
#     list1=df[(df.skillLables=="[]")|(df.positionLables=="[]")].index.tolist()
    list1 = df[(df.positionLables == "[]")].index.tolist()
    df.drop(list1,inplace=True)
    df.reset_index(drop=True,inplace=True)
    df=df.apply(lambda x: salary(x),axis=1)
    path2=path1+path2
    df.to_excel(path2,encoding="UTF-8",engine="xlsxwriter",index=False)