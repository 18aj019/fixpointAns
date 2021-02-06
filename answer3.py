#!/usr/bin/env python
# coding: utf-8


import pandas as pd #df作成 csvList作成
import datetime
#dataframe作成,成形
#f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
data = pd.read_csv("test.csv").values.tolist()
#print(data)
df = pd.read_csv("test.csv",sep=",",header=None)
df.columns = ["date","ipv4","ping"]
date_list = []
ping_list = []
print("Nの入力")
n = int(input())
print("m,tの入力")
m = int(input())
t = float(input())
ipf = 0
#print(df)




#Ipv4Ad抽出
is_dup = df.duplicated(subset=["ipv4"])#IPad抽出
    #print(df[~is_dup].ipv4)
ip_list = []
for i in df[~is_dup].ipv4:
    ip_list.append(i)
#print(ip_list)




for i in range(len(ip_list)):
    ipf = 0
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
    ipf = func3(ip,date_list,ping_list,n,ipf)
    print()
    func4(ip,date_list,ping_list,m,t,ipf)





def func3(ip,date_list,ping_list,n,ipf):
    #故障状態算出プログラム
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
            if ipf == 0 :
                print("IP: %s"%(ip))
                ipf = 1
            time2 = pd.to_datetime(date_list[k],format='%Y%m%d%H%M%S')
            time3 =  time2 - time1
            print("%sより%sまで故障発生" %(time1,time2))
            print("故障期間: %s" %(time3))
        else :
            f = 0
            continue
    return ipf




def func4(ip,date_list,ping_list,m,t,ipf):
     #過負荷状態算出プログラム
    for i in range(len(ping_list)):
        ktime = 0.0
        time = 0
        j = i - m 
        length =  m + 1
        if j < 0:
            j = 0
        time1 = pd.to_datetime(date_list[j],format='%Y%m%d%H%M%S')
        time2 = pd.to_datetime(date_list[i],format='%Y%m%d%H%M%S')
        
        for j in range(j,i + 1,1):
            #print(i)
            #print(ping_list[j])
            if ping_list[j] == '-':
                length = length - 1
            else :
                ktime = ktime + float(ping_list[j])
                #print(ktime)
                #print("ping_list %s" %(ping_list[j]))
        try:
            ktime = ktime / length
        except ZeroDivisionError:
            ktime = 0
        #print(ktime)
        if ktime >= t:
            if ipf == 0:
                ipf = 1
                print("IP: %s"%(ip))
            print("%sから%sまで過負荷状態" %(time1,time2))
            print("過負荷期間: %s" %(time2-time1))
            
            
        







