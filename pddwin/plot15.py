import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
sys.path.append("../") # 返回上层路径
from service import service

class Ui_MainWindow(QMainWindow):
    # 构造方法
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)  # 只显示最小化和关闭按钮
        self.setupUi(self) # 初始化窗体设置
    def setupUi(self, MainWindow):  
        #MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(307, 267)
        #self.retranslateUi(MainWindow)
        

        #fig = plt.figure()
        #fig.canvas.set_window_title('分析圖表')
        #fig.suptitle("Title for whole figure", fontsize=16) 

        fig, (ax1, ax2) = plt.subplots(2, 1)

         
        #fig.canvas.set_window_title('分析圖表')
        fig.canvas.manager.set_window_title('分析圖表')
        fig.suptitle("Title for whole figure", fontsize=16)   
        # make a little extra space between the subplots
        fig.subplots_adjust(hspace=0.5)

        dt = 0.01
        t = np.arange(0, 30, dt)

        # Fixing random state for reproducibility
        np.random.seed(19680801)


        nse1 = np.random.randn(len(t))                 # white noise 1
        nse2 = np.random.randn(len(t))                 # white noise 2
        r = np.exp(-t / 0.05)

        cnse1 = np.convolve(nse1, r, mode='same') * dt   # colored noise 1
        cnse2 = np.convolve(nse2, r, mode='same') * dt   # colored noise 2

        # two signals with a coherent part and a random part
        s1 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse1
        s2 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse2

        ax1.plot(t, s1, t, s2)
        ax1.set_xlim(0, 5)
        ax1.set_xlabel('time')
        ax1.set_ylabel('s1 and s2')
        ax1.grid(True)

        cxy, f = ax2.csd(s1, s2, 256, 1. / dt)
        ax2.set_ylabel('CSD (db)')

        #plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
        #plt.title('hello')
        
        plt.show()
    #def retranslateUi(self, MainWindow):
       # _translate = QtCore.QCoreApplication.translate
       # MainWindow.setWindowTitle(_translate("MainWindow", "班级设置"))
       