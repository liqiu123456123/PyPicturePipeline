import os
import os.path
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QMessageBox
import ImgMark

class Ui_RenameWindow(QMainWindow):

    def __init__(self):
        super(Ui_RenameWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 800, 341))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 100, 16))
        self.radioButton.setChecked(True) #
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 30, 100, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 60, 100, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 90, 120, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(220, 90, 74, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 90, 61, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(390, 90, 74, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 90, 61, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(108, 90, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 800, 341))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 121, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(135, 20, 201, 21))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(360, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 210, 491, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(0, 130)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        MainWindow.setCentralWidget(self.centralwidget)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage('加载成功…… ')
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)

        self.setStyleSheet(""" 
         
            QLabel {  
    color: #666; /* 文本颜色 */  
    background-color: #f7d78c; /* 背景颜色，通常设置为透明 */  
} 
        """)
        self.setStyleSheet("background-color: #E1FFFF;font-weight: bold;font-size: 14px;font-family: 'Microsoft YaHei';")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片批量重命名"))
        self.groupBox.setTitle(_translate("MainWindow", "重命名设置"))
        self.radioButton.setText(_translate("MainWindow", "文件名大写"))
        self.radioButton_2.setText(_translate("MainWindow", "文件名小写"))
        self.radioButton_3.setText(_translate("MainWindow", "文件名编号"))
        self.label.setText(_translate("MainWindow", "设置模板："))
        self.label_2.setText(_translate("MainWindow", "起始编号："))
        self.lineEdit_2.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "编号增量："))
        self.lineEdit_3.setText(_translate("MainWindow", "1"))
        self.comboBox.setItemText(0, _translate("MainWindow", "img_***"))
        self.comboBox.setItemText(1, _translate("MainWindow", "fil_***"))
        self.comboBox.setItemText(2, _translate("MainWindow", "pic_***"))
        self.groupBox_2.setTitle(_translate("MainWindow", "图片设置"))
        self.label_4.setText(_translate("MainWindow", "选择图片路径："))
        self.pushButton.setText(_translate("MainWindow", "选择"))
        self.pushButton_2.setText(_translate("MainWindow", "重命名"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "图片名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "图片路径"))
        self.pushButton.clicked.connect(self.getFiles)
        self.pushButton_2.clicked.connect(self.reName)


    def getFiles(self):
        try:
            self.img_path = QFileDialog.getExistingDirectory(None, "选择图片文件夹路径", os.getcwd())
            self.lineEdit_4.setText(self.img_path)
            self.list = os.listdir(self.img_path)
            num=0
            self.tableWidget.setRowCount(0)
            self.tableWidget.clearContents()
            for i in range(0, len(self.list)):
                filepath = os.path.join(self.img_path, self.list[i])
                if os.path.isfile(filepath):
                    imgType = os.path.splitext(filepath)[1]
                    if ImgMark.Ui_MarkWindow().isImg(imgType):
                        num += 1
                        self.tableWidget.insertRow(i)
                        self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.list[i]))
                        self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.img_path))
            self.statusbar.showMessage('共有图片 '+str(num)+' 张')
        except Exception:
            QMessageBox.warning(None, '警告', '请选择一个有效路径……', QMessageBox.Ok)

    def reName(self):
        num = 0
        filename = ""
        newfilename = ""
        try:
            for i in range(self.tableWidget.rowCount()):
                filename = self.tableWidget.item(i,0).text()
                filepath = os.path.join(self.img_path, filename)
                if os.path.isfile(filepath):
                    imgType = os.path.splitext(filepath)[1]
                    if ImgMark.Ui_MarkWindow().isImg(imgType):
                        if self.radioButton.isChecked():
                            newfilename=str(filename).upper()
                            newfilepath = os.path.join(self.img_path, newfilename)
                            os.rename(filepath,newfilepath)
                        elif self.radioButton_2.isChecked():
                            newfilename = str(filename).lower()
                            newfilepath = os.path.join(self.img_path, newfilename)
                            os.rename(filepath, newfilepath)
                        elif self.radioButton_3.isChecked():
                            strid=self.comboBox.currentText()
                            id=int(self.lineEdit_2.text())
                            step=int(self.lineEdit_3.text())
                            template='{:0>3d}'
                            newfilename = strid[0:4]+template.format(id+step*i)+imgType
                            newfilepath = os.path.join(self.img_path, newfilename)
                            os.rename(filepath, newfilepath)
                        num += 1
                        self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(newfilename))
            self.statusbar.showMessage('批量重命名完成，共处理图片 ' + str(num) + ' 张')
        except Exception as e:
            print(e)
            QMessageBox.warning(None, '警告', '请选择正确的重命名方式！', QMessageBox.Ok)
