# plot_web_api_realtime.py
"""
A live auto-updating plot of random numbers pulled from a web API
"""

import time
import datetime as dt
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import json
import pymysql # 导入操作MySQL数据库的模块
import mysql.connector

#url = "https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8"
url = "http://192.168.1.24/wintech/getchart1python.php"

# function to pull out a float from the requests response object
def pull_float(response):
    #jsonr = response.json()
   # strr = jsonr["data"][0]
   # fig, ax = plt.subplots()
    xs = []
    ys = []

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
                print(strr)
                if strr:
                  flt = round(float(strr), 2)
                 # return fltr
                  xs.append(dt.datetime.now().strftime('%H:%M:%S'))
                  ys.append(flt)
                  # Limit x and y lists to 10 items
                  xs = xs[-10:]
                  ys = ys[-10:]
                  # Draw x and y lists
                  ax.clear()
                  ax.plot(xs, ys)
                  # Format plot
                  ax.set_ylim([0,255])
                  plt.xticks(rotation=45, ha='right')
                  plt.subplots_adjust(bottom=0.20)
                  ax.set_title('Plot of random numbers from https://qrng.anu.edu.au')
                  ax.set_xlabel('Date Time (hour:minute:second)')
                  ax.set_ylabel('Random Number')

                else:
                  return None


# Create figure for plotting
fig, ax = plt.subplots()
xs = []
ys = []

def animate(i, xs:list, ys:list):
    # grab the data from thingspeak.com
    response = requests.get(url)
    flt = pull_float(response)
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(flt)
    # Limit x and y lists to 10 items
    xs = xs[-10:]
    ys = ys[-10:]
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)
    # Format plot
    ax.set_ylim([0,255])
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.20)
    ax.set_title('Plot of random numbers from https://qrng.anu.edu.au')
    ax.set_xlabel('Date Time (hour:minute:second)')
    ax.set_ylabel('Random Number')

# Set up plot to call animate() function every 1000 milliseconds
ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys), interval=10000)

plt.show()

