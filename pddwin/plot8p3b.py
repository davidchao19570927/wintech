from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np
from testplot2pyqt5 import Ui_Dialog
#from testplot2pyqt6 import Ui_Dialog
import matplotlib.animation as animation
import matplotlib
matplotlib.use("Qt5Agg")  # 聲明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import time
from matplotlib.animation import FuncAnimation
import schedule
import tkinter as tk
from tkinter import messagebox
import threading as thd
from PyQt5.QtCore import QTimer

plt.rcParams['font.sans-serif']=['SimHei']   #防止中文标签乱码，还有通过导入字体文件的方法
plt.rcParams['axes.unicode_minus']=False

cnt = 1
#創建一個matplotlib圖形繪製類
class MyFigure(FigureCanvas):
    def __init__(self,width=5, height=4, dpi=100):
        #第一步：創建一個創建Figure
        #self.fig = Figure(figsize=(width, height), dpi=dpi)

        #第二步：在父類中激活Figure窗口
        super(MyFigure,self).__init__(self.fig) #此句必不可少，否則不能顯示圖形
        #第三步：創建一個子圖，用於繪製圖形用，111表示子圖編號，如matlab的subplot(1,1,1)
        #self.axes = self.fig.add_subplot(111)
        #self.axes = self.fig.subplots(2,2)

        
    #第四步：就是畫圖，【可以在此類中畫，也可以在其它類中畫】
       

class MainDialogImgBW(QDialog,Ui_Dialog):
    def __init__(self):
        super(MainDialogImgBW,self).__init__()
      
        self.setupUi(self)
        self.setWindowTitle("顯示matplotlib繪製圖形")
        self.setMinimumSize(0,0)

        #第五步：定義MyFigure類的一個實例
        #self.F = MyFigure(width=3, height=2, dpi=100)
        
        #self.F.plotsin()
       # self.plotcos()
        
        #第六步：在GUI的groupBox中創建一個佈局，用於添加MyFigure類的實例（即圖形）後其他部件。
        self.gridlayout = QGridLayout(self.groupBox)  # 繼承容器groupBox
       
       # self.gridlayout.addWidget(self.F,0,1)
        #fig = plt.figure(figsize=(7,7))
        
        '''
        fig = plt.figure(figsize=(7,7))
        xs = []
        ys = []
        '''
        self.igure = plt.figure()
        self.axes = self.igure.add_subplot(221)
        self.axes1 = self.igure.add_subplot(222)
        self.axes2 = self.igure.add_subplot(223)
        self.axes3 = self.igure.add_subplot(224)
        self.canvas = FigureCanvas(self.igure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.show()
        self.gridlayout.addWidget(self.toolbar)
        self.plotcos2()
        self.gridlayout.addWidget(self.canvas)
        self.mytimer = QTimer(self)
        self.mytimer.timeout.connect(self.plotcos3)
        self.mytimer.start(5000)
       # anim = FuncAnimation(fig,  self.plotcos3(), interval=10)
       # t = thd.Thread(target=self.t2)
       # t.start()
       # t.join()
        #self.run()
        #schedule.every(10).seconds.do(self.run)
        #schedule.every(10).seconds.do(self.plotcos2)
        #while True:
        # schedule.run_pending()  # run_pending：运行所有可以运行的任务

        '''  
        self.axes.clear()
        self.axes1.clear()
        self.axes2.clear()
        self.axes3.clear()
        #self.plotcos2()
        #self.gridlayout.addWidget(self.canvas)
        '''
       # self.plotcos2()
       # self.gridlayout.addWidget(self.canvas)
        #補充：另創建一個實例繪圖並顯示
        #self.plotother()
        #anim = FuncAnimation(fig, self.plotcos2(2), interval=10)
        #plt.show()
    '''    
    def run(self):
        print("I'm doing something...")    
    '''
    def plotcos3(self):
       
        global cnt
        self.axes.clear()
        self.axes1.clear()
        self.axes2.clear()
        self.axes3.clear()
        #root = tk.Tk()
        #root.withdraw()
        #messagebox.showinfo('my messagebox', 'hello world')
        self.plotcos2()
        self.gridlayout.addWidget(self.canvas)
        cnt = cnt + 1
     
    def plotcos2(self):
        self.axes.clear()
        self.axes1.clear()
        self.axes2.clear()
        self.axes3.clear()
        if cnt % 2 == 0 :
          xs = [1.5,1.7,1.8,1.9,1.92,1.93,1.95,1.979,1.984,1.987,1.9912,1.9919,2.9926]
          ys = [0.99,1.286,1.387,12.388,1.4111,1.486,1.5103,1.687,1.794,1.878,1.9177,1.985,-10.998]
        else :
          ys = [1.5,1.7,1.8,1.9,1.92,1.93,1.95,1.979,1.984,1.987,1.9912,1.9919,2.9926]
          xs = [0.99,1.286,1.387,12.388,1.4111,1.486,1.5103,1.687,1.794,1.878,1.9177,1.985,-10.998]
        t = np.arange(0.0, 360.0, 0.01)
        s = -10 + np.sin(0.00558 * np.pi * t)*200
       # self.axes.plot(t, s)
        self.axes.set(xlabel='時間(ns)', ylabel='振幅(mV)',
         title='波形') 
        #self.axes.title.set_size(4)
        self.axes.plot(xs,ys)

        #ys = [1.5,1.7,1.8,1.9,1.92,1.93,1.95,1.979,1.984,1.987,1.9912,1.9919,2.9926]
        #xs = [0.99,1.286,1.387,12.388,1.4111,1.486,1.5103,1.687,1.794,1.878,1.9177,1.985,-10.998]
        if cnt % 2 == 0 :
          ys = [1.5,1.7,1.8,1.9,1.92,1.93,1.95,1.979,1.984,1.987,1.9912,1.9919,2.9926]
          xs = [0.99,1.286,1.387,12.388,1.4111,1.486,1.5103,1.687,1.794,1.878,1.9177,1.985,-10.998]
        else :
          xs = [1.5,1.7,1.8,1.9,1.92,1.93,1.95,1.979,1.984,1.987,1.9912,1.9919,2.9926]
          ys = [0.99,1.286,1.387,12.388,1.4111,1.486,1.5103,1.687,1.794,1.878,1.9177,1.985,-10.998]
        t = np.arange(0.0, 360.0, 0.01)
        s = -10 + np.sin(0.00558 * np.pi * t)*200
       # self.axes1.plot(t, s)
        self.axes1.set(xlabel='頻率(MHz)',title='頻譜') 
        self.axes1.plot(xs,ys)

        xs = [1.5,1.7,1.8,1.9,1.92,1.93,1.95,1.979,1.984,1.987,1.9912,1.9919,2.9926]
        ys = [0.99,1.286,1.387,12.388,1.4111,1.486,1.5103,1.687,1.794,1.878,1.9177,1.985,-10.998]
        t = np.arange(0.0, 360.0, 0.01)
        s = -10 + np.sin(0.00558 * np.pi * t)*200
        self.axes2.plot(t, s)
        self.axes2.set(xlabel='相位(。)', ylabel='放電量(mV)',
         title='相位 VS 放電量') 
        self.axes2.scatter(xs,ys)
        

        xs = [1.5,1.7,1.8,1.9,1.92,1.93,1.95,1.979,1.984,1.987,1.9912,1.9919,2.9926]
        ys = [0.99,1.286,1.387,12.388,1.4111,1.486,1.5103,1.687,1.794,1.878,1.9177,1.985,-10.998]
        t = np.arange(0.0, 360.0, 0.01)
        s = -10 + np.sin(0.00558 * np.pi * t)*200
        #self.axes3.plot(t, s)
        self.axes3.set(xlabel='等效頻率(MHz)', ylabel='等效時間(ns)',
         title='TF map') 
        self.axes3.scatter(xs,ys)
        plt.tight_layout()
        #plt.grid()
        self.axes.grid()
        self.axes1.grid()
        self.axes2.grid()
        self.axes3.grid()
        self.canvas.draw()
              
    def plotcos(self):
       #t = np.arange(0.0, 5.0, 0.01)
       # s = np.cos(2 * np.pi * t)
       # self.F.axes.plot(t, s)
       # self.F.fig.suptitle("cos")
        xs = [1.5,1.7,1.8,1.9,1.92,1.93,1.95,1.979,1.984,1.987,1.9912,1.9919,2.9926]
        ys = [0.99,1.286,1.387,12.388,1.4111,1.486,1.5103,1.687,1.794,1.878,1.9177,1.985,-10.998]
        t = np.arange(0.0, 360.0, 0.01)
        s = -10 + np.sin(0.00558 * np.pi * t)*200
        #self.F.axes.plot(t, s)
        #self.F.axes.set(xlabel='相位(。)', ylabel='放電量(mV)',
        # title='相位 VS 放電量')

        self.F.axes[0, 0].plot(t, s)
        self.F.axes[0, 0].set(xlabel='相位(。)', ylabel='放電量(mV)',
         title='相位 VS 放電量') 
        self.F.axes[0, 0].scatter(xs,ys)
      
        self.F.axes[1, 1].plot(t, s)
        self.F.axes[1, 1].set(xlabel='相位(。)', ylabel='放電量(mV)',
         title='相位 VS 放電量') 
        self.F.axes[1, 1].scatter(xs,ys) 
        

    def plotother(self):
        F1 = MyFigure(width=5, height=4, dpi=100)
        F1.fig.suptitle("Figuer_4")
        F1.axes1 = F1.fig.add_subplot(221)
        x = np.arange(0, 50)
        y = np.random.rand(50)
        F1.axes1.hist(y, bins=50)
        F1.axes1.plot(x, y)
        F1.axes1.bar(x, y)
        F1.axes1.set_title("hist")
        F1.axes2 = F1.fig.add_subplot(222)
        ## 調用figure下面的add_subplot方法，類似於matplotlib.pyplot下面的subplot方法
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        F1.axes2.plot(x, y)
        F1.axes2.set_title("line")
        # 散點圖
        F1.axes3 = F1.fig.add_subplot(223)
        F1.axes3.scatter(np.random.rand(20), np.random.rand(20))
        F1.axes3.set_title("scatter")
        # 折線圖
        #F1.axes4 = F1.fig.add_subplot(224)
        #x = np.arange(0, 5, 0.1)
        #F1.axes4.plot(x, np.sin(x), x, np.cos(x))
        #F1.axes4.set_title("sincos")

        xs = [1.5,1.7,1.8,1.9,1.92,1.93,1.95,1.979,1.984,1.987,1.9912,1.9919,2.9926]
        ys = [0.99,1.286,1.387,12.388,1.4111,1.486,1.5103,1.687,1.794,1.878,1.9177,1.985,-10.998]
        F1.axes4 = F1.fig.add_subplot(224)
        t = np.arange(0.0, 360.0, 0.01)
        s = -10 + np.sin(0.00558 * np.pi * t)*200
        F1.axes4.plot(t, s)
        F1.axes4.set(xlabel='相位(。)', ylabel='放電量(mV)',
         title='相位 VS 放電量')
        F1.axes4.scatter(xs,ys)

        #self.gridlayout.addWidget(F1, 0, 2)

    def zoom(self):
        self.toolbar.zoom()
    
    # 每隔10秒钟执行
    def t2(self):
     while 1:
        self.plotcos3()
        time.sleep(20)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainDialogImgBW()
    main.show()
    #app.installEventFilter(main)
    sys.exit(app.exec_())
   