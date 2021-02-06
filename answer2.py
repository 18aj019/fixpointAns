#!/usr/bin/env python
# coding: utf-8

# In[7]:


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
print("Nの入力")
n = int(input())
#print(df)


# In[8]:


#Ipv4Ad抽出
is_dup = df.duplicated(subset=["ipv4"])#IPad抽出
    #print(df[~is_dup].ipv4)
ip_list = []
for i in df[~is_dup].ipv4:
    ip_list.append(i)
#print(ip_list)


# In[13]:


for i in range(len(ip_list)):
    ip = ip_list[i]
    date_list = []
    ping_list = []
    #print (ip)
    length = len(data)
    for index,column in df.iterrows() :
        #print(list)
        if ip == column["ipv4"]:
            date_list.append(column["date"])
            ping_list.append(column["ping"])
    #print(date_list)   
    #print(ping_list)
    func3(ip,date_list,ping_list,n)


# In[14]:


def func3(ip,date_list,ping_list,n):
    f = 0
    time1 = datetime.datetime.now()
    time2 = datetime.datetime.now()
    time3 = datetime.datetime.now()
    
    for k in range(len(ping_list)):
        if ping_list[k] == '-' and f == 0:
            f = 1
            time1 = pd.to_datetime(date_list[k],format='%Y%m%d%H%M%S')
            #print(time1)
        elif ping_list[k] == '-' and f > 0 :
            f = f + 1
        elif ping_list[k] != '-' and f >= n:
            f = 0 
            time2 = pd.to_datetime(date_list[k],format='%Y%m%d%H%M%S')
            time3 =  time2 - time1
            print("IP:%s %sより%sまで故障発生" %(ip,time1,time2))
            print("故障期間 %s" %(time3))
        else :
            f = 0
            continue


# In[37]:





# In[ ]:




