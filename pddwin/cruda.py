from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from dba import  *
db = DataBase("data.db")
 
 
class Ui_win(object):
    def setupUi(self, win):
        win.setObjectName("win")
        win.resize(833, 570)
        win.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.Fname = QtWidgets.QLabel(win)
        self.Fname.setGeometry(QtCore.QRect(40, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setWeight(75)
        self.Fname.setFont(font)
        self.Fname.setAutoFillBackground(True)
        self.Fname.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Fname.setObjectName("Fname")
        self.Sname = QtWidgets.QLabel(win)
        self.Sname.setGeometry(QtCore.QRect(40, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setWeight(75)
        self.Sname.setFont(font)
        self.Sname.setAutoFillBackground(True)
        self.Sname.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Sname.setObjectName("Sname")
        self.number = QtWidgets.QLabel(win)
        self.number.setGeometry(QtCore.QRect(40, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setWeight(75)
        self.number.setFont(font)
        self.number.setAutoFillBackground(True)
        self.number.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.number.setObjectName("number")
        self.email = QtWidgets.QLabel(win)
        self.email.setGeometry(QtCore.QRect(40, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setAutoFillBackground(True)
        self.email.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.email.setObjectName("email")
        self.major = QtWidgets.QLabel(win)
        self.major.setGeometry(QtCore.QRect(450, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
 
        font.setWeight(75)
        self.major.setFont(font)
        self.major.setAutoFillBackground(True)
        self.major.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.major.setObjectName("major")
        self.gpa = QtWidgets.QLabel(win)
        self.gpa.setGeometry(QtCore.QRect(450, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
 
        font.setWeight(75)
        self.gpa.setFont(font)
        self.gpa.setAutoFillBackground(True)
        self.gpa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gpa.setObjectName("gpa")
        self.year = QtWidgets.QLabel(win)
        self.year.setGeometry(QtCore.QRect(450, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
 
        font.setWeight(75)
        self.year.setFont(font)
        self.year.setAutoFillBackground(True)
        self.year.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.year.setObjectName("year")
        self.gender = QtWidgets.QLabel(win)
        self.gender.setGeometry(QtCore.QRect(450, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
 
        font.setWeight(75)
        self.gender.setFont(font)
        self.gender.setAutoFillBackground(True)
        self.gender.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gender.setObjectName("gender")
        self.FnameLabel = QtWidgets.QLineEdit(win)
        self.FnameLabel.setGeometry(QtCore.QRect(180, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.FnameLabel.setFont(font)
        self.FnameLabel.setObjectName("FnameLabel")
        self.SnameLabel = QtWidgets.QLineEdit(win)
        self.SnameLabel.setGeometry(QtCore.QRect(180, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.SnameLabel.setFont(font)
        self.SnameLabel.setObjectName("SnameLabel")
        self.email_label = QtWidgets.QLineEdit(win)
        self.email_label.setGeometry(QtCore.QRect(180, 130, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.numberLabel = QtWidgets.QLineEdit(win)
        self.numberLabel.setGeometry(QtCore.QRect(180, 180, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.numberLabel.setFont(font)
        self.numberLabel.setObjectName("numberLabel")
        self.majorLabel = QtWidgets.QLineEdit(win)
        self.majorLabel.setGeometry(QtCore.QRect(580, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.majorLabel.setFont(font)
        self.majorLabel.setObjectName("majorLabel")
        self.gpaLabel = QtWidgets.QLineEdit(win)
        self.gpaLabel.setGeometry(QtCore.QRect(580, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.gpaLabel.setFont(font)
        self.gpaLabel.setObjectName("gpaLabel")
        self.yearLabel = QtWidgets.QLineEdit(win)
        self.yearLabel.setGeometry(QtCore.QRect(580, 130, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.yearLabel.setFont(font)
        self.yearLabel.setObjectName("yearLabel")
        self.Male_btn = QtWidgets.QRadioButton(win)
        self.Male_btn.setGeometry(QtCore.QRect(600, 180, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
 
        font.setWeight(75)
        self.Male_btn.setFont(font)
        self.Male_btn.setObjectName("Male_btn")
        self.female_btn = QtWidgets.QRadioButton(win)
        self.female_btn.setGeometry(QtCore.QRect(690, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
 
        font.setWeight(75)
        self.female_btn.setFont(font)
        self.female_btn.setObjectName("female_btn")
        self.remove_btn = QtWidgets.QPushButton(win)
        self.remove_btn.setGeometry(QtCore.QRect(590, 240, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(10)
 
        font.setWeight(75)
        self.remove_btn.setFont(font)
        self.remove_btn.setObjectName("remove_btn")
        self.submit_btn = QtWidgets.QPushButton(win)
        self.submit_btn.setGeometry(QtCore.QRect(160, 240, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(10)
 
        font.setWeight(75)
        self.submit_btn.setFont(font)
        self.submit_btn.setObjectName("submit_btn")
        self.clear_btn = QtWidgets.QPushButton(win)
        self.clear_btn.setGeometry(QtCore.QRect(450, 240, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(10)
 
        font.setWeight(75)
        self.clear_btn.setFont(font)
        self.clear_btn.setObjectName("clear_btn")
        self.update_btn = QtWidgets.QPushButton(win)
        self.update_btn.setGeometry(QtCore.QRect(300, 240, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(10)
 
        font.setWeight(75)
        self.update_btn.setFont(font)
        self.update_btn.setObjectName("update_btn")
        self.listWidget = QtWidgets.QListWidget(win)
        self.listWidget.setGeometry(QtCore.QRect(35, 300, 761, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
 
        self.retranslateUi(win)
        QtCore.QMetaObject.connectSlotsByName(win)
 
        self.msg = QtWidgets.QMessageBox()
 
    def populate(self):
        self.listWidget.clear()
        for row in db.fetch():
            self.listWidget.addItem(str(row))
 
    def Clear(self):
        self.FnameLabel.clear()
        self.SnameLabel.clear()
        self.email_label.clear()
        self.numberLabel.clear()
        self.gpaLabel.clear()
        self.majorLabel.clear()
        self.yearLabel.clear()
        self.Male_btn.setChecked(False)
        self.female_btn.setChecked(False)
 
    def select(self):
        try:
            selected_item = self.listWidget.currentItem().text()
            selected_item = selected_item[1: -1]
            selected_item = selected_item.split(",")
            index = int(selected_item[0])
            items = db.fetchone_f(index)
 
            self.Clear()
            self.FnameLabel.insert(str(items[1]))
            self.SnameLabel.insert(str(items[2]))
            self.email_label.insert(str(items[3]))
            self.numberLabel.insert(str(items[4]))
            self.majorLabel.insert(str(items[5]))
            self.gpaLabel.insert(str(items[6]))
            self.yearLabel.insert(str(items[7]))
            if items[-1] == "Male":
                self.Male_btn.toggle()
            if items[-1] == "Female":
                self.female_btn.toggle()
            else:
                pass
        except:
            pass
 
    def update(self):
        try:
            selected_item = self.listWidget.currentItem().text()
            selected_item = selected_item[1: -1]
            selected_item = selected_item.split(",")
            index = int(selected_item[0])
            items = db.fetchone_f(index)
            gender_text = items[-1]
            db.update(index, self.FnameLabel.text(), self.SnameLabel.text(), self.email_label.text(), self.numberLabel.text(), self.majorLabel.text(), self.gpaLabel.text(), self.yearLabel.text(), gender_text)
            self.populate()
            self.Clear()
        except:
            if self.FnameLabel.text() == '' or self.SnameLabel.text() == '' or self.email_label.text() == '' or self.numberLabel.text() == '' or self.majorLabel.text() == '' or self.gpaLabel.text() == '' or self.yearLabel.text() == '' or (not self.Male_btn.isChecked() and not self.female_btn.isChecked()):
                self.msg.setIcon(QtWidgets.QMessageBox.Critical)
                self.msg.setInformativeText('Please, select an item!')
                self.msg.setWindowTitle("Error")
                self.msg.exec_()
                return
 
    def Submit(self):
        if self.FnameLabel.text() == '' or self.SnameLabel.text() == '' or self.email_label.text() == '' or self.numberLabel.text() == '' or self.majorLabel.text() == '' or self.gpaLabel.text() == '' or self.yearLabel.text() == '' or (not self.Male_btn.isChecked() and not self.female_btn.isChecked()):
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            self.msg.setInformativeText('Please, include all field!')
            self.msg.setWindowTitle("Error")
            self.msg.exec_()
            return
        else:
            gender_text = ""
            if self.Male_btn.isChecked():
                gender_text = self.Male_btn.text()
            elif self.female_btn.isChecked():
                gender_text = self.female_btn.text()
            else:
                pass
            db.insert(self.FnameLabel.text(), self.SnameLabel.text(), self.email_label.text(), self.numberLabel.text(), self.majorLabel.text(), self.gpaLabel.text(), self.yearLabel.text(), gender_text)
            self.listWidget.addItem(self.FnameLabel.text() + self.SnameLabel.text() + self.email_label.text() + self.numberLabel.text() + self.majorLabel.text() + self.gpaLabel.text() + self.yearLabel.text() + gender_text)
            self.Clear()
            self.populate()
 
    def remove(self):
        try:
            selected_item = self.listWidget.currentItem().text()
            selected_item = selected_item[1: -1]
            selected_item = selected_item.split(",")
            index = int(selected_item[0])
            db.remove(index)
            self.populate()
            self.Clear()
        except:
            if self.FnameLabel.text() == '' or self.SnameLabel.text() == '' or self.email_label.text() == '' or self.numberLabel.text() == '' or self.majorLabel.text() == '' or self.gpaLabel.text() == '' or self.yearLabel.text() == '' or (not self.Male_btn.isChecked() and not self.female_btn.isChecked()):
                self.msg.setIcon(QtWidgets.QMessageBox.Critical)
                self.msg.setInformativeText('Please, select an item!')
                self.msg.setWindowTitle("Error")
                self.msg.exec_()
                return
 
    def retranslateUi(self, win):
        _translate = QtCore.QCoreApplication.translate
        win.setWindowTitle(_translate("win", "Dialog"))
        self.Fname.setText(_translate("win", "First Name"))
        self.Sname.setText(_translate("win", "Second Name"))
        self.number.setText(_translate("win", "Number"))
        self.email.setText(_translate("win", "Email Adress"))
        self.major.setText(_translate("win", "Major"))
        self.gpa.setText(_translate("win", "GPA"))
        self.year.setText(_translate("win", "Study Year"))
        self.gender.setText(_translate("win", "Gender"))
        self.Male_btn.setText(_translate("win", "Male"))
        self.female_btn.setText(_translate("win", "Female"))
        self.remove_btn.setText(_translate("win", "Remove"))
        self.remove_btn.clicked.connect(self.remove)
        self.submit_btn.setText(_translate("win", "Submit"))
        self.submit_btn.clicked.connect(self.Submit)
        self.clear_btn.setText(_translate("win", "Clear"))
        self.clear_btn.clicked.connect(self.Clear)
        self.update_btn.setText(_translate("win", "Update"))
        self.update_btn.clicked.connect(self.update)
        self.listWidget.itemSelectionChanged.connect(self.select)
        self.populate()
 
class DataBase:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS data (ID INTEGER PRIMARY KEY, fname TEXT, sname TEXT,
                email TEXT, number TEXT, major TEXT, gpa TEXT, year NUMERIC, gender TEXT)""")
        self.conn.commit()
 
    def fetch(self):
        self.cur.execute("SELECT * FROM data")
        rows = self.cur.fetchall()
        return rows
 
    def fetchone_f(self, ID):
        self.cur.execute("SELECT * FROM data WHERE ID = ?", (ID,))
        row = self.cur.fetchone()
        return row
 
    def insert(self, fname, sname, email, number, major, gpa, year, gender):
        self.cur.execute("INSERT INTO data VALUES(NULL, ? , ?, ?, ?, ?, ?, ?, ?)",
                         (fname, sname, email, number, major, gpa, year, gender))
        self.conn.commit()
 
    def remove(self, ID):
        self.cur.execute("DELETE FROM data WHERE ID=?", (ID,))
        self.conn.commit()
 
    def update(self, ID, fname, sname, email, number, major, gpa, year, gender):
        self.cur.execute("UPDATE data SET fname = ?, sname = ?, email = ?, number = ?, major = ?, gpa = ?, year = ?, gender = ? WHERE ID = ?",
                         (fname, sname, email, number, major, gpa, year, gender, ID))
        self.conn.commit()
 
    def __del__(self):
        self.conn.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QDialog()
    ui = Ui_win()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())