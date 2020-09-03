import os
import pandas as  pd
path="C:/Users/YYF/PycharmProjects/机器学习/venv/数据采集实验/数据采集课设/新建文本文档.txt"
zhiwei=[]
with open(path,'r',encoding="UTF-8") as file_to_read:
    while True:
        lines=file_to_read.readline()
        if not lines:
            break
        lines=str(lines.split(" ")[0].strip("\n"))
        if (len(lines) !=0):
            zhiwei.append(lines)
# print(zhiwei)
print(len(set(zhiwei)))

print(zhiwei.index("Flash"))


print(zhiwei)


list1=os.listdir("C:/Users/YYF/PycharmProjects/机器学习/venv/数据采集实验/数据采集课设/lagoujob/")
for i in range(len(list1)) :
    list1[i]=list1[i].replace("_","/").split(".")[0]

print(len(list1))
l= [list for list in  zhiwei if list not in list1]
print(l)
# df=pd.DataFrame({"zhiwei": zhiwei})
# print(df)
# df.to_excel("./lagoujob/zhiwei.xlsx")
