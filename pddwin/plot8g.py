import matplotlib.pyplot as plt
import numpy as np
import time
import datetime as dt
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import json
import pymysql # 导入操作MySQL数据库的模块
import mysql.connector

#plt.style.use('_mpl-gallery')

# make the data
def animate(i, xs:list, ys:list):
  np.random.seed(3)
  x = 4 + np.random.normal(0, 2, 24)
  y = 4 + np.random.normal(0, 2, len(x))
# size and color:
  sizes = np.random.uniform(15, 80, len(x))
  colors = np.random.uniform(15, 80, len(x))

# plot
  #fig, ax = plt.subplots()
  ax.clear() 
  ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

  ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
         ylim=(0, 8), yticks=np.arange(1, 8))

fig, ax = plt.subplots()
xs = []
ys = []
ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys), interval=10000)
plt.show()