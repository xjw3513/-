import xlrd
import pymssql
import datetime

# 连接本地sql server     地址     用户名  密码   数据库
conn = pymssql.connect("DESKTOP-HVMANSO", "sa", "123456", "zhaopin")
# 建立cursor
cursor = conn.cursor()
# excel文件
fname = "Java.xls"
#打开文件
bk = xlrd.open_workbook(fname)
#打开工作表
sh = bk.sheets()[0]
#获取行数
start_time=datetime.datetime.now()
sql3=''
# 遍历所有行
for i in range(1,sh.nrows):
  a = []
  sql = '('
  # 遍历所有列
  for j in range(sh.ncols):
    # 将excel每一列的值用，隔开
     sql += "'" + str(sh.cell(i, j).value) + "'" + ','
  # 组合成sql语句(value1,value2,value3,,)
  sql2 = sql.strip(",")
  sql3 += sql2.strip()+'),'
  # 1000行执行一次sql
  if i%1000==0:
    sql3 = sql3.rstrip(",")
    sql3 = sql3.replace("'","''")
    sql1 = "insert into Table_1(businessZones, companyFullName,companyLabelList,financeStage,skillLables,companySize,city,district,salary,secondType,workYear,education,firstType,thirdType,positionName,positionLables,positionAdvantage) values %s " % sql3
    # 执行sql语句
    cursor.execute(sql1)
    sql = ""
    sql3=""
sql3 = sql3.rstrip(",")
sql1 = "insert into Flow(businessZones, companyFullName,companyLabelList,financeStage,skillLables,companySize,city,district,salary,secondType,workYear,education,firstType,thirdType,positionName,positionLables,positionAdvantage) values %s " % sql3
cursor.execute(sql1)
# commit提交变更
conn.commit()
# 结束时间
end_time = datetime.datetime.now()
speed = end_time - start_time
# 打印花费时间
print(speed)