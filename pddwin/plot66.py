import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys  # 导入sys模块
import main
from service import service
from PyQt5.QtGui import QPixmap # 导入QPixmap类

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
      x=0
      for i in range(100):
        x=x+0.04
        y = np.sin(x)
        plt.scatter(x, y)
        plt.title("Real Time plot")
        plt.xlabel("x")
        plt.ylabel("sinx")
        plt.pause(0.05)
        if x >= 3 :
        # ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
         plt.clf()
         ui.setupUi(self)
    #plt.show()
    '''
    def setupUi2():
      x=0
      for i in range(100):
        x=x+0.04
        y = np.sin(x)
        plt.scatter(x, y)
        plt.title("Real Time plot")
        plt.xlabel("x")
        plt.ylabel("sinx")
        plt.pause(0.05)
    #plt.show()
    '''
# 主方法
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    #ui.setupUi(MainWindow)
   #MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程