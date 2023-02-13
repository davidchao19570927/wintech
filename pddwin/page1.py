import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class _MainWindow(QWidget):
    def __init__(self):
        super(_MainWindow, self).__init__()
        self.resize(600, 400)
        self.setWindowTitle('RPC测试')
        self.initUi()

    def initUi(self):
        self.left_widget = QListWidget(self)  # 左侧选项列表
        # self.left_widget.move(100,400)

        self.left_widget.insertItem(0,"RPC自动化测试")
        self.left_widget.insertItem(1,"RPC接口压测")
        # self.left_widget.setLineWidth(500)
        self.stack1 = QWidget()
        # self.stack1.move(300,300)
        self.stack2 = QWidget()
        # self.stack3 = QWidget()
        self.stack1UI()
        self.stack2UI()
        # self.stack3UI()
        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        # self.Stack.addWidget(self.stack3)

        # 创建一个QSplitter,用来控制布局管理器大小
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.left_widget)  # 将左侧的布局 添加至QSplitter
        splitter.addWidget(self.Stack)  # 将右侧的布局 添加至QSplitter
        splitter.setSizes([100, 500])  # 设置左右布局占比

        # 创建一个布局管理器
        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter)
        self.setLayout(hbox)
        self.left_widget.currentRowChanged.connect(self.display)

    def stack1UI(self):
        layout = QFormLayout()
        font = QFont()
        font.setPointSize(11)

        self.topLeft1 = QFrame()
        self.topLeft1.setMinimumSize(450, 350)

        self.Lable_modify = QLabel("点击“打开”修改配置文件，点击“执行”开始接口测试", self.topLeft1)
        self.Lable_modify.setGeometry(QRect(30, 20, 380, 30))
        self.Lable_modify.setFont(font)

        self.PushButton_modify = QPushButton("打开", self.topLeft1)
        self.PushButton_modify.setGeometry(QRect(60, 60, 50, 30))
        self.PushButton_modify.setFont(font)

        self.PushButton_Interface_run = QPushButton("执行", self.topLeft1)
        self.PushButton_Interface_run.setGeometry(QRect(240, 60, 50, 30))
        self.PushButton_Interface_run.setFont(font)

        self.textEdit_Interface = QTextEdit(self.topLeft1)
        self.textEdit_Interface.setGeometry(QRect(25, 100, 400, 260))

        scroll = QScrollArea()    # 滚动
        scroll.setWidget(self.topLeft1)
        # 设置窗体全局布局以及子布局的添加
        layout.addWidget(scroll)
        self.stack1.setLayout(layout)

    def stack2UI(self):
        layout = QFormLayout()
        font = QFont()
        font.setPointSize(11)

        self.topLeft2 = QFrame()
        self.topLeft2.setMinimumSize(450, 350)

        self.Lable_service = QLabel("service:", self.topLeft2)
        self.Lable_service.setGeometry(QRect(30, 20, 80, 30))
        self.Lable_service.setFont(font)

        self.LineEdit_service = QLineEdit(self.topLeft2)
        self.LineEdit_service.setGeometry(QRect(100, 20, 100, 30))

        self.Lable_method = QLabel("method:", self.topLeft2)
        self.Lable_method.setGeometry(QRect(250, 20, 80, 30))
        self.Lable_method.setFont(font)

        self.LineEdit_method = QLineEdit(self.topLeft2)
        self.LineEdit_method.setGeometry(QRect(320, 20, 100, 30))

        self.Lable_params = QLabel("params:", self.topLeft2)
        self.Lable_params.setGeometry(QRect(30, 60, 80, 30))
        self.Lable_params.setFont(font)

        self.LineEdit_params = QLineEdit(self.topLeft2)
        self.LineEdit_params.setGeometry(QRect(100, 60, 320, 30))

        self.Lable_res_params = QLabel("返回校验:", self.topLeft2)
        self.Lable_res_params.setGeometry(QRect(30, 100, 80, 30))
        self.Lable_res_params.setFont(font)

        self.LineEdit_res_params = QLineEdit(self.topLeft2)
        self.LineEdit_res_params.setGeometry(QRect(100, 100, 320, 30))

        self.Lable_time_interval = QLabel("循环间隔:", self.topLeft2)
        self.Lable_time_interval.setGeometry(QRect(30, 140, 80, 30))
        self.Lable_time_interval.setFont(font)

        self.LineEdit_time_interval = QLineEdit(self.topLeft2)
        self.LineEdit_time_interval.setText("3")
        self.LineEdit_time_interval.setGeometry(QRect(100, 140, 100, 30))

        self.Lable_times = QLabel("循环次数:", self.topLeft2)
        self.Lable_times.setGeometry(QRect(250, 140, 80, 30))
        self.Lable_times.setFont(font)

        self.LineEdit_times = QLineEdit(self.topLeft2)
        self.LineEdit_times.setText("1000")
        self.LineEdit_times.setGeometry(QRect(320, 140, 100, 30))

        self.PushButton_Pressure_run = QPushButton("执行", self.topLeft2)
        self.PushButton_Pressure_run.setGeometry(QRect(100, 180, 50, 30))
        self.PushButton_Pressure_run.setFont(font)

        self.PushButton_Pressure_stop = QPushButton("停止", self.topLeft2)
        self.PushButton_Pressure_stop.setGeometry(QRect(320, 180, 50, 30))
        self.PushButton_Pressure_stop.setFont(font)

        self.textEdit_Pressure = QTextEdit(self.topLeft2)
        self.textEdit_Pressure.setGeometry(QRect(25, 220, 400, 120))

        scroll = QScrollArea()  # 滚动
        scroll.setWidget(self.topLeft2)
        # 设置窗体全局布局以及子布局的添加
        layout.addWidget(scroll)
        self.stack2.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = _MainWindow()
    MyWindow.show()
    sys.exit(app.exec_())
