#!/usr/bin/env python
# coding: utf-8

import pandas as pd #df作成 csvList作成
import csv 
import datetime
csv_file = open("./test.csv", "r",encoding="utf_8")
#f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
data = pd.read_csv("test.csv").values.tolist()
#print(data)
df = pd.read_csv("test.csv",sep=",",header=None)
df.columns = ["date","ipv4","ping"]
date_list = []
ping_list = []
#print(df)






#Ipv4Ad抽出
is_dup = df.duplicated(subset=["ipv4"])#IPad抽出
    #print(df[~is_dup].ipv4)
ip_list = []
for i in df[~is_dup].ipv4:
    ip_list.append(i)
#print(ip_list)





for i in range(len(ip_list)):
    ip = ip_list[i]
    date_list = []
    ping_list = []
    print (ip)
    length = len(data)
    for index,column in df.iterrows() :
        #print(list)
        if ip == column["ipv4"]:
            date_list.append(column["date"])
            ping_list.append(column["ping"])
    print(date_list)   
    print(ping_list)
    func3(ip,date_list,ping_list)
        
            
def func3(ip,date_list,ping_list):
    f = 0
    time1 = datetime.datetime.now()
    time2 = datetime.datetime.now()
    time3 = datetime.datetime.now()
    
    for k in range(len(ping_list)):
        if ping_list[k] == '-' and f == 0:
            f = 1
            time1 = pd.to_datetime(date_list[k],format='%Y%m%d%H%M%S')
            #print(time1)
        elif ping_list[k] == '-' and f == 1:
            continue
        elif ping_list[k] != '-' and f == 1:
            f = 0 
            time2 = pd.to_datetime(date_list[k],format='%Y%m%d%H%M%S')
            time3 =  time2 - time1
            print("IP:%s は%sより%sまで故障発生\n" %(ip,time1,time2))
            print("IP:%s Time:%s\n" %(ip,time3))
        else :
            continue

    






# In[ ]:




