# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from service import service
from baseinfo import student,classes,grade
from query import studentinfo
#from settings import classes,grade
from system import user
#from StudentMS  import plot15
import plot15
import plot8p3b
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap # 导入QPixmap类
class Ui_MainWindow(QMainWindow):
    # 构造方法
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)  # 只显示最小化和关闭按钮
        self.setupUi(self) # 初始化窗体设置
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 583)
        #MainWindow.setStyleSheet("#MainWindow { border-image: url(/images/wintech.jpg) 0 0 0 0 stretch stretch; }")
        #self.centralwidget = QtWidgets.QWidget(MainWindow)
        #self.centralwidget.setObjectName("centralwidget")`
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/appstu.ICO"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        #self.centralwidget.setStyleSheet("border-image: url(:/newPrefix/images/main.jpg);")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1, 1, 900, 540))
        #self.label.setText("用户名：")
        # 设置文本对齐方式
        self.label.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setPixmap(QPixmap('wintech.jpg')) # 为label设置图片


        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiongrade = QtWidgets.QAction(MainWindow)
        self.actiongrade.setObjectName("actiongrade")
        self.actionclass = QtWidgets.QAction(MainWindow)
        self.actionclass.setObjectName("actionclass")
        self.actionstudent = QtWidgets.QAction(MainWindow)
        self.actionstudent.setObjectName("actionstudent")
        self.actionstudentinfo = QtWidgets.QAction(MainWindow)
        self.actionstudentinfo.setObjectName("actionstudentinfo")
        self.actionuserinfo = QtWidgets.QAction(MainWindow)
        self.actionuserinfo.setObjectName("actionuserinfo")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionplot15 = QtWidgets.QAction(MainWindow)
        self.actionplot15.setObjectName("actionplot15")
        self.actionplot8m = QtWidgets.QAction(MainWindow)
        self.actionplot8m.setObjectName("actionplot8m")
        self.menu.addAction(self.actiongrade)
        self.menu.addAction(self.actionclass)
        self.menu_2.addAction(self.actionstudent)
        self.menu_3.addAction(self.actionstudentinfo)
        self.menu_4.addAction(self.actionuserinfo)
        self.menu_4.addAction(self.actionexit)
        self.menu_5.addAction(self.actionplot15)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
     
        self.btnAnaly = QtWidgets.QPushButton(MainWindow)
        self.btnAnaly.setGeometry(QtCore.QRect(60, 180, 191, 132))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.btnAnaly.setFont(font)
        self.btnAnaly.setObjectName("btnAnaly")

        self.btnRestore = QtWidgets.QPushButton(MainWindow)
        self.btnRestore.setGeometry(QtCore.QRect(260, 180, 191, 132))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.btnRestore.setFont(font)
        self.btnRestore.setObjectName("btnRestore")

        self.retranslateUi(MainWindow)
        self.actionexit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        datetime = QtCore.QDateTime.currentDateTime()  # 获取当前日期时间
        time = datetime.toString("yyyy-MM-dd HH:mm:ss")  # 对日期时间进行格式化
        # 状态栏中显示登录用户、登录时间，以及版权信息
        self.statusbar.showMessage("当前登录用户：" + service.userName + " | 登录时间：" + time + "  | 版权所有：成浩科電股份有限公司",0)
        # 为基础设置菜单中的QAction绑定triggered信号
        self.menu.triggered[QtWidgets.QAction].connect(self.openSet)
        # 为基本信息管理菜单中的QAction绑定triggered信号
        self.menu_2.triggered[QtWidgets.QAction].connect(self.openBase)
        # 为系统查询菜单中的QAction绑定triggered信号
        self.menu_3.triggered[QtWidgets.QAction].connect(self.openQuery)
        # 为系统管理菜单中的QAction绑定triggered信号
        self.menu_4.triggered[QtWidgets.QAction].connect(self.openSys)
         # 为系统管理菜单中的QAction绑定triggered信号
        self.menu_5.triggered[QtWidgets.QAction].connect(self.openPlot15)

        self.btnAnaly.clicked.connect(self.openPlot15) # 绑定添加按钮的单击信号
    # 基础设置菜单对应槽函数
    def openSet(self,m):
        if m.text()=="年级设置":
            self.m = grade.Ui_MainWindow()  # 创建年级设置窗体对象
            self.m.show()  # 显示窗体
        elif  m.text()=="班级设置":
            self.m = classes.Ui_MainWindow()  # 创建班级设置窗体对象
            self.m.show()  # 显示窗体
        #elif  m.text()=="班级设置":
        #    self.m = dbgrid15a.studentApp()  # 创建班级设置窗体对象
        #    self.m.show()  # 显示窗体    

    # 基本信息管理菜单对应槽函数
    def openBase(self,m):
        if  m.text()=="学生管理":
            self.m = student.Ui_MainWindow()  # 创建学生管理窗体对象
            self.m.show()  # 显示窗体

    # 系统查询菜单对应槽函数
    def openQuery(self,m):
        if  m.text()=="学生信息查询":
            self.m = studentinfo.Ui_MainWindow()  # 创建学生信息查询窗体对象
            self.m.show()  # 显示窗体

    # 系统管理菜单对应槽函数
    def openSys(self,m):
        if  m.text()=="用户维护":
            self.m = user.Ui_MainWindow()  # 创建用户维护窗体对象
            self.m.show()  # 显示窗体
    # 系统管理菜单对应槽函数
    def openPlot15(self,m):
        if  m.text()=="檢測":
           # self.m = plot15.Ui_MainWindow()  # 创建檢測
            self.m = plot8p3b.MainDialogImgBW()  # 创建檢測
           # self.m = plot8o.Ui_MainWindow()  # 创建檢測
            self.m.show()  # 显示窗体
    def openPlot15(self):
       #if  m.text()=="檢測":
           # self.m = plot15.Ui_MainWindow()  # 创建檢測
            self.m = plot8p3b.MainDialogImgBW()  # 创建檢測
           # self.m = plot8o.Ui_MainWindow()  # 创建檢測
            self.m.show()  # 显示窗体

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "局部放電監測管理系统"))
        self.menu.setTitle(_translate("MainWindow", "基础设置"))
        self.menu_2.setTitle(_translate("MainWindow", "基本信息管理"))
        self.menu_3.setTitle(_translate("MainWindow", "系统查询"))
        self.menu_4.setTitle(_translate("MainWindow", "系统管理"))
        self.menu_5.setTitle(_translate("MainWindow", "分析圖"))
        self.actiongrade.setText(_translate("MainWindow", "年级设置"))
        self.actionclass.setText(_translate("MainWindow", "班级设置"))
        #self.crud.setText(_translate("MainWindow", "CRUD"))
        self.actionstudent.setText(_translate("MainWindow", "学生管理"))
        self.actionstudentinfo.setText(_translate("MainWindow", "学生信息查询"))
        self.actionuserinfo.setText(_translate("MainWindow", "用户维护"))
        self.actionexit.setText(_translate("MainWindow", "退出"))
        self.actionplot15.setText(_translate("MainWindow", "檢測"))
        self.btnAnaly.setText(_translate("MainWindow", "檢測"))
        self.btnRestore.setText(_translate("MainWindow", "回調"))
import img_rc