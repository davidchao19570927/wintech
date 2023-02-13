from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
#from testplot2pyqt5 import Ui_Dialog 
import random
import numpy as np 
import matplotlib

#from PyQt5.QtWidgets import *

matplotlib.use("Qt5Agg")  # 聲明使用QT5

plt.rcParams['font.sans-serif']=['SimHei']   #防止中文标签乱码，还有通过导入字体文件的方法
plt.rcParams['axes.unicode_minus']=False

class Window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)  # 只显示最小化和关闭按钮
        self.igure = plt.figure()
        self.axes = self.igure.add_subplot(111)
        # We want the axes cleared every time plot() is called
       # self.axes.hold(False)
        self.canvas = FigureCanvas(self.igure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.hide()
 
        # Just some button 
        self.button1 = QtWidgets.QPushButton('Plot')
        self.button1.clicked.connect(self.plot)
 
        self.button2 = QtWidgets.QPushButton('Zoom')
        self.button2.clicked.connect(self.zoom)
         
        self.button3 = QtWidgets.QPushButton('Pan')
        self.button3.clicked.connect(self.pan)
         
        self.button4 = QtWidgets.QPushButton('Home')
        self.button4.clicked.connect(self.home)
 

        # set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        
        btnlayout = QtWidgets.QHBoxLayout()
        btnlayout.addWidget(self.button1)
        btnlayout.addWidget(self.button2)
        btnlayout.addWidget(self.button3)
        btnlayout.addWidget(self.button4)
        qw = QtWidgets.QWidget(self)
        qw.setLayout(btnlayout)
        layout.addWidget(qw)
        
        self.setLayout(layout)
 
    def home(self):
        self.toolbar.home()
    def zoom(self):
        self.toolbar.zoom()
    def pan(self):
        self.toolbar.pan()
         
    def plot(self):
        ''' plot some random stuff '''
        #data = [random.random() for i in range(25)]
        #self.axes.plot(data, '*-')
        xs = [1.5,1.7,1.8,1.9,1.92,1.93,1.95,1.979,1.984,1.987,1.9912,1.9919,2.9926]
        ys = [0.99,1.286,1.387,12.388,1.4111,1.486,1.5103,1.687,1.794,1.878,1.9177,1.985,-10.998]
        t = np.arange(0.0, 360.0, 0.01)
        s = -10 + np.sin(0.00558 * np.pi * t)*200
        self.axes.plot(t, s)
        self.axes.set(xlabel='相位(。)', ylabel='放電量(mV)',
         title='相位 VS 放電量') 
        self.axes.scatter(xs,ys)
             
        self.canvas.draw()

        
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
 
    main = Window()
    main.setWindowTitle('Simple QTpy and MatplotLib example with Zoom/Pan')
    main.show()
 
    sys.exit(app.exec_())