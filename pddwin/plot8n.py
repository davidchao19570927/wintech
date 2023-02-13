import matplotlib.pyplot as plt
import time
import datetime as dt
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import json
import pymysql # 导入操作MySQL数据库的模块
import mysql.connector
import numpy as np
import tkinter as tk
from tkinter import ttk

app = tk.Tk() 
app.geometry('200x100')

labelTop = tk.Label(app,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"],
                            state="readonly")

comboExample.grid(column=0, row=1)
comboExample.current(0)

print(comboExample.current(), comboExample.get())

app.mainloop() 

plt.rcParams['font.sans-serif']=['SimHei']   #防止中文标签乱码，还有通过导入字体文件的方法
plt.rcParams['axes.unicode_minus']=False
#plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

xs = []
ys = []
i = 0
db_settings = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "ab145694",
            "db": "wintech",
            "charset": "utf8"
        }
        # con = pymysql.connect('localhost', 'root', 'ab145694', 'wintech')
con = pymysql.connect(**db_settings)
with con.cursor() as cursor:
           # 資料庫設定
            cursor.execute("SELECT * FROM his4 ")
            rows = cursor.fetchall()
            for row in rows:
                # print row["Id"], row["Name"]
                # SERVER_HOST = "192.168.1.106"
                # ipaddr = str(row["ipaddr"])
                strr = row[2]
                #strr2 = row[3]
                #print(strr)
                if strr:
                   strr = round(float(strr), 3)
                   if (strr > 200 or strr < -200) :
                    strr = '0'
                   xs.append(strr)
            cursor.execute("SELECT * FROM his5 ")
            rows = cursor.fetchall()
            for row in rows:
                # print row["Id"], row["Name"]
                # SERVER_HOST = "192.168.1.106"
                # ipaddr = str(row["ipaddr"])
                #strr = row[2]
                strr = row[2]
                #print(strr)
                if strr:
                   strr = round(float(strr), 3)
                   if (strr > 200 or strr < -200) :
                    strr = '0'
                   ys.append(strr)       
                   #ys.append(strr2)
                   #x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
                   #y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#畫點
#xs = [1.5,1.7,1.8,1.9,1.92,1.93,1.95,1.979,1.984,1.987,1.9912,1.9919,2.9926]
#ys = [0.99,1.286,1.387,12.388,1.4111,1.486,1.5103,1.687,1.794,1.878,1.9177,1.985,-10.998]
#plt.scatter(xs, ys)

#fig, ax = plt.subplots()
#fig = plt.figure(figsize=(3, 6))
fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.scatter(xs, ys)
# s = 6 + np.sin(0.00558 * np.pi * t)*6
ax1 = fig.add_subplot(111)
#t = np.arange(0.0, 6.0, 0.01)
#s = 2 + np.sin(0.35 * np.pi * t)*2 其中值 2 值是變動的, 去 Y 陣列中最大值(12.388)乘2取整數=24和最小值(-10.998)除2取整數=-5
#max =int(max(ys) * 2)
#min = int(min(ys) / 2)
t = np.arange(0.0, 360.0, 0.01)
#s = -5 + np.sin(0.00558 * np.pi * t)*24

#s = min + np.sin(0.00558 * np.pi * t)*max
s = -10 + np.sin(0.00558 * np.pi * t)*200
ax1.plot(t, s)
ax1.set(xlabel='相位(。)', ylabel='放電量(mV)',
       title='相位 VS 放電量')
#plt.grid()
ax1.scatter(xs,ys)
#fig, ax2 = plt.subplots()
#ax2.scatter(xs, ys)
#fig.savefig("test.png")
#畫折線
#x = np.array(xs)
#y = np.array(ys)
#plt.plot(x, y)

#畫這線加 title
#fig = plt.figure()
# 畫圖（點圖）
#fig, ax = plt.subplots()
#ax = fig.add_subplot(3,2,1)

#ax = fig.subplots()
#ax.plot(xs, ys)
#ax.set_xlabel('x')
#ax.set_ylabel(' y')

plt.show()

